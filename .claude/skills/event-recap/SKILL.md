---
name: event-recap
description: Generate a post-event recap post for SAME SF LinkedIn from notes, photos, or highlights. Auto-invoked when user says "event recap", "write a recap", "post-event", "what happened at", or "summarize the event".
---

# Event Recap Post Generator

Generate a post-event recap that captures the energy and impact of a SAME SF event.

## Before Generating

1. **Read these files**:
   - `data/brand-voice.md` — energetic, specific tone for recaps
   - `data/exclusion-list.md` — banned words/phrases

## Input Required

Run this checklist. Ask for any missing items:
- **Event name**: What was it?
- **Date**: When did it happen?
- **Highlights**: Key moments, quotes, surprises, milestones
- **Numbers**: Attendance, dollars raised, scholarships awarded, photos taken
- **People to name**: Speakers, sponsors, volunteers, special guests
- **Photos**: Available? Photo album link?
- **What's next**: Upcoming event to tease?
- **Audience**: Members / Sponsors / DoD / Students / General
- **Tone**: Celebratory / Casual / Reflective

**Output rule**: Always produce Version A (short) + Version B (full) + 1 alt opening.

## Recap Post Structure

### Short Recap (1 post, same week as event)
```
[Energetic opening — reaction, not summary]
"What an evening!" / "What a day out on the course!" / "The energy in that room..."

[2-3 highlight paragraphs with specifics]
- Name people: speakers, sponsors, volunteers
- Include numbers: attendance, dollars raised, scholarships
- Capture a moment: a quote, a surprise, a connection made

[Thank sponsors/partners by name]

[Forward-looking close + CTA]
- Photo album link
- Next event teaser
- "If you missed it, here's what happened..."

#SAMESF [+ event hashtag] [+ 2-3 relevant hashtags]
```
- 200-400 words
- Photo carousel recommended (suggest 6-8 images)

### Extended Recap Series (2-3 posts over 1-2 weeks)

**Post 1 — Highlights & Gratitude** (1-2 days after)
- Overall energy and key moments
- Thank attendees and sponsors broadly

**Post 2 — Sponsor Deep Dive** (3-5 days after)
- Specific sponsor recognition with impact callouts
- Tag each sponsor organization

**Post 3 — People & Impact** (1-2 weeks after)
- Scholarship recipients, speaker quotes, volunteer recognition
- Impact numbers and what they mean

## Writing Rules for Recaps

- **Open with energy, not a summary**: "What an evening!" beats "On December 11, SAME SF hosted..."
- **Show, don't tell**: "The room held service members, industry partners, and first-time guests" beats "The event was well-attended"
- **Name names**: Every recap should mention at least 3-5 specific people or organizations
- **Numbers are emotional**: "$12,000 raised" means more when connected to "enough to fund 4 student scholarships"
- **Always include a next step**: Photo link, next event, or call to get involved

## After Generating

Offer to:
1. Generate recap graphics or photo carousel frames via `/post-graphic`
2. Save to Notion via `/save-to-notion`
3. Generate a matching thank-you email via `/email-campaign`
