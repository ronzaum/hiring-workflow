"""
schemas.py — Pydantic v2 request/response models for the hiring workflow API.

Separate Create / Update / Out shapes per resource to keep each endpoint clean.
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


# ─── STEP ─────────────────────────────────────────────────────────────────────

class StepOut(BaseModel):
    """Read-only representation of a single pipeline step."""
    model_config = ConfigDict(from_attributes=True)

    id:           int
    role_id:      int
    step_number:  int
    step_name:    str
    status:       str
    output_file:  Optional[str]
    completed_at: Optional[datetime]


class StepUpdate(BaseModel):
    """Patch payload for a step — only fields that can change."""
    status:      Optional[str] = None   # "pending"|"in_progress"|"complete"|"skipped"
    output_file: Optional[str] = None


# ─── ROLE ─────────────────────────────────────────────────────────────────────

class RoleCreate(BaseModel):
    """Payload for POST /roles."""
    company:               str
    role_title:            str
    status:                Optional[str]  = "active"
    interview_probability: Optional[float] = None
    go_no_go:              Optional[str]  = None
    notes:                 Optional[str]  = None


class RoleUpdate(BaseModel):
    """Patch payload for PATCH /roles/{id} — all fields optional."""
    status:                Optional[str]  = None
    interview_probability: Optional[float] = None
    go_no_go:              Optional[str]  = None
    notes:                 Optional[str]  = None


class RoleOut(BaseModel):
    """Full role record returned by the API, including its steps."""
    model_config = ConfigDict(from_attributes=True)

    id:                    int
    company:               str
    role_title:            str
    status:                str
    interview_probability: Optional[float]
    go_no_go:              Optional[str]
    notes:                 Optional[str]
    created_at:            datetime
    updated_at:            datetime
    steps:                 List[StepOut] = []


class RoleOutSlim(BaseModel):
    """Slimmer role record for list responses (no steps)."""
    model_config = ConfigDict(from_attributes=True)

    id:                    int
    company:               str
    role_title:            str
    status:                str
    interview_probability: Optional[float]
    go_no_go:              Optional[str]
    created_at:            datetime
    updated_at:            datetime


# ─── CV ───────────────────────────────────────────────────────────────────────

class CVGenerateRequest(BaseModel):
    """
    Payload for POST /cv/generate.

    Supply the full CV text using [SECTION] markers (same format as CV_master.txt).
    `output_filename` sets the Content-Disposition filename; defaults to CV.pdf.
    """
    cv_content:      str
    output_filename: Optional[str] = "CV.pdf"


class CVGenerateResponse(BaseModel):
    """
    Returned when generation fails before writing a file.
    On success the endpoint streams a FileResponse — this schema is error-only.
    """
    detail: str


# ─── ANALYZE ──────────────────────────────────────────────────────────────────

class CompanyAnalysisResponse(BaseModel):
    """
    Structured positioning brief returned by POST /roles/{id}/analyze.

    Every field is grounded in identity.txt and profile_master.md — nothing
    is invented or extrapolated beyond what the candidate has actually done.
    """
    # What the company actually does, their stage, and current focus
    company_briefing:     str

    # Founder background and what they personally signal they care about
    # (sourced from public posts, interviews, LinkedIn, funding announcements)
    founder_profile:      str

    # Recent public signals — posts, announcements, or themes revealing priorities
    recent_signals:       List[str]

    # One-paragraph: how to frame the candidate's identity for this specific
    # company and founder, given everything found in research
    positioning_angle:    str

    # Specific words and phrases the company/founder uses — mirror these
    language_to_mirror:   List[str]

    # Specific proof points from profile_master that land hardest here
    # Referenced by actual achievement, not invented
    proof_points:         List[str]

    # "go" or "no-go" based on genuine fit assessment
    go_no_go:             str

    # 0–100 estimated interview probability given current positioning
    interview_probability: int
