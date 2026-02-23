"""
routes/cv.py — CV PDF generation endpoint.

Wraps master/generate_cv.py without rewriting its logic.
Accepts CV text in the standard [SECTION]-marker format, renders a PDF via
WeasyPrint, and streams it back as a file download.

Endpoint
────────
POST /cv/generate   → multipart or JSON body → PDF file download
"""

import sys
import tempfile
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from api.schemas import CVGenerateRequest

router = APIRouter(prefix="/cv", tags=["cv"])

# ─── PATH SETUP ───────────────────────────────────────────────────────────────

# Resolve the repo root (two levels up from api/routes/) and add to sys.path
# so we can import generate_cv as a module without installing it.
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

# Import the two pure functions from master/generate_cv.py.
# We do NOT call main() — we only use parse_cv and generate_body.
try:
    from master.generate_cv import parse_cv, generate_body  # type: ignore
    from master.generate_cv import TEMPLATE_PATH             # type: ignore
except ImportError as exc:
    raise RuntimeError(
        "Could not import master/generate_cv.py. "
        "Ensure WeasyPrint is installed and master/ is on the path."
    ) from exc


# ─── ENDPOINT ─────────────────────────────────────────────────────────────────

@router.post("/generate")
def generate_cv(payload: CVGenerateRequest):
    """
    Generate a CV PDF from raw CV content (section-marker format).

    - Parses content with `parse_cv`
    - Assembles HTML body with `generate_body`
    - Renders PDF via WeasyPrint using the master HTML template
    - Returns the PDF as a file download

    The temp file is created with delete=False so FileResponse can stream it;
    cleanup is left to the OS (temp dir is purged on reboot).
    """
    # Validate template exists before doing any work
    if not TEMPLATE_PATH.exists():
        raise HTTPException(
            status_code=500,
            detail=f"CV template not found at {TEMPLATE_PATH}",
        )

    try:
        # Lazy import here to keep the error message clear if WeasyPrint missing
        from weasyprint import HTML  # type: ignore
    except ImportError:
        raise HTTPException(
            status_code=500,
            detail="WeasyPrint is not installed. Run: pip install weasyprint",
        )

    try:
        sections = parse_cv(payload.cv_content)
        body     = generate_body(sections)
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
        html     = template.replace("{{BODY}}", body)
    except Exception as exc:
        raise HTTPException(status_code=422, detail=f"CV parse error: {exc}")

    # Write PDF to a named temp file
    try:
        tmp = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
        tmp.close()
        HTML(string=html, base_url=str(TEMPLATE_PATH.parent)).write_pdf(tmp.name)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"PDF render error: {exc}")

    # Sanitise filename for Content-Disposition header
    filename = (payload.output_filename or "CV.pdf").replace('"', "").replace("/", "_")

    return FileResponse(
        path=tmp.name,
        media_type="application/pdf",
        filename=filename,
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
