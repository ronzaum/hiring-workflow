Run Step 8: Sync Architecture.

Your job is to audit the current state of the entire hiring workflow system and update the master architecture document so it accurately reflects reality.

1. Read every file in the system:
   - /workflow/master/workflow_architecture.md (current architecture doc)
   - /workflow/master/writing_rules.txt
   - /workflow/master/identity.txt
   - /CLAUDE.md
   - All files in /.claude/commands/
   - All files in /workflow/system/

2. Compare the current architecture doc against what actually exists:
   - Are all slash commands listed and accurately described?
   - Does the file structure map match what is actually on disk?
   - Do the step definitions reflect what the command files actually do?
   - Do the tone rules, identity rules, and design principles still reflect how the system operates?
   - Has anything been added, removed, or changed that the architecture doc doesn't reflect?

3. Identify every discrepancy between the architecture doc and the real system.

4. List all changes you intend to make before editing. Show me the diff in plain language. Wait for my confirmation before writing.

5. After confirmation, update /workflow/master/workflow_architecture.md in place:
   - Update the "Last Updated" date
   - Correct any outdated descriptions
   - Add any new steps, files, or rules that exist but aren't documented
   - Remove any references to things that no longer exist
   - Do not change the philosophy, identity, or tone rules unless I have explicitly changed those

Do not rewrite the document from scratch. Make targeted edits only.
