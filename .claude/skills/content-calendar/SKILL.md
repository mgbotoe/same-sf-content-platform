---
name: content-calendar
description: Plan a full month of SAME SF LinkedIn content with themes, military holidays, event campaigns, and posting schedule. Auto-invoked when user says "content calendar", "monthly plan", "what should we post", "plan the month", or "content schedule".
---

# Monthly Content Calendar Generator

Plan a full month of SAME SF LinkedIn content based on upcoming events, military holidays, recurring series, and content mix targets.

## Before Generating

1. **Read ALL data files**:
   - `data/military-holidays.md` — check for observances this month
   - `data/content-themes.md` — recurring series and content mix targets
   - `data/campaign-templates.md` — active campaign sequences
   - `data/brand-voice.md` — posting frequency and best practices

2. **Check the `campaigns/` directory** for any active campaign files.

## Input Required

Ask for any missing information:
- **Which month and year?**
- **Upcoming events**: Any SAME SF events this month or next?
- **Active campaigns**: Is a Golf Tournament, Gala, or Site Visit campaign running?
- **Special content**: Any members to spotlight, sponsors to recognize, announcements?
- **Last month's gaps**: Anything we missed or should follow up on?

## Calendar Output Format

### Monthly Overview
```
## [Month Year] Content Calendar — SAME SF

**Military observances this month**: [List from calendar]
**Active campaigns**: [Event campaigns in progress]
**Content mix target**: [X] posts total

| Week | Mon | Tue | Wed | Thu | Fri |
|---|---|---|---|---|---|
| Week 1 | | [Post] | | [Post] | |
| Week 2 | [Post] | | | [Post] | [Post] |
| Week 3 | | [Post] | | [Post] | |
| Week 4 | [Post] | | [Post] | [Post] | |
```

### Detailed Post Plan
For each planned post:
```
**[Date] — [Post Title/Topic]**
- Series: [#MemberMonday / #ThrowbackThursday / Campaign / Standalone]
- Content type: [Text / Image / Carousel / Poll]
- Brief: [1-2 sentence description of the post]
- Priority: [Must post / Recommended / Optional/flexible]
- Skill to use: [/linkedin-sequence / /military-holiday / /member-spotlight / /throwback / /event-recap]
```

## Content Mix Rules

Target distribution per month (from `content-themes.md`):

| Type | Target/Month | Notes |
|---|---|---|
| Event campaign posts | 3-5 | Tier 1 campaigns ~1/week; includes TBTs and sponsor spotlights that serve the campaign |
| Military observances | Per calendar | Non-negotiable. Never skip major ones |
| Member/volunteer spotlights | 1-2 | Highest per-post engagement |
| Scholarship/STEM | 1-2 | Peaks around Gala season |
| Throwback Thursday | 2-3 | Can serve campaigns (TBT to last year's event) |
| Industry/infrastructure | 1-2 | Site visit content |
| Community resources | As needed | Responsive to current events |

**Monthly budget check**: Sum the above — must stay at or under 12 total. In heavy campaign months, TBTs and spotlights can do double duty by tying into the event.

## Planning Rules

- **Posting frequency**: 1-2 posts/week baseline, up to 3/week max during campaigns
- **Hard cap**: 12 posts/month across all content types
- **Best days**: Tuesday, Wednesday, Thursday (primary). Friday morning secondary. Avoid weekends.
- **Best time**: 7:00 AM Pacific, every post (consistency matters — 6.1% vs 4.2% engagement)
- **Min gap**: 24+ hours between posts (algorithm promotes only 1 post/account/24hrs)
- **Never post promotional content** on the same day as a solemn military observance
- **Space campaign posts** at least 1 day apart
- **Include at least 1 non-campaign post per week** even during heavy campaigns
- **Thursday = #ThrowbackThursday** when no campaign post is scheduled
- **Monday = #MemberMonday** when no campaign post is scheduled
- **Never post 2 promotional posts back-to-back** — interleave with value content

## Campaign Tier Awareness

When planning months with active campaigns, check `data/campaign-templates.md` for the tier system:

- **Tier 1 (Gala, Golf Tournament)**: 8-10 week runway, ~1 campaign post/week. Start planning 3 months before event.
- **Tier 2 (Industry Day, Site Visit)**: 3-4 week runway, 2-4 total posts.
- **Tier 3 (Happy Hour, Meetup)**: 1-2 week runway, 1-2 total posts.

**Collision handling**: When a campaign post + observance + TBT land in the same week, cap at 3 total. Observances are non-negotiable (post day-of). Campaign posts flex. TBTs are most flexible — skip or shift.

## Email Calendar Integration

Also plan email sends that align with LinkedIn. Map each email type to its Mailchimp template:

| Email Purpose | Template | ID |
|---|---|---|
| Event Announcement | SAME SF Event Announcement | `11869797` |
| Event Reminder / Last Call | SAME SF Event Reminder | `11869798` |
| Know Before You Go | SAME SF Know Before You Go | `11869799` |
| Monthly Newsletter | SAME SF Newsletter Template v3 | `11869768` |

```
**Email [N]: [Type]**
- Send date: [Date]
- Template: [Template name + ID from table above]
- Aligns with LinkedIn post: [Which post]
- Purpose: [Invitation / Reminder / Thank you / Newsletter]
```

## After Generating

### MANDATORY steps (do not skip):
1. Generate all posts for the month using the appropriate skills
2. **Image checkpoint**: Present image recommendations for each post and ASK the user which ones to generate. Some posts work better with real photos or text-only. Graphics cost API money — never auto-generate without approval. See `/post-graphic` Image Strategy table.
3. Save the calendar to Notion via `/save-to-notion`
4. Create a campaign folder in `campaigns/[month-year]/`
5. **Create campaign kickoff reminders in Notion** (see below)

### Campaign Kickoff Reminders (Auto-Created in Notion)

After planning the month, look ahead 1-3 months for upcoming events that will need campaign runways. For each one, create a Notion Content Calendar entry as a reminder:

| Event Tier | Reminder Timing | Example |
|---|---|---|
| Tier 1 (Gala, Golf) | 10 weeks before event | Gala is Dec 10 → create reminder for Oct 1 |
| Tier 2 (Site Visit, Industry Day) | 4 weeks before event | Site Visit is Apr 15 → reminder for Mar 18 |
| Tier 3 (Happy Hour, Meetup) | 2 weeks before event | Happy Hour is Mar 20 → reminder for Mar 6 |

**Notion entry format for kickoff reminders:**
- **Title**: "START CAMPAIGN: [Event Name] ([Tier])"
- **Status**: "Idea"
- **Date**: The kickoff date (NOT the event date)
- **Post Type**: "Campaign"
- **Draft Content**: Include: event name, event date, tier level, number of posts needed, link to campaign template in `data/campaign-templates.md`, and the skill to use (`/event-campaign` or `/linkedin-sequence`)

**Also check**: Are there any kickoff reminders that should have been created for the CURRENT month? If so, flag them to the user immediately — don't just add them silently to Notion if the window is already open.

**Known annual events to always check:**

| Event | Month | Tier | Kickoff |
|---|---|---|---|
| Monthly Meeting w/Speaker | Monthly | 3 | 2 weeks before |
| Tinker Fest (USCG partnership) | June | 2 | May |
| Golf Tournament | July | 1 | May |
| A/E/C AI & Cybersecurity Summit | September | 1 | July |
| Member Appreciation | September | 2 | August |
| Dams & Levees (yearly or bi-yearly) | Varies (Mar?) | 2 | 4 weeks before |
| Holiday Gala | December | 1 | October |
| Site Visits | Quarterly | 2 | 4 weeks before |

### File Naming Convention
All post files and graphics use date prefixes: `MM-DD-[slug].md` and `MM-DD-[slug]-graphic.png`
This ensures the posting order is immediately visible in the folder.
