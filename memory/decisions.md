# Key Decisions

## Mailchimp API — cta_button Push Pattern (2026-05-03)
When pushing event email content via template sections API:
- `cta_button` mc:edit section must wrap the ENTIRE `<td>` including VML (Outlook) block + `<a href>` anchor
- Section value = full button HTML: VML + `<a href="REAL_URL">Button Text</a>`
- Always do a fresh GET after push to verify correct URL is present
- **Why:** Prior template had mc:edit wrapping only button text, not the href. URL was hardcoded outside mc:edit region — impossible to override via sections API.
- Raw HTML PUTs to `content_type: "template"` campaigns do NOT persist — Mailchimp re-renders from template on every GET.

## No GitHub Actions Cron for Distillation (2026-05-03)
- Distill only useful with live session context — cron runs can't access that
- PreCompact hook + manual `/distill-session` + `/loop 30m` for long sessions is the correct stack

## Folder Restructure (2026-05-03) — Approved in Principle, Pending Execution
- Create `campaigns/hero/` for multi-post event campaigns
- Move `03-uscg-open-house-2026/` → `hero/uscg-open-house-2026/`
- Create `campaigns/archive/` for JSON exports, past posts, completed work
- Create `campaigns/_index.md` as active campaign tracker
- Move loose root files to archive/ or data/

## Mailchimp Plan — Standard Recommended (2026-05-03)
- Custom-coded templates sunset on Essentials 5/31/2026 — DO NOT upgrade to Essentials
- Standard plan (~$30-45/mo at 1.5K contacts) is the correct upgrade target
- Free plan may lose custom-coded template support 5/31/2026 — insurance: export campaign HTML locally

## Distill-Session Skill Invocation Blocked (2026-05-03)
- `distill-session` skill has `disable-model-invocation: true`
- Must be written as a manual log — cannot invoke via Skill tool
