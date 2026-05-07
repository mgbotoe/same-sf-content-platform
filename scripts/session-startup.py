"""
Session startup script — runs via SessionStart hook.
Pulls Mailchimp scheduled campaigns and writes a snapshot
to .claude/runtime/mailchimp-scheduled.md
"""

import os
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone


def load_api_key():
    # 1. Environment variable
    key = os.environ.get("MAILCHIMP_API_KEY")
    if key:
        return key
    # 2. .mcp.json (authoritative source for this project)
    root = os.path.dirname(os.path.dirname(__file__))
    mcp_path = os.path.join(root, ".mcp.json")
    if os.path.exists(mcp_path):
        try:
            with open(mcp_path) as f:
                mcp = json.load(f)
            key = (mcp.get("mcpServers", {})
                      .get("mailchimp", {})
                      .get("env", {})
                      .get("MAILCHIMP_API_KEY"))
            if key:
                return key
        except Exception:
            pass
    # 3. .env file
    env_path = os.path.join(root, ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("MAILCHIMP_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def get_scheduled_campaigns(api_key):
    # Mailchimp API key format: key-dcXX (datacenter in suffix)
    dc = api_key.split("-")[-1]
    url = f"https://{dc}.api.mailchimp.com/3.0/campaigns?status=schedule&count=20"
    req = urllib.request.Request(url)
    import base64
    credentials = base64.b64encode(f"anystring:{api_key}".encode()).decode()
    req.add_header("Authorization", f"Basic {credentials}")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def get_sent_recent(api_key, count=5):
    dc = api_key.split("-")[-1]
    url = f"https://{dc}.api.mailchimp.com/3.0/campaigns?status=sent&count={count}&sort_field=send_time&sort_dir=DESC"
    req = urllib.request.Request(url)
    import base64
    credentials = base64.b64encode(f"anystring:{api_key}".encode()).decode()
    req.add_header("Authorization", f"Basic {credentials}")
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def pt_time(utc_str):
    if not utc_str:
        return "TBD"
    try:
        dt = datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
        # Convert to PT (UTC-7 PDT / UTC-8 PST — use PDT for summer)
        from datetime import timedelta
        pt = dt - timedelta(hours=7)
        return pt.strftime("%a %b %-d at %-I:%M %p PT")
    except Exception:
        return utc_str


def main():
    api_key = load_api_key()
    if not api_key:
        print("MAILCHIMP_API_KEY not found — skipping Mailchimp startup check")
        return

    output_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        ".claude", "runtime", "mailchimp-scheduled.md"
    )

    lines = [
        f"# Mailchimp Snapshot — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        ""
    ]

    try:
        data = get_scheduled_campaigns(api_key)
        campaigns = data.get("campaigns", [])
        if campaigns:
            lines.append("## Scheduled to Send")
            for c in campaigns:
                send_time = c.get("send_time") or c.get("schedule_time", "")
                lines.append(f"- **{c['settings']['subject_line']}**")
                lines.append(f"  - Campaign: {c['settings'].get('title', 'Untitled')}")
                lines.append(f"  - Sends: {pt_time(send_time)}")
                lines.append(f"  - ID: `{c['id']}`")
        else:
            lines.append("## Scheduled to Send")
            lines.append("- None")
        lines.append("")
    except Exception as e:
        lines.append(f"## Scheduled to Send")
        lines.append(f"- Error fetching: {e}")
        lines.append("")

    try:
        sent_data = get_sent_recent(api_key)
        sent = sent_data.get("campaigns", [])
        if sent:
            lines.append("## Recently Sent (last 5)")
            for c in sent:
                lines.append(f"- **{c['settings']['subject_line']}** — sent {pt_time(c.get('send_time', ''))}")
        lines.append("")
    except Exception as e:
        lines.append(f"## Recently Sent")
        lines.append(f"- Error fetching: {e}")
        lines.append("")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Mailchimp snapshot written to {output_path}")
    if campaigns:
        print(f"  {len(campaigns)} campaign(s) scheduled to send")


if __name__ == "__main__":
    main()
