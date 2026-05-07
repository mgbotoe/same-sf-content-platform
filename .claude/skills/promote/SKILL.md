---
name: promote
description: Extract key learnings from daily logs and promote them to identity/memory.md. Run after productive sessions.
---

Daily log promotion — extract signal from raw session logs into long-term memory.

## Hot/Cold Memory Architecture

- **Hot:** `identity/memory.md` — always in context, kept under 2500 tokens
- **Cold:** `memory/*.md` — topic files searched on-demand
  - `memory/campaigns.md` — campaign history, status, decisions
  - `memory/preferences.md` — recurring patterns, content choices
  - `memory/decisions.md` — key decisions with reasoning
  - `memory/people.md` — key contacts, approval history

## Steps

1. Read the last 3 days of `daily-logs/` files
2. Read current `identity/memory.md` and relevant `memory/*.md` files
3. **Curation pass on `identity/memory.md`**:
   - Collapse runs of near-identical Session Log entries (ghost distills)
   - Drop duplicate entries across days; keep most recent
   - Don't collapse across distinct facts
4. Extract and route:
   - **Campaign decisions** (version chosen, why) → `memory/campaigns.md`
   - **Content preferences** → `memory/preferences.md`
   - **Key decisions** → `memory/decisions.md`
   - **People context** → `memory/people.md`
   - **Active campaigns / open threads** → `identity/memory.md` Active Work
5. For `identity/memory.md` (hot):
   - Only promote things needed every session
   - Keep under 2500 tokens — push detail to cold files
6. Report what was promoted, what was skipped, what got collapsed.
7. Write current Unix timestamp to `.claude/runtime/promote-last-run.ts`:
   ```bash
   date +%s > .claude/runtime/promote-last-run.ts
   ```
