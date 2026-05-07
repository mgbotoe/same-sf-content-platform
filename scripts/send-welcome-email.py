"""
SAME SF — Automated Welcome Email Sender
Sends the welcome email to any subscribers who haven't received it yet.

How it works:
1. Creates a campaign targeting subscribers NOT tagged "Welcome Sent"
2. Mailchimp handles the filtering natively (no temp segments, no race conditions)
3. Verifies recipients exist before sending
4. Sends the campaign
5. Tags recipients with "Welcome Sent" so they're excluded next time

Run manually:   python scripts/send-welcome-email.py
Dry run:        python scripts/send-welcome-email.py --dry-run
Logs:           logs/welcome-email.log (all runs are logged)
"""

import urllib.request
import json
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path

# === LOGGING ===
# All output goes to both console and log file
PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

log = logging.getLogger("welcome-email")
log.setLevel(logging.INFO)
# File handler — appends to log file, keeps full history
fh = logging.FileHandler(LOG_DIR / "welcome-email.log", encoding="utf-8")
fh.setFormatter(logging.Formatter("%(asctime)s  %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
# Console handler — same output to terminal
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter("%(message)s"))
log.addHandler(fh)
log.addHandler(ch)

# Load .env from project root
env_path = PROJECT_ROOT / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip())

# === CONFIG ===
API_KEY = os.environ.get("MAILCHIMP_API_KEY", "")
if not API_KEY:
    log.error("MAILCHIMP_API_KEY not set in .env or environment")
    sys.exit(1)
SERVER = API_KEY.split("-")[-1]  # e.g. "us18"
LIST_ID = "9d174b3762"
TEMPLATE_ID = 11869770
WELCOME_TAG_ID = 3077075      # "Welcome Sent" static segment / tag
SEGMENT_ID = 3077126          # "Not Yet Welcomed" saved segment (auto-excludes tagged)
BASE_URL = f"https://{SERVER}.api.mailchimp.com/3.0"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

DRY_RUN = "--dry-run" in sys.argv


def api_request(method, path, data=None):
    """Make a Mailchimp API request."""
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(
        f"{BASE_URL}/{path}",
        data=body,
        method=method,
        headers=HEADERS
    )
    try:
        resp = urllib.request.urlopen(req)
        content = resp.read().decode("utf-8")
        return json.loads(content) if content.strip() else {}
    except urllib.error.HTTPError as e:
        error = e.read().decode("utf-8")
        log.error("  API Error (%s): %s", e.code, error[:500])
        return None


def delete_campaign(campaign_id):
    """Delete a campaign draft."""
    api_request("DELETE", f"campaigns/{campaign_id}")


def get_sent_to_emails(campaign_id):
    """Get email addresses of everyone the campaign was sent to."""
    emails = []
    offset = 0
    while True:
        result = api_request(
            "GET",
            f"reports/{campaign_id}/sent-to?count=500&offset={offset}"
        )
        if not result:
            break
        members = result.get("sent_to", [])
        if not members:
            break
        emails.extend(m.get("email_address") for m in members)
        offset += len(members)
        if offset >= result.get("total_items", 0):
            break
    return emails


def tag_members(emails):
    """Tag members with 'Welcome Sent' so they don't get it again."""
    if not emails:
        return
    # Mailchimp accepts up to 500 members per batch
    for i in range(0, len(emails), 500):
        batch = emails[i:i + 500]
        result = api_request(
            "POST",
            f"lists/{LIST_ID}/segments/{WELCOME_TAG_ID}",
            {"members_to_add": batch}
        )
        if result:
            added = len(result.get("members_added", []))
            errors = len(result.get("errors", []))
            log.info("  Batch %d: %d tagged, %d errors", i // 500 + 1, added, errors)


def main():
    dry = " (DRY RUN)" if DRY_RUN else ""
    log.info("=== SAME SF Welcome Email%s ===", dry)
    log.info("  Date: %s", datetime.now().strftime("%Y-%m-%d %H:%M"))
    log.info("")

    # Step 1: Create campaign targeting everyone NOT tagged "Welcome Sent"
    # Mailchimp handles the filtering — no temp segments, no race conditions
    today = datetime.now().strftime("%b %d, %Y")
    log.info("Creating campaign (target: NOT tagged 'Welcome Sent')...")

    campaign = api_request("POST", "campaigns", {
        "type": "regular",
        "recipients": {
            "list_id": LIST_ID,
            "segment_opts": {
                "saved_segment_id": SEGMENT_ID
            }
        },
        "settings": {
            "subject_line": "Welcome to the SAME San Francisco Post",
            "preview_text": "Here's what to expect and how to get involved.",
            "from_name": "SAME San Francisco",
            "reply_to": "samesanfrancisco@gmail.com",
            "title": f"Welcome Email - {today}",
            "template_id": TEMPLATE_ID
        }
    })

    if not campaign:
        log.error("  Failed to create campaign. Aborting.")
        return

    campaign_id = campaign.get("id")
    recipient_count = campaign.get("recipients", {}).get("recipient_count", 0)
    log.info("  Campaign: %s", campaign_id)
    log.info("  Recipients: %d", recipient_count)
    log.info("")

    # Step 2: Verify there are recipients
    if recipient_count == 0:
        log.info("No subscribers need a welcome email. Cleaning up...")
        delete_campaign(campaign_id)
        log.info("  Campaign deleted. Done.")
        return

    # Step 3: Run send checklist
    log.info("Running send checklist...")
    checklist = api_request("GET", f"campaigns/{campaign_id}/send-checklist")
    if checklist and not checklist.get("is_ready"):
        log.error("  Campaign not ready:")
        for item in checklist.get("items", []):
            if item.get("type") == "error":
                log.error("    - %s", item.get("details"))
        delete_campaign(campaign_id)
        log.error("  Campaign deleted. Aborting.")
        return
    log.info("  Checklist passed.")
    log.info("")

    # Step 4: Send (or dry run)
    if DRY_RUN:
        log.info("DRY RUN: Would send to %d subscribers.", recipient_count)
        delete_campaign(campaign_id)
        log.info("  Campaign deleted. Done.")
        return

    log.info("Sending welcome email to %d subscribers...", recipient_count)
    req = urllib.request.Request(
        f"{BASE_URL}/campaigns/{campaign_id}/actions/send",
        data=b"",
        method="POST",
        headers=HEADERS
    )
    try:
        urllib.request.urlopen(req)
        log.info("  Sent!")
    except urllib.error.HTTPError as e:
        log.error("  Send failed (%s): %s", e.code, e.read().decode("utf-8")[:300])
        return
    log.info("")

    # Step 5: Tag recipients so they won't get it again
    log.info("Waiting for delivery report...")
    sent_emails = []
    for attempt in range(4):
        time.sleep(10)
        sent_emails = get_sent_to_emails(campaign_id)
        if sent_emails:
            break
        log.info("  Report not ready, retrying (%d/4)...", attempt + 1)

    if sent_emails:
        log.info("  Delivered to %d subscribers.", len(sent_emails))
        log.info("Tagging recipients with 'Welcome Sent'...")
        tag_members(sent_emails)
    else:
        log.warning("  Could not retrieve sent-to list.")
        log.warning("  Tag recipients manually in Mailchimp to prevent re-sends.")
    log.info("")

    log.info("Done!")


if __name__ == "__main__":
    main()


# === WINDOWS TASK SCHEDULER SETUP ===
#
# To run this every Monday at 8:00 AM:
#
# 1. Open Task Scheduler (search "Task Scheduler" in Start)
# 2. Click "Create Basic Task"
# 3. Name: "SAME SF Welcome Email"
# 4. Trigger: Weekly, Monday, 8:00 AM
# 5. Action: Start a program
#    - Program: python
#    - Arguments: C:\Workspace\SAMESF\scripts\send-welcome-email.py
#    - Start in: C:\Workspace\SAMESF
# 6. Check "Open the Properties dialog" → under Conditions, uncheck
#    "Start the task only if the computer is on AC power"
# 7. Finish
#
# To test first: python scripts/send-welcome-email.py --dry-run
