#!/usr/bin/env python3
"""
Add mc:edit attributes to newsletter template HTML.
Transforms newsletter-html-raw.html → newsletter-template-v2.html
"""

import re
import sys

INPUT = r"C:\Workspace\SAMESF\campaigns\05-may-2026\newsletter-html-raw.html"
OUTPUT = r"C:\Workspace\SAMESF\campaigns\05-may-2026\newsletter-template-v2.html"

with open(INPUT, "r", encoding="utf-8") as f:
    html = f.read()

# Map: (0-indexed occurrence of vcCardInner) -> mc:edit name
# [1] Welcome to 2026        -> welcome_note
# [2] SPOTLIGHT EVENT        -> spotlight
# [4] PHOTOS (recap)         -> section2
# [5] STEM & SCHOLARSHIPS    -> section3
# [6] COMMUNITY              -> section4
# [7] INDUSTRY NEWS          -> section5
# [11] SAVE THE DATE         -> events_calendar
MC_EDIT_MAP = {
    1: "welcome_note",
    2: "spotlight",
    4: "section2",
    5: "section3",
    6: "section4",
    7: "section5",
    11: "events_calendar",
}

STANDARD_TAG = '<td class="vcCardInner" style="padding: 28px 32px 32px 32px;mso-line-height-rule: exactly;">'
TAGGED_TEMPLATE = '<td mc:edit="{name}" class="vcCardInner" style="padding: 28px 32px 32px 32px;mso-line-height-rule: exactly;">'

# Find all vcCardInner positions
positions = [m.start() for m in re.finditer(r'<td class="vcCardInner"', html)]
print(f"Found {len(positions)} vcCardInner tds")

# Process from END to START so byte offsets stay valid
for idx in sorted(MC_EDIT_MAP.keys(), reverse=True):
    pos = positions[idx]
    actual = html[pos:pos + len(STANDARD_TAG)]
    if actual != STANDARD_TAG:
        print(f"  WARNING [{idx}]: tag mismatch at pos {pos}: {actual[:60]}")
        continue
    name = MC_EDIT_MAP[idx]
    new_tag = TAGGED_TEMPLATE.format(name=name)
    html = html[:pos] + new_tag + html[pos + len(STANDARD_TAG):]
    print(f"  [{idx}] Added mc:edit='{name}' at pos {pos}")

# Verify
mc_edits = re.findall(r'mc:edit="([^"]+)"', html)
print(f"\nmc:edit blocks in output: {mc_edits}")

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nSaved to: {OUTPUT}")
print(f"File size: {len(html)} chars")
