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
