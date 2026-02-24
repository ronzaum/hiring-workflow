Run Step 0: Role Analysis.

First, ask me to paste the job description if I haven't already provided it.

Then:
1. Read /workflow/master/identity.txt and /workflow/master/writing_rules.txt.
2. Deeply analyse the role description and company context.
3. Identify:
   - Core problem this role is solving
   - What the hiring manager truly wants (vs what the JD literally says)
   - Hiring risk (what makes a candidate fail at this role)
   - Failure modes (what this person will be blamed for in 6 months)
   - Rejection profile (who gets screened out and why)
4. Estimate interview probability as a percentage with reasoning.
5. Make a Go / No-go recommendation with clear rationale.

Ask me: "What is the company name and role title?" to determine the output folder.

Save output to: /workflow/roles/[CompanyName_RoleTitle]/01_role_analysis.md

Format the output clearly with headers for each section. Be direct. Do not pad.

---

After saving, append the following to the Step Log section of /workflow/roles/[CompanyName_RoleTitle]/00_application_master.md:

### /0_Role_Analysis
Date: [date]
Go/No-go: [decision]
Interview probability: [%]
Core problem identified: [one sentence]
Key hiring risk: [one sentence]
Rejection profile summary: [one sentence]
