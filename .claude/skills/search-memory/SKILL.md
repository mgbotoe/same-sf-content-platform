---
name: search-memory
description: Search all memory tiers — hot, cold, and raw daily logs — for past context about campaigns, decisions, or content history.
allowed-tools: Bash, Read
---

Search the memory system for past context:

## Search Order

1. **Check hot memory first** — read `identity/memory.md` (already in context)
2. **Check cold memory** — read relevant `memory/*.md` files (campaigns, decisions, preferences, people)
3. **Search daily log archive** — FTS5 full-text search for raw session history

## Daily Log Search

1. Ensure the index is up to date:
   ```bash
   python3 .claude/scripts/index-daily-logs.py
   ```

2. Search using FTS5 syntax:
   ```bash
   python3 .claude/scripts/search-logs.py "$ARGUMENTS"
   ```

   Supported query syntax:
   - Simple words: `golf tournament`
   - Phrases: `"version B"`
   - Boolean: `mailchimp AND campaign`
   - Negation: `linkedin NOT email`
   - Prefix: `milit*`
   - Date filter: `--date 2026-04-05`
   - Limit: `--limit 20`

3. If results found, read the full source file for context if needed.

4. **Summarize** — structured pass before surfacing anything:
   - **Direct answer** — one sentence answering the question
   - **Confidence** — `high` (direct evidence found) / `medium` (inferred from context) / `low` (partial match only)
   - **Supporting evidence** — 2-3 key facts or excerpts with dates
   - **Gaps** — what wasn't found, if relevant to the question

   Never dump raw log output. If confidence is `low`, say so explicitly rather than presenting weak matches as answers.
