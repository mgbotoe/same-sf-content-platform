"""SAME SF Mailchimp MCP Server — full read/write access to Mailchimp Marketing API."""

import os
import json
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mailchimp")

API_KEY = os.environ.get("MAILCHIMP_API_KEY", "")
DC = os.environ.get("MAILCHIMP_SERVER_PREFIX", "")
if not DC and "-" in API_KEY:
    DC = API_KEY.split("-")[-1]

BASE_URL = f"https://{DC}.api.mailchimp.com/3.0"
AUTH = ("anystring", API_KEY)


def mc_request(method: str, path: str, params: dict = None, json_data: dict = None) -> dict:
    url = f"{BASE_URL}{path}"
    try:
        r = requests.request(method, url, auth=AUTH, params=params, json=json_data, timeout=30)
        if r.status_code >= 400:
            err = r.json() if r.headers.get("content-type", "").startswith("application/json") else {}
            return {"error": True, "status": r.status_code, "detail": err.get("detail", r.text[:500])}
        return r.json() if r.text else {"success": True, "status": r.status_code}
    except Exception as e:
        return {"error": True, "detail": str(e)}


# ── Campaigns ──────────────────────────────────────────────

@mcp.tool()
def list_campaigns(count: int = 20, status: str = "") -> str:
    """List email campaigns. Optional status filter: save, paused, schedule, sending, sent."""
    params = {"count": count, "sort_field": "send_time", "sort_dir": "DESC"}
    if status:
        params["status"] = status
    data = mc_request("GET", "/campaigns", params=params)
    if data.get("error"):
        return json.dumps(data)
    campaigns = [
        {"id": c["id"], "title": c.get("settings", {}).get("title", ""),
         "subject": c.get("settings", {}).get("subject_line", ""),
         "status": c["status"], "send_time": c.get("send_time", ""),
         "emails_sent": c.get("emails_sent", 0)}
        for c in data.get("campaigns", [])
    ]
    return json.dumps({"total": data.get("total_items", 0), "campaigns": campaigns}, indent=2)


@mcp.tool()
def get_campaign(campaign_id: str) -> str:
    """Get full details of a specific campaign by ID."""
    data = mc_request("GET", f"/campaigns/{campaign_id}")
    return json.dumps(data, indent=2)


@mcp.tool()
def create_campaign(list_id: str, subject_line: str, from_name: str, reply_to: str,
                    title: str = "", preview_text: str = "") -> str:
    """Create a new campaign draft. Returns campaign ID for setting content and sending.
    Use list_audiences first to get the list_id."""
    payload = {
        "type": "regular",
        "recipients": {"list_id": list_id},
        "settings": {
            "subject_line": subject_line,
            "from_name": from_name,
            "reply_to": reply_to,
            "title": title or subject_line,
            "preview_text": preview_text
        }
    }
    data = mc_request("POST", "/campaigns", json_data=payload)
    if data.get("error"):
        return json.dumps(data)
    return json.dumps({"campaign_id": data["id"], "status": data["status"],
                       "title": data["settings"]["title"]}, indent=2)


@mcp.tool()
def set_campaign_content(campaign_id: str, html: str) -> str:
    """Set the HTML content of a campaign. Campaign must be in 'save' (draft) status."""
    data = mc_request("PUT", f"/campaigns/{campaign_id}/content", json_data={"html": html})
    return json.dumps(data, indent=2)


@mcp.tool()
def set_campaign_content_from_template(campaign_id: str, template_id: int) -> str:
    """Set campaign content using an existing Mailchimp template."""
    data = mc_request("PUT", f"/campaigns/{campaign_id}/content",
                      json_data={"template": {"id": template_id}})
    return json.dumps(data, indent=2)


@mcp.tool()
def send_campaign(campaign_id: str, confirm: bool = False) -> str:
    """Send a campaign immediately. Set confirm=True to actually send.
    Without confirm=True, returns campaign details for review instead of sending."""
    if not confirm:
        data = mc_request("GET", f"/campaigns/{campaign_id}")
        return json.dumps({
            "WARNING": "Campaign NOT sent. Set confirm=True to send.",
            "campaign_id": campaign_id,
            "subject": data.get("settings", {}).get("subject_line", ""),
            "list_id": data.get("recipients", {}).get("list_id", ""),
            "status": data.get("status", "")
        }, indent=2)
    data = mc_request("POST", f"/campaigns/{campaign_id}/actions/send")
    return json.dumps(data, indent=2)


@mcp.tool()
def schedule_campaign(campaign_id: str, send_time: str) -> str:
    """Schedule a campaign for future delivery. send_time format: 2026-03-15T14:00:00+00:00"""
    data = mc_request("POST", f"/campaigns/{campaign_id}/actions/schedule",
                      json_data={"schedule_time": send_time})
    return json.dumps(data, indent=2)


@mcp.tool()
def delete_campaign(campaign_id: str) -> str:
    """Delete a campaign. Only works on campaigns that haven't been sent."""
    data = mc_request("DELETE", f"/campaigns/{campaign_id}")
    return json.dumps(data, indent=2)


# ── Templates ──────────────────────────────────────────────

@mcp.tool()
def list_templates(count: int = 20) -> str:
    """List saved email templates."""
    data = mc_request("GET", "/templates", params={"count": count, "type": "user"})
    if data.get("error"):
        return json.dumps(data)
    templates = [
        {"id": t["id"], "name": t["name"], "type": t.get("type", ""),
         "date_created": t.get("date_created", "")}
        for t in data.get("templates", [])
    ]
    return json.dumps({"total": data.get("total_items", 0), "templates": templates}, indent=2)


@mcp.tool()
def get_template(template_id: int) -> str:
    """Get a specific template's details and HTML content."""
    data = mc_request("GET", f"/templates/{template_id}")
    return json.dumps(data, indent=2)


# ── Audiences/Lists ───────────────────────────────────────

@mcp.tool()
def list_audiences(count: int = 20) -> str:
    """List all audiences (subscriber lists)."""
    data = mc_request("GET", "/lists", params={"count": count})
    if data.get("error"):
        return json.dumps(data)
    lists = [
        {"id": l["id"], "name": l["name"],
         "member_count": l["stats"]["member_count"],
         "campaign_count": l["stats"]["campaign_count"]}
        for l in data.get("lists", [])
    ]
    return json.dumps({"total": data.get("total_items", 0), "audiences": lists}, indent=2)


@mcp.tool()
def get_audience(list_id: str) -> str:
    """Get details of a specific audience/list."""
    data = mc_request("GET", f"/lists/{list_id}")
    return json.dumps(data, indent=2)


@mcp.tool()
def list_segments(list_id: str) -> str:
    """List segments/tags for an audience."""
    data = mc_request("GET", f"/lists/{list_id}/segments", params={"count": 50})
    if data.get("error"):
        return json.dumps(data)
    segments = [
        {"id": s["id"], "name": s["name"], "member_count": s["member_count"],
         "type": s.get("type", "")}
        for s in data.get("segments", [])
    ]
    return json.dumps({"total": data.get("total_items", 0), "segments": segments}, indent=2)


# ── Reports ────────────────────────────────────────────────

@mcp.tool()
def list_reports(count: int = 20) -> str:
    """List campaign performance reports."""
    data = mc_request("GET", "/reports", params={"count": count})
    if data.get("error"):
        return json.dumps(data)
    reports = [
        {"campaign_id": r["id"], "title": r.get("campaign_title", ""),
         "subject": r.get("subject_line", ""), "send_time": r.get("send_time", ""),
         "emails_sent": r.get("emails_sent", 0),
         "opens": r.get("opens", {}).get("unique_opens", 0),
         "open_rate": r.get("opens", {}).get("open_rate", 0),
         "clicks": r.get("clicks", {}).get("unique_clicks", 0),
         "click_rate": r.get("clicks", {}).get("click_rate", 0),
         "unsubscribes": r.get("unsubscribed", 0)}
        for r in data.get("reports", [])
    ]
    return json.dumps({"total": data.get("total_items", 0), "reports": reports}, indent=2)


@mcp.tool()
def get_report(campaign_id: str) -> str:
    """Get detailed performance report for a specific campaign."""
    data = mc_request("GET", f"/reports/{campaign_id}")
    return json.dumps(data, indent=2)


# ── Automations ────────────────────────────────────────────

@mcp.tool()
def list_automations() -> str:
    """List all automation workflows."""
    data = mc_request("GET", "/automations")
    if data.get("error"):
        return json.dumps(data)
    autos = [
        {"id": a["id"], "title": a.get("settings", {}).get("title", ""),
         "status": a["status"], "emails_sent": a.get("emails_sent", 0)}
        for a in data.get("automations", [])
    ]
    return json.dumps({"total": len(autos), "automations": autos}, indent=2)


# ── Account ────────────────────────────────────────────────

@mcp.tool()
def get_account_info() -> str:
    """Get Mailchimp account details — name, contact info, industry, plan."""
    data = mc_request("GET", "/")
    if data.get("error"):
        return json.dumps(data)
    return json.dumps({
        "account_name": data.get("account_name", ""),
        "email": data.get("email", ""),
        "first_name": data.get("first_name", ""),
        "last_name": data.get("last_name", ""),
        "total_subscribers": data.get("total_subscribers", 0),
        "industry_stats": data.get("industry_stats", {}),
        "pricing_plan": data.get("pricing_plan_type", "")
    }, indent=2)


if __name__ == "__main__":
    mcp.run()
