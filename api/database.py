"""
database.py — SQLAlchemy engine, session factory, and table initialisation.

Database lives at api/hiring_workflow.db (SQLite).
Import `SessionLocal` for a per-request DB session and `init_db()` on startup.
"""

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# ─── PATH ─────────────────────────────────────────────────────────────────────

# Resolves to hiring_workflow/api/hiring_workflow.db regardless of cwd.
DB_PATH = Path(__file__).parent / "hiring_workflow.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

# ─── ENGINE ───────────────────────────────────────────────────────────────────

# check_same_thread=False is required for SQLite when FastAPI shares a single
# connection across async threads in the same process.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ─── BASE ─────────────────────────────────────────────────────────────────────


class Base(DeclarativeBase):
    """Shared declarative base — all ORM models inherit from this."""
    pass


# ─── DEPENDENCY ───────────────────────────────────────────────────────────────

def get_db():
    """FastAPI dependency that yields a DB session and closes it on teardown."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ─── INIT ─────────────────────────────────────────────────────────────────────

def init_db() -> None:
    """Create all tables defined in models.py. Safe to call repeatedly."""
    # Import here so models register against Base before create_all.
    from api import models  # noqa: F401
    Base.metadata.create_all(bind=engine)
