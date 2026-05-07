---
name: heartbeat
description: Proactive session check-in — surface upcoming content deadlines, pending approvals, and stale drafts.
---

Proactive heartbeat — check content pipeline state:

1. **Check upcoming campaigns** — read `campaigns/` for any posts with upcoming dates in the next 7 days
2. **Check pending approvals** — any campaign files marked as needing JR Gregory review?
3. **Check Notion status** — any items stuck in `Drafting` or `Review` that should have moved?
4. **Check validate-dates** — any recently edited campaign files that haven't been validated?
5. **Check graphics backlog** — any posts that have content but no graphic decision yet?

**Act** based on what you find:
- Upcoming content due in < 3 days → surface with the post date and what's needed
- Pending approval sitting > 48h → flag it
- Stale drafts → note them
- Nothing actionable → silent

**Only surface if something is actionable.** Silent heartbeats are good.
**Zero terminal output when silent.** If nothing is actionable, produce absolutely no output to the conversation — no "heartbeat complete", no summaries, no follow-up questions. The heartbeat is invisible unless something needs attention.

**Distill only if something new happened** — check the last `## [HH:MM] Session Distill` timestamp in today's log. If no new work since then, skip entirely (no entry, no output). If there IS new work, execute distillation steps inline (do NOT use the Skill tool — `distill-session` has `disable-model-invocation`). Read `.claude/skills/distill-session/SKILL.md` and follow the steps directly. Write silently — no confirmation, no output to the conversation.
