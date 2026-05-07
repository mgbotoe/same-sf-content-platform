---
name: linkedin-sequence
description: Generate a multi-post LinkedIn sequence for SAME SF events, campaigns, or initiatives. Auto-invoked when user says "linkedin posts", "post sequence", "linkedin campaign", "generate posts", or "posting schedule".
---

# LinkedIn Sequence Generator

Generate a multi-post LinkedIn sequence for SAME SF from raw content, event details, or campaign briefs.

## Before Generating

1. **Read these files** (every time, no exceptions):
   - `data/brand-voice.md` — tone and structure rules
   - `data/exclusion-list.md` — banned words/phrases
   - `data/content-themes.md` — hashtag strategy and series definitions
   - `data/campaign-templates.md` — sequence structures for known event types

2. **Identify the campaign type**: Golf Tournament, Holiday Gala, Site Visit, Member Appreciation, Military Holiday, or Custom.

3. **If it matches a known campaign type**, follow the sequence template from `campaign-templates.md`.

## Input Required

Run this checklist. Ask for any missing items:
- **Event/topic**: What is this about?
- **Key dates**: Event date, registration deadlines, early bird cutoffs
- **Number of posts**: How many posts in the sequence? (default: 5)
- **Key details**: Venue, speakers, sponsors, special guests, registration links
- **Photos/assets**: Any images to reference or describe for graphics?
- **Target audience**: Members / Sponsors / DoD / Students / General
- **Tone**: Celebratory / Casual / Formal / Solemn
- **CTA style**: Soft / Moderate / Strong
- **Repeat or first-time event?**

**Sensitivity check**: If this involves tragedy, disaster, or solemn content, PAUSE and confirm tone with the user before drafting.

## Output Format

For each post in the sequence, provide **two versions + one alt opening**:

```
### Post [N] of [Total] — [Category]
**Suggested date**: [Date]
**Content type**: [Text only / Single image / Carousel / Video]
**Audience**: [Primary audience segment]

---

**Version A (Short — 150-250 words)**:
[Punchy, scannable post text]

**Version B (Full — 300-500 words)**:
[Detailed post with more context]

**Alt opening**:
[One alternative first line or angle]

---

[Full post text, ready to copy-paste into LinkedIn]

---

**Hashtags**: #SAMESF [+ 2-4 relevant hashtags]
**Graphic suggestion**: [Brief description of recommended visual]
**Notes**: [Any tagging instructions, timing notes, or cross-promotion ideas]
```

## Quality Checklist

Before outputting each post, verify:
- [ ] First two lines pass the "so what?" test — would you stop scrolling?
- [ ] No words from the exclusion list
- [ ] No generic corporate openers ("excited to announce", "proud to share")
- [ ] Uses "we" language, not third-person
- [ ] Includes specific details (names, numbers, dates, places)
- [ ] Has a clear CTA on promotional posts
- [ ] 3-5 hashtags, always including #SAMESF
- [ ] Post length: 150-300 words (up to 500 for major recaps)
- [ ] Emojis: 0-2 max, none on solemn content
- [ ] Suggested graphic matches content type

## Sequence Pacing Rules

- **Don't repeat the same CTA** in consecutive posts — vary the angle
- **Alternate between** informational, emotional, and action-oriented posts
- **Space promotional posts** at least 1 day apart
- **Include at least 1 "human" post** per sequence (spotlight, story, behind-the-scenes)
- **Build a narrative arc**: tease → inform → engage → drive → celebrate

## After Generating

### Image Checkpoint (MANDATORY — do not skip)
After drafting all posts, present an **image recommendation table** and ASK the user before generating anything. Graphics cost API money — don't auto-generate.

```
| Post | Recommended Image | Action Needed |
|---|---|---|
| Post 1 — [Title] | Real photo of [venue] | User provides photo / Generate photorealistic / Skip |
| Post 2 — [Title] | Generated branded graphic | Generate? (Y/N) |
| Post 3 — [Title] | Real event photos | User provides / Skip |
| Post 4 — [Title] | Text-only post | No graphic needed |
```

**Wait for user to confirm** which graphics to generate. Only then invoke `/post-graphic` for approved items.

Refer to the Image Strategy table in `/post-graphic` SKILL.md for guidance on when to recommend real photos vs generated graphics vs text-only.

**Graphic naming**: `[MM-DD]-[post-slug]-graphic.png` (matches the post file naming convention)

### Then offer to:
1. Save the sequence to Notion via `/save-to-notion`
2. Generate matching Mailchimp emails via `/email-campaign`
