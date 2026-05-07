# Mailchimp Newsletter Template Section Map

**Template ID**: 11869768
**Template defaults**: `scripts/template_defaults.json`
**Total sections**: 80

This maps every editable section name to its visual position in the newsletter.
Use this when building newsletter content to put things in the RIGHT section.

---

## Visual Order (top to bottom)

### 1. Preview & Header

| Section | Purpose | Notes |
|---|---|---|
| `preview_text` | Email preview text (inbox snippet) | Plain text, no HTML |
| `header_image` | Banner image at very top | Links to LinkedIn page |
| `header_subtitle` | "March 2026 Newsletter" line | Below banner |
| `header_tagline` | "Strengthening community through..." | Below subtitle |

### 2. Welcome Block

| Section | Purpose | Notes |
|---|---|---|
| `welcome_heading` | Welcome section title | e.g., "Welcome to 2026" |
| `welcome_image` | Optional image in welcome area | Can be empty |
| `welcome_body` | Main welcome paragraph(s) | Keep short, tease what's below |
| `welcome_closing` | Closing line with link | e.g., "Follow us on LinkedIn" |
| `welcome_button` | Optional CTA button | Can be empty |

### 3. Photo Gallery

| Section | Purpose | Notes |
|---|---|---|
| `photo_gallery_heading` | Gallery title + label | e.g., "OUR POST IN ACTION" |
| `photo_gallery_img_1` | Top-left photo | Full img tag with src |
| `photo_gallery_img_2` | Top-right photo | Full img tag with src |
| `photo_gallery_img_3` | Bottom-left photo | Full img tag with src |
| `photo_gallery_img_4` | Bottom-right photo | Full img tag with src |
| `photo_gallery_caption` | Caption below photos | Italic, centered |
| `photo_gallery_button` | "View All Photos" button | Can be empty |

### 4. Quote Block

| Section | Purpose | Notes |
|---|---|---|
| `quote_text` | Pull quote in large text | e.g., Sid Osgood quote |
| `quote_attribution` | Quote attribution line | Name, title, credentials |

### 5. Event Spotlight (USCG block)

**THIS IS THE EVENT SPOTLIGHT SECTION.** Originally built for USCG Industry Day.
Reuse for whatever the current featured event is.

| Section | Purpose | Notes |
|---|---|---|
| `uscg_heading` | Event label + title | e.g., "SPOTLIGHT EVENT" + event name |
| `uscg_image` | Event flyer/image | Can be empty |
| `uscg_body` | Event description paragraphs | Main content |
| `uscg_details` | Date/time/location table | Structured details |
| `uscg_closing` | Additional info (pricing, eligibility) | Good for pricing callout |
| `uscg_button` | "Register Now" CTA button | Links to registration |
| `uscg_disclaimer` | Small disclaimer text | Can be empty |

### 6. Save the Date

| Section | Purpose | Notes |
|---|---|---|
| `save_date_heading` | Label + event name | e.g., "SAVE THE DATE" + Golf Tournament |
| `save_date_body` | Description | Brief teaser |
| `save_date_callout` | Date callout box | Highlighted date |
| `save_date_button` | CTA button | e.g., "I'm Interested!" |

### 7. Speakers / Get Involved

| Section | Purpose | Notes |
|---|---|---|
| `speakers_heading` | Label + title | e.g., "GET INVOLVED" + "Share Your Expertise" |
| `speakers_body` | Description | Call for speakers, volunteer ask, etc. |
| `speakers_button` | CTA button | e.g., "Submit a Topic" |

### 8. STEM & Scholarships

| Section | Purpose | Notes |
|---|---|---|
| `stem_heading` | Label + title | e.g., "STEM & SCHOLARSHIPS" |
| `stem_image` | Optional image | Can be empty |
| `stem_body` | Content paragraphs | Scholarship updates, recap, etc. |
| `stem_button` | CTA button | Can be empty |

### 9. Engineers Week / Community

| Section | Purpose | Notes |
|---|---|---|
| `engineers_week_heading` | Label + title | e.g., "COMMUNITY" + topic |
| `engineers_week_body` | Content paragraphs | Flexible community content |
| `engineers_week_button` | CTA button | Can be empty |

### 10. New Members

| Section | Purpose | Notes |
|---|---|---|
| `new_members_heading` | Label + title | "WELCOME ABOARD" + "New Members" |
| `new_members_body` | Welcome text + member names | |
| `new_members_button` | "Become a Member" button | |

### 11. News / Industry Briefs

| Section | Purpose | Notes |
|---|---|---|
| `news_heading` | Label + title | e.g., "INDUSTRY NEWS" or "MARCH IN REVIEW" |
| `news_item_1` | First news brief | Title + short description |
| `news_item_2` | Second news brief | Title + short description |
| `news_item_3` | Third news brief | Can be empty |

### 12. Sponsors

| Section | Purpose | Notes |
|---|---|---|
| `sponsors_heading` | Label + title | "OUR PARTNERS" |
| `sponsor_top` | Top sponsor tier label | e.g., "DIAMOND PARTNER" |
| `sponsor_col_1` | Sponsor logo 1 | img tag |
| `sponsor_col_2` | Sponsor logo 2 | img tag |
| `sponsor_col_3` | Sponsor logo 3 | img tag |
| `sponsor_col_4` | Sponsor logo 4 | img tag |
| `sponsor_col_5` | Sponsor logo 5 | img tag |
| `sponsors_closing` | "Interested in partnering?" line | |

### 13. Member Spotlight + Honoring Service (side by side)

| Section | Purpose | Notes |
|---|---|---|
| `member_spotlight` | Left column — spotlight or "What's Next" | Flexible content |
| `honoring_service` | Right column — upcoming observances | Military holidays |

### 14. Upcoming Events Calendar

| Section | Purpose | Notes |
|---|---|---|
| `events_heading` | Label + title | "WHAT'S AHEAD" + "2026 at a Glance" |
| `event_date_1` | Date column row 1 | e.g., "APR 16" |
| `event_desc_1` | Description column row 1 | Event name + brief |
| `event_date_2` through `event_date_7` | Date rows 2-7 | |
| `event_desc_2` through `event_desc_7` | Description rows 2-7 | |
| `events_closing` | Closing text | "Stay tuned for more details!" |
| `events_button` | "See All Events" button | |

### 15. Footer

| Section | Purpose | Notes |
|---|---|---|
| `footer_heading` | "Let's Stay Connected" | |
| `footer_text` | Follow us text | |
| `footer_image` | Photo (clickable, links to LinkedIn) | |
| `footer_button` | "Follow Our LinkedIn" button | |
| `footer_social` | Social media links | LinkedIn, email, website |
| `footer_logo` | SAME SF logo | Centered |
| `footer_legal` | Copyright + unsubscribe | |

---

## Section Naming Conventions

- Sections prefixed with `uscg_` = **Event Spotlight** (reusable for any featured event)
- Sections prefixed with `stem_` = **STEM & Scholarships** (reusable for any content block)
- Sections prefixed with `engineers_week_` = **Community content** (reusable)
- `_heading` = label + title at top of block
- `_body` = main content paragraphs
- `_button` = CTA button (set to empty string to hide)
- `_image` = optional image (set to empty string to hide)

## How to Clear a Section

Set the section value to an empty string `""` to hide content. Note: the container/wrapper may still render as an empty block in some cases. If so, hide the block in the Mailchimp editor.

## Critical Rule

**Never push partial sections.** Always load ALL 80 defaults from `scripts/template_defaults.json` first, then overlay changes. Otherwise unlisted sections revert to template defaults and wipe manual edits.
