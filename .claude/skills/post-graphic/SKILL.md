---
name: post-graphic
description: Generate LinkedIn post graphics and images for SAME SF using Gemini image generation. Auto-invoked when user says "create graphic", "make an image", "post graphic", "linkedin image", "generate graphic", or "design a post image".
---

# Post Graphic Generator

Generate branded LinkedIn graphics for SAME SF posts using image generation.

## Before Generating

1. **Read `data/brand-voice.md`** for visual tone guidance.
2. **Determine graphic type** based on the post content.

## SAME SF Visual Brand

### Colors (from official SAME logo)
- **SAME Red**: #C41E3A — primary accent, headlines, energy
- **SAME Blue**: #003478 — backgrounds, professional weight
- **White**: #FFFFFF — text on dark backgrounds, clean space
- **Dark gray**: #333333 — body text on light backgrounds
- **NO GOLD as default** — gold is not a SAME SF brand color

### Branch-Specific Color Exceptions
When creating graphics for a specific military branch event (birthday, observance), use that branch's official colors as accents alongside the SAME Blue background.

**Sources**: Federal Standard 595C, Pantone Matching System, official branch brand/design guides.

| Branch | Accent Colors | Hex (official) | Source |
|---|---|---|---|
| U.S. Army | Black + Army Gold | #000000 + #FFCB05 | Army Palette Card (DVIDSHUB) |
| U.S. Navy | Navy Blue + Gold | #003B4F + #E8B00F | Navy Design Guide (usnavy.github.io) |
| U.S. Marine Corps | Scarlet + Gold | #8C1717 + #CD7F32 | USMC Brand Guide 2009 |
| U.S. Air Force | Ultramarine Blue + Yellow | #00308F + #FFCD00 | USAF official, Pantone 116 |
| U.S. Coast Guard | CG Blue + Racing Stripe Orange | #003B71 + #CF4E38 | Pantone 307C + FS 595C #12250 |
| U.S. Space Force | Space Dark Blue + Silver | #0B1736 + #C0C0C0 | USSF Branding (restricted palette) |
| National Guard | Dark Blue + Gold | #003478 + #FFD700 | NGB Branding Guidelines |
| Seabees (NCB) | Navy Blue + Gold | #003B4F + #E8B00F | Follows USN colors |

**Important**: CG "orange" is actually a warm red-orange (#CF4E38), NOT bright orange. USMC gold is a bronze tone (#CD7F32), NOT bright yellow.

**Rule**: Branch colors are accent only (stripes, icons, small text). The SAME Blue background and white primary text stay consistent across all graphics.

### Typography Direction
- Bold, clean sans-serif for headlines
- Professional, readable for body text
- Military-inspired but modern — not overly formal

### Logo Files
- **Standard (white background)**: `assets/SanFranciscoPost-Logo.jpg`
- **Black version**: `assets/SanFranciscoPost-Logo-Black.png`
- **Transparent**: `assets/SanFranciscoPost-Logo-Transparent.png`
- Use transparent version for overlays on colored backgrounds
- Use black version on light/white backgrounds
- **Never ask Gemini to generate the logo** — AI-generated branding text is never accurate. Always composite the real file after generation using the Pillow step below.

## Graphic Types & Specifications

### LinkedIn Single Image Post
- **Size**: 1200 x 627 pixels
- **Use for**: Event announcements, military holidays, sponsor recognition

### LinkedIn Carousel Slide
- **Size**: 1080 x 1080 pixels (square)
- **Use for**: Throwbacks, Then & Now, scholarship spotlights, event recaps
- **Slides**: 4-8 per carousel

### Email Header
- **Size**: 600 x 200 pixels
- **Use for**: Mailchimp email headers

## Image Strategy — When to Generate vs. Use Real Photos

**Not every post needs a generated graphic.** Before generating, determine the right image approach:

| Post Type | Recommended Image | Why |
|---|---|---|
| Events at real venues (Gala, USCG Open House, Site Visits) | **Real photos** of the venue, or photorealistic generation | People connect with real places — warm and tangible |
| TBT / Event recaps | **Actual event photos** — do NOT generate | These posts ARE the photos |
| Member / Volunteer spotlights | **Real headshots** from the user | Authenticity matters |
| Military observances (branch birthdays) | **Generated branded graphic** | Works great — mascots, flags, bold text |
| Abstract concepts (Engineers Week, Call for Presentations) | **Generated graphic** or **text-only** | User's choice |
| Solemn observances (Memorial Day, 9/11, Pearl Harbor) | **Minimal generated graphic** or **none** | Less is more |

### Warmth & Personality Principles
- **Avoid flat corporate boxes.** If a graphic is just bold text on a navy rectangle, it's not adding value.
- **When a real place exists, show it.** CEU Oakland, Marines' Memorial, the Golden Gate Bridge — real imagery beats abstract every time.
- **Photorealistic generation** is an option: ask Gemini for a "warm, photorealistic image of [venue/location] at golden hour" style when no real photo is available but a real place is involved.
- **The Seabee Birthday graphic is the bar** — mascot, personality, movement. Not just text on a background.

## Text on Graphics — Less Is More

**8 words max on the image. Everything else goes in the post caption.**

People are already reading the LinkedIn caption. Duplicating details on the graphic is redundant and clutters the image. Mobile screens are small — text must be legible at phone size.

| Put ON the graphic | Put IN the caption |
|---|---|
| Event name (3-5 words) | Full description |
| Date | Agenda / schedule |
| ONE key detail (location OR "Free") | CTA / registration info |
| SAME SF branding | Hashtags, tagging, links |

**Examples:**
- Engineers Week graphic: "National Engineers Week" + "Feb 16-22, 2026" = 7 words
- USCG Industry Day: "USCG Industry Day" + "March 12 | CEU Oakland" + "Free" = 8 words
- Seabee Birthday: "Happy 84th Birthday, Seabees!" + "Can Do!" = 7 words

**Rule**: If you can't read every word on the graphic at phone screen size, there's too much text.

## Graphic Prompt Construction

When generating (after user confirms they want a graphic), construct the prompt with:

1. **Subject**: What the graphic shows
2. **Text overlay**: Key words/dates to include (keep to 5-8 words max)
3. **Style**: Match to post type (see below)
4. **Colors**: SAME Blue (#003478) + SAME Red (#C41E3A) + White — NO GOLD
5. **Mood**: Matches the post tone (celebratory, solemn, energetic, grateful)

### Style A — Branded Graphic (military observances, abstract concepts)
```
Professional LinkedIn graphic for a military engineering organization.
Dark blue background (#003478). Red (#C41E3A) accent elements. White text.
Subject: [what the image shows/represents]
Text: "[exact text for overlay]"
Style: Clean, modern, professional with subtle military/engineering aesthetic
Mood: [celebratory/solemn/energetic/informative]
Include visual elements with personality — icons, mascots, flags, or silhouettes that bring the graphic to life. Avoid flat empty backgrounds.
No logo, no watermark, no branding text, no text in the bottom right corner. Leave the bottom right corner clear.
```

### Style B — Photorealistic Venue/Location (events at real places)
```
Warm, photorealistic LinkedIn image for a professional engineering event.
Subject: [venue name and location — be specific]
Show: [exterior/interior, key architectural features, surrounding area]
Lighting: Warm, inviting — golden hour or well-lit interior
Text overlay: "[event name]" and "[date]" in clean white text with subtle dark overlay for readability
Colors: SAME Blue (#003478) and Red (#C41E3A) accent bars or borders
Mood: Welcoming, professional, makes the viewer want to attend
Photo-realistic quality, NOT illustrated or abstract.
```

## Generation Command

Use the Gemini image generation script. **Always specify the correct size.**

```bash
python "C:/Users/Mgbot/.claude/skills/gemini-image-gen/scripts/generate_image.py" \
  --prompt "YOUR PROMPT HERE" \
  --output "OUTPUT PATH" \
  --size "SIZE" \
  --style "professional" \
  --api-key "$GEMINI_API_KEY"
```

### Size defaults by type (MANDATORY — always pass `--size`):

| Type | `--size` value | When |
|---|---|---|
| LinkedIn single image | `1200x627` | **Default for all LinkedIn posts** |
| LinkedIn carousel slide | `1080x1080` | Throwbacks, Then & Now, recaps |
| Email header | `600x200` | Mailchimp email banners |

**If no type is specified, default to `1200x627` (LinkedIn post).**

### Output path convention:
- Campaign graphics: `campaigns/[campaign-name]/[graphic-name].png`
- Standalone graphics: `assets/standalone/[graphic-name].png`

## Graphic Types by Content

| Post Type | Recommended Approach | Style |
|---|---|---|
| Military birthday | Generated graphic — mascots, flags, personality | Style A |
| Event announcement (real venue) | Real photo or photorealistic generation | Style B |
| Sponsor recognition | Clean branded layout | Style A |
| Member spotlight | **Real headshot from user** — don't generate | N/A |
| Throwback Thursday | **Real event photos** — don't generate | N/A |
| Event recap | **Real event photos** — don't generate | N/A |
| Scholarship | Academic/STEM imagery | Style A |
| Solemn observance | Minimal graphic or text-only | Style A (muted) |
| Golf tournament | Real course photo or photorealistic | Style B |
| Gala | Real venue photo or photorealistic | Style B |

## Solemn Observance Graphics

For Memorial Day, Pearl Harbor, 9/11, Veterans Day:
- **Muted, respectful color treatment** (darker navy, minimal red)
- **No celebratory elements** (no confetti, no bright colors)
- **Simple composition** with plenty of negative space
- **Text**: Observance name + date only, no marketing language

## After Generating — MANDATORY Visual QA

**Every graphic MUST be visually inspected before it is considered done.** Use the Read tool to view each generated image, then run this checklist:

### Visual QA Checklist (check every item)
- [ ] **Brand colors**: Only SAME Red (#C41E3A), SAME Blue (#003478), and White. NO gold/yellow/orange UNLESS it's a branch-specific graphic using the official branch colors from the table above (e.g., CG red-orange #CF4E38, USMC scarlet #8C1717)
- [ ] **Text accuracy**: Every word spelled correctly — check "San Francisco", "Seabees", names, dates
- [ ] **No duplicate text**: Same words/phrases do not appear twice
- [ ] **Date accuracy**: All dates match the event details
- [ ] **Composition**: Not too busy — enough negative space, text is readable
- [ ] **Readability**: Text is large enough, sufficient contrast against background
- [ ] **Tone match**: Celebratory graphics look celebratory, solemn ones look solemn

### If any check fails:
1. Identify the specific issue
2. Regenerate with a corrected prompt that explicitly addresses the problem
3. Re-inspect the new graphic
4. Repeat until all checks pass

### After QA passes — Logo Compositing (event graphics only)

**When to include the logo:**
- Event announcements and campaign graphics — yes, SAME SF co-branding matters
- Sponsor recognition — yes
- Major milestone posts — yes

**When NOT to include the logo:**
- Observance graphics (branch birthdays, Military Appreciation Month, Memorial Day, etc.) — the occasion is the focus, not SAME SF branding
- TBTs and engagement posts — no logo needed
- Solemn observances — never

Never rely on Gemini to render the logo — AI-generated branding text is always inaccurate. When the logo IS needed, composite the real file using Pillow:

**Logo file**: `assets/SanFranciscoPost-Logo-Transparent.png` (use on dark backgrounds)

```python
from PIL import Image

base = Image.open("PATH/TO/GRAPHIC.png").convert("RGBA")
logo = Image.open("assets/SanFranciscoPost-Logo-Transparent.png").convert("RGBA")

# Resize logo to 180px wide, maintain aspect ratio
logo_w = 180
logo_h = int(logo.height * (logo_w / logo.width))
logo = logo.resize((logo_w, logo_h), Image.LANCZOS)

# Place bottom right with 20px padding
x = base.width - logo_w - 20
y = base.height - logo_h - 20

base.paste(logo, (x, y), logo)
base.save("PATH/TO/GRAPHIC.png")
```

Run this after every generation, before saving the final file. The intermediate no-logo file can be deleted after compositing.

### After logo compositing:
- Save graphics to campaign folder with `MM-DD-` date prefix
- Note the file path in the post content for reference
- Offer to generate additional sizes (carousel → single image, or vice versa)

## Skill Integration

This skill is called by other skills when graphics are needed:
- `/linkedin-sequence` → suggests graphics per post
- `/email-campaign` → suggests email header graphics
- `/event-campaign` → generates full graphics plan
- `/military-holiday` → generates observance graphic
- `/member-spotlight` → generates spotlight frame
- `/throwback` → generates vintage-styled graphic
