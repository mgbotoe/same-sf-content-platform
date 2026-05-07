"""Parse all campaign .md files into structured JSON for Notion push."""

import os
import re
import json
import glob

CAMPAIGNS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "campaigns")
GITHUB_BASE = "https://raw.githubusercontent.com/mgbotoe/samesf-graphics/main"

# Content type mapping based on metadata keywords
CONTENT_TYPE_MAP = {
    "observance": "Observance",
    "celebratory": "Observance",
    "solemn": "Observance",
    "professional observance": "Observance",
    "remembrance": "Observance",
    "event": "Event Announcement",
    "newsletter": "Newsletter",
    "throwback": "Engagement",
    "tbt": "Engagement",
    "call for": "Engagement",
}

THEME_MAP = {
    "military": "Military & Service",
    "army": "Military & Service",
    "navy": "Military & Service",
    "coast guard": "Military & Service",
    "marine": "Military & Service",
    "air force": "Military & Service",
    "space force": "Military & Service",
    "seabee": "Military & Service",
    "veteran": "Military & Service",
    "armed forces": "Military & Service",
    "patriot": "Military & Service",
    "pearl harbor": "Military & Service",
    "national guard": "Military & Service",
    "independence": "Military & Service",
    "memorial": "Military & Service",
    "engineer": "Technical Excellence",
    "stem": "STEM Outreach",
    "women in engineering": "DEI & Leadership",
    "industry day": "Public-Private Collab",
    "gala": "Public-Private Collab",
}


def find_graphics(folder):
    """Find all .png/.jpg graphics in a campaign folder."""
    graphics = []
    for ext in ("*.png", "*.jpg"):
        graphics.extend(glob.glob(os.path.join(folder, ext)))
    return graphics


def get_github_url(local_path):
    """Convert local graphic path to GitHub raw URL."""
    # Extract relative path from campaigns/ onward
    campaigns_idx = local_path.replace("\\", "/").find("campaigns/")
    if campaigns_idx == -1:
        return None
    rel = local_path.replace("\\", "/")[campaigns_idx:]
    return f"{GITHUB_BASE}/{rel}"


def detect_content_type(metadata_text, title):
    """Detect Notion Content Type from metadata."""
    combined = (metadata_text + " " + title).lower()
    for key, val in CONTENT_TYPE_MAP.items():
        if key in combined:
            return val
    return "Thought Leadership"


def detect_theme(title):
    """Detect Notion Theme from title."""
    title_lower = title.lower()
    for key, val in THEME_MAP.items():
        if key in title_lower:
            return val
    return "Military & Service"


def detect_audience(content_type, title):
    """Detect target audience."""
    title_lower = title.lower()
    if content_type == "Newsletter":
        return '["Members", "Sponsors", "General"]'
    if "industry day" in title_lower:
        return '["Members", "Sponsors", "DoD", "General"]'
    if content_type == "Observance":
        return '["Members", "DoD", "General"]'
    return '["Members", "General"]'


def detect_platform(metadata_text):
    """Detect platform from metadata."""
    lower = metadata_text.lower()
    if "newsletter" in lower and "linkedin" in lower:
        return "Both"
    if "newsletter" in lower or "mailchimp" in lower:
        return "Newsletter"
    return "LinkedIn"


def parse_date(metadata_text):
    """Extract publish date from metadata."""
    # Look for "Post date:" or "Date:" lines
    patterns = [
        r"\*\*Post date\*\*:\s*\w+,\s*(\w+ \d{1,2},\s*\d{4})",
        r"\*\*Date\*\*:\s*(\w+ \d{1,2},\s*\d{4})",
    ]
    for pat in patterns:
        m = re.search(pat, metadata_text)
        if m:
            from datetime import datetime
            try:
                dt = datetime.strptime(m.group(1).strip(), "%B %d, %Y")
                return dt.strftime("%Y-%m-%d")
            except ValueError:
                pass
    # Try extracting from filename (MM-DD pattern)
    return None


def parse_date_from_filename(filename):
    """Extract date from filename like 02-17-engineers-week.md."""
    m = re.match(r"(\d{2})-(\d{2})-", os.path.basename(filename))
    if m:
        month, day = int(m.group(1)), int(m.group(2))
        return f"2026-{month:02d}-{day:02d}"
    return None


def extract_section(text, header_pattern):
    """Extract content between a header and the next --- or ## header."""
    pattern = rf"(?:^|\n)#+\s*{header_pattern}.*?\n(.*?)(?=\n---|\n## |\Z)"
    m = re.search(pattern, text, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


def extract_hashtags(text):
    """Extract hashtag lines from post text."""
    hashtags = set()
    for line in text.split("\n"):
        tags = re.findall(r"#\w+", line)
        if len(tags) >= 2:  # Lines with multiple hashtags
            hashtags.update(tags)
    return " ".join(sorted(hashtags)) if hashtags else ""


def parse_campaign_file(filepath):
    """Parse a single campaign .md file into structured data."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract title (first # line)
    title_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else os.path.basename(filepath)
    # Clean title — remove " — Date" suffix for Notion
    title_clean = re.sub(r"\s*[—–-]\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s*\d{4}.*$", "", title)

    # Extract metadata block (between title and first ---)
    meta_match = re.search(r"^#.*?\n(.*?)(?=\n---)", content, re.DOTALL)
    metadata = meta_match.group(1).strip() if meta_match else ""

    # Extract versions
    version_a = extract_section(content, r"Version A")
    version_b = extract_section(content, r"Version B")

    # For multi-post files (like USCG sequence), get Post 1 versions
    if not version_a:
        version_a = extract_section(content, r"Version A \(Short")
    if not version_b:
        version_b = extract_section(content, r"Version B \(Full")

    # Extract alt opening
    alt_opening = extract_section(content, r"Alt Opening")

    # Extract hashtags from version content
    hashtags = extract_hashtags(version_a + "\n" + version_b)

    # Detect properties
    content_type = detect_content_type(metadata, title)
    theme = detect_theme(title)
    platform = detect_platform(metadata)
    audience = detect_audience(content_type, title)

    # Parse date
    pub_date = parse_date(metadata) or parse_date_from_filename(filepath)

    # Find graphics
    folder = os.path.dirname(filepath)
    graphics = find_graphics(folder)
    graphic_urls = [get_github_url(g) for g in graphics if get_github_url(g)]

    return {
        "title": title_clean,
        "status": "Drafting",
        "content_type": content_type,
        "platform": platform,
        "publish_date": pub_date,
        "theme": theme,
        "audience": audience,
        "draft": version_a,
        "alt_version": version_b,
        "hashtags": hashtags,
        "notes": f"Alt Opening: {alt_opening}" if alt_opening else "",
        "graphic_urls": graphic_urls,
        "source_file": filepath,
    }


def main():
    """Parse all campaign files and output JSON."""
    results = []
    for root, dirs, files in os.walk(CAMPAIGNS_DIR):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            # Skip non-post files
            if f in ("design-philosophy.md", "same-national-posts.md", "email-content.md"):
                continue
            filepath = os.path.join(root, f)
            try:
                data = parse_campaign_file(filepath)
                results.append(data)
                print(f"  Parsed: {data['title']} ({data['publish_date']})")
            except Exception as e:
                print(f"  ERROR parsing {filepath}: {e}")

    # Output JSON
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notion-batch.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n{len(results)} posts parsed -> {output_path}")
    return results


if __name__ == "__main__":
    main()
