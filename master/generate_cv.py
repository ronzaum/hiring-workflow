#!/usr/bin/env python3
"""
CV PDF Generator
Converts a section-marked CV markdown file into a formatted PDF.

Usage:
  python3 generate_cv.py <input_md> <output_pdf>

Example:
  python3 master/generate_cv.py \
    roles/Acme_DeploymentLead/05_tailored_CV_final.md \
    roles/Acme_DeploymentLead/Acme_DeploymentLead_CV.pdf

Input format: CV markdown using [SECTION] markers (same as CV_master.txt).
DO NOT AUTO-EDIT this script. Changes must be made manually.
"""

import sys
import re
from pathlib import Path

try:
    from weasyprint import HTML
except ImportError:
    print("WeasyPrint not installed. Run: pip3 install weasyprint")
    sys.exit(1)


# ─── CONSTANTS ────────────────────────────────────────────────────────────────

TAG_RE = re.compile(r'^\[([A-Z][A-Z0-9_]*)\]$')

TEMPLATE_PATH = Path(__file__).parent / "CV_template.html"


# ─── PARSING ──────────────────────────────────────────────────────────────────

def parse_cv(content: str) -> dict:
    """
    Parse CV content into a dict of sections.
    Multiple [ROLE] blocks are collected into sections['ROLES'] as a list.
    Comment lines (starting with #) are ignored.
    """
    sections = {}
    roles = []
    current_tag = None
    current_lines = []

    for line in content.split('\n'):
        # Skip comment lines
        if line.strip().startswith('#'):
            continue

        m = TAG_RE.match(line.strip())
        if m:
            tag = m.group(1)
            # Save previous section
            if current_tag == 'ROLE':
                block = '\n'.join(current_lines).strip()
                if block:
                    roles.append(block)
            elif current_tag:
                sections[current_tag] = '\n'.join(current_lines).strip()
            current_tag = tag
            current_lines = []
        elif current_tag is not None:
            current_lines.append(line)

    # Save last section
    if current_tag == 'ROLE':
        block = '\n'.join(current_lines).strip()
        if block:
            roles.append(block)
    elif current_tag:
        sections[current_tag] = '\n'.join(current_lines).strip()

    sections['ROLES'] = roles
    return sections


# ─── HTML HELPERS ─────────────────────────────────────────────────────────────

def esc(text: str) -> str:
    """Escape HTML special characters."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))


def build_contact_html(contact_line: str) -> str:
    """Render contact line: links for email/linkedin/github, plain for rest."""
    parts = [p.strip() for p in contact_line.split('|')]
    rendered = []
    for part in parts:
        if '@' in part:
            rendered.append(f'<a href="mailto:{esc(part)}">{esc(part)}</a>')
        elif 'linkedin.com' in part:
            rendered.append(f'<a href="https://{esc(part)}">{esc(part)}</a>')
        elif 'github.com' in part:
            rendered.append(f'<a href="https://{esc(part)}">{esc(part)}</a>')
        else:
            rendered.append(f'<span class="contact-plain">{esc(part)}</span>')
    return ' <span class="contact-sep">|</span> '.join(rendered)


def build_role_html(role_block: str) -> str:
    """Convert a single role block into HTML."""
    lines = [l for l in role_block.split('\n') if l.strip()]
    if not lines:
        return ''

    html = '<div class="role-block">'

    # First line: role header — bold title, regular rest
    header = lines[0]
    if ' | ' in header:
        title, rest = header.split(' | ', 1)
        html += (f'<p class="role-header">'
                 f'<span class="role-title-bold">{esc(title)}</span>'
                 f' | {esc(rest)}</p>')
    else:
        html += f'<p class="role-header"><span class="role-title-bold">{esc(header)}</span></p>'

    # Remaining lines
    for line in lines[1:]:
        stripped = line.strip()
        if stripped.startswith('•'):
            bullet_text = stripped[1:].strip()
            html += f'<p class="bullet">• {esc(bullet_text)}</p>'
        elif stripped.startswith('→'):
            html += f'<p class="role-note">{esc(stripped)}</p>'
        else:
            html += f'<p class="role-intro">{esc(stripped)}</p>'

    html += '</div>'
    return html


def build_education_html(edu_text: str) -> str:
    """Render education list. Bold the institution/course name (before ' - ')."""
    html = ''
    for line in edu_text.split('\n'):
        line = line.strip()
        if not line:
            continue

        if ' - ' in line:
            institution, detail = line.split(' - ', 1)
            # Special case: "See Project!" rendered as a link placeholder
            if 'See Project!' in detail:
                detail_html = detail.replace(
                    'See Project!',
                    '<span class="edu-link">See Project!</span>'
                )
                html += (f'<p class="edu-item">'
                         f'<span class="edu-bold">{esc(institution)}</span>'
                         f' - {detail_html}</p>')
            else:
                html += (f'<p class="edu-item">'
                         f'<span class="edu-bold">{esc(institution)}</span>'
                         f' - {esc(detail)}</p>')
        else:
            html += f'<p class="edu-item"><span class="edu-bold">{esc(line)}</span></p>'
    return html


def build_bullets_html(text: str) -> str:
    """Render a block of bullet lines."""
    html = ''
    for line in text.split('\n'):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('•'):
            html += f'<p class="bullet">• {esc(stripped[1:].strip())}</p>'
        else:
            html += f'<p class="role-intro">{esc(stripped)}</p>'
    return html


def build_extras_html(languages: str, technical: str, additional: str) -> str:
    html = ''
    if languages:
        # Languages renders inline: "Languages: [content]" — label underlined, value on same line
        html += f'<p class="role-intro"><span class="subsection-label">Languages:</span> {esc(languages.strip())}</p>'
    if technical:
        html += '<p class="subsection-header">Technical and Systems Work:</p>'
        html += build_bullets_html(technical)
    if additional:
        html += '<p class="subsection-header">Additional:</p>'
        html += build_bullets_html(additional)
    return html


# ─── HTML ASSEMBLY ────────────────────────────────────────────────────────────

def generate_body(sections: dict) -> str:
    name             = sections.get('NAME', '').strip()
    contact          = sections.get('CONTACT', '').strip()
    intro            = sections.get('INTRO', '').strip()
    roles            = sections.get('ROLES', [])
    education        = sections.get('EDUCATION', '').strip()
    skills           = sections.get('SKILLS', '').strip()
    extras_lang      = sections.get('EXTRAS_LANGUAGES', '').strip()
    extras_tech      = sections.get('EXTRAS_TECHNICAL', '').strip()
    extras_add       = sections.get('EXTRAS_ADDITIONAL', '').strip()

    body = ''

    # Header
    body += f'<p class="name">{esc(name)}</p>\n'
    body += f'<p class="contact">{build_contact_html(contact)}</p>\n'
    body += f'<p class="intro">{esc(intro)}</p>\n'

    # Work experience
    body += '<p class="section-header">Work Experience</p>\n'
    for role in roles:
        body += build_role_html(role) + '\n'

    # Two-column bottom
    body += '<div class="bottom-section">\n'

    # Left: Education + Skills
    body += '<div class="col-left">\n'
    body += '<p class="section-header">Education + Skills</p>\n'
    body += build_education_html(education) + '\n'
    body += '<p class="subsection-header">Professional Skills:</p>\n'
    body += build_bullets_html(skills) + '\n'
    body += '</div>\n'

    # Right: Extras
    body += '<div class="col-right">\n'
    body += '<p class="section-header">Extras</p>\n'
    body += build_extras_html(extras_lang, extras_tech, extras_add) + '\n'
    body += '</div>\n'

    body += '</div>\n'

    return body


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    input_path  = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"Error: input file not found: {input_path}")
        sys.exit(1)

    if not TEMPLATE_PATH.exists():
        print(f"Error: template not found: {TEMPLATE_PATH}")
        sys.exit(1)

    content  = input_path.read_text(encoding='utf-8')
    template = TEMPLATE_PATH.read_text(encoding='utf-8')
    sections = parse_cv(content)
    body     = generate_body(sections)
    html     = template.replace('{{BODY}}', body)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(TEMPLATE_PATH.parent)).write_pdf(str(output_path))
    print(f"PDF generated: {output_path}")


if __name__ == '__main__':
    main()
