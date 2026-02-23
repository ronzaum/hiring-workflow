"""
models.py — SQLAlchemy ORM models for the hiring workflow API.

Two tables:
  Role  — one record per job application
  Step  — 10 records per Role, tracking the fixed pipeline steps
"""

from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Float, DateTime, ForeignKey, Text
)
from sqlalchemy.orm import relationship

from api.database import Base


# ─── ROLE ─────────────────────────────────────────────────────────────────────

class Role(Base):
    """Represents a single job application (company + role title)."""

    __tablename__ = "roles"

    id                   = Column(Integer, primary_key=True, index=True)
    company              = Column(String(200), nullable=False)
    role_title           = Column(String(200), nullable=False)
    # Status values: "active" | "submitted" | "rejected" | "offer" | "archived"
    status               = Column(String(50), nullable=False, default="active")
    interview_probability = Column(Float, nullable=True)   # 0.0–1.0
    go_no_go             = Column(String(10), nullable=True)  # "go" | "no-go"
    notes                = Column(Text, nullable=True)
    created_at           = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at           = Column(DateTime, default=datetime.utcnow,
                                  onupdate=datetime.utcnow, nullable=False)

    # One-to-many: a Role has many Steps
    steps = relationship(
        "Step",
        back_populates="role",
        cascade="all, delete-orphan",
        order_by="Step.step_number",
    )


# ─── STEP ─────────────────────────────────────────────────────────────────────

# Fixed pipeline steps — seeded on Role creation.
PIPELINE_STEPS = [
    (0,  "Role Analysis"),
    (1,  "Fit Diagnostic"),
    (2,  "Draft CV (V1)"),
    (3,  "HM Review"),
    (4,  "Revise CV"),
    (5,  "Cover Letter"),
    (6,  "LinkedIn Message"),
    (7,  "Finalise Application"),
    (8,  "Sync Architecture"),
    (9,  "Update Learnings"),
]


class Step(Base):
    """Tracks completion of a single pipeline step for a given Role."""

    __tablename__ = "steps"

    id           = Column(Integer, primary_key=True, index=True)
    role_id      = Column(Integer, ForeignKey("roles.id"), nullable=False, index=True)
    step_number  = Column(Integer, nullable=False)   # 0–9
    step_name    = Column(String(100), nullable=False)
    # Status values: "pending" | "in_progress" | "complete" | "skipped"
    status       = Column(String(20), nullable=False, default="pending")
    output_file  = Column(String(500), nullable=True)  # relative path to output .md / .pdf
    completed_at = Column(DateTime, nullable=True)

    role = relationship("Role", back_populates="steps")
