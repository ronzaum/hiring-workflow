# Feature Implementation Plan — Folder Restructure

**Overall Progress:** `100%`

---

## TLDR
Reorganise the project root into a clean two-folder split: `workflow/` (all hiring inputs and outputs) and `product/` (technical and meta docs). Commands stay flat. All internal path references update to match. README updated at root.

---

## Critical Decisions
- **Commands stay flat** — `.claude/commands/` is not restructured; invocation names unchanged (`/explore`, `/0_Start`, etc.)
- **`master/` contents unchanged** — only the parent path changes; nothing inside is edited
- **`CHANGELOG.md` moves to `product/`** — technical/meta docs belong there
- **`api/` stays at root** — Python package constraint; moving it would break all internal imports and the uvicorn command
- **`Hiring_Workflow_Architecture.md` moved to `product/`** — was a floating duplicate at root
- **`9_Sync_Architecture` is a workflow command** — stays in the flat commands list, not product

---

## Tasks

- [x] 🟩 **Step 1: Move data folders under `workflow/`**
  - [x] 🟩 Move `master/` → `workflow/master/`
  - [x] 🟩 Move `roles/` → `workflow/roles/`
  - [x] 🟩 Move `system/` → `workflow/system/`

- [x] 🟩 **Step 2: Set up `product/`**
  - [x] 🟩 Create `product/` folder
  - [x] 🟩 Move `CHANGELOG.md` → `product/CHANGELOG.md`
  - [x] 🟩 Move `Hiring_Workflow_Architecture.md` → `product/`
  - [x] 🟩 Move `plan_restructure.md` → `product/`

- [x] 🟩 **Step 3: Update path references in `CLAUDE.md`**
  - [x] 🟩 Update all master file paths (`/master/` → `/workflow/master/`)
  - [x] 🟩 Update roles and system paths

- [x] 🟩 **Step 4: Update path references in all command files**
  - [x] 🟩 `0_Start.md` — roles + system paths
  - [x] 🟩 `1_Role_Analysis.md` — master + roles paths
  - [x] 🟩 `2_Fit_Diagnostic.md` — master + roles paths
  - [x] 🟩 `3_Draft_CV.md` — master + roles paths
  - [x] 🟩 `4_HM_Review.md` — roles paths
  - [x] 🟩 `5_Revise_CV.md` — master + roles paths + generate_cv.sh command
  - [x] 🟩 `6_Cover_Letter.md` — master + roles paths
  - [x] 🟩 `7_LinkedIn_Message.md` — master + roles paths
  - [x] 🟩 `8_Finalise.md` — master + roles + system paths
  - [x] 🟩 `9_Sync_Architecture.md` — master + system paths
  - [x] 🟩 `10_Update_Learnings.md` — master + system + roles paths
  - [x] 🟩 `explore.md` — master paths
  - [x] 🟩 `api/routes/cv.py` — sys.path now points to workflow/
  - [x] 🟩 `api/routes/analyze.py` — identity + profile paths updated
  - [x] 🟩 `workflow/master/generate_cv.py` — docstring examples updated
  - [x] 🟩 `workflow/master/generate_cv.sh` — docstring examples updated

- [x] 🟩 **Step 5: Update `workflow_architecture.md`**
  - [x] 🟩 Rewrite the file structure map to reflect new layout
  - [x] 🟩 Update step output paths and system tracking paths
  - [x] 🟩 Update "Last Updated" date (rev 3)

- [x] 🟩 **Step 6: Update `README.md` at root**
  - [x] 🟩 Update file structure map
  - [x] 🟩 Update API path references

---

Completed: 2026-02-24
