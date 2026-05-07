---
name: event-campaign
description: Generate a complete event campaign with LinkedIn posts, Mailchimp emails, graphics plan, and posting timeline. Auto-invoked when user says "full campaign", "event campaign", "campaign plan", "promote this event", or "marketing plan".
---

# Full Event Campaign Generator

Generate a complete multi-channel campaign for a SAME SF event — LinkedIn sequence + Email sequence + Graphics plan + Posting timeline.

## Before Generating

1. **Read ALL data files**:
   - `data/brand-voice.md`
   - `data/exclusion-list.md`
   - `data/content-themes.md`
   - `data/campaign-templates.md`
   - `data/military-holidays.md` (check for conflicts or tie-in opportunities)

2. **Identify event type** and pull the matching template from `campaign-templates.md`.

## Input Required

Run this checklist. Ask for any missing items:
- **Event name**: What is it?
- **Event date**: When?
- **Venue**: Where?
- **Registration link**: URL
- **Key people**: Speakers, hosts, special guests
- **Sponsors**: Confirmed sponsors and their tiers
- **Target audience**: Members / Sponsors / DoD / Students / General
- **Tone**: Celebratory / Casual / Formal
- **CTA style overall**: Soft → Strong ramp or consistent moderate
- **Budget/scope**: How many posts? How many emails? Graphics needed?
- **Special elements**: Scholarships, awards, entertainment, traditions
- **Photos available**: Historical or current photos to use
- **Repeat or first-time event?**

**Sensitivity check**: If this involves solemn content, PAUSE and confirm before drafting.

**Output rule**: Each LinkedIn post in the campaign must include Version A (short) + Version B (full) + 1 alt opening. Emails include 2 subject line options + 1 alt opening.

## Output Structure

### 1. Campaign Overview
```
**Event**: [Name]
**Date**: [Date]
**Campaign window**: [Start date] → [End date]
**Channels**: LinkedIn ([X] posts) + Email ([X] emails) + Graphics ([X] assets)
```

### 2. Master Timeline
A unified calendar showing when each piece publishes across all channels:

```
| Date | Channel | Content | Status |
|---|---|---|---|
| [Date] | LinkedIn | Post 1: Save the Date | Draft |
| [Date] | Email | Email 1: Announcement | Draft |
| [Date] | LinkedIn | Post 2: Sponsor reveal | Draft |
| ... | ... | ... | ... |
```

### 3. LinkedIn Sequence
Follow the `/linkedin-sequence` format for each post.

### 4. Email Sequence
Follow the `/email-campaign` format for each email. Use the Mailchimp template workflow — map each email to the correct template ID (see `/email-campaign` template table: Announcement `11869797`, Reminder `11869798`, Know Before You Go `11869799`).

### 5. Graphics Plan
For each visual asset needed:
```
**Asset [N]**: [Description]
**Used in**: Post [X], Email [Y]
**Format**: [LinkedIn single image 1200x627 / Carousel 1080x1080 / Email header 600x200]
**Key elements**: [Text, logos, photos needed]
```

### 6. Cross-Promotion Opportunities
- Military holidays that fall within the campaign window
- SAME National content to reshare
- Partner organizations to tag or cross-post with
- Sacramento Post or other regional tie-ins

## Campaign Quality Rules

- **No two consecutive LinkedIn posts** should have the same angle or CTA
- **Email and LinkedIn content** should complement, not duplicate
- **At least 30% of posts** should be non-promotional (stories, spotlights, throwbacks)
- **Check military holidays calendar** for conflicts (don't promote an event on a solemn day)
- **Plan for engagement**: Include at least 1 interactive element (poll, question, tag challenge)

## After Generating

1. Save the full campaign to `campaigns/[event-name]-[year]/` directory
2. Offer to push to Notion via `/save-to-notion`
3. Offer to generate all graphics via `/post-graphic`
