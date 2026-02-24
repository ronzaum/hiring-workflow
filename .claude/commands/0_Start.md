Run: Start — Context Setup.

This is the entry point for every session. It establishes context for all subsequent slash commands.
No analysis is performed here. Start sets up the role record and loads what already exists.

---

## Step 1 — Ask which mode

Ask me:

> "New role, existing reference, or update to existing role?"

Wait for my answer before proceeding.

---

## Mode 1 — New Role

### Collect input

Ask for the following if not already provided:
- Company name and role title (used to name the folder)
- Full job description (paste in full — do not summarise or truncate)
- Any additional context: referral, connection at the company, specific goal or angle

Do not proceed until the JD is provided in full.

### Create the role folder and master file

Create folder: /workflow/roles/[CompanyName_RoleTitle]/

Create file: /workflow/roles/[CompanyName_RoleTitle]/00_application_master.md

Use this structure:

---

# Application Master — [Company] | [Role Title]

Started: [date]
Status: In Progress
Folder: /workflow/roles/[CompanyName_RoleTitle]/

---

## Role Description

[Paste the full JD here verbatim]

---

## Additional Context

[Any referral, connection, or goal provided — or "None provided"]

---

## Step Log

_Updated after each step is completed._

### /start
Date: [date]
Mode: New Role
Summary: Folder created. Ready for Step 0.

---

## CV Changes

_Populated during Steps 2 and 4._

---

## Final Outcome

_Populated during Step 7 and after result is known._

---

### Confirm and hand off

Tell me:
- The folder name created
- Next command to run: `/1_Role_Analysis`

---

## Mode 2 — Existing Reference

### Identify the role

Ask: "Which role? Provide company name and role title."

If unclear, list all folders in /workflow/roles/ and ask me to confirm which one.

### Load context

Read:
- /workflow/roles/[CompanyName_RoleTitle]/00_application_master.md
- All files that exist in /workflow/roles/[CompanyName_RoleTitle]/

### Output a status summary

Report:
- Steps completed (list files that exist)
- Steps remaining (list files that do not yet exist)
- Current status from the Step Log
- Any open flags or unresolved items noted in the master file
- Suggested next command to run

Full context is now loaded. All subsequent slash commands in this session can reference it without re-reading.

---

## Mode 3 — Update Existing Role

### Identify the role

Ask: "Which role? Provide company name and role title."

If unclear, list all folders in /workflow/roles/ and ask me to confirm which one.

### Load context

Read:
- /workflow/roles/[CompanyName_RoleTitle]/00_application_master.md
- All files that exist in /workflow/roles/[CompanyName_RoleTitle]/
- /workflow/system/rejection_log.md
- /workflow/system/master_change_log.md

### Accept input

Ask me to provide the update. Accept any format:
- Rejection email
- Interview transcript
- Recruiter feedback
- Verbal notes
- Any combination of the above

Do not proceed until I have supplied the input.

### Process and update

1. Update /workflow/roles/[CompanyName_RoleTitle]/00_application_master.md:
   - Append to the Final Outcome section with date, input type, and summary of what was received
   - Update Status if appropriate (e.g. Rejected, Interview Scheduled, Offer Received)

2. Append to /workflow/system/rejection_log.md:
   - Date, Company, Role, Outcome stage, Summary of feedback, Any patterns noted

3. Append to /workflow/system/master_change_log.md:
   - Only if positioning insights, signal patterns, or recurring gaps are present in the feedback
   - If nothing new: skip this step, do not pad

4. After writing, tell me:
   - What was updated and where
   - Whether `/10_Update_Learnings` should be run (flag it if the feedback contains patterns worth synthesising — do not run it automatically)
