"""
main.py — FastAPI application entry point for the hiring workflow API.

Run with:
  cd hiring_workflow
  uvicorn api.main:app --reload

Auto-docs available at:
  http://127.0.0.1:8000/docs     (Swagger UI)
  http://127.0.0.1:8000/redoc   (ReDoc)
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.database import init_db
from api.routes.roles import router as roles_router
from api.routes.cv import router as cv_router
from api.routes.analyze import router as analyze_router


# ─── LIFESPAN ─────────────────────────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run startup tasks before serving requests."""
    init_db()   # creates SQLite tables if they don't exist yet
    yield       # hand off to the running app


# ─── APP ──────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="Hiring Workflow API",
    description=(
        "REST API exposing the AI-native hiring workflow — "
        "role pipeline tracking, step management, CV PDF generation, "
        "and autonomous company research + positioning."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

# ─── ROUTERS ──────────────────────────────────────────────────────────────────

app.include_router(roles_router)
app.include_router(cv_router)
app.include_router(analyze_router)


# ─── HEALTH ───────────────────────────────────────────────────────────────────

@app.get("/health", tags=["meta"])
def health():
    """Liveness probe — returns 200 when the server is up."""
    return {"status": "ok"}
