# Changelog

All notable changes to this project will be documented here.

---

## [Unreleased]

---

## [0.2.0] — 2026-02-23

### Added
- `POST /roles/{id}/analyze` — autonomous company research + positioning endpoint
  - Reads `master/identity.txt` and `master/profile_master.md` at request time
  - Runs Claude Opus 4.6 in an agentic loop (up to 15 iterations) with `web_search_20250305`
  - Researches: founder background, funding history, product focus, recent public signals, tech stack
  - Returns structured JSON: company briefing, founder profile, recent signals, positioning angle, language to mirror, proof points, go/no-go, interview probability
  - All claims grounded in master files — nothing invented
  - Requires `ANTHROPIC_API_KEY` env var
- `CompanyAnalysisResponse` Pydantic schema in `api/schemas.py`
- `anthropic>=0.40.0` added to `api/requirements.txt`

---

## [0.1.0] — 2026-02-23

### Added
- `api/` — self-contained FastAPI layer (SQLite via SQLAlchemy, Pydantic v2)
- `POST /roles` — create a role; auto-seeds all 10 pipeline steps as `pending`
- `GET /roles` — list all roles, newest first (slim, no step detail)
- `GET /roles/{id}` — single role with full step list
- `PATCH /roles/{id}` — partial update: status, interview_probability, go_no_go, notes
- `DELETE /roles/{id}` — delete role and cascade-delete its steps
- `GET /roles/{id}/steps` — list pipeline steps ordered by step_number
- `PATCH /roles/{id}/steps/{step_number}` — update step status or output_file; auto-stamps `completed_at` when status set to `complete`
- `POST /cv/generate` — generate PDF from section-marker CV text; wraps `master/generate_cv.py` directly; returns file download
- `GET /health` — liveness probe
- `.gitignore` entries for `api/hiring_workflow.db`, `__pycache__`, `*.pyc`, `*.pyo`
- Fixed typo: `.claude/commands/implment.md` → `implement.md`
