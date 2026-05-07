---
name: email-campaign
description: Generate Mailchimp-ready email content for SAME SF events and communications. Auto-invoked when user says "email campaign", "mailchimp", "newsletter", "email blast", "email sequence", or "send an email".
---

# Email Campaign Generator

Generate Mailchimp-ready email content for SAME SF events, newsletters, and communications.

## Before Generating

1. **Read these files** (every time):
   - `data/brand-voice.md` — tone rules
   - `data/exclusion-list.md` — banned words/phrases
   - `data/campaign-templates.md` — email template structures

2. **Determine email type** and select the matching Mailchimp template:

| Email Type | Template | Template ID |
|---|---|---|
| Event Announcement / Invitation | SAME SF Event Announcement | `11869797` |
| Event Reminder / Last Call | SAME SF Event Reminder | `11869798` |
| Know Before You Go (logistics) | SAME SF Know Before You Go | `11869799` |
| Monthly Newsletter | SAME SF Newsletter Template v3 | `11869768` |
| Welcome | Welcome New Subscribers | `11869770` |

> **⚠️ Mailchimp Classic Builder deprecated May 31, 2026.** After that date, all editing must happen in Mailchimp's New Builder UI. Until then, use `set_campaign_content_from_template` — do NOT use `set_campaign_content` with raw HTML for new campaigns.

## Input Required

Run this checklist. Ask for any missing items:
- **Email type**: Invitation / Reminder / Thank You / Newsletter / Custom
- **Event details**: Name, date, venue, registration link
- **Audience segment**: Members / Sponsors / DoD / Students / General
- **Tone**: Celebratory / Casual / Formal
- **CTA style**: Soft / Moderate / Strong
- **Key message**: What's the ONE thing the reader should do after reading?
- **Any specific content**: Quotes, stats, sponsor names to include
- **Repeat or first-time event?**

**Sensitivity check**: If this involves tragedy, disaster, or solemn content, PAUSE and confirm tone with the user before drafting.

**Output rule**: Always produce 2 subject line options + 1 alt opening line per email.

## Output Format

```
### Email [N]: [Type]
**Subject line**: [Under 50 characters]
**Preview text**: [Under 90 characters — what shows after subject in inbox]
**Send date**: [Suggested date]

---

[EMAIL BODY — Plain text with formatting notes]

**Header image suggestion**: [Description for graphic]

[Opening line — warm, direct, no "Dear Members"]

[Body — 3-4 short paragraphs max]

**[CTA BUTTON TEXT]** → [URL]

[Closing line]

[Signature: SAME San Francisco Post]

---

**Notes**: [Audience segment, A/B test suggestions, timing]
```

## Email Writing Rules

### Subject Lines
- Under 50 characters
- Create urgency OR curiosity, not both
- No ALL CAPS, no excessive punctuation
- Good: "Two days until the Gala" / "Your invite: Golf Tournament Aug 29"
- Bad: "EXCITING NEWS! Don't Miss This Amazing Event!!!"

### Body Content
- **Opening**: Skip "Dear Members" — start with energy or a direct statement
- **Length**: 150-250 words for invitations, 100-150 for reminders, 200-300 for recaps
- **Paragraphs**: 2-3 sentences max each
- **Formatting**: Use bold for key details (date, time, venue), bullet lists for logistics
- **CTA**: One primary CTA button per email, above the fold
- **Tone**: Same brand voice as LinkedIn but slightly more personal — you're in their inbox

### Mailchimp Specifics
- Write merge tags where appropriate: `*|FNAME|*` for personalization
- Suggest A/B test variants for subject lines
- Note any conditional content blocks (e.g., different content for members vs. prospects)

## Email Sequence Patterns

### Event Invitation Sequence (3-4 emails)
1. **Announcement** (6-8 weeks out): Save the date, early details
2. **Details + Early Bird** (4 weeks out): Full details, registration open
3. **Last Call** (1 week out): Final push, social proof, urgency
4. **Day-of Reminder** (morning of): Logistics, what to bring, excitement

### Post-Event Sequence (2 emails)
1. **Thank You** (1-2 days after): Highlights, gratitude, photos
2. **Impact Report** (1-2 weeks after): Stats, outcomes, next event teaser

## Monthly Newsletter Structure (8 Sections)

SAME SF newsletters follow this exact 8-section format:

1. **Welcome Note** — 2-3 sentences, warm tone, include LinkedIn follow reminder
2. **Spotlight Event** — Blue header bar, hero image, fundraising target, "Sponsorships Still Available!", tiered sponsor logos
3. **Partner Event** — Optional cross-promotion of related events
4. **Leadership/Conference Highlights** — When applicable, include member names and photos
5. **Recent Event Recap** — Photo from event, informal tone for casual events
6. **Military Observances** — List upcoming observances with brief acknowledgments and branch mottos
7. **Upcoming Events Calendar** — 3-4 months ahead
8. **Stay Connected Footer** — LinkedIn follow button, group photo, SAME logo

### Newsletter Visual Rules
- Header banner: Golden Gate Bridge with SAME branding
- Section headers: Navy blue bars with white text
- CTA buttons: Red ("Register Here", "Visit our website")
- Sponsor logos tiered by level:
  - Top tier: alone/centered
  - Second tier: row of 3-4
  - Third tier: row of 2-3
- Monthly cadence, typically first week of month

## After Generating

Offer to:
1. **Push to Mailchimp as draft** — Use `create_campaign` (audience ID: `9d174b3762`) + `set_campaign_content` to create a draft campaign directly in Mailchimp
2. Save to Notion via `/save-to-notion`
3. Generate matching LinkedIn posts via `/linkedin-sequence`
4. Create header graphics via `/post-graphic`

### Mailchimp Draft Workflow
```
1. create_campaign(list_id="9d174b3762", subject_line="...", preview_text="...",
                  from_name="SAME San Francisco Post", reply_to="samesanfrancisco@gmail.com")

2. set_campaign_content_from_template(campaign_id="<id>", template_id=<ID from table above>)
   — DO NOT use set_campaign_content(html=...) for new campaigns

3. User opens draft in Mailchimp UI, edits content sections, reviews layout

4. send_campaign(campaign_id="<id>", confirm=True) — or send from Mailchimp UI
```

**Template sections to fill per email type:**

Event Announcement (11869797): `preview_text`, `subtitle`, `eyebrow`, `headline`, `body_copy`, `event_details`, `signoff`, `cta_button` + update button href  
Event Reminder (11869798): same sections — `eyebrow` → urgency label (e.g. "Last Call"), `event_details` → include registration deadline line in red  
Know Before You Go (11869799): `preview_text`, `eyebrow`, `headline`, `body_intro`, `logistics`, `schedule`, `what_to_bring`, `contact`, `signoff`
