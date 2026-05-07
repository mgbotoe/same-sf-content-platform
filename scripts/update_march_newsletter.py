"""One-time script to update March newsletter campaign sections."""
import urllib.request
import json
import os
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

API_KEY = os.environ["MAILCHIMP_API_KEY"]
SERVER = API_KEY.split("-")[-1]
BASE = f"https://{SERVER}.api.mailchimp.com/3.0"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

CAMPAIGN_ID = "54de049039"
TEMPLATE_ID = 11869768

# Style helpers
def p(s):
    return f'<p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 16px; color: #374151; line-height: 1.6; padding: 0;">{s}</p>'

def p_last(s):
    return f'<p style="margin: 0; font-family: Arial, Helvetica, sans-serif; font-size: 16px; color: #374151; line-height: 1.6; padding: 0;">{s}</p>'

def label(color, text):
    return f'<p style="margin: 0 0 8px 0; font-family: Arial, Helvetica, sans-serif; font-size: 12px; font-weight: bold; color: {color}; line-height: 1.3; text-transform: uppercase; letter-spacing: 1.5px; padding: 0;">{text}</p>'

def heading(text):
    return (
        '<h2 class="vcHeading" style="margin: 0 0 16px 0; '
        "font-family: Georgia, 'Times New Roman', Times, serif; "
        'font-size: 24px; font-weight: bold; color: #003478; '
        f'line-height: 1.3;">{text}</h2>'
    )

def callout(s):
    return (
        '<p style="margin: 0; font-family: Arial, Helvetica, sans-serif; '
        'font-size: 14px; color: #003478; line-height: 1.5; '
        'background-color: #F0F4FF; padding: 12px 16px; border-radius: 4px; '
        f'border-left: 3px solid #003478;">{s}</p>'
    )

def mini_label(text):
    return (
        '<p style="margin: 0 0 12px 0; font-family: Arial, Helvetica, sans-serif; '
        'font-size: 11px; font-weight: bold; color: #C41E3A; line-height: 1.3; '
        f'text-transform: uppercase; letter-spacing: 1.5px; padding: 0;">{text}</p>'
    )

def mini_p(s):
    return f'<p style="margin: 0 0 8px 0; font-family: Arial, Helvetica, sans-serif; font-size: 15px; color: #374151; line-height: 1.6; padding: 0;">{s}</p>'

def mini_p_last(s):
    return f'<p style="margin: 0; font-family: Arial, Helvetica, sans-serif; font-size: 15px; color: #374151; line-height: 1.6; padding: 0;">{s}</p>'

def event_p(s):
    return f'<p style="margin: 0; font-family: Arial, Helvetica, sans-serif; font-size: 15px; color: #374151; line-height: 1.5; padding: 0;">{s}</p>'


# Load ALL 80 template defaults as base — nothing gets reset
defaults_path = Path(__file__).resolve().parent / "template_defaults.json"
with open(defaults_path) as f:
    sections = json.load(f)

# Now overlay ONLY our March content on top
overrides = {
    "preview_text": (
        "Join us April 16 for a Geospatial Tools panel featuring Trimble, "
        "plus a recap of our Lemoore chapter's Seabee Birthday celebration."
    ),
    "header_subtitle": (
        '<p style="margin: 0; font-family: Arial, Helvetica, sans-serif; '
        'font-size: 16px; color: #6B7280; line-height: 1.4; padding: 0;">'
        "March 2026 Newsletter</p>"
    ),
    "welcome_heading": "Looking Ahead + Looking Back",
    "welcome_image": "",
    "welcome_body": p_last(
        "This month we&#39;re looking back at an outstanding event in the "
        "Central Valley and looking ahead to our April panel with Trimble. "
        "Read on for both, plus upcoming events and how to stay connected."
    ),
    "welcome_closing": (
        '<p style="margin: 0; font-family: Arial, Helvetica, sans-serif; '
        'font-size: 16px; color: #374151; line-height: 1.6; padding: 0;">'
        '<a href="https://www.linkedin.com/company/society-of-amercian-military-engineers-san-francisco-post/" '
        'style="color: #003478; text-decoration: underline; font-weight: bold;">'
        "Follow us on LinkedIn &rarr;</a></p>"
    ),
    # --- PHOTO GALLERY (generic highlights + Lemoore photos) ---
    "photo_gallery_heading": (
        label("#C41E3A", "OUR POST IN ACTION")
        + heading("SAME San Francisco Post Highlights")
    ),
    "photo_gallery_img_1": (
        '<img src="https://raw.githubusercontent.com/mgbotoe/samesf-graphics'
        '/main/campaigns/03-march-2026/cmc-zetino-ens-al-nuaimi.jpeg" '
        'alt="CMC Zetino and ENS Al Nuaimi cut the 84th Seabee Birthday cake" '
        'style="width: 100%; height: auto; display: block; border-radius: 4px;">'
    ),
    "photo_gallery_img_2": (
        '<img src="https://raw.githubusercontent.com/mgbotoe/samesf-graphics'
        '/main/campaigns/03-march-2026/greg-woods-presentation.jpeg" '
        'alt="Greg Woods presents on resilient solar power at NAS Lemoore" '
        'style="width: 100%; height: auto; display: block; border-radius: 4px;">'
    ),
    "photo_gallery_caption": (
        '<p style="margin: 16px 0 0 0; font-family: Arial, Helvetica, sans-serif; '
        'font-size: 14px; color: #6B7280; line-height: 1.5; text-align: center; '
        'font-style: italic; padding: 0;">From site visits to celebrations, '
        "our Post connects military, government, and industry professionals "
        "across the Bay Area and beyond.</p>"
    ),
    # --- GEOSPATIAL PANEL (event spotlight — replacing old USCG) ---
    "uscg_heading": (
        label("#C41E3A", "EVENT SPOTLIGHT")
        + heading("Geospatial Tools for A/E/C &amp; Asset Management")
    ),
    "uscg_image": "",
    "uscg_body": (
        p(
            "Join us on <strong>Thursday, April 16</strong> at the "
            "<strong>Chicken Pie Shop in Walnut Creek</strong> for an industry "
            "panel discussion on Geospatial Tools for A/E/C and Asset Management, "
            "featuring experts from <strong>Trimble</strong>."
        )
        + p(
            "This panel will walk through how modern geospatial tools are changing "
            "design, construction, and long-term asset management across "
            "infrastructure sectors. Real-world applications and data-driven "
            "workflows, not theory."
        )
        + p(
            "<strong>Buffet dinner and a drink ticket included</strong> with "
            "every registration."
        )
    ),
    "uscg_details": (
        '<table border="0" cellpadding="0" cellspacing="0" width="100%">'
        '<tr><td style="padding: 8px 0; font-family: Arial, Helvetica, sans-serif; '
        'font-size: 15px; color: #374151; line-height: 1.5;">'
        "<strong>Date:</strong> Thursday, April 16, 2026<br>"
        "<strong>Time:</strong> 6:00 PM &ndash; 8:30 PM<br>"
        "<strong>Location:</strong> Chicken Pie Shop, 1251 Arroyo Way, Walnut Creek, CA 94596"
        "</td></tr></table>"
    ),
    "uscg_closing": callout(
        "<strong>Pricing:</strong> "
        "Government: $40 &bull; Member: $50 &bull; Non-Member: $75<br>"
        "Bulk (3 attendees): $175<br>"
        "Sponsorship Entry (5 attendees): $1,000 &bull; "
        "Sponsorship Deluxe (10 attendees): $3,000"
    ),
    "uscg_button": (
        '<a href="https://app.memberplanet.com/#/event/samesanfranciscopost/'
        'geospatialtoolsforaecassetmanagement" '
        'style="display: inline-block; background-color: #C41E3A; color: #FFFFFF; '
        'font-family: Arial, Helvetica, sans-serif; font-size: 16px; '
        'font-weight: bold; text-decoration: none; padding: 12px 28px; '
        'border-radius: 4px;">Register Now</a>'
    ),
    "uscg_disclaimer": "",
    # --- LEMOORE RECAP ---
    "stem_heading": (
        label("#C41E3A", "EVENT RECAP")
        + heading("Lemoore Field Chapter: Lunch &amp; Learn + Seabee Birthday")
    ),
    "stem_image": "",
    "stem_body": (
        p(
            "On March 5, the Lemoore Field Chapter brought together more than "
            "25 members and guests at Naval Air Station Lemoore for a Lunch and "
            "Learn on resilient solar power, followed by the 84th Seabee Birthday "
            "celebration."
        )
        + p(
            "Greg Woods, Managing Director of Renewable Solar Inc (RSI) and a "
            "retired Navy Civil Engineer Corps Commander, delivered a presentation "
            "on Heat Related Issues and the methods RSI uses to build resilient "
            "solar power systems."
        )
        + p(
            "Following the presentation, the chapter celebrated the 84th Seabee "
            "Birthday. In a time-honored tradition, the oldest and youngest "
            "active-duty Seabees in attendance cut the birthday cake together: "
            "Command Master Chief Zetino from Fleet Readiness Center West and "
            "ENS Wed Al Nuaimi, Assistant Public Works Officer for NAS Lemoore."
        )
        + callout(
            "<strong>Who was there:</strong> Public Works Department Lemoore, "
            "NAVFAC Southwest, Harper Construction, Bush Construction, Fresno "
            "State University, Vanir Construction Management, Fleet Readiness "
            "Center-West, and Renewable Solar Inc."
        )
    ),
    "stem_button": "",
    # --- CLEAR engineers_week (no longer needed) ---
    "engineers_week_heading": "",
    "engineers_week_body": "",
    "engineers_week_button": "",
    # --- MARCH NEWS BRIEFS ---
    "news_heading": (
        label("#C41E3A", "MARCH IN REVIEW")
        + heading("Around the Post")
    ),
    "news_item_1": (
        '<p style="margin: 0 0 4px 0; font-family: Arial, Helvetica, sans-serif; '
        'font-size: 15px; font-weight: bold; color: #003478; line-height: 1.4;">'
        "ISEF Science &amp; Engineering Fair Review</p>"
        + mini_p_last(
            "On March 8, board members JR Gregory and Madina Gbotoe served on the "
            "ISEF Review Board, evaluating 110 candidates for acceptance into the "
            "International Science and Engineering Fair competition. Supporting the "
            "next generation of scientists and engineers is at the heart of what we do."
        )
    ),
    "news_item_2": (
        '<p style="margin: 0 0 4px 0; font-family: Arial, Helvetica, sans-serif; '
        'font-size: 15px; font-weight: bold; color: #003478; line-height: 1.4;">'
        "Stantec Hosts Bay Area LEADS</p>"
        + mini_p_last(
            "On March 18, Stantec hosted Bay Area LEADS in Walnut Creek, including "
            "a teacher job shadow day. Programs like these strengthen the connection "
            "between industry professionals and educators, building the pipeline for "
            "future A/E/C talent."
        )
    ),
    "news_item_3": "",
    "member_spotlight": (
        mini_label("WHAT&#39;S NEXT")
        + mini_p_last(
            "<strong>Fresno State Student Chapter</strong> &mdash; The Lemoore "
            "Field Chapter is heading to Fresno State to welcome new Student "
            "Chapter leadership. Stay tuned for details on this outreach event."
        )
    ),
    "honoring_service": (
        mini_label("HONORING SERVICE")
        + mini_p("Looking ahead:")
        + mini_p("<strong>May 16 &mdash; Armed Forces Day</strong>")
        + mini_p("Honoring those currently serving in all branches.")
        + mini_p("<strong>May 25 &mdash; Memorial Day</strong>")
        + mini_p_last("Remembering those who gave their lives in service.")
    ),
    "event_date_1": "APR 16",
    "event_desc_1": event_p(
        "<strong>Geospatial Tools Panel</strong> &mdash; Chicken Pie Shop, Walnut Creek. Featuring Trimble."
    ),
    "event_date_2": "MAY 18-21",
    "event_desc_2": event_p(
        "<strong>SAME JETC</strong> &mdash; National conference &amp; exhibition"
    ),
    "event_date_3": "JUN TBD",
    "event_desc_3": event_p(
        "<strong>Tinker Fest</strong> &mdash; USCG partnership event"
    ),
    "event_date_4": "JUL TBD",
    "event_desc_4": event_p(
        "<strong>Annual Golf Tournament</strong> &mdash; STEM scholarship fundraiser"
    ),
    "event_date_5": "SEP TBD",
    "event_desc_5": event_p(
        "<strong>A/E/C AI &amp; Cybersecurity Summit</strong> &mdash; Multi-day summit"
    ),
    "event_date_6": "SEP 24",
    "event_desc_6": event_p(
        "<strong>Fresno State Welcome Back BBQ</strong> &mdash; Student chapter outreach"
    ),
    "event_date_7": "DEC 10",
    "event_desc_7": event_p(
        "<strong>Annual Holiday Gala</strong> &mdash; Scholarship awards &amp; celebration"
    ),
}

# Merge overrides on top of defaults
sections.update(overrides)

data = json.dumps({"template": {"id": TEMPLATE_ID, "sections": sections}}).encode("utf-8")
req = urllib.request.Request(
    f"{BASE}/campaigns/{CAMPAIGN_ID}/content",
    data=data,
    method="PUT",
    headers=HEADERS,
)
try:
    resp = urllib.request.urlopen(req)
    result = json.loads(resp.read().decode("utf-8"))
    html = result.get("html", "")
    print(f"Content set! HTML length: {len(html)} chars")
    print(f"Has Lemoore: {'Lemoore' in html}")
    print(f"Has March: {'March 2026' in html}")
    print(f"Has Trimble: {'Trimble' in html}")
    print(f"Has Geospatial: {'Geospatial' in html}")
    print(f"Has Chicken Pie Shop: {'Chicken Pie Shop' in html}")
except urllib.error.HTTPError as e:
    print(f"Error {e.code}: {e.read().decode('utf-8')[:500]}")
