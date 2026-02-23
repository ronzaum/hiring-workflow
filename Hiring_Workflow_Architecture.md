# Hiring Workflow Architecture -- Claude Code Implementation

Last Updated: 2026-02-20

------------------------------------------------------------------------

# Core Philosophy

This workflow treats job applications as a structured, repeatable system
similar to disciplined product development.

The objective is not volume.\
The objective is **interview rate per role via positioning clarity**.

Key principles:

-   Separate thinking from execution.
-   Enforce checkpoints.
-   Use adversarial review before submission.
-   Maintain one stable identity.
-   Adjust signal emphasis per role, not identity.
-   Compound learning across applications.
-   Preserve warmth and humanity in writing.
-   Avoid sterile, clinical, or generative-AI phrasing.

This system optimizes for precision, signal density, and hiring manager
clarity.

------------------------------------------------------------------------

# North Star

Primary metric:

**Interview rate per role.**

Not: - Number of applications - Activity volume - Surface-level
alignment

Success is defined as: A hiring manager immediately understanding where
Ron fits and choosing to interview.

------------------------------------------------------------------------

# Core Identity Rule

Identity remains stable across roles.

Expression changes. Identity does not.

Ron is positioned as:

An ex-founder, multidisciplinary operator who embeds with teams,
structures ambiguous problems, and drives execution across product,
systems, and client environments.

Each role amplifies a different vector: - Deployment: execution +
embedding + system translation - GTM: strategy to execution + iteration
speed - Founder's Associate: ambiguity + structured thinking + ownership

------------------------------------------------------------------------

# Tone Integrity Rules

All written outputs must follow:

-   Warm but direct.
-   No clinical corporate tone.
-   No generic motivational language.
-   No overused application phrases.
-   No sterile or templated AI phrasing.
-   No exaggerated claims.
-   No invented experience.
-   No title inflation.

If uncertain about a claim, clarification must be requested.

------------------------------------------------------------------------

# Master Documents (Never Auto-Edited)

These files are permanent source of truth.

/master/CV_master.txt\
Canonical CV. Never modified automatically.

/master/profile_master.md\
Verified achievements and metrics only.

/master/linkedin_master.txt\
Current LinkedIn headline, about, and experience.

/master/writing_rules.txt\
Structural constraints, character limits, banned phrases, tone
guardrails.

/master/identity.txt\
Single stable identity statement.

------------------------------------------------------------------------

# Application Workflow Architecture

Order is fixed and cannot be rearranged.

CV → Cover Letter (if required) → LinkedIn → Finalise

------------------------------------------------------------------------

## STEP 0 --- Role Analysis

Output: /roles/\[company_role\]/01_role_analysis.md

Purpose: - Deep analysis of role description and company context. -
Identify core problem. - Identify hiring risk. - Define failure modes. -
Define what the hiring manager truly wants. - Define rejection
profile. - Estimate interview probability. - Go / No-go decision.

Primary input must be pasted JD text.

------------------------------------------------------------------------

## STEP 1 --- Fit Diagnostic

Output: /roles/\[company_role\]/02_fit_diagnostic.md

Purpose: - Compare role analysis against: - CV_master -
profile_master - identity - Produce alignment checklist: - 🟢
Strong signals - 🟠 Partial signals - 🔴 Missing signals - Identify
positioning mismatches. - Clarify highest-impact adjustments.

------------------------------------------------------------------------

## STEP 2 --- Draft CV (V1)

Output: /roles/\[company_role\]/03_tailored_CV_v1.md

Purpose: - Mechanical transformation of CV_master. - Apply
writing_rules. - Preserve warmth and clarity. - Mirror role language. -
Maintain identity integrity.

No hiring manager simulation at this stage.

------------------------------------------------------------------------

## STEP 3 --- Hiring Manager Review

Output: /roles/\[company_role\]/04_HM_review.md

Purpose: - Full adversarial roleplay. - Simulate real hiring manager
evaluation.

Must include: - 10-second scan judgement. - 🟢 Strength signals. - 🟠
Doubts. - 🔴 Rejection risks. - Missing proof. - Interview probability
%. - Clear rewrite instructions.

Tone must be brutally honest, not polite.

------------------------------------------------------------------------

## STEP 4 --- Revise CV (Loop)

Output: /roles/\[company_role\]/05_tailored_CV_final.md

Purpose: - Apply all review corrections. - Re-check tone integrity. -
Re-check identity clarity. - Loop back to Hiring Manager Review if
necessary.

Stops only when signal clarity is high and mismatches are minimal or
irreducible.

------------------------------------------------------------------------

## STEP 5 --- Cover Letter / Written Questions (If Required)

Output: /roles/\[company_role\]/06_cover_letter_final.md

Process: - Confirm whether cover letter or written questions are
required. - If yes: - Draft - Hiring manager review - Revise loop -
Enforce tone integrity rules. - Avoid repetition from CV.

If not required, skip and log.

------------------------------------------------------------------------

## STEP 6 --- LinkedIn Message

Output: /roles/\[company_role\]/07_linkedin_message.md

Purpose: - Use predefined LinkedIn template. - Reference final CV. -
Include proof. - Include intelligent question. - Maintain warmth. -
Avoid generic intros.

------------------------------------------------------------------------

## STEP 7 --- Finalise Application

Outputs: - /roles/\[company_role\]/08_finalisation_record.md - Update
/system/application_tracker.xlsx - Update /system/master_change_log.md -
Update /system/rejection_log.md (after outcome)

Process: - Confirm: "Are we done?" - If yes: - Generate 1-page
finalisation record. - Log probability estimate. - Log positioning
notes. - Append tracking data. - If no: - Return to appropriate step.

------------------------------------------------------------------------

# System Tracking Files

/system/application_tracker.xlsx\
Database of roles applied.

/system/master_change_log.md\
Tracks positioning evolution and recurring signal gaps.

/system/rejection_log.md\
Logs feedback and outcome patterns.

------------------------------------------------------------------------

# Core Design Principles

1.  Separate diagnosis from transformation.
2.  Separate drafting from adversarial review.
3.  Never change identity per role.
4.  Only shift signal emphasis.
5.  Optimize for hiring manager clarity.
6.  Loop until signal density is high.
7.  Compound learning across roles.

------------------------------------------------------------------------

This document defines the full architecture and operating logic of the
Hiring Workflow System implemented in Claude Code.
