# Hiring Workflow — Claude Code Operating Instructions
# Last Updated: 2026-02-20

---

## Core Philosophy

This workflow treats job applications as a structured, repeatable system.
The objective is **interview rate per role via positioning clarity** — not volume.

---

## Identity Rule

Identity is stable across all roles. Expression changes. Identity does not.
Always read `/master/identity.txt` before any output.

Do NOT invent, inflate, or assume experience. If uncertain about a claim, ask.

---

## Tone Integrity Rules

All written outputs must follow:
- Warm but direct
- No clinical corporate tone
- No generic motivational language
- No overused application phrases
- No sterile or templated AI phrasing
- No exaggerated claims
- No invented experience
- No title inflation

Always check `/master/writing_rules.txt` before drafting any output.

---

## Master Files — Read Only

These files are the permanent source of truth. NEVER auto-edit them.

Content masters:
- `/master/CV_master.txt`
- `/master/CV_master(lock).pdf`
- `/master/profile_master.md`
- `/master/linkedin_master.txt`
- `/master/writing_rules.txt`
- `/master/identity.txt`
- `/master/cv_master_templatingandchangecontrol.txt`

CV generation infrastructure (do not auto-edit):
- `/master/CV_template.html`
- `/master/generate_cv.py`
- `/master/generate_cv.sh`

## Editable Outputs Rule

Files inside `/roles/[CompanyName_RoleTitle]/` are editable outputs. They are never masters.
This includes generated PDFs. You may read, edit, or regenerate them at any time.

---

## Fixed Workflow Order

Steps cannot be rearranged or skipped.

**CV → Cover Letter (if required) → LinkedIn → Finalise**

| Step | Output File |
|------|------------|
| Step 0: Role Analysis | `01_role_analysis.md` |
| Step 1: Fit Diagnostic | `02_fit_diagnostic.md` |
| Step 2: Draft CV (V1) | `03_tailored_CV_v1.md` |
| Step 3: Hiring Manager Review | `04_HM_review.md` |
| Step 4: Revise CV (Loop) | `05_tailored_CV_final.md` |
| Step 5: Cover Letter (if required) | `06_cover_letter_final.md` |
| Step 6: LinkedIn Message | `07_linkedin_message.md` |
| Step 7: Finalise Application | `08_finalisation_record.md` |

All outputs go in: `/roles/[CompanyName_RoleTitle]/`

---

## Step Definitions

### Step 0 — Role Analysis
- Deep analysis of JD and company context
- Identify: core problem, hiring risk, failure modes, what the HM truly wants, rejection profile
- Estimate interview probability
- Go / No-go decision
- **Input required:** pasted JD text

### Step 1 — Fit Diagnostic
- Compare role analysis against CV_master, profile_master, identity
- Produce alignment checklist: 🟢 Strong / 🟠 Partial / 🔴 Missing signals
- Identify positioning mismatches and highest-impact adjustments

### Step 2 — Draft CV (V1)
- Mechanical transformation of CV_master
- Apply writing_rules, mirror role language, maintain identity integrity
- No hiring manager simulation at this stage

### Step 3 — Hiring Manager Review
- Full adversarial roleplay — simulate a real HM evaluating the CV
- Must include: 10-second scan judgement, 🟢 strengths, 🟠 doubts, 🔴 rejection risks, missing proof, interview probability %, rewrite instructions
- Tone must be brutally honest, not polite

### Step 4 — Revise CV (Loop)
- Apply all review corrections
- Re-check tone integrity and identity clarity
- Loop back to Step 3 if necessary
- Stop only when signal clarity is high and mismatches are minimal or irreducible

### Step 5 — Cover Letter (if required)
- Confirm whether required
- If yes: draft → HM review → revise loop → enforce tone rules → avoid CV repetition
- If not required: skip and log

### Step 6 — LinkedIn Message
- Use predefined LinkedIn template
- Reference final CV, include proof, include intelligent question
- Maintain warmth, avoid generic intros

### Step 7 — Finalise Application
- Ask: "Are we done?"
- If yes: generate 1-page finalisation record, log probability estimate and positioning notes
- Update: application_tracker, master_change_log
- Update rejection_log after outcome is known

---

## North Star Metric

**Interview rate per role.** Not application volume. Not activity.

Success = a hiring manager immediately understanding where Ron fits and choosing to interview.
