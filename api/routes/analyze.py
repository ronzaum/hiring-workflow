"""
routes/analyze.py — Autonomous company research + positioning endpoint.

POST /roles/{id}/analyze

Given only a role record (company + role title from the DB), this endpoint:
  1. Reads identity.txt and profile_master.md from disk (the candidate's stable truth)
  2. Runs Claude autonomously with the web_search tool — researching founders,
     funding history, blog posts, LinkedIn activity, product focus, recent signals
  3. Synthesises all research against the candidate's actual identity and experience
  4. Returns a structured positioning brief: what to lead with, what language to
     mirror, which proof points land hardest for this specific company and person

Nothing is invented. All claims are grounded in the master files.
"""

import json
import os
import re
from pathlib import Path
from typing import Any

import anthropic
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import Role
from api.schemas import CompanyAnalysisResponse

router = APIRouter(prefix="/roles", tags=["analyze"])

# ─── PATHS ────────────────────────────────────────────────────────────────────

# Repo root is two levels above api/routes/; master files now live under workflow/
_REPO_ROOT    = Path(__file__).resolve().parents[2]
_IDENTITY_PATH = _REPO_ROOT / "workflow" / "master" / "identity.txt"
_PROFILE_PATH  = _REPO_ROOT / "workflow" / "master" / "profile_master.md"

# ─── CONSTANTS ────────────────────────────────────────────────────────────────

# Model to use — Opus for deepest reasoning on the research + synthesis task
_MODEL        = "claude-opus-4-6"
_MAX_TOKENS   = 8192
_MAX_LOOPS    = 15   # hard cap on agentic iterations to prevent runaway costs

# The web_search tool — Anthropic executes searches server-side
_TOOLS: list[dict] = [
    {
        "type": "web_search_20250305",
        "name": "web_search",
    }
]


# ─── PROMPTS ──────────────────────────────────────────────────────────────────

_SYSTEM_PROMPT = """\
You are a strategic career positioning agent with access to web search.

Your task:
1. Research the given company thoroughly and autonomously — use web search to find:
   - What the company actually does and where they're focused right now
   - Founder(s) background, career history, and what they personally signal they care about
     (LinkedIn posts, interviews, podcasts, essays, tweets/X posts)
   - Funding history and stage
   - Recent product announcements, company blog posts, or press
   - Tech stack and engineering culture signals
   - What problems they're actively trying to solve

2. After thorough research, synthesise everything against the candidate profile provided.
   Produce a precise positioning brief showing how THIS candidate fits THIS company.

Critical constraints:
- NEVER invent or extrapolate experience beyond what is explicitly stated in the candidate profile
- If a proof point isn't in the profile, do not use it
- If you are uncertain about a fit signal, mark it as partial, not strong
- Identity is stable — only the framing changes per company

Output format:
Return ONLY a valid JSON object — no prose, no markdown, no code fences.
The JSON must match this exact structure:

{
  "company_briefing": "2-3 sentences: what they do, their stage, current focus",
  "founder_profile": "2-3 sentences: founder background and what they personally care about based on public signals",
  "recent_signals": ["signal 1", "signal 2", "signal 3"],
  "positioning_angle": "1 paragraph: exactly how to frame the candidate's identity for this company and founder",
  "language_to_mirror": ["phrase or word from their communications", "..."],
  "proof_points": ["specific achievement from the candidate profile that lands hardest here", "..."],
  "go_no_go": "go",
  "interview_probability": 72
}
"""


def _build_user_prompt(company: str, role_title: str, identity: str, profile: str) -> str:
    """Construct the initial user message with all candidate context."""
    return f"""\
Company: {company}
Role: {role_title}

---

CANDIDATE IDENTITY (stable — do not alter or invent beyond this):
{identity}

---

CANDIDATE PROFILE — verified experience and proof points only:
{profile}

---

Research {company} now. Use as many web searches as you need to build a complete picture.
When you have enough, produce the positioning JSON as instructed.
"""


# ─── AGENTIC LOOP ─────────────────────────────────────────────────────────────

def _run_research_loop(
    client: anthropic.Anthropic,
    user_prompt: str,
) -> str:
    """
    Run the agentic tool-use loop until Claude returns a final answer.

    Pattern:
      - Send message with web_search tool available
      - If stop_reason == "tool_use": add assistant turn, continue
      - If stop_reason == "end_turn": extract and return text content
      - Hard cap at _MAX_LOOPS iterations
    """
    messages: list[dict[str, Any]] = [
        {"role": "user", "content": user_prompt}
    ]

    for iteration in range(_MAX_LOOPS):
        response = client.messages.create(
            model=_MODEL,
            max_tokens=_MAX_TOKENS,
            system=_SYSTEM_PROMPT,
            tools=_TOOLS,
            messages=messages,
        )

        # Always append the assistant turn to maintain conversation history
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            # Extract the final text block from the response content
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
            raise ValueError("end_turn reached but no text block found in response")

        if response.stop_reason == "tool_use":
            # Build tool_result acknowledgements for every tool_use block.
            # web_search is server-side — Anthropic executes the search and
            # returns results embedded in the response content. We still need
            # to send back tool_result entries to continue the conversation.
            tool_results = [
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": "Search executed.",
                }
                for block in response.content
                if hasattr(block, "type") and block.type == "tool_use"
            ]
            if tool_results:
                messages.append({"role": "user", "content": tool_results})
            continue

        # Any other stop_reason (e.g. max_tokens) — break and use what we have
        break

    raise ValueError(
        f"Research loop did not reach end_turn after {_MAX_LOOPS} iterations. "
        "The model may have hit a token limit or entered an unexpected state."
    )


# ─── OUTPUT PARSING ───────────────────────────────────────────────────────────

def _parse_json_response(raw: str) -> dict:
    """
    Extract and parse the JSON object from Claude's final response.

    Handles cases where the model wraps JSON in markdown code fences despite
    instructions not to — strips them before parsing.
    """
    # Strip optional ```json ... ``` or ``` ... ``` fences
    cleaned = re.sub(r"^```(?:json)?\s*", "", raw.strip(), flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```$", "", cleaned.strip())

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Claude response was not valid JSON: {exc}\n\nRaw:\n{raw[:500]}")


# ─── ENDPOINT ─────────────────────────────────────────────────────────────────

@router.post("/{role_id}/analyze", response_model=CompanyAnalysisResponse)
def analyze_role(role_id: int, db: Session = Depends(get_db)):
    """
    Autonomously research a company and return a positioning brief.

    Requires ANTHROPIC_API_KEY in the environment.

    The endpoint reads identity.txt and profile_master.md from disk,
    then runs an agentic Claude loop (with web_search) to research the
    company before synthesising everything into a structured positioning brief.
    """
    # ── 1. Fetch role record ──────────────────────────────────────────────────
    role = db.get(Role, role_id)
    if not role:
        raise HTTPException(status_code=404, detail=f"Role {role_id} not found")

    # ── 2. Read master files from disk ───────────────────────────────────────
    for path, label in [(_IDENTITY_PATH, "identity.txt"), (_PROFILE_PATH, "profile_master.md")]:
        if not path.exists():
            raise HTTPException(
                status_code=500,
                detail=f"Master file not found: {label} (expected at {path})"
            )

    identity = _IDENTITY_PATH.read_text(encoding="utf-8").strip()
    profile  = _PROFILE_PATH.read_text(encoding="utf-8").strip()

    # ── 3. Initialise Anthropic client ───────────────────────────────────────
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="ANTHROPIC_API_KEY environment variable is not set",
        )

    client = anthropic.Anthropic(api_key=api_key)

    # ── 4. Build prompt and run agentic research loop ────────────────────────
    user_prompt = _build_user_prompt(
        company=role.company,
        role_title=role.role_title,
        identity=identity,
        profile=profile,
    )

    try:
        raw_response = _run_research_loop(client, user_prompt)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Research loop failed: {exc}",
        )

    # ── 5. Parse and validate Claude's JSON output ───────────────────────────
    try:
        data = _parse_json_response(raw_response)
        result = CompanyAnalysisResponse(**data)
    except (ValueError, TypeError) as exc:
        raise HTTPException(
            status_code=422,
            detail=f"Failed to parse model output into positioning brief: {exc}",
        )

    return result
