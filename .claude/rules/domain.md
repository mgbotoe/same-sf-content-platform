# Domain Rules — SAME SF Content Agent

## Content Generation

- **Read `data/exclusion-list.md` first.** Before any content generation, every time.
- **Run `python scripts/validate-dates.py`** after creating or editing any campaign file. Non-negotiable.
- **Every post passes the "so what?" test** — if a reader can't tell why they care in the first two lines, rewrite the opening.
- **No generic LinkedIn corporate speak** — "excited to announce", "thrilled to share", "proud to present" are banned.
- **Hashtags:** 3-5 max. Always `#SAMESF`. Contextual: `#AECCommunity`, `#MilitaryEngineers`, `#STEMeducation`, `#BayAreaInfrastructure`.
- **Version selection:** Version A (short) for solemn observances, reminders, TBT. Version B (full) for first announcements, milestones. When in doubt: B for the first post of the week, A for the second.

## Military Observances

- Respectful, factual tone. **No emojis on solemn observances** (Veterans Day, Memorial Day, 9/11, Pearl Harbor).
- Post day-of only — never schedule in advance.
- Derive ordinals from founding years in `data/military-holidays.md` — never calculate manually.

## Graphics

- **Always present an image recommendation table after drafting.** Ask which to generate.
- Not every post needs a generated graphic — some are better with real photos, some text-only.
- Graphics cost API money. Never auto-generate.
- Generated graphics must pass brand color check: SAME Red `#C41E3A`, SAME Blue `#003478`. No gold.

## Publishing Workflow

1. Draft content → validate dates → exclusion list check
2. Present graphic options → get approval
3. Sync to Notion via `/save-to-notion` → update status to `Review`
4. JR Gregory approval (event posts + newsletters)
5. Sync graphics to `samesf-graphics` GitHub repo
6. Publish / schedule

## Mailchimp

- `send_campaign` requires `confirm=True` AND explicit user approval in this session.
- Always `get_campaign` and show content for review before sending.
- Audience ID: `9d174b3762`. List label: `SAME San Francisco Post`.
- Free plan — no A/B tests, no advanced automation.

## Notion

- Do NOT create new databases. The Communications Hub already exists.
- Content Calendar status flow: `Idea → Drafting → Review → Scheduled → Posted`
- Version A goes in "Draft", Version B in "Alt Version", alt opening in "Notes".
