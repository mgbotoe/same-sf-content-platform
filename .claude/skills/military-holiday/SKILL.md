---
name: military-holiday
description: Generate a military holiday or observance post for SAME SF LinkedIn. Auto-invoked when user says "military holiday", "branch birthday", "memorial day post", "veterans day post", "holiday post", or references a military observance.
---

# Military Holiday Post Generator

Generate a LinkedIn post for a military holiday or observance, following SAME SF's voice and the calendar in `data/military-holidays.md`.

## Before Generating

1. **Read these files**:
   - `data/military-holidays.md` — verify the date and observance type
   - `data/brand-voice.md` — tone rules (especially solemn vs. celebratory)
   - `data/exclusion-list.md` — banned words/phrases

2. **Determine observance type**:
   - **Solemn** (Memorial Day, Pearl Harbor, 9/11, Veterans Day): No emojis, measured tone
   - **Celebratory** (Branch birthdays, Armed Forces Day, Independence Day): Light emoji OK, highlight contributions
   - **Professional** (Engineers Week, Women in Engineering Day, Hire a Veteran Day): Mission-focused, CTA-oriented

## Input

If the user doesn't specify, ask:
- **Which holiday/observance?** (or check today's date against the calendar)
- **Any SAME SF tie-in?** (member who served in that branch, relevant event coming up)
- **Year-specific details?** (e.g., "389th Birthday" — calculate the ordinal)

**CRITICAL: For solemn observances (Memorial Day, Pearl Harbor, 9/11), PAUSE and confirm with the user before drafting.** Ask: "This is a solemn observance. Any specific details to include or avoid?"

**Output rule**: Always produce Version A (short) + Version B (full) + 1 alt opening.

## Post Structure by Type

### Solemn Observance
```
[Factual opening statement — what happened, when, why it matters]

[1-2 sentences connecting to SAME SF's mission of service]

[Closing tribute line — simple, respectful]

#NeverForget #HonorAndRemember #SAMESF
```
- No emojis
- 80-150 words
- Do NOT add a CTA or promotional content

### Branch Birthday / Celebratory
```
[Birthday greeting with branch age — calculate the ordinal]

[2-3 sentences: branch's contribution to engineering/infrastructure + connection to SAME SF]

[Salute/recognition closing]

[1 relevant emoji max] #SAMESF #[BranchHashtag]
```
- 1 emoji max (flag, branch-related)
- 150-250 words
- Can mention SAME SF members who serve/served in that branch

### Professional Observance
```
[What the day recognizes and why it matters]

[How SAME SF supports this through programs, events, or partnerships]

[CTA: join, attend, connect]

#SAMESF #[RelevantHashtag]
```
- 150-250 words
- Always include a CTA

## Ordinal Year Calculation

For branch birthdays, calculate the correct ordinal:
- U.S. Army: Founded June 14, 1775
- U.S. Marine Corps: Founded November 10, 1775
- U.S. Coast Guard: Founded August 4, 1790
- U.S. Air Force: Founded September 18, 1947
- U.S. Space Force: Founded December 20, 2019
- National Guard: Founded December 13, 1636
- Army Corps of Engineers: Founded June 16, 1775
- Seabees: Founded March 5, 1942

Calculate: [Current year] - [Founded year] = ordinal (e.g., 2026 - 1775 = "251st Birthday")

## After Generating (MANDATORY)

1. **Run date validation**: `python scripts/validate-dates.py <path-to-new-file>`
   - Verifies day-of-week matches actual calendar
   - Verifies ordinal matches founding year (from `data/military-holidays.md`)
   - Verifies founding year is correct
   - **Do NOT present the post to the user until all checks pass**
   - If any check fails, fix the error and re-run before showing the draft

2. **Show verification output** to the user alongside the draft

3. Offer to:
   - Generate a branded graphic via `/post-graphic`
   - Add to the content calendar in Notion via `/save-to-notion`
