# Hot Memory

Always loaded into context. Keep under 2500 tokens.
Detailed context lives in `memory/*.md` — search on-demand, don't duplicate here.

## Current State

- **Active campaigns:** Feb–Dec 2026 planned in `campaigns/` (31 posts)
- **Content calendar:** Notion DB `e711f5af-58c2-4d7e-bfe8-d577c06b10e1`
- **Mailchimp:** SAME SF account, ~978 subscribers, Audience ID `9d174b3762`, 325 campaigns sent
- **Graphics repo:** `C:\Workspace\samesf-graphics` — hosted at `https://raw.githubusercontent.com/mgbotoe/samesf-graphics/main/campaigns/...`
- **Approval gate:** JR Gregory approves event posts + newsletters before publish
- **Observance posts:** Day-of only, never scheduled in advance
- **Date validation:** Always run `python scripts/validate-dates.py` before marking any campaign complete

## Active Work

- **Mine Cleanup email** — Scheduled May 12 at 7 AM PT (Campaign `3619932539`). Registration link still needed for May 18 newsletter + LinkedIn update.
- **May 18 Newsletter** — Draft ready (`05-18-may-newsletter.md`, template `11869800`). Blocked on Mine Cleanup registration link.
- **Geospatial recap** (May 5) — Needs photos before drafting.
- **Mine Cleanup LinkedIn** (May 7) — JR Gregory approved (2026-05-04). Version A + graphic ready to post.
- **Military Appreciation Month** (May 11) — Scheduled.
- **KBYG template** (`11869799`) — Needs New Builder version before May 31, 2026.
- **Folder restructure** — Approved in principle. Not yet executed. See `memory/decisions.md`.
- **3 .mil addresses** (MacCumbee, Jenkinson, Anaya) — Must be added to Mailchimp manually via UI.

## Key Facts

- SAME SF brand colors: Red `#C41E3A`, Blue `#003478`, White `#FFFFFF` — NO GOLD
- Primary hashtag: `#SAMESF` on every post
- Banned phrases: `data/exclusion-list.md` — read before every content generation
- Version A = short (solemn, reminders, TBT), Version B = full (first announcements, milestones)
- Mailchimp `send_campaign` requires `confirm=True` — never send without explicit approval
- Gemini API key: in `.env` — never hardcode

## Key People

- Madina Gbotoe — content creator / communications
- JR Gregory, P.L.S. — approval gate for event posts + newsletters
- Scott MacCumbee, PE — Incoming President
- Isabel Andaya, EIT — Young Professional leader
- Steven "Sid" Osgood, P.E., PMP, F.SAME — Past President, USCG

## Standing Rules

## Session Log

- [2026-05-03] Major SOUL.md overhaul: added Marketing Brain (5 frameworks), Campaign Stack (Hero/Hub/Hygiene + tiers), Campaign Brief Standard, Measurement Instinct, Audience Segmentation, Campaign Retrospective, Posting Guardrails, Escalation Protocol
- [2026-05-03] Exclusion list expanded: 10 new banned words + Banned Structural Patterns section
- [2026-05-03] Fixed Mailchimp cta_button push pattern — mc:edit must wrap full button HTML including VML + href. Both Event Announcement (11869797) and Event Reminder (11869798) templates rebuilt and patched.
- [2026-05-03] Mine Cleanup email scheduled: May 12 at 7 AM PT
- [2026-05-03] Member sync: 64 new subscribers added, 197 tagged as Members, sync script built (`scripts/sync-members.py`), quarterly cadence (Mar/Jun/Sep/Dec)
- [2026-05-03] Heartbeat Standing Rule added — `/loop 30m /heartbeat` at every session start, mandatory
- [2026-05-03] SOUL.md: Military & AEC Audience Layer added; sub-deadline rule + runway calc in Campaign Intake; observance closing-question rules; logo rule for graphics
- [2026-05-04] JR approved Mine Cleanup LinkedIn (May 7). Military Appreciation scheduled. Auto-promote hook wired to SessionStart.
- [2026-05-05] Drafted Mine Cleanup LinkedIn Event page (plain text, official EPA language). Event share post approved. Duplicate files pending cleanup.
