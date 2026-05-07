"""
Validate a rendered newsletter HTML before pushing to Mailchimp.

Catches the unfilled-template content that would otherwise ship: placeholder
button hrefs, leftover boilerplate copy, and generic default alt text. The
newsletter template has 80 editable sections — easy to forget one.

Usage:
    python scripts/validate-newsletter.py path/to/newsletter.html
    python scripts/validate-newsletter.py                            # check all newsletter HTML
"""

import glob
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

PLACEHOLDER_PHRASES = [
    "Article Title Goes Here",
    "Second Article Title",
    "Third Article Title",
    "Brief description of the article",
    "Your text here",
    "Lorem ipsum",
    "PLACEHOLDER",
    "TODO",
    "FIXME",
    "[insert",
    "[INSERT",
]

GENERIC_ALT_TEXT = [
    'alt="Sponsor Logo"',
    'alt="Diamond Partner Logo"',
    'alt="Gallery photo"',
    'alt="Image"',
    'alt="image"',
]

MUSTACHE = re.compile(r"\{\{[^}]+\}\}")
EMPTY_HREF = re.compile(r'href\s*=\s*"\s*"', re.IGNORECASE)
EMPTY_SRC = re.compile(r'src\s*=\s*"\s*"', re.IGNORECASE)
HASH_HREF = re.compile(r'href\s*=\s*"#"', re.IGNORECASE)
MSO_CONDITIONAL = re.compile(r"<!--\[if[^\]]*\]>.*?<!\[endif\]-->", re.DOTALL)
MAILCHIMP_MERGE = re.compile(r"\*\|[A-Z_:]+\|\*")
ALLOWED_MERGE_TAGS = {
    "*|MC:SUBJECT|*", "*|UNSUB|*", "*|HTML:LIST_ADDRESS_HTML|*",
    "*|LIST:COMPANY|*", "*|LIST:ADDRESS|*", "*|UPDATE_PROFILE|*",
    "*|FNAME|*", "*|LNAME|*", "*|EMAIL|*", "*|CURRENT_YEAR|*",
    "*|REWARDS|*", "*|REWARDS_TEXT|*", "*|MC_PREVIEW_TEXT|*",
    "*|ARCHIVE|*", "*|FORWARD|*",
}


def line_of(content, index):
    return content.count("\n", 0, index) + 1


def find_phrase(content, phrase):
    """Return list of line numbers where phrase appears (case-insensitive)."""
    hits = []
    low = content.lower()
    needle = phrase.lower()
    start = 0
    while True:
        idx = low.find(needle, start)
        if idx == -1:
            break
        hits.append(line_of(content, idx))
        start = idx + len(needle)
    return hits


def strip_mso(content):
    """Remove Outlook MSO conditional blocks. Real CTAs have both MSO + non-MSO
    versions with matching hrefs, so checking the non-MSO copy is sufficient."""
    return MSO_CONDITIONAL.sub("", content)


def validate_file(filepath):
    errors = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    non_mso = strip_mso(content)

    # 1. Placeholder copy
    for phrase in PLACEHOLDER_PHRASES:
        hits = find_phrase(content, phrase)
        for ln in hits:
            errors.append(("ERROR", f"Line {ln}: placeholder text '{phrase}'"))

    # 2. Generic alt text (default template values that should be customized)
    for alt in GENERIC_ALT_TEXT:
        hits = find_phrase(content, alt)
        for ln in hits:
            errors.append(("WARN", f"Line {ln}: generic alt {alt} — replace with descriptive text"))

    # 3. Unfilled button hrefs (href="#" outside MSO blocks)
    for m in HASH_HREF.finditer(non_mso):
        ln = line_of(non_mso, m.start())
        errors.append(("ERROR", f"Line ~{ln}: button has href=\"#\" — fill in real URL"))

    # 4. Empty href / src
    for m in EMPTY_HREF.finditer(content):
        errors.append(("ERROR", f"Line {line_of(content, m.start())}: empty href=\"\""))
    for m in EMPTY_SRC.finditer(content):
        errors.append(("ERROR", f"Line {line_of(content, m.start())}: empty src=\"\""))

    # 5. Mustache markers (defensive — we don't use them, but flag if any leaked in)
    for m in MUSTACHE.finditer(content):
        errors.append(("ERROR", f"Line {line_of(content, m.start())}: unfilled marker {m.group(0)}"))

    # 6. Mailchimp merge tags outside the allowed set (footer/header tags are fine,
    #    but body content should not contain raw merge tags)
    seen_merge = set()
    for m in MAILCHIMP_MERGE.finditer(content):
        tag = m.group(0)
        if tag in ALLOWED_MERGE_TAGS or tag in seen_merge:
            continue
        seen_merge.add(tag)
        errors.append(("WARN", f"Line {line_of(content, m.start())}: unexpected merge tag {tag}"))

    return errors


def main():
    if len(sys.argv) > 1:
        files = [sys.argv[1]]
    else:
        campaigns_dir = os.path.join(PROJECT_ROOT, "campaigns")
        files = sorted(glob.glob(os.path.join(campaigns_dir, "**", "*newsletter*.html"), recursive=True))

    if not files:
        print("No newsletter HTML files found.")
        sys.exit(1)

    total_errors = 0
    total_warnings = 0

    for filepath in files:
        rel = os.path.relpath(filepath, PROJECT_ROOT)
        results = validate_file(filepath)
        errs = [r for r in results if r[0] == "ERROR"]
        warns = [r for r in results if r[0] == "WARN"]

        if errs or warns:
            label = "FAIL" if errs else "WARN"
            print(f"\n  {label}  {rel}")
            for sev, msg in results:
                marker = "[!]" if sev == "ERROR" else "[?]"
                print(f"         {marker} {msg}")
            total_errors += len(errs)
            total_warnings += len(warns)
        else:
            print(f"  PASS  {rel}")

    print(f"\n{'='*60}")
    print(f"Files checked: {len(files)}")
    print(f"Errors:        {total_errors}")
    print(f"Warnings:      {total_warnings}")
    if total_errors == 0:
        print("READY TO PUSH" if total_warnings == 0 else "READY (warnings above are advisory)")
    else:
        print(f"BLOCKED — fix {total_errors} error(s) before pushing to Mailchimp")
        sys.exit(1)


if __name__ == "__main__":
    main()
