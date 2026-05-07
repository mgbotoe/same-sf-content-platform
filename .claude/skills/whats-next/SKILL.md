---
name: whats-next
description: Check what's coming up for SAME SF content — upcoming posts, pending reviews, observances, and campaign kickoffs. Auto-invoked when user says "what's next", "what's posting", "posting opportunities", "what should we post", "what's coming up", or "this month".
---

# What's Next — Posting Opportunity Scanner

Scan the content calendar, military holidays, campaign files, and Notion to give the user a clear picture of what's coming up and what needs attention.

## When to Run

This skill is the **starting point** for any content planning session. Run it when the user asks:
- "What's next?"
- "What's posting this month?"
- "What are the posting opportunities?"
- "What should we work on?"
- "What's coming up?"

## Data Sources to Check

### 0. Mailchimp — Scheduled Campaigns (ALWAYS check first)
Pull scheduled campaigns via `mcp__mailchimp__list_campaigns` with `status: "schedule"`. Report:
- Campaign name, subject line, scheduled send date/time (convert to PT)
- Flag anything sending within 7 days as **IMMINENT**
- Cross-check against `campaigns/_index.md` — if a campaign is scheduled in Mailchimp but not reflected in the index, update the index

### 1. Military Holidays (check second)
Read `data/military-holidays.md` and identify:
- Any observances in the **current month** or **next 30 days**
- Whether a post already exists for each one (check `campaigns/` directory)
- Flag any observances that DON'T have a post file yet

### 2. Notion Content Calendar
Query the Content Calendar database (`e711f5af-58c2-4d7e-bfe8-d577c06b10e1`) and report:
- **Scheduled**: Posts with status "Scheduled" — these are ready to go
- **Review**: Posts with status "Review" — these need JR Gregory's approval
- **Drafting**: Posts still being worked on
- **Idea**: Posts that are just concepts, not yet written

Use Notion search or fetch to get current entries. Filter by the current month and next month.

### 3. Campaign Files
Check the `campaigns/` directory for:
- Which months have folders and post files
- Any months with NO content yet (gap alert)
- Active campaign sequences (multi-post files)

### 4. Campaign Kickoff Alerts
Cross-reference `data/campaign-templates.md` tier system against known events:

| Event | Month | Tier | When to Start |
|---|---|---|---|
| Monthly Meeting w/Speaker | Monthly | Tier 3 | 2 weeks before (confirm date + speaker with JR) |
| Tinker Fest (USCG partnership) | June | Tier 2 | May (3-4 weeks out) |
| Golf Tournament | July | Tier 1 | May (8-10 weeks out) |
| A/E/C AI & Cybersecurity Summit | September | Tier 1 | July (8-10 weeks out) |
| Member Appreciation | September | Tier 2 | August (3-4 weeks out) |
| Dams & Levees (yearly or bi-yearly) | Varies | Tier 2 | 4 weeks before |
| Holiday Gala | December | Tier 1 | October (8-10 weeks out) |
| Site Visits | Quarterly | Tier 2 | 4 weeks before |

If the current date falls within a campaign kickoff window, alert the user.

### 5. Posting Frequency Check
Count posts in the current month and check against limits:
- Are we on track for 8-12 posts this month?
- Have we exceeded 3 posts in any week?
- Are we spacing posts 24+ hours apart?
- Is the content mix healthy? (60% value / 25% thought leadership / 15% promotional)

## Output Format

Present a clear, scannable summary:

```
## [Month Year] — Content Status

### Mailchimp Queue
- [Campaign name] — sends [Day, Date] at 7:00 AM PT ⚡ IMMINENT (if within 7 days)
- [Campaign name] — sends [Date]

### This Week
- [Day]: [Post title] — [Status: Scheduled/Review/Draft]
- [Day]: [Post title] — [Status]

### Upcoming Observances (Next 30 Days)
- [Date]: [Observance] — [Has post? Yes/No] [If no: "NEEDS POST"]
- [Date]: [Observance] — [Has post? Yes/No]

### Campaign Kickoffs Needed
- [Event]: Tier [N], should start [date range] — [Started? Yes/No]

### Posts Needing Attention
- [Post title] — Status: Review (needs JR Gregory approval)
- [Post title] — Status: Drafting (incomplete)

### Month Stats
- Posts this month: [N] of 12 max
- Posts this week: [N] of 3 max
- Content mix: [X]% value / [X]% thought leadership / [X]% promotional

### Recommendations
- [Actionable suggestion based on gaps]
```

## Rules

- **Don't generate content** — this skill only reports what's needed. Let the user decide what to create next.
- **Always show the "NEEDS POST" flag** for observances without content files.
- **Always show campaign kickoff alerts** if we're inside or approaching a kickoff window.
- **Be honest about gaps** — if there's nothing scheduled for next week, say so.
- **Reference the right skill** for each gap — e.g., "Use `/military-holiday` for the Seabee Birthday post."
