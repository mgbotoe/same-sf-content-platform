# SAME SF Newsletter — Stripo Setup Guide

Build our newsletter template once in Stripo, then reuse it every month. Full drag-and-drop editing, 1-click export to Mailchimp.

---

## Step 1: Create a Free Stripo Account

1. Go to **https://stripo.email**
2. Click **"Sign Up"** (top right)
3. Sign up with Google or email — free plan is all you need
4. Once logged in, you'll see your dashboard

---

## Step 2: Start a New Template

1. Click **"New Template"** button
2. Choose **"Start from scratch"** (we'll build our own design)
3. Pick **"Basic"** as the starting structure (1-column)

---

## Step 3: Set Global Styles First

Before adding any content, set the overall look. Click the **General Settings** tab (gear icon):

### Email Settings
- **Email width**: 660px
- **Background color** (canvas/outer): `#EAEDF2` (light gray)
- **Content area background**: `#FFFFFF` (white — this is the default card color)

### Typography
- **Headings font**: Georgia, serif
- **Headings color**: `#003478` (SAME Blue)
- **Body font**: Arial, sans-serif
- **Body text color**: `#374151`
- **Body text size**: 16px
- **Line height**: 1.6
- **Link color**: `#003478`

### Buttons (global)
- **Background color**: `#C41E3A` (SAME Red)
- **Text color**: `#FFFFFF`
- **Border radius**: 24px (pill shape)
- **Font size**: 16px, Bold
- **Padding**: 14px top/bottom, 36px left/right

---

## Step 4: Build Each Section

Build the newsletter top-to-bottom. Each section below maps to a Stripo block.

### SECTION 1: Header Card
**Stripo block**: Image + Text

1. Drag an **Image** block → This is where the SAME SF banner goes
   - Upload: `assets/SanFranciscoPost-Logo.jpg` or your existing banner
   - Link to: `https://www.linkedin.com/company/society-of-amercian-military-engineers-san-francisco-post/`
   - Background color of row: `#003478` (SAME Blue)

2. Below the image, drag a **Text** block:
   - Line 1: **SAME SF Post** — Georgia, 28px, Bold, `#003478`, centered
   - Line 2: **February 2026 Newsletter** — Arial, 16px, `#6B7280`, centered
   - Line 3: *Strengthening community through service, leadership, and collaboration.* — Georgia, 14px, italic, `#6B7280`, centered

3. **Card styling** for this row:
   - Background: `#FFFFFF`
   - Border: 1px solid `#D1D5DB`
   - Padding: 0 on image, 32px on text

---

### RED DIVIDER DASH (between sections)
**Stripo block**: Spacer + Custom HTML (or thin image)

- Insert a **Spacer** block, then inside it place a small centered element:
  - Width: 120px
  - Height: 3px
  - Color: `#C41E3A` (SAME Red)
- OR: Use a **Divider** block set to 3px, `#C41E3A`, 120px wide, centered

---

### SECTION 2: Welcome Card
**Stripo block**: Text (with optional Image)

1. **Row background**: `#F0F4FF` (light blue)
2. **Top accent bar**: Add a 6px tall row/stripe at the top with background `#C41E3A`
   - Easiest way: Add a **Spacer** block at top of this section, set height to 6px, background `#C41E3A`
3. **Border**: 1px solid `#D1D5DB`
4. **Content**:
   - Optional: Scott MacCumbee headshot (120px circle)
   - Heading: **Welcome to 2026** — Georgia, 24px, Bold, `#003478`
   - Body paragraphs (16px, `#374151`, Arial)
   - LinkedIn link in text

---

### SECTION 3: USCG Industry Day (Spotlight)
**Stripo block**: Text + Image + Button

1. **Row background**: `#FFFFFF`
2. **Top accent bar**: 6px, `#CF4E38` (CG Orange — ONLY this section uses orange)
3. **Border**: 1px solid `#D1D5DB`
4. **Content**:
   - Label: **SPOTLIGHT EVENT** — 12px, Bold, `#CF4E38`, uppercase, letter-spacing 1.5px
   - Heading: **USCG Industry Day & Open House** — Georgia, 24px, Bold, `#003478`
   - Sub: Co-hosted by... — 14px, Bold, `#374151`
   - Image: USCG flyer (upload from `campaigns/03-uscg-open-house-2026/`)
   - Body text paragraphs
   - Bullet list (What you'll get)
   - **Event details box**: Nested container with:
     - Background: `#F9FAFB`
     - Border: 1px solid `#E5E7EB`
     - Left border: 4px solid `#CF4E38`
     - Date, Time, Location, Cost, After fields
   - Button: **Register Now** → link TBD
   - Disclaimer text: 12px, italic, `#6B7280`

---

### RED DIVIDER DASH
(same as above — 120px, 3px, `#C41E3A`)

---

### SECTION 4: Engineers Week
**Stripo block**: Text

1. **Row background**: `#F0F4FF`
2. **Top accent bar**: 6px, `#C41E3A` (SAME Red)
3. **Border**: 1px solid `#D1D5DB`
4. **Content**:
   - Label: **COMMUNITY** — 12px, Bold, `#C41E3A`, uppercase
   - Heading: **It's National Engineers Week!** — Georgia, 24px, Bold
   - 3 body paragraphs

---

### SECTION 5: Call for Speakers
**Stripo block**: Text + Button

1. **Row background**: `#FFFFFF`
2. **Top accent bar**: 6px, `#C41E3A`
3. **Border**: 1px solid `#D1D5DB`
4. **Content**:
   - Label: **GET INVOLVED** — 12px, Bold, `#C41E3A`, uppercase
   - Heading: **Share Your Expertise** — Georgia, 24px, Bold
   - 3 body paragraphs
   - Button: **Submit a Topic** → `mailto:samesanfrancisco@gmail.com?subject=Presentation%20Submission`

---

### SECTION 6: Two Mini-Cards (Side by Side)
**Stripo block**: 2-Column layout

1. **Left column** — Member Spotlight:
   - Background: `#FFFFFF`, Border: 1px solid `#D1D5DB`
   - Label: **MEMBER SPOTLIGHT** — 11px, Bold, `#C41E3A`, uppercase
   - Optional: Sam Lee headshot (100px circle)
   - Text about Sam Lee + SAME Fellows

2. **Right column** — Honoring Service:
   - Background: `#FFFFFF`, Border: 1px solid `#D1D5DB`
   - Label: **HONORING SERVICE** — 11px, Bold, `#C41E3A`, uppercase
   - Seabee Birthday text
   - "We're proud to stand alongside those who serve, lead, and build."

---

### RED DIVIDER DASH
(same — 120px, 3px, `#C41E3A`)

---

### SECTION 7: Upcoming Events Timeline
**Stripo block**: Text (or Table)

1. **Row background**: `#FFFFFF`
2. **Top accent bar**: 6px, `#C41E3A`
3. **Border**: 1px solid `#D1D5DB`
4. **Content**:
   - Label: **WHAT'S AHEAD** — 12px, Bold, `#C41E3A`, uppercase
   - Heading: **2026 at a Glance** — Georgia, 24px, Bold
   - Timeline rows (each row = date badge + event name):
     - Date badges: Background `#003478`, white text, 12px bold, rounded 4px
     - MAR 12 — USCG Industry Day
     - APR TBD — Monthly Meeting w/Speaker
     - JUN TBD — Tinker Fest
     - JUL TBD — Annual Golf Tournament
     - SEP TBD — A/E/C AI & Cybersecurity Summit
     - SEP TBD — Member Appreciation Day
     - DEC 10 — Annual Holiday Gala
   - Thin dividers between rows: 1px `#E5E7EB`
   - Button: **Visit Our Website** → `https://www.same.org/sf`

---

### SECTION 8: Footer (Navy Card)
**Stripo block**: Text + Image + Button + Social Links

1. **Row background**: `#003478` (SAME Blue — dark card)
2. **All text color**: `#FFFFFF`
3. **Content**:
   - Heading: **Let's Stay Connected** — Georgia, 24px, Bold, white
   - Two columns:
     - Left: body text (15px, white)
     - Right: Group photo (optional, upload)
   - Button: **Follow Our LinkedIn** — White background (`#FFFFFF`), blue text (`#003478`), pill shape
   - Social links: LinkedIn | Email | Website — white links
   - White divider line (1px)
   - SAME SF logo (upload `assets/SanFranciscoPost-Logo-Transparent.png`, 220px wide)
   - Copyright text — 12px, `#AAAAAA`
   - Unsubscribe/Update preferences links

---

## Step 5: Connect Mailchimp + Export

1. In Stripo, go to **Export** (top right)
2. Choose **Mailchimp** from the integrations list
3. Connect your Mailchimp account (one-time OAuth login)
4. Select your audience (SAME San Francisco Post)
5. Click **Export** — it pushes the template directly to Mailchimp

---

## Step 6: Monthly Reuse Workflow

Every month, you'll do this:

1. **Open Stripo** → Find your saved "SAME SF Newsletter" template
2. **Duplicate it** → Name it "March 2026 Newsletter" (or whatever month)
3. **Edit content**:
   - Drag to rearrange sections
   - Click any text to edit it
   - Click images to swap them
   - Delete sections you don't need this month
   - Add new sections by dragging blocks
4. **Export to Mailchimp** → 1-click push
5. **Send from Mailchimp** as usual

---

## Design Specs Quick Reference

### Colors
| Name | Hex | Where |
|---|---|---|
| SAME Blue | `#003478` | Headings, date badges, footer card |
| SAME Red | `#C41E3A` | Accent bars, labels, buttons, divider dashes |
| CG Orange | `#CF4E38` | USCG section ONLY (accent bar, label, event box border) |
| Canvas Gray | `#EAEDF2` | Email background (outer) |
| Card White | `#FFFFFF` | Most card backgrounds |
| Card Light Blue | `#F0F4FF` | Welcome + Engineers Week cards |
| Body Text | `#374151` | Main paragraph text |
| Secondary Text | `#6B7280` | Labels, subtitles, disclaimers |
| Border Gray | `#D1D5DB` | Card borders |
| Divider Gray | `#E5E7EB` | Inner divider lines |
| Footer Muted | `#AAAAAA` | Copyright, footer fine print |

### Fonts
| Element | Font | Size | Weight |
|---|---|---|---|
| Main heading (SAME SF Post) | Georgia | 28px | Bold |
| Section headings | Georgia | 24px | Bold |
| Section labels (COMMUNITY, etc.) | Arial | 12px | Bold, UPPERCASE |
| Mini-card labels | Arial | 11px | Bold, UPPERCASE |
| Body text | Arial | 16px | Normal |
| Mini-card body text | Arial | 15px | Normal |
| Footer text | Arial | 15px | Normal |
| Disclaimer/fine print | Arial | 12px | Normal/Italic |

### Buttons
| Style | Background | Text Color | Border Radius |
|---|---|---|---|
| Primary (red pill) | `#C41E3A` | `#FFFFFF` | 24px |
| Footer (white pill) | `#FFFFFF` | `#003478` | 24px |

### Layout
| Setting | Value |
|---|---|
| Email width | 660px |
| Card padding (inner) | 28-32px |
| Card border | 1px solid `#D1D5DB` |
| Accent bar height | 6px |
| Red divider dash | 120px wide, 3px tall, `#C41E3A` |
| Gap between cards | 16px |

---

## Logo + Image Files

Upload these to Stripo's image library:
- `assets/SanFranciscoPost-Logo-Transparent.png` — footer logo (220px wide)
- `assets/SanFranciscoPost-Logo.jpg` — header banner (or your existing banner)
- USCG flyer from `campaigns/03-uscg-open-house-2026/`
- Any headshots or group photos you have

---

## Important Brand Rules

- **CG Orange (#CF4E38)** = ONLY on USCG co-branded sections. Never on general SAME content.
- **No gold** — gold is NOT a SAME brand color.
- **SAME Red (#C41E3A)** = accent bars, labels, buttons, dividers on all non-USCG sections.
- **Always include** Mailchimp merge tags: `*|ARCHIVE|*`, `*|UPDATE_PROFILE|*`, `*|UNSUB|*`
