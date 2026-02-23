You are now in Exploration Mode. Do NOT implement anything.

---

## Phase 1 — Load the current system

Before responding, read every file in the workflow:

- /master/workflow_architecture.md
- /master/writing_rules.txt
- /master/identity.txt
- /CLAUDE.md
- All files in /.claude/commands/

This is so you know exactly what already exists before evaluating anything new.

---

## Phase 2 — Confirm readiness

Once you have read the system, respond with exactly this:

"I've reviewed the full workflow. Describe the change or feature you want to explore and I'll analyse it before we touch anything."

Nothing else. Wait for the user to describe the change.

---

## Phase 3 — Analyse the proposed change

When the user describes the change:

1. **Check for existing overlap**
   - Does this already exist in any command file, master file, or CLAUDE.md?
   - Does it partially exist somewhere that should be extended rather than duplicated?
   - If overlap is found: name the file and line, and propose editing it rather than creating something new.

2. **Understand the change**
   - What exactly is being added, changed, or removed?
   - Which files would be touched?
   - Where does it fit in the workflow sequence?
   - Does it affect any other commands upstream or downstream?

3. **Identify constraints**
   - What is the simplest version of this change?
   - What must it NOT do (scope boundaries)?
   - Does it conflict with any existing rule, tone constraint, or design principle?

4. **Surface ambiguities**
   - List every part of the description that is unclear, assumed, or undefined.
   - Do not fill in gaps yourself. Flag them explicitly.
   - Do not assume scope beyond what was explicitly described.

---

## Phase 4 — Respond with your analysis

Structure your response as:

**What I understand you want:**
[Your interpretation of the change in plain language]

**Overlap check:**
[What already exists that relates to this — file name and what it does. If none, say "No overlap found."]

**What this would touch:**
[List of files that would be created or modified]

**Simplest implementation:**
[One paragraph describing the minimal version of this change]

**Questions and ambiguities:**
[Numbered list. Every unresolved question gets its own line. If none, say "No open questions."]

---

## Phase 5 — Iterate

After your analysis, wait for the user to answer your questions or clarify.

Continue going back and forth until you have no remaining questions.

When all questions are resolved, end your final response with:

**Do I implement?**

Do not implement until the user explicitly says "implement" or "yes implement" or equivalent confirmation.
