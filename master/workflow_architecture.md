# Hiring Workflow Architecture — Master Document
# Source of truth for system logic, philosophy, and structure.
# Update this document via /9_Sync_Architecture after any system changes.

Last Updated: 2026-02-23 (rev 2)

---

# Core Philosophy

This workflow treats job applications as a structured, repeatable system
similar to disciplined product development.

The objective is not volume.
The objective is **interview rate per role via positioning clarity**.

Key principles:

- Separate thinking from execution.
- Enforce checkpoints.
- Use adversarial review before submission.
- Maintain one stable identity.
- Adjust signal emphasis per role, not identity.
- Compound learning across applications.
- Preserve warmth and humanity in writing.
- Avoid sterile, clinical, or generative-AI phrasing.

This system optimises for precision, signal density, and hiring manager clarity.

---

# North Star

Primary metric: **Interview rate per role.**

Not:
- Number of applications
- Activity volume
- Surface-level alignment

Success is defined as: A hiring manager immediately understanding where
Ron fits and choosing to interview.

---

# Core Identity Rule

Identity remains stable across roles.

Expression changes. Identity does not.

Ron is positioned as:

An ex-founder, multidisciplinary operator who embeds with teams,
structures ambiguous problems, and drives execution across product,
systems, and client environments.

Each role amplifies a different vector:
- Deployment: execution + embedding + system translation
- GTM: strategy to execution + iteration speed
- Founder's Associate: ambiguity + structured thinking + ownership

---

# Tone Integrity Rules

All written outputs must follow:

- Warm but direct.
- No clinical corporate tone.
- No generic motivational language.
- No overused application phrases.
- No sterile or templated AI phrasing.
- No exaggerated claims.
- No invented experience.
- No title inflation.

If uncertain about a claim, clarification must be requested.

---

# File Structure

```
hiring_workflow/
├── CLAUDE.md                          ← Claude's operating instructions (auto-loaded)
├── master/
│   ├── workflow_architecture.md       ← This document (living system master)
│   ├── CV_master.txt                  ← Canonical CV — never auto-edited
│   ├── profile_master.md     ← Verified achievements and metrics only
│   ├── linkedin_master.txt            ← Current LinkedIn headline, about, experience
│   ├── writing_rules.txt              ← Structural constraints, tone guardrails, banned phrases
│   └── identity.txt                   ← Single stable identity statement
├── roles/
│   └── [CompanyName_RoleTitle]/
│       ├── 00_application_master.md   ← Living record for this role (created by /start, updated by all steps)
│       ├── 01_role_analysis.md
│       ├── 02_fit_diagnostic.md
│       ├── 03_tailored_CV_v1.md
│       ├── 04_HM_review.md
│       ├── 05_tailored_CV_final.md
│       ├── 06_cover_letter_final.md   ← Only if required
│       ├── 07_linkedin_message.md
│       └── 08_finalisation_record.md
├── system/
│   ├── application_tracker.md         ← Database of roles applied
│   ├── master_change_log.md           ← Positioning evolution and signal gaps
│   ├── rejection_log.md               ← Feedback and outcome patterns
│   └── learnings.md                   ← Synthesised intelligence across all applications
└── .claude/
    └── commands/
        ├── 0_Start.md
        ├── 1_Role_Analysis.md
        ├── 2_Fit_Diagnostic.md
        ├── 3_Draft_CV.md
        ├── 4_HM_Review.md
        ├── 5_Revise_CV.md
        ├── 6_Cover_Letter.md
        ├── 7_LinkedIn_Message.md
        ├── 8_Finalise.md
        ├── 9_Sync_Architecture.md
        ├── 10_Update_Learnings.md
        └── explore.md
```

---

# Master Documents — Never Auto-Edited

These files are permanent source of truth. Claude must never modify them automatically.

- `master/CV_master.txt` — Canonical CV
- `master/profile_master.md` — Verified achievements and metrics only
- `master/linkedin_master.txt` — Current LinkedIn headline, about, and experience
- `master/writing_rules.txt` — Structural constraints, character limits, banned phrases, tone guardrails
- `master/identity.txt` — Single stable identity statement

`master/workflow_architecture.md` is updated only via `/9_Sync_Architecture`.

---

# Application Workflow

Order is fixed and cannot be rearranged.

**/start → CV → Cover Letter (if required) → LinkedIn → Finalise**

---

## Start — Application Intake and Mission Brief
**Slash command:** `/start`
**Output:** `/roles/[CompanyName_RoleTitle]/00_application_master.md`

Purpose:
- Single entry point for every new role
- Accepts all input in one go: JD, company, goal, context
- Reads all master files before producing any output
- Produces a mission brief covering: role summary, company context, positioning angle, fit assessment, risk assessment, step-by-step plan, open questions
- Creates the role folder and the `00_application_master.md` file
- Waits for go/no-go confirmation before handing off to Step 0

The `00_application_master.md` file is the living record for the entire application. Every subsequent step appends a structured summary to it. At the end of the workflow it contains: the full JD, mission brief, step-by-step log, CV changes, and final outcome.

---

## Step 0 — Role Analysis
**Slash command:** `/1_Role_Analysis`
**Output:** `/roles/[company_role]/01_role_analysis.md`

Purpose:
- Deep analysis of role description and company context
- Identify core problem the role is solving
- Identify what the HM truly wants (vs what the JD literally says)
- Identify hiring risk and failure modes
- Define rejection profile
- Estimate interview probability
- Go / No-go decision

Primary input: pasted JD text.

---

## Step 1 — Fit Diagnostic
**Slash command:** `/2_Fit_Diagnostic`
**Output:** `/roles/[company_role]/02_fit_diagnostic.md`

Purpose:
- Compare role analysis against CV_master, profile_master, identity
- Produce alignment checklist:
  - 🟢 Strong signals
  - 🟠 Partial signals
  - 🔴 Missing signals
- Identify positioning mismatches
- Clarify highest-impact adjustments

---

## Step 2 — Draft CV (V1)
**Slash command:** `/3_Draft_CV`
**Output:** `/roles/[company_role]/03_tailored_CV_v1.md`

Purpose:
- Mechanical transformation of CV_master
- Apply writing_rules
- Preserve warmth and clarity
- Mirror role language
- Maintain identity integrity

No hiring manager simulation at this stage.

---

## Step 3 — Hiring Manager Review
**Slash command:** `/4_HM_Review`
**Output:** `/roles/[company_role]/04_HM_review.md`

Purpose:
- Full adversarial roleplay
- Simulate real hiring manager evaluation

Must include:
- 10-second scan judgement
- 🟢 Strength signals
- 🟠 Doubts
- 🔴 Rejection risks
- Missing proof
- Interview probability %
- Clear rewrite instructions

Tone must be brutally honest, not polite.

---

## Step 4 — Revise CV (Loop)
**Slash command:** `/5_Revise_CV`
**Output:** `/roles/[company_role]/05_tailored_CV_final.md`

Purpose:
- Apply all review corrections
- Re-check tone integrity
- Re-check identity clarity
- Loop back to Step 3 if necessary

Stops only when signal clarity is high and mismatches are minimal or irreducible.

---

## Step 5 — Cover Letter / Written Questions (If Required)
**Slash command:** `/6_Cover_Letter`
**Output:** `/roles/[company_role]/06_cover_letter_final.md`

Process:
- Confirm whether cover letter or written questions are required
- If yes: draft → HM review → revise loop → enforce tone integrity → avoid CV repetition
- If not required: skip and log

---

## Step 6 — LinkedIn Message
**Slash command:** `/7_LinkedIn_Message`
**Output:** `/roles/[company_role]/07_linkedin_message.md`

Purpose:
- Reference final CV
- Include proof
- Include intelligent question
- Maintain warmth
- Avoid generic intros
- Maximum 4–6 sentences

---

## Step 7 — Finalise Application
**Slash command:** `/8_Finalise`
**Outputs:**
- `/roles/[company_role]/08_finalisation_record.md`
- Update `/system/application_tracker.md`
- Update `/system/master_change_log.md`
- Update `/system/rejection_log.md` after outcome

Process:
- Confirm: "Are we done?"
- If yes: generate 1-page finalisation record, log probability estimate, log positioning notes, append tracking data
- If no: return to appropriate step

---

## Step 8 — Sync Architecture
**Slash command:** `/9_Sync_Architecture`
**Output:** Updates `master/workflow_architecture.md` in place

Purpose:
- Review all recent changes to the system
- Update this document to reflect current state
- Ensure architecture stays accurate as the system evolves

---

## Step 9 — Update Learnings
**Slash command:** `/10_Update_Learnings`
**Output:** Updates `system/learnings.md` in place

Purpose:
- Synthesise intelligence across all completed applications
- Identify patterns in what lands, what fails, and what keeps appearing
- Track interview rate by role type
- Surface irreducible gaps and open hypotheses
- Compound learning so each application benefits from all previous ones

Run after each completed application cycle. Only analyses roles with a finalisation record.
Shows a plain-language summary and waits for confirmation before writing.

---

# System Tracking Files

- `system/application_tracker.md` — Database of roles applied
- `system/master_change_log.md` — Tracks positioning evolution and recurring signal gaps
- `system/rejection_log.md` — Logs feedback and outcome patterns
- `system/learnings.md` — Synthesised intelligence across all applications (updated via `/10_Update_Learnings`)

---

## Explore — Workflow Change Exploration
**Slash command:** `/explore`
**Output:** None — conversation only until "implement" is confirmed

Purpose:
- Gate before any change or new feature is added to the workflow
- Claude reads the full system first, then asks: "Describe the change"
- Analyses proposed change for overlap with existing commands, files touched, simplest implementation, and open questions
- Goes back and forth until all ambiguities are resolved
- Ends every reply with **"Do I implement?"**
- Nothing is built until the user explicitly confirms

Not part of the application workflow sequence. A meta-command for evolving the system itself.

---

# Core Design Principles

1. Separate diagnosis from transformation.
2. Separate drafting from adversarial review.
3. Never change identity per role.
4. Only shift signal emphasis.
5. Optimise for hiring manager clarity.
6. Loop until signal density is high.
7. Compound learning across roles.
