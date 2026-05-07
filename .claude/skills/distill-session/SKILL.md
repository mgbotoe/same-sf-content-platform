---
name: distill-session
description: Compress and save the key context from this session to the daily log. Run before ending a long session.
disable-model-invocation: true
---

**Short-circuit check (run FIRST):**

Before doing anything, assess: did this session contain real work?

Signals of a "ghost session" (skip distill):
- No user messages beyond automated startup
- No file edits
- No substantive tool calls

If 3+ of those are true: append ONE line to `daily-logs/YYYY-MM-DD.md` under `## Ghost Distills`:
`- [HH:MM] no-op — scheduler spawn, no work to distill`
Create the section if missing. Then exit.

---

Session distillation — save this session's context to the daily log:

1. Summarize what was accomplished in this session (3-5 bullets)
2. List any open tasks or threads left unfinished (campaigns in progress, pending approvals, graphics to generate)
3. Extract any preferences or patterns Dina demonstrated
4. Append to `daily-logs/YYYY-MM-DD.md` (today's date) under a `## [HH:MM] Session Distill` heading
   - Create the file with a `# Daily Log — YYYY-MM-DD` header if it doesn't exist
5. Also append a one-liner to `identity/memory.md` under `## Session Log`:
   Format: `- [YYYY-MM-DD] <what was done, 1 line>`
6. Do not output any confirmation to the conversation. Write silently.

Token budget: keep the daily log entry under 200 words. Keep the identity/memory.md one-liner under 20 words.
