Run Step 4: Revise CV (Loop).

1. Read:
   - /master/CV_master.txt
   - /master/writing_rules.txt
   - /master/identity.txt
   - /roles/[CompanyName_RoleTitle]/03_tailored_CV_v1.md
   - /roles/[CompanyName_RoleTitle]/04_HM_review.md

2. Apply every correction flagged in the HM review:
   - Fix all 🔴 rejection risks
   - Address all 🟠 doubts where possible
   - Strengthen 🟢 signals
   - Add or sharpen proof where missing

3. Re-check:
   - Tone integrity against writing_rules
   - Identity consistency against identity.txt
   - No invented or inflated claims

4. After producing the revision, state:
   - What changed and why
   - What could not be fixed and why (irreducible gaps)
   - Whether another loop is recommended or if the CV is submission-ready

If another loop is needed, flag it clearly. I will then run /3_HM_Review again on this version.

5. Output format — REQUIRED for PDF generation:
   The file must use section markers exactly as defined in CV_master.txt.
   Read /master/cv_master_templatingandchangecontrol.txt for the full format spec.
   Markers: [NAME] [CONTACT] [INTRO] [ROLE] (one per role) [EDUCATION] [SKILLS]
            [EXTRAS_LANGUAGES] [EXTRAS_TECHNICAL] [EXTRAS_ADDITIONAL]
   The [EDUCATION] block must be copied verbatim from CV_master.txt — it is non-editable.

Save output to: /roles/[CompanyName_RoleTitle]/05_tailored_CV_final.md

6. Generate the PDF:
   Run the following command in the terminal:
   bash master/generate_cv.sh roles/[CompanyName_RoleTitle]/05_tailored_CV_final.md roles/[CompanyName_RoleTitle]/[CompanyName_RoleTitle]_CV.pdf

   The PDF is an editable output. If adjustments are needed, edit the markdown source and re-run the command.

---

After saving, do two things:

1. Append the following to the Step Log section of /roles/[CompanyName_RoleTitle]/00_application_master.md:

### /4_Revise_CV
Date: [date]
Rejection risks fixed: [list]
Doubts addressed: [list]
Irreducible gaps remaining: [list or "none"]
Submission-ready: [yes / no — another loop needed]

2. Update the CV Changes section of /roles/[CompanyName_RoleTitle]/00_application_master.md:
- Append what changed between V1 and final
- Note any irreducible gaps that remain in the final version
