#!/usr/bin/env python3
"""
Build May 2026 newsletter HTML from the February template base.
Fixes: correct section order, removes February leftover sections, no em dashes.
Output: campaigns/05-may-2026/may-newsletter-ready.html
"""

import re

BASE_HTML = r"C:\Workspace\SAMESF\campaigns\05-may-2026\newsletter-html-raw.html"
OUTPUT = r"C:\Workspace\SAMESF\campaigns\05-may-2026\may-newsletter-ready.html"

P       = 'style="margin: 0 0 16px 0;font-family: Arial, Helvetica, sans-serif;font-size: 16px;color: #374151;line-height: 1.6;padding: 0;"'
P_LAST  = 'style="margin: 0;font-family: Arial, Helvetica, sans-serif;font-size: 16px;color: #374151;line-height: 1.6;padding: 0;"'
P_BOLD  = 'style="margin: 0 0 16px 0;font-family: Arial, Helvetica, sans-serif;font-size: 16px;color: #374151;line-height: 1.6;padding: 0;font-weight: bold;"'
EYEBROW = 'style="margin: 0 0 8px 0;font-family: Arial, Helvetica, sans-serif;font-size: 12px;font-weight: bold;color: #C41E3A;line-height: 1.3;text-transform: uppercase;letter-spacing: 1.5px;padding: 0;"'
H2      = "style=\"margin: 0 0 16px 0; font-family: Georgia, 'Times New Roman', Times, serif; font-size: 24px; font-weight: bold; color: #003478; line-height: 1.3;\""
LI      = 'style="margin: 0 0 8px 0;font-family: Arial, Helvetica, sans-serif;font-size: 16px;color: #374151;line-height: 1.6;"'
UL      = 'style="margin: 0 0 16px 0; padding-left: 20px;"'

STANDARD_TD  = '<td class="vcCardInner" style="padding: 28px 32px 32px 32px;mso-line-height-rule: exactly;">'
QUOTE_TD     = '<td class="vcCardInner" style="padding: 36px 40px 36px 40px;mso-line-height-rule: exactly;">'
EMPTY_INNER  = '<p style="margin:0;font-size:0;line-height:0;"> </p>'


def section(eyebrow_text, heading_text, body_html):
    return f"""{STANDARD_TD}
<div>
<p {EYEBROW}>{eyebrow_text}</p>
<h2 class="vcHeading" {H2}>{heading_text}</h2>
</div>
{body_html}
</td>"""


def welcome_section(heading_text, body_html):
    return f"""{STANDARD_TD}
<h2 class="vcHeading" {H2}>{heading_text}</h2>
{body_html}
</td>"""


def empty_section(td_opening):
    return f"""{td_opening}
{EMPTY_INNER}
</td>"""


# ── SECTION CONTENT (no em dashes) ───────────────────────────────────────────

SEC1_WELCOME = welcome_section(
    "May 2026",
    f"""<p {P}>Registration opens today for our June 16 event with EPA Region 9. Details below. This issue also has a scholarship recipient heading to SF State and a recap of last month's panel in Walnut Creek.</p>
<p {P_LAST}>If you're not following us on LinkedIn yet, that's where the updates and photos happen between newsletters.</p>"""
)

SEC2_SPOTLIGHT = section(
    "SPOTLIGHT EVENT",
    "EPA &times; SAME SF: Abandoned Mine Cleanup Information Exchange",
    f"""<p {P}>EPA Region 9 and the SAME SF Post are co-hosting the first Abandoned Mine Cleanup Information Exchange on <strong>June 16, 2026</strong> at the EPA Region 9 Office in San Francisco, 9:00 AM to 1:30 PM.</p>
<p {P}>This is a technical forum for practitioners working on CERCLA hardrock mine sites. The day covers three presentation sessions: residential mine cleanup projects, geomorphic and natural reclamation-focused repository design, and large-scale mine waste excavation in remote terrain, plus poster sessions and breakout discussions.</p>
<p {P}><strong>Registration is open today.</strong> Limited to 3 attendees per firm. Abstract submissions closed May 19.</p>
<table border="0" cellpadding="0" cellspacing="0" style="margin: 16px 0 24px 0;border-collapse: collapse;">
<tr><td style="padding: 12px 24px;background-color: #C41E3A;border-radius: 4px;">
<a href="[REGISTRATION LINK]" style="font-family: Arial, Helvetica, sans-serif;font-size: 14px;font-weight: bold;color: #ffffff;text-decoration: none;display: block;">Register Now &rarr;</a>
</td></tr>
</table>
<p {P_LAST}><a href="https://docs.google.com/forms/d/e/1FAIpQLScOo962FBwpg_rI6a1ezs03uY3WabjJt3xFk7gSAmSZyK8Hhw/viewform" style="color: #003478;text-decoration: underline;">Submit an Abstract (closes May 19)</a></p>"""
)

SEC3_HORIZON = section(
    "ON THE HORIZON",
    "Coming September 10: Federal AI Summit at Stanford",
    f"""<p {P}>Mark your calendars. On September 10, 2026, SAME SF and Stanford's Center for Integrated Facility Engineering (CIFE) are hosting the Federal AI Summit: AI for A/E/C at Stanford University. A full day of speakers, panels, and networking on AI's role in federal infrastructure.</p>
<p {P_LAST}>Early bird pricing is open: $250 for SAME members. <a href="http://www.federalaisummit.org" style="color: #003478;text-decoration: underline;">Learn more at federalaisummit.org</a></p>"""
)

SEC4_SCHOLARSHIP = section(
    "SCHOLARSHIP SPOTLIGHT",
    "Aron Mejia",
    f"""<p {P}>Aron Mejia is graduating from Oakland Military Institute this spring with a 3.0 GPA, headed to San Francisco State University to major in Electrical Engineering.</p>
<p {P}>His path there is unconventional, and that's what makes it worth telling.</p>
<p {P}>Since 2018, Aron has been a musician at his church, attending four days a week and steadily taking on more responsibility. By 2023, he was the musical director, overseeing more than 10 musicians playing at camps and conventions with up to 1,000 people in attendance. That same year, he became the audio and sound engineer, a role that put him directly in charge of the systems that make large events work.</p>
<p {P}>He's also done hands-on electrical work, installing lights, outlets, and circuit breakers alongside his father during summers.</p>
<p {P}>"My goal is to become an electrical engineer and improve my family's financial future," Aron writes. "I hope to start a company and continue to expand my understanding of audio engineering."</p>
<p {P}>The thread connecting all of it: music, sound, electricity, leadership. SF State is where it comes together.</p>
<p {P_LAST}>SAME SF is proud to support Aron's next chapter. This is exactly the kind of story our scholarship program exists for.</p>"""
)

SEC5_RECAP = section(
    "EVENT RECAP",
    "April Recap: Geospatial Tools for A/E/C",
    f"""<p {P}>Our April 16 panel at the Chicken Pie Shop in Walnut Creek brought together professionals for an evening on geospatial tools: LiDAR, GNSS, reality capture, and digital twins and how they're changing infrastructure delivery. Trimble led the conversation.</p>
<p {P_LAST}><a href="https://www.linkedin.com/company/same-san-francisco-post/" style="color: #003478;text-decoration: underline;">Head to our LinkedIn page to see photos from the evening.</a></p>"""
)

SEC6_OBSERVANCES = section(
    "MILITARY OBSERVANCES",
    "May &amp; June Observances",
    f"""<p {P_BOLD}>May</p>
<ul {UL}>
<li {LI}><strong>Armed Forces Day</strong> | Saturday, May 16 | Honoring all who serve</li>
<li {LI}><strong>Memorial Day</strong> | Monday, May 25 | We remember</li>
</ul>
<p {P_BOLD}>Coming in June</p>
<ul {UL}>
<li {LI}><strong>June 14</strong> | U.S. Army Birthday &amp; Flag Day</li>
<li {LI}><strong>June 16</strong> | U.S. Army Corps of Engineers Birthday</li>
<li {LI}><strong>June 23</strong> | International Women in Engineering Day</li>
</ul>"""
)

SEC7_EVENTS = section(
    "ON THE CALENDAR",
    "Upcoming Events",
    f"""<table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;font-family: Arial, Helvetica, sans-serif;font-size: 15px;color: #374151;">
<tr style="background-color: #003478;"><td style="padding: 10px 12px;font-weight: bold;color: #ffffff;width: 25%;">Date</td><td style="padding: 10px 12px;font-weight: bold;color: #ffffff;">Event</td><td style="padding: 10px 12px;font-weight: bold;color: #ffffff;">Details</td></tr>
<tr style="background-color: #f8f9fa;"><td style="padding: 10px 12px;border-bottom: 1px solid #e5e7eb;"><strong>June 16</strong></td><td style="padding: 10px 12px;border-bottom: 1px solid #e5e7eb;">Abandoned Mine Cleanup Information Exchange</td><td style="padding: 10px 12px;border-bottom: 1px solid #e5e7eb;">EPA Region 9 Office, SF</td></tr>
<tr><td style="padding: 10px 12px;border-bottom: 1px solid #e5e7eb;"><strong>September 10</strong></td><td style="padding: 10px 12px;border-bottom: 1px solid #e5e7eb;">Federal AI Summit: AI for A/E/C</td><td style="padding: 10px 12px;border-bottom: 1px solid #e5e7eb;">Stanford University</td></tr>
<tr style="background-color: #f8f9fa;"><td style="padding: 10px 12px;border-bottom: 1px solid #e5e7eb;"><strong>July</strong></td><td style="padding: 10px 12px;border-bottom: 1px solid #e5e7eb;">Golf Tournament</td><td style="padding: 10px 12px;border-bottom: 1px solid #e5e7eb;">Date TBD</td></tr>
<tr><td style="padding: 10px 12px;"><strong>December</strong></td><td style="padding: 10px 12px;">Holiday Gala</td><td style="padding: 10px 12px;">Date TBD</td></tr>
</table>"""
)

# ── REPLACEMENT MAP ───────────────────────────────────────────────────────────
# Maps vcCardInner index (0-based) to replacement full td content
# Spec order: Welcome > Spotlight > Federal AI Summit > Scholarship > Recap > Observances > Events
REPLACEMENTS = {
    1:  SEC1_WELCOME,                      # Welcome
    2:  SEC2_SPOTLIGHT,                    # Mine Cleanup spotlight
    3:  empty_section(QUOTE_TD),           # Quote block (Feb only) -> hidden
    4:  SEC3_HORIZON,                      # PHOTOS slot -> Federal AI Summit
    5:  SEC4_SCHOLARSHIP,                  # STEM slot -> Scholarship
    6:  SEC5_RECAP,                        # COMMUNITY slot -> Geospatial Recap
    7:  SEC6_OBSERVANCES,                  # INDUSTRY NEWS slot -> Observances
    9:  empty_section(STANDARD_TD),        # GET INVOLVED (Feb only) -> hidden
    10: empty_section(STANDARD_TD),        # WELCOME ABOARD (Feb only) -> hidden
    11: SEC7_EVENTS,                       # SAVE THE DATE -> Events Calendar
    12: empty_section(STANDARD_TD),        # WHAT'S AHEAD (Feb only) -> hidden
}

# ── BUILD ─────────────────────────────────────────────────────────────────────

with open(BASE_HTML, "r", encoding="utf-8") as f:
    html = f.read()

positions = [m.start() for m in re.finditer(r'<td class="vcCardInner"', html)]
print(f"Total vcCardInner sections found: {len(positions)}")


def find_closing_td(h, start):
    depth, i = 0, start
    while i < len(h):
        if h[i:i+3] == '<td':
            depth += 1
        elif h[i:i+5] == '</td>':
            depth -= 1
            if depth == 0:
                return i + 5
        i += 1
    return -1


# Process end-to-start to preserve offsets
for idx in sorted(REPLACEMENTS.keys(), reverse=True):
    pos = positions[idx]
    end = find_closing_td(html, pos)
    if end == -1:
        print(f"ERROR: no closing </td> for [{idx}]")
        continue
    html = html[:pos] + REPLACEMENTS[idx] + html[end:]
    print(f"  [{idx}] replaced")

# Fix title tag
html = re.sub(r'<title>[^<]*</title>', '<title>SAME SF Post | May 2026</title>', html)

# Final em dash sweep on my content (catch any missed)
# Only replace in text content, not HTML attributes
em_dash_count = html.count('&mdash;') + html.count('—')
if em_dash_count:
    print(f"\nWARNING: {em_dash_count} em dashes still in HTML")
    # Show context around each
    for m in re.finditer(r'&mdash;|—', html):
        print(f"  pos {m.start()}: ...{html[max(0,m.start()-40):m.end()+40]}...")

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nSaved: {OUTPUT} ({len(html)} chars)")
