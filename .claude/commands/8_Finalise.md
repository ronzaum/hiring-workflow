Run Step 7: Finalise Application.

Ask me: "Are we done with this application?"

If NO: Ask which step to return to and stop.

If YES:

1. Read:
   - /workflow/master/identity.txt
   - /workflow/master/writing_rules.txt
   - All outputs in /workflow/roles/[CompanyName_RoleTitle]/

2. Generate a 1-page finalisation record containing:
   - Role: company, title, date applied
   - Go/No-go decision from Step 0 and rationale
   - Final interview probability estimate
   - Key positioning decisions made (what was emphasised, what was dropped)
   - Irreducible gaps (weaknesses that could not be fixed)
   - Anything to watch for if an interview is granted
   - Cover letter: yes/no
   - LinkedIn message: sent to whom

3. Append a new row to /workflow/system/application_tracker.md with:
   - Date, Company, Role, Folder path, Interview %, Status: Applied

4. Append to /workflow/system/master_change_log.md:
   - Any new positioning decisions or signal patterns observed

Save finalisation record to: /workflow/roles/[CompanyName_RoleTitle]/08_finalisation_record.md

Remind me: "Update rejection_log.md after you receive an outcome."

---

After saving, update the Final Outcome section of /workflow/roles/[CompanyName_RoleTitle]/00_application_master.md with:

### /7_Finalise
Date applied: [date]
Final interview probability: [%]
Cover letter submitted: [yes / no]
LinkedIn message sent: [yes / no — to whom]
Key positioning decisions: [brief list]
Irreducible gaps: [brief list or "none"]
Watch for in interview: [one or two points]
Status: Applied — outcome pending
