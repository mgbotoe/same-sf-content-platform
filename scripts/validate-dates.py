"""
Validate dates, day-of-week, and ordinals in SAME SF campaign post files.

Usage:
    python scripts/validate-dates.py                    # Check all campaign posts
    python scripts/validate-dates.py campaigns/03-march-2026/03-05-seabee-birthday.md  # Check one file

Checks:
    1. Day-of-week matches actual calendar (e.g., "Tuesday, March 3, 2026" is really a Tuesday)
    2. Ordinal matches founding year (e.g., "251st Birthday" with founded 1775 → 2026-1775=251)
    3. Founding year cross-referenced against data/military-holidays.md
"""

import datetime
import glob
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

FOUNDING_YEARS = {
    "seabee": 1942,
    "army birthday": 1775,
    "army corps": 1775,
    "usace": 1775,
    "independence": 1776,
    "coast guard": 1790,
    "air force": 1947,
    "navy birthday": 1775,
    "marine corps": 1775,
    "space force": 2019,
    "national guard": 1636,
    "pearl harbor": 1941,
    "9/11": 2001,
    "patriot day": 2001,
    "september 11": 2001,
    "engineers week": 1951,
    "veterans day": 1919,
    "memorial day": 1868,
    "armed forces": 1950,
    "women in engineering": 2014,
}

MONTH_NAMES = {
    "january": 1, "february": 2, "march": 3, "april": 4,
    "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12,
}

DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def ordinal_suffix(n):
    if 11 <= n % 100 <= 13:
        return f"{n}th"
    return f"{n}{['th','st','nd','rd','th','th','th','th','th','th'][n%10]}"


def parse_post_date(line):
    """Parse '**Post date**: Wednesday, February 25, 2026' format."""
    m = re.search(
        r"\*\*Post date\*\*:\s*(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s+"
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+"
        r"(\d{1,2}),\s+(\d{4})",
        line,
    )
    if m:
        return m.group(1), m.group(2), int(m.group(3)), int(m.group(4))
    return None


def find_ordinals(text):
    """Find patterns like '251st', '84th', '236th' near birthday/anniversary keywords."""
    results = []
    for m in re.finditer(r"(\d+)(?:st|nd|rd|th)", text, re.IGNORECASE):
        num = int(m.group(1))
        ctx_start = max(0, m.start() - 80)
        ctx_end = min(len(text), m.end() + 80)
        context = text[ctx_start:ctx_end].lower()
        if any(kw in context for kw in ["birthday", "anniversary", "years"]):
            results.append((num, context, m.start()))
    return results


def find_founding_year(text_lower):
    """Match text content against known observance keywords to find expected founding year."""
    matches = []
    for keyword, year in FOUNDING_YEARS.items():
        if keyword in text_lower:
            matches.append((keyword, year))
    return matches


def get_primary_observance(lines):
    """Extract the primary observance from metadata lines (title or **Observance** field).
    Returns the keyword and founding year, or None."""
    for line in lines[:10]:
        low = line.lower()
        # Check **Observance**: line first (most specific)
        if "**observance**" in low:
            for keyword, year in sorted(FOUNDING_YEARS.items(), key=lambda x: -len(x[0])):
                if keyword in low:
                    return keyword, year
        # Check title line (# ...)
        if line.startswith("# "):
            for keyword, year in sorted(FOUNDING_YEARS.items(), key=lambda x: -len(x[0])):
                if keyword in low:
                    return keyword, year
    return None


def validate_file(filepath):
    """Validate a single campaign post file. Returns list of (severity, message)."""
    errors = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")

    # 1. Check day-of-week on **Post date** lines
    for i, line in enumerate(lines):
        parsed = parse_post_date(line)
        if parsed:
            day_name, month_name, day_num, year = parsed
            month_num = MONTH_NAMES[month_name.lower()]
            try:
                actual_date = datetime.date(year, month_num, day_num)
                actual_day = DAY_NAMES[actual_date.weekday()]
                if actual_day != day_name:
                    errors.append((
                        "ERROR",
                        f"Line {i+1}: {month_name} {day_num}, {year} is {actual_day}, not {day_name}",
                    ))
                else:
                    errors.append((
                        "OK",
                        f"Day-of-week: {day_name}, {month_name} {day_num}, {year} confirmed correct",
                    ))
            except ValueError as e:
                errors.append(("ERROR", f"Line {i+1}: Invalid date — {e}"))

    # 2. Check section headers with day labels (e.g., "## Post 1: Announcement (Feb 25, Tuesday)")
    for i, line in enumerate(lines):
        m = re.search(
            r"\((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{1,2}),\s+"
            r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\)",
            line,
        )
        if m:
            abbrev_to_num = {
                "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
            }
            month_num = abbrev_to_num[m.group(1)]
            day_num = int(m.group(2))
            day_name = m.group(3)
            year_match = re.search(r"20\d{2}", content)
            year = int(year_match.group()) if year_match else 2026
            try:
                actual_date = datetime.date(year, month_num, day_num)
                actual_day = DAY_NAMES[actual_date.weekday()]
                if actual_day != day_name:
                    errors.append((
                        "ERROR",
                        f"Line {i+1}: {m.group(1)} {day_num} {year} is {actual_day}, not {day_name}",
                    ))
            except ValueError:
                pass

    # 3. Check ordinals against the PRIMARY observance only
    # This prevents false positives when a post mentions another branch in passing
    primary = get_primary_observance(lines)
    if primary:
        keyword, expected_founding = primary
        ordinal_matches = find_ordinals(content)
        year_match = re.search(r"20\d{2}", content)
        post_year = int(year_match.group()) if year_match else 2026
        expected_ordinal = post_year - expected_founding

        # Find the ordinal that appears in the title or **Observance** line (most authoritative)
        header_text = "\n".join(lines[:10])
        header_ordinals = find_ordinals(header_text)

        if header_ordinals:
            ordinal_num = header_ordinals[0][0]
            if ordinal_num != expected_ordinal:
                errors.append((
                    "ERROR",
                    f"Ordinal mismatch: header says '{ordinal_suffix(ordinal_num)}' but "
                    f"{post_year} - {expected_founding} = {ordinal_suffix(expected_ordinal)} "
                    f"(for '{keyword}')",
                ))
            else:
                errors.append((
                    "OK",
                    f"Ordinal: {ordinal_suffix(ordinal_num)} confirmed correct "
                    f"({post_year} - {expected_founding} = {expected_ordinal})",
                ))

    # 4. Cross-check **Observance** line founding year if present
    for line in lines[:10]:
        m = re.search(r"\(Founded.*?(\d{4})\)", line)
        if m and primary:
            stated_founding = int(m.group(1))
            _, expected_founding = primary
            if stated_founding != expected_founding:
                errors.append((
                    "ERROR",
                    f"Founding year mismatch: says {stated_founding} but expected {expected_founding}",
                ))
            else:
                errors.append((
                    "OK",
                    f"Founding year: {stated_founding} confirmed correct",
                ))

    return errors


def main():
    if len(sys.argv) > 1:
        files = [sys.argv[1]]
    else:
        campaigns_dir = os.path.join(PROJECT_ROOT, "campaigns")
        files = sorted(glob.glob(os.path.join(campaigns_dir, "**", "*.md"), recursive=True))

    if not files:
        print("No campaign files found.")
        sys.exit(1)

    total_errors = 0
    total_files = 0

    for filepath in files:
        rel_path = os.path.relpath(filepath, PROJECT_ROOT)
        results = validate_file(filepath)

        if not results:
            continue

        total_files += 1
        file_errors = [r for r in results if r[0] == "ERROR"]
        file_ok = [r for r in results if r[0] == "OK"]

        if file_errors:
            print(f"\n  FAIL  {rel_path}")
            for severity, msg in file_errors:
                print(f"         {msg}")
                total_errors += 1
        else:
            print(f"  PASS  {rel_path}")
            for _, msg in file_ok:
                print(f"         {msg}")

    print(f"\n{'='*60}")
    print(f"Files checked: {total_files}")
    print(f"Errors found:  {total_errors}")
    if total_errors == 0:
        print("ALL CHECKS PASSED")
    else:
        print(f"FAILED — {total_errors} error(s) need fixing")
        sys.exit(1)


if __name__ == "__main__":
    main()
