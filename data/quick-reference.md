# SAME SF Content Operations — Quick Reference

## What Do I Say?

| I need to... | Say this |
|---|---|
| Plan next month's posts | "content calendar for March" |
| Write LinkedIn posts for an event | "linkedin sequence for [event name]" |
| Run a full campaign (posts + emails + graphics) | "event campaign for [event name]" |
| Write a military observance post | "military holiday post for [observance]" |
| Feature a member, sponsor, or partner | "member spotlight for [name]" |
| Write a Throwback Thursday post | "throwback to [event/topic]" |
| Write a post-event recap | "event recap for [event name]" |
| Create a post graphic | "post graphic for [topic]" |
| Write a Mailchimp email | "email campaign for [event/topic]" |
| Push content to Notion | "save to notion" |
| Check how posts are doing | "performance review" |
| See what's coming up this month | "what's posting this month" |

## Posting Rules (Cheat Sheet)

- **When**: Tuesday, Wednesday, Thursday (primary). Friday morning OK.
- **Time**: 7:00 AM Pacific, every post. Always.
- **Frequency**: 1-2 posts/week baseline. Up to 3/week during campaigns.
- **Hard cap**: 12 posts/month. No exceptions.
- **Gap**: 24+ hours between posts.
- **Links**: Put registration links in first comment, not post body.
- **Mix**: Never post 2 promotional posts back-to-back.
- **Hashtag**: Always include `#SAMESF`.
- **Emojis**: 0-3 max. Zero on solemn observances.

## Campaign Tiers (How Far Ahead?)

| Event Type | Start Promoting | Total Posts |
|---|---|---|
| Gala / Golf Tournament | 8-10 weeks before | 8-10 posts |
| Site Visit / Industry Day | 3-4 weeks before | 2-4 posts |
| Happy Hour / Meetup | 1-2 weeks before | 1-2 posts |

## Content Mix Target

- 60% value content (spotlights, TBTs, stories)
- 25% thought leadership (industry, STEM, panel recaps)
- 15% promotional (register, join, donate)

## Send Day & Time Decision Guide

**LinkedIn posts — always 7:00 AM PT. Pick the day by content type:**

| Content type | Best day | Notes |
|---|---|---|
| Event announcement (first) | Tuesday | Best reach day, sets the week |
| Last call / reminder | Thursday | Close to weekend, creates urgency |
| Military observance | Day-of only | Non-negotiable — never early |
| Recap / TBT | Thursday | Lower stakes, later in week is fine |
| Thought leadership | Wednesday | Mid-week engagement peak |
| Newsletter promo | Tuesday | Drive opens before Thursday drop-off |

**Email (Mailchimp) — always 7:00 AM PT. Pick the day:**

| Email type | Best day | Avoid |
|---|---|---|
| Event announcement | Tuesday | Monday (low open), Friday (ignored) |
| Newsletter | Monday or Tuesday | Thursday/Friday (weekend near) |
| Last call / reminder | Tuesday or Wednesday | Thursday (too close to weekend) |
| Know Before You Go | Wednesday (2-3 days before event) | Day-of (too late) |

**Spacing rules when multiple sends are in the same week:**
- Email + LinkedIn same day: OK if different content
- Two emails same week: minimum 48-hour gap, different topics only
- Email announcement + LinkedIn last call: stagger by 3-5 days
- Never send email and post the same promo content on the same day

## When Things Collide (Same Week)

1. **Observances are non-negotiable** — post day-of, always
2. **Campaign posts flex** — bump by a day or shift to next week
3. **TBTs are most flexible** — skip or shift

Max 3 posts in any week, even during collisions.

## Approval Required

- Event posts and newsletters: **JR Gregory** must approve
- Military observances: Post **day-of only**, never early
- Solemn observances (Memorial Day, Pearl Harbor, 9/11): Confirm with user before drafting

## Files That Matter

| File | What's in it |
|---|---|
| `data/military-holidays.md` | All observances, founding years, ordinal reference |
| `data/brand-voice.md` | Voice rules, do/don't examples |
| `data/exclusion-list.md` | Banned AI words — read before every post |
| `data/content-themes.md` | Recurring series and content pillars |
| `data/campaign-templates.md` | Event campaign structures and tier system |

## Validation

After creating any campaign post, run:
```
python scripts/validate-dates.py
```
This checks day-of-week, ordinals, and founding years automatically.
