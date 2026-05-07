"""
Fix double border on event_details cards.

The template already wraps event_details in a card table with border-left.
Previous push added ANOTHER card table inside → double line.
Fix: push plain <p> tags only.
"""
import os, json, requests

API_KEY = os.environ.get("MAILCHIMP_API_KEY") or open("C:/Workspace/SAMESF/.env").read().split("MAILCHIMP_API_KEY=")[1].split()[0]
BASE = "https://us18.api.mailchimp.com/3.0"
auth = ("anystring", API_KEY)

p = lambda text, last=False: (
    f'<p style="margin:0{"" if last else " 0 10px 0"};'
    f'font-family:Arial,Helvetica,sans-serif;font-size:15px;'
    f'color:#374151;line-height:1.6;">{text}</p>'
)

def bold(label):
    return f'<strong style="color:#003478;">{label}</strong>'

MINE_CLEANUP_ID = "3619932539"
AI_SUMMIT_ID    = "46ab747d2e"

mine_details = "".join([
    p(f"📅 {bold('Date:')} Tuesday, June 16, 2026"),
    p(f"🕘 {bold('Time:')} 9:00 AM – 1:30 PM PDT (Check-in 8:45 AM)"),
    p(f"📍 {bold('Location:')} EPA Region 9 Office, San Francisco, CA", last=True),
])

ai_details = "".join([
    p(f"📅 {bold('Date:')} Thursday, September 10, 2026"),
    p(f"📍 {bold('Location:')} Stanford University, Stanford, CA"),
    p(f"🎫 {bold('Early Bird:')} $250 for SAME members (available for a limited time)", last=True),
])

def push(campaign_id, sections, label):
    # Check if scheduled — unschedule first if needed
    info = requests.get(f"{BASE}/campaigns/{campaign_id}", auth=auth).json()
    status = info.get("status")
    print(f"{label}: status={status}")

    if status == "schedule":
        r = requests.post(f"{BASE}/campaigns/{campaign_id}/actions/unschedule", auth=auth)
        print(f"  Unscheduled: {r.status_code}")

    r = requests.put(
        f"{BASE}/campaigns/{campaign_id}/content",
        auth=auth,
        json={"template": {"id": info["settings"].get("template_id", 11869797), "sections": sections}},
    )
    print(f"  Content push: {r.status_code}")
    if r.status_code != 200:
        print(f"  Error: {r.text[:300]}")
        return False

    if status == "schedule":
        sched = info.get("send_time", "")
        if sched:
            r2 = requests.post(
                f"{BASE}/campaigns/{campaign_id}/actions/schedule",
                auth=auth,
                json={"schedule_time": sched},
            )
            print(f"  Rescheduled to {sched}: {r2.status_code}")
    return True

# Get template IDs from campaign info
mine_info = requests.get(f"{BASE}/campaigns/{MINE_CLEANUP_ID}", auth=auth).json()
ai_info   = requests.get(f"{BASE}/campaigns/{AI_SUMMIT_ID}",    auth=auth).json()

mine_tmpl = mine_info.get("settings", {}).get("template_id", 11869797)
ai_tmpl   = ai_info.get("settings", {}).get("template_id", 11869797)
print(f"Mine template_id: {mine_tmpl}, AI template_id: {ai_tmpl}")

push(MINE_CLEANUP_ID, {"event_details": mine_details}, "Mine Cleanup")
push(AI_SUMMIT_ID,    {"event_details": ai_details},   "AI Summit")

print("Done.")
