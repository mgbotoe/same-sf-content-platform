"""Generate USCG Industry Day flyer — Structural Authority design philosophy."""

from PIL import Image, ImageDraw, ImageFont
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONTS_DIR = os.path.join(
    os.path.expanduser("~"),
    ".claude/plugins/cache/anthropic-agent-skills/document-skills/1ed29a03dc85/skills/canvas-design/canvas-fonts",
)
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "uscg-industry-day-flyer.png")

# Brand colors
SAME_BLUE = (0, 52, 120)       # #003478
SAME_RED = (196, 30, 58)       # #C41E3A
CG_ORANGE = (207, 78, 56)      # #CF4E38
WHITE = (255, 255, 255)
LIGHT_GRAY = (220, 225, 235)
DARK_OVERLAY = (0, 40, 90)     # Slightly lighter than SAME_BLUE for contrast zones

# Canvas: 8.5x11 at 150 DPI
W, H = 1275, 1650

img = Image.new("RGB", (W, H), SAME_BLUE)
draw = ImageDraw.Draw(img)

# Load fonts
def font(name, size):
    path = os.path.join(FONTS_DIR, name)
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

title_font = font("BigShoulders-Bold.ttf", 72)
subtitle_font = font("InstrumentSans-Bold.ttf", 30)
section_font = font("InstrumentSans-Bold.ttf", 26)
body_font = font("InstrumentSans-Regular.ttf", 24)
body_bold = font("InstrumentSans-Bold.ttf", 24)
detail_font = font("InstrumentSans-Regular.ttf", 20)
small_font = font("InstrumentSans-Regular.ttf", 16)
time_font = font("GeistMono-Bold.ttf", 22)
time_body = font("InstrumentSans-Regular.ttf", 22)
free_font = font("BigShoulders-Bold.ttf", 48)
cta_font = font("InstrumentSans-Bold.ttf", 28)

# === TOP: CG Orange racing stripe ===
draw.rectangle([0, 0, W, 18], fill=CG_ORANGE)

# === Thin white line under stripe ===
draw.rectangle([0, 18, W, 21], fill=WHITE)

# === HEADER ZONE (navy bg, already base color) ===
y = 50

# "INDUSTRY DAY" - large title
draw.text((80, y), "INDUSTRY DAY", font=title_font, fill=WHITE)
y += 85

# "& OPEN HOUSE" subtitle
draw.text((80, y), "& OPEN HOUSE", font=font("BigShoulders-Bold.ttf", 52), fill=CG_ORANGE)
y += 70

# Thin horizontal rule
draw.rectangle([80, y, W - 80, y + 2], fill=CG_ORANGE)
y += 20

# "U.S. Coast Guard Civil Engineering Unit Oakland"
draw.text((80, y), "U.S. Coast Guard  |  Civil Engineering Unit Oakland", font=subtitle_font, fill=LIGHT_GRAY)
y += 40

# "Co-hosted by SAME San Francisco Post"
draw.text((80, y), "Co-hosted by SAME San Francisco Post", font=detail_font, fill=LIGHT_GRAY)
y += 55

# === DATE/TIME/LOCATION BAND (CG Orange) ===
band_top = y
band_h = 130
draw.rectangle([0, band_top, W, band_top + band_h], fill=CG_ORANGE)

# Date block
draw.text((80, band_top + 18), "THURSDAY", font=font("BigShoulders-Bold.ttf", 28), fill=WHITE)
draw.text((80, band_top + 50), "MARCH 12, 2026", font=font("BigShoulders-Bold.ttf", 44), fill=WHITE)
draw.text((80, band_top + 95), "2:00 PM - 5:00 PM", font=font("GeistMono-Regular.ttf", 22), fill=WHITE)

# FREE badge (right side)
free_x = W - 280
draw.rectangle([free_x, band_top + 20, free_x + 200, band_top + band_h - 20], fill=WHITE)
draw.text((free_x + 32, band_top + 30), "FREE", font=free_font, fill=CG_ORANGE)

y = band_top + band_h

# === MAIN CONTENT ZONE (slightly lighter navy) ===
content_top = y
draw.rectangle([0, content_top, W, content_top + 700], fill=DARK_OVERLAY)
y = content_top + 30

# Left column: Agenda
left_x = 80
draw.text((left_x, y), "AGENDA", font=section_font, fill=CG_ORANGE)
y += 40

agenda = [
    ("2:00 PM", "Opening Remarks (CEUO CO / SAME SF)"),
    ("2:15 PM", "CEUO Briefing"),
    ("", "Branch chiefs, structure, contracting process"),
    ("2:30 PM", "Panel Discussion"),
    ("", "Opportunities, challenges & Q&A"),
    ("3:15 PM", "Networking + Breakout Sessions"),
    ("", "Conf Room H: Industry showcase & networking"),
    ("", "Rooms A-E: Field-specific breakouts & 1-on-1s"),
    ("4:45 PM", "Closing Remarks"),
    ("5:00 PM", "Event Complete / No-host Social"),
]

for time_str, desc in agenda:
    if time_str:
        draw.text((left_x, y), time_str, font=time_font, fill=WHITE)
        draw.text((left_x + 160, y), desc, font=time_body, fill=WHITE)
        y += 35
    else:
        draw.text((left_x + 160, y), desc, font=detail_font, fill=LIGHT_GRAY)
        y += 28

y += 15

# Divider
draw.rectangle([left_x, y, W - 80, y + 1], fill=(255, 255, 255, 80))
y += 25

# WHO SHOULD ATTEND section
draw.text((left_x, y), "WHO SHOULD ATTEND", font=section_font, fill=CG_ORANGE)
y += 40

attendees = [
    "General Contractors & Specialty Subcontractors",
    "A/E Firms & Engineering Consultants",
    "Small Businesses Exploring Federal Contracting",
    "Construction & Facilities Professionals",
]

for item in attendees:
    # Bullet point
    draw.ellipse([left_x + 4, y + 8, left_x + 14, y + 18], fill=CG_ORANGE)
    draw.text((left_x + 28, y), item, font=body_font, fill=WHITE)
    y += 34

y += 15

# Key message
draw.text((left_x, y), "Direct access to Coast Guard civil engineering leadership.", font=body_bold, fill=WHITE)
y += 35
draw.text((left_x, y), "Real conversations. Real opportunities.", font=body_font, fill=LIGHT_GRAY)

y = content_top + 700

# === CONTACT / REGISTRATION BAND ===
contact_top = y
contact_h = 120
draw.rectangle([0, contact_top, W, contact_top + contact_h], fill=SAME_BLUE)

# Thin CG orange line at top
draw.rectangle([0, contact_top, W, contact_top + 3], fill=CG_ORANGE)

cy = contact_top + 20
draw.text((80, cy), "QUESTIONS?", font=section_font, fill=CG_ORANGE)
cy += 38
draw.text((80, cy), "LT Duncan Clark, Construction Manager, CEU Oakland", font=body_font, fill=WHITE)
cy += 30
draw.text((80, cy), "Duncan.G.Clark@uscg.mil", font=body_bold, fill=LIGHT_GRAY)

y = contact_top + contact_h

# === LOGO ZONE — anchored to bottom ===
# Bottom stripe takes 21px, disclaimer ~20px, logo ~120px, padding
bottom_stripe_top = H - 21
disclaimer_y = bottom_stripe_top - 30
logo_max_h = 120

# Load and place SAME SF logo
try:
    logo_path = os.path.join(ASSETS_DIR, "SanFranciscoPost-Logo-Transparent.png")
    logo = Image.open(logo_path).convert("RGBA")

    ratio = logo_max_h / logo.height
    logo_w = int(logo.width * ratio)
    logo_h_actual = int(logo.height * ratio)
    logo = logo.resize((logo_w, logo_h_actual), Image.LANCZOS)

    logo_x = (W - logo_w) // 2
    logo_y = disclaimer_y - logo_h_actual - 15

    img.paste(logo, (logo_x, logo_y), logo)
except Exception as e:
    print(f"Logo load failed: {e}")
    logo_y = disclaimer_y - 30

# === SAVE THE DATE / REGISTRATION CTA ===
# Fill the gap between contact and logo with a centered CTA block
cta_zone_top = y + contact_h + 20
cta_zone_bottom = logo_y - 40
cta_center_y = (cta_zone_top + cta_zone_bottom) // 2

# CTA box
box_w = 500
box_h = 120
box_x = (W - box_w) // 2
box_y = cta_center_y - box_h // 2

# Outlined box
draw.rectangle([box_x, box_y, box_x + box_w, box_y + box_h], outline=CG_ORANGE, width=3)

# "SAVE THE DATE" text centered in box
save_text = "SAVE THE DATE"
save_font = font("BigShoulders-Bold.ttf", 42)
bbox_save = draw.textbbox((0, 0), save_text, font=save_font)
save_tw = bbox_save[2] - bbox_save[0]
draw.text(((W - save_tw) // 2, box_y + 15), save_text, font=save_font, fill=CG_ORANGE)

# "Registration details coming soon" below
reg_text = "Registration details coming soon"
bbox_reg = draw.textbbox((0, 0), reg_text, font=detail_font)
reg_tw = bbox_reg[2] - bbox_reg[0]
draw.text(((W - reg_tw) // 2, box_y + 70), reg_text, font=detail_font, fill=LIGHT_GRAY)

# Thin separator above logo area
sep_y = logo_y - 25
draw.rectangle([80, sep_y, W - 80, sep_y + 1], fill=CG_ORANGE)

# === DISCLAIMER ===
disclaimer = "This event does not constitute official U.S. Coast Guard endorsement of SAME or any participating organization."
bbox = draw.textbbox((0, 0), disclaimer, font=small_font)
text_w = bbox[2] - bbox[0]
draw.text(((W - text_w) // 2, disclaimer_y), disclaimer, font=small_font, fill=LIGHT_GRAY)

# === Bottom CG orange stripe (mirror top) ===
draw.rectangle([0, H - 18, W, H], fill=CG_ORANGE)
draw.rectangle([0, H - 21, W, H - 18], fill=WHITE)

# Save
img.save(OUTPUT_PATH, "PNG", dpi=(150, 150))
print(f"Flyer saved to: {OUTPUT_PATH}")
print(f"Size: {W}x{H} px (8.5x11 at 150 DPI)")
