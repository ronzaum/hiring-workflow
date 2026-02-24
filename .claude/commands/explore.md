You are now in Exploration Mode. Do NOT implement anything.

---

## Phase 1 — Confirm readiness

Do NOT read any files yet.

Respond with exactly this:

"Ready. Describe the change or feature you want to explore and I'll analyse it before we touch anything."

Nothing else. Wait for the user to describe the change.

---

## Phase 3 — Analyse the proposed change

When the user describes the change, read only the files that are plausibly relevant to it.
- If the change touches a specific command: read that command file only.
- If the change touches identity or tone: read identity.txt and writing_rules.txt.
- If the change touches workflow structure or step order: read CLAUDE.md (already loaded) and the relevant step command files.
- If scope is unclear: read the file listing in /.claude/commands/ (Glob only, not full reads) to orient yourself before deciding what to read.
- Do NOT read the full architecture doc or all command files unless the change explicitly requires it.

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
