"""
routes/roles.py — CRUD endpoints for roles and their pipeline steps.

Endpoints
─────────
GET    /roles                          → list all roles (slim, no steps)
POST   /roles                          → create role; auto-seeds 10 pending steps
GET    /roles/{role_id}                → single role + steps
PATCH  /roles/{role_id}                → update status / probability / notes / go-no-go
DELETE /roles/{role_id}                → delete role + cascade steps
GET    /roles/{role_id}/steps          → list steps for a role
PATCH  /roles/{role_id}/steps/{step_number} → update step status / output_file
"""

from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import Role, Step, PIPELINE_STEPS
from api.schemas import (
    RoleCreate, RoleUpdate, RoleOut, RoleOutSlim,
    StepOut, StepUpdate,
)

router = APIRouter(prefix="/roles", tags=["roles"])


# ─── HELPER ───────────────────────────────────────────────────────────────────

def _get_role_or_404(role_id: int, db: Session) -> Role:
    """Fetch a Role by id or raise 404."""
    role = db.get(Role, role_id)
    if not role:
        raise HTTPException(status_code=404, detail=f"Role {role_id} not found")
    return role


# ─── ROLE ENDPOINTS ───────────────────────────────────────────────────────────

@router.get("", response_model=List[RoleOutSlim])
def list_roles(db: Session = Depends(get_db)):
    """Return all roles, newest first, without step detail."""
    return db.query(Role).order_by(Role.created_at.desc()).all()


@router.post("", response_model=RoleOut, status_code=status.HTTP_201_CREATED)
def create_role(payload: RoleCreate, db: Session = Depends(get_db)):
    """
    Create a new role and auto-seed all 10 pipeline steps as pending.
    Returns the full role + seeded steps.
    """
    role = Role(**payload.model_dump())
    db.add(role)
    db.flush()  # assign role.id before seeding steps

    # Seed one Step row per pipeline entry
    for step_number, step_name in PIPELINE_STEPS:
        db.add(Step(
            role_id=role.id,
            step_number=step_number,
            step_name=step_name,
        ))

    db.commit()
    db.refresh(role)
    return role


@router.get("/{role_id}", response_model=RoleOut)
def get_role(role_id: int, db: Session = Depends(get_db)):
    """Return a single role with its full step list."""
    return _get_role_or_404(role_id, db)


@router.patch("/{role_id}", response_model=RoleOut)
def update_role(role_id: int, payload: RoleUpdate, db: Session = Depends(get_db)):
    """Partial update — only provided fields are written."""
    role = _get_role_or_404(role_id, db)

    for field, value in payload.model_dump(exclude_none=True).items():
        setattr(role, field, value)

    role.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(role)
    return role


@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    """Delete a role and cascade-delete its steps."""
    role = _get_role_or_404(role_id, db)
    db.delete(role)
    db.commit()


# ─── STEP ENDPOINTS ───────────────────────────────────────────────────────────

@router.get("/{role_id}/steps", response_model=List[StepOut])
def list_steps(role_id: int, db: Session = Depends(get_db)):
    """Return all steps for a role, ordered by step_number."""
    _get_role_or_404(role_id, db)  # 404 if role missing
    return (
        db.query(Step)
        .filter(Step.role_id == role_id)
        .order_by(Step.step_number)
        .all()
    )


@router.patch("/{role_id}/steps/{step_number}", response_model=StepOut)
def update_step(
    role_id: int,
    step_number: int,
    payload: StepUpdate,
    db: Session = Depends(get_db),
):
    """
    Update a step's status or output_file.
    Automatically sets completed_at when status is set to 'complete'.
    """
    _get_role_or_404(role_id, db)

    step = (
        db.query(Step)
        .filter(Step.role_id == role_id, Step.step_number == step_number)
        .first()
    )
    if not step:
        raise HTTPException(
            status_code=404,
            detail=f"Step {step_number} not found for role {role_id}",
        )

    for field, value in payload.model_dump(exclude_none=True).items():
        setattr(step, field, value)

    # Auto-stamp completion time
    if payload.status == "complete" and step.completed_at is None:
        step.completed_at = datetime.utcnow()

    db.commit()
    db.refresh(step)
    return step
