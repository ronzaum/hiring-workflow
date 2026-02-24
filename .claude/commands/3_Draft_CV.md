Run Step 2: Draft CV (V1).

1. Read:
   - /workflow/master/CV_master.txt
   - /workflow/master/profile_master.md
   - /workflow/master/writing_rules.txt
   - /workflow/master/identity.txt
   - /workflow/roles/[CompanyName_RoleTitle]/01_role_analysis.md
   - /workflow/roles/[CompanyName_RoleTitle]/02_fit_diagnostic.md

2. Produce a tailored CV draft by mechanically transforming CV_master:
   - Apply all writing_rules constraints
   - Mirror language from the role description where authentic
   - Emphasise signals identified in the fit diagnostic
   - De-emphasise or remove signals flagged as distracting
   - Maintain identity integrity — do not invent or inflate
   - Preserve warmth and clarity in every line

3. Do NOT run a hiring manager simulation at this stage. Draft only.

4. Flag any lines where you were uncertain and explain why.

5. Output format — REQUIRED for PDF generation:
   The file must use section markers exactly as defined in CV_master.txt.
   Read /workflow/master/cv_master_templatingandchangecontrol.txt for the full format spec.
   Markers: [NAME] [CONTACT] [INTRO] [ROLE] (one per role) [EDUCATION] [SKILLS]
            [EXTRAS_LANGUAGES] [EXTRAS_TECHNICAL] [EXTRAS_ADDITIONAL]
   The [EDUCATION] block must be copied verbatim from CV_master.txt — it is non-editable.

Save output to: /workflow/roles/[CompanyName_RoleTitle]/03_tailored_CV_v1.md

---

After saving, do two things:

1. Append the following to the Step Log section of /workflow/roles/[CompanyName_RoleTitle]/00_application_master.md:

### /2_Draft_CV
Date: [date]
Positioning angle used: [one sentence]
Key language mirrored from JD: [2–3 phrases]
Signals emphasised: [brief list]
Signals removed or de-emphasised: [brief list]
Uncertain lines flagged: [count]

2. Populate the CV Changes section of /workflow/roles/[CompanyName_RoleTitle]/00_application_master.md with:
- What was changed from CV_master
- What was removed
- What language was mirrored from the JD
- Any lines flagged as uncertain
