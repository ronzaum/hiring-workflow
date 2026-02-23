# Hiring Workflow

A structured, AI-native system for managing job applications — built on Claude Code.

The problem: most job applications fail not because of weak experience, but because of weak positioning. The same background lands differently depending on how it's framed, what's emphasised, and whether the CV reads the way a hiring manager actually scans.

This system treats applications like a product development cycle: diagnose before you build, review adversarially before you ship, and compound learning across every role.

---

## How it works

A fixed 10-step pipeline. Steps cannot be rearranged or skipped.

| Step | Command | Output |
|------|---------|--------|
| Start | `/0_Start` | `00_application_master.md` — living record for the role |
| 0 — Role Analysis | `/1_Role_Analysis` | Deep JD analysis: hiring risk, failure modes, rejection profile, go/no-go |
| 1 — Fit Diagnostic | `/2_Fit_Diagnostic` | Signal alignment: 🟢 Strong / 🟠 Partial / 🔴 Missing vs. CV master |
| 2 — Draft CV (V1) | `/3_Draft_CV` | Mechanical transformation of CV master to mirror role language |
| 3 — HM Review | `/4_HM_Review` | Adversarial hiring manager simulation — brutally honest, not polite |
| 4 — Revise CV | `/5_Revise_CV` | Apply corrections, loop until signal density is high |
| 5 — Cover Letter | `/6_Cover_Letter` | Draft → HM review → revise loop (skip and log if not required) |
| 6 — LinkedIn Message | `/7_LinkedIn_Message` | Warm outreach with proof and an intelligent question |
| 7 — Finalise | `/8_Finalise` | Finalisation record, probability estimate, tracker update |
| 8 — Sync Architecture | `/9_Sync_Architecture` | Keeps this doc accurate as the system evolves |
| 9 — Update Learnings | `/10_Update_Learnings` | Compound intelligence across all completed applications |

Each step reads from master files (CV, profile, identity, writing rules) and writes a structured output to the role folder. Every step appends a summary to `00_application_master.md`, so the full application history is always in one place.

---

## What's in the repo

```
hiring-workflow/
├── CLAUDE.md                          ← Claude's operating instructions (auto-loaded)
├── Hiring_Workflow_Architecture.md    ← Architecture overview
├── master/
│   ├── workflow_architecture.md       ← Full system design and step definitions
│   ├── generate_cv.py                 ← CV generation script (MD → PDF via HTML template)
│   ├── generate_cv.sh                 ← Shell wrapper
│   ├── CV_template.html               ← HTML/CSS CV template
│   └── writing_rules.txt              ← Tone guardrails, banned phrases, output rules
└── .claude/
    └── commands/                      ← Slash command prompts (one per pipeline step)
```

Personal master files (CV, profile, application history) are excluded via `.gitignore`.

---

## Design principles

1. Separate diagnosis from transformation — role analysis before CV drafting
2. Separate drafting from adversarial review — never self-review your own CV
3. Never change identity per role — shift signal emphasis only
4. Optimise for hiring manager clarity — not application volume
5. Compound learning — each application improves the next

---

## North star metric

**Interview rate per role.** Not number of applications. Not activity.

Success = a hiring manager immediately understanding where you fit and choosing to interview.

---

## API

A self-contained FastAPI layer exposes the workflow as a REST API — useful for integrations, portfolio demos, or tooling built on top of the pipeline.

**Stack:** FastAPI · SQLAlchemy · SQLite · Pydantic v2 · WeasyPrint

**Run locally:**

```bash
pip install -r api/requirements.txt
uvicorn api.main:app --reload
```

Auto-docs at `http://127.0.0.1:8000/docs`

**Endpoints:**

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Liveness probe |
| GET | `/roles` | List all roles |
| POST | `/roles` | Create role (auto-seeds 10 pipeline steps) |
| GET | `/roles/{id}` | Get role + steps |
| PATCH | `/roles/{id}` | Update status / probability / notes |
| DELETE | `/roles/{id}` | Delete role and steps |
| GET | `/roles/{id}/steps` | List pipeline steps for a role |
| PATCH | `/roles/{id}/steps/{step_number}` | Mark step complete / update output file |
| POST | `/cv/generate` | Generate CV PDF from section-marker text |

The CV endpoint wraps `master/generate_cv.py` directly — no logic duplication.

---

## Stack

Claude Code · Python · FastAPI · HTML/CSS
