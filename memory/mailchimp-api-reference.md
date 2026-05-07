# Mailchimp Reference — Free Plan Limits & API v3

_Researched May 2026. Sources: official Mailchimp help docs and developer API reference._

---

## 1. Free Plan Limits & Features

| Feature | Free Plan | Essentials | Standard | Premium |
|---|---|---|---|---|
| **Contact limit** | 250 | Up to 50,000 | Up to 100,000 | Up to 200,000 |
| **Monthly sends** | 500 | 10x contact limit | 12x contact limit | 15x contact limit |
| **Daily send limit** | 250 | No daily cap | No daily cap | No daily cap |
| **Automations** | One-click welcome email ONLY | Single email automations, flows up to 4 steps | Expanded flows + flow templates | Unlimited |
| **Segmentation** | Basic only | Basic | Advanced segmentation + pre-built segments | Advanced |
| **A/B testing** | No | Yes (up to 3 variations) | Yes | Multivariate |
| **Templates** | Limited selection (basic, featured, themed) | All Mailchimp templates | All + custom-coded templates | All |
| **Custom-coded templates** | No | No | Yes | Yes |

### Free Plan Key Constraints

- **500 sends/month, 250/day.** If contact count exceeds 250, sending is paused (no service interruption while under limit — hold placed immediately on exceeding).
- **Automations: one-click welcome email only.** Classic Automations multi-step series are NOT available on Free. Classic Automations are also only accessible to accounts that have previously created one.
- **Segmentation does not work for campaigns on the Free plan.** This is confirmed for our account — do not attempt to use segments in campaign sends.
- **No A/B testing** on Free.
- **No custom-coded templates** on Free (Essentials gets all standard templates; Standard gets custom-coded).

### What "One-click automated welcome email" Means on Free

- Single email only — not a multi-email series.
- Trigger: Signup (when someone subscribes to your audience).
- Default delay: 1 day after signup.
- Cannot replicate to multiple audiences — must create a new automation per audience.
- This is a Classic Automation feature. Navigate: Automations > Classic Automations > Welcome new subscribers > Single email tab.

---

## 2. Classic Automations — Types & Triggers

### Automation Categories

| Category | Triggers on |
|---|---|
| Featured | Account-specific recommendations |
| Tagged contact | Tag added to contact |
| Subscriber activity | Signup, audience field changes, group joins/leaves |
| E-commerce | Purchase, abandoned cart, product retargeting |
| Date-based | Birthday, anniversary, list added date, specific date |
| API | API 3.0 call, Event API (Premium only) |

### Welcome New Subscribers — Available Types

| Type | Emails | Default Trigger |
|---|---|---|
| **Welcome message** | 1 | Signup, delay: 1 day |
| **Onboarding series** | 5 | Email 1: Signup immediately; Emails 2-5: previous email sent + 1 day |
| **Education series** | 3 | Email 1: Signup + 1 day; Emails 2-3: previous email sent + 1 day |

**Free plan gets: Welcome message (1 email) only.**
**Essentials gets: Single email automations + flows up to 4 steps.**
**Standard gets: Expanded flows + flow templates.**

### All Trigger Types (Classic Automations)

**Campaign activity triggers:**
- Sent campaign, Opened campaign, Not opened campaign, Clicked campaign, Not clicked campaign, Specific link clicked

**Subscriber/audience triggers:**
- Manual add, Signup, Changes in audience field, Joins group, Leaves group, Added tag

**Series triggers (use within a multi-step sequence):**
- Previous email sent, Previous email opened, Previous email not opened, Previous email clicked, Previous email not clicked, Specific link in previous email clicked

**E-commerce triggers:**
- Purchase any product, Purchase specific product, Purchase from category, Time since last purchase, Abandoned Cart, Email Retargeting

**API triggers:**
- API 3.0 (post subscriber email ID to endpoint), Event API (Premium only)

**Date-based triggers:**
- List added date, Recurring dates, Birthdays, Specific date

### Important: Classic Automations Deprecation Note

Classic Automations are being transitioned to "Automation Flows" (formerly Customer Journeys). It is possible to convert a Classic Automation to a Marketing Automation Flow. Classic Automations are only available to paid accounts that have previously created one.

---

## 3. Mailchimp API v3 — Classic Automations Endpoints

Base URL: `https://<dc>.api.mailchimp.com/3/`

### Endpoints

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/automations` | List all classic automations |
| `POST` | `/automations` | Create a new classic automation |
| `GET` | `/automations/{workflow_id}` | Get automation info |
| `POST` | `/automations/{workflow_id}/actions/start-all-emails` | Start all automation emails |
| `POST` | `/automations/{workflow_id}/actions/pause-all-emails` | Pause all emails |
| `POST` | `/automations/{workflow_id}/archived` | Archive automation |
| `GET` | `/automations/{workflow_id}/emails` | List emails in workflow |
| `GET` | `/automations/{workflow_id}/emails/{workflow_email_id}` | Get workflow email info |
| `PATCH` | `/automations/{workflow_id}/emails/{workflow_email_id}` | Update workflow email |
| `POST` | `/automations/{workflow_id}/emails/{workflow_email_id}/actions/pause` | Pause email |
| `POST` | `/automations/{workflow_id}/emails/{workflow_email_id}/actions/start` | Start email |
| `GET` | `/automations/{workflow_id}/emails/{workflow_email_id}/queue` | Get subscriber queue |
| `POST` | `/automations/{workflow_id}/emails/{workflow_email_id}/queue` | Add subscriber to queue |
| `GET` | `/automations/{workflow_id}/removed-subscribers` | List removed subscribers |
| `POST` | `/automations/{workflow_id}/removed-subscribers` | Remove subscriber from workflow |

### POST /automations — Create Automation

```json
{
  "recipients": {
    "list_id": "YOUR_LIST_ID"
  },
  "settings": {
    "title": "Welcome New Subscribers"
  },
  "trigger_settings": {
    "workflow_type": "welcomeSeries"
  }
}
```

**Supported `workflow_type` values for PATCH updates:** `abandonedBrowse`, `abandonedCart`, `emailFollowup`, `singleWelcome`

Note: The `trigger_settings` object returns information for the first email in the workflow. Trigger defaults can be changed per-email after creation.

### POST /automations/{workflow_id}/emails/{workflow_email_id}/queue — Add Subscriber

```json
{
  "email_address": "subscriber@example.com"
}
```

Use this to manually add a subscriber to a workflow, bypassing default trigger settings. Also use to trigger a series of emails in an API 3.0 workflow type.

---

## 4. Mailchimp API v3 — Templates Endpoints

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/templates` | List templates |
| `POST` | `/templates` | Add/create a new template |
| `GET` | `/templates/{template_id}` | Get template info |
| `PATCH` | `/templates/{template_id}` | Update existing template |
| `DELETE` | `/templates/{template_id}` | Delete template |
| `GET` | `/templates/{template_id}/default-content` | Get template default content |

### POST vs PATCH — mc:edit Behavior

**Critical finding (confirmed from our project experience):**

- `POST /templates` — Creates a new template. When you include the full HTML with `mc:edit` attributes, Mailchimp processes and preserves those `mc:edit` sections as editable fields.
- `PATCH /templates/{id}` — Updates an existing template. **PATCH may strip or not properly register mc:edit sections** when the HTML is provided. Our project confirmed: use `POST` to create templates with `mc:edit` sections, not `PATCH` to recreate them.

**The API docs do not explicitly document this difference** — it was discovered empirically. The safe workflow is:
1. Use `POST` to create the template initially with full HTML containing `mc:edit` attributes.
2. Use `PATCH` only for metadata updates (name, etc.) — not for replacing the full HTML body when mc:edit sections must be preserved.

### Setting Campaign Content Using a Template

```
POST /campaigns/{campaign_id}/content
{
  "template": {
    "id": 11869800,
    "sections": {
      "welcome_note": "<p>Your welcome text here</p>",
      "spotlight": "<p>Spotlight content</p>",
      "section2": "<p>Section 2 content</p>",
      "section3": "<p>Section 3 content</p>",
      "section4": "<p>Section 4 content</p>",
      "section5": "<p>Section 5 content</p>",
      "events_calendar": "<p>Upcoming events</p>"
    }
  }
}
```

Section names must exactly match the `mc:edit` attribute values in the template HTML.

---

## 5. mc:edit — How It Works in Coded Templates

### Core Rules

- `mc:edit="unique_name"` on an HTML element makes it an editable content area in the Mailchimp campaign editor.
- **Names must be unique** within a template. Duplicate names = content conflicts.
- The name becomes a database field — if you rename an `mc:edit` attribute after content is saved, the content is lost.
- **Supported container elements:** `<div>`, `<td>` (table cell), and any block-level container element.
- **Also supported on `<img>`** — allows image replacement, resize, and edit via campaign editor.
- **Do NOT nest** `mc:edit` elements inside other `mc:edit` elements.
- **Do NOT place** editable images inside an editable content container.

### href Attributes and mc:edit

`mc:edit` controls the **content** of an element, not `href` attributes directly. To make a link's URL editable:
- Place `mc:edit` on a containing `<td>` or `<div>` and let the editor control the full `<a>` tag including href.
- Or use merge tags / hardcode the URL — `mc:edit` alone does not expose `href` as a separate field.

### Naming Conventions

```html
mc:edit="header"          <!-- email header content -->
mc:edit="header_image"    <!-- editable header image -->
mc:edit="body"            <!-- main content area -->
mc:edit="sidebar"         <!-- left or right column -->
mc:edit="footer"          <!-- footer content -->
```

### Additional Template Language Tags

| Tag | Purpose |
|---|---|
| `mc:hideable` | Hide/show element in campaign editor. No value needed. |
| `mc:repeatable` | Allow element duplication in editor. Use on block-level elements. |
| `mc:label="name"` | Display name for an mc:edit section in the editor. Optional — falls back to mc:edit name. |
| `mc:variant` | Used with mc:repeatable to switch between discrete HTML blocks. |

### Editable CSS

Prefix CSS properties with `/*@editable*/` to make them editable in the campaign builder:

```css
/*@tab Header*/ /*@section Header Style*/
/*@editable*/ color:#202020 !important;
/*@editable*/ font-family:Arial;
/*@editable*/ font-size:34px;
```

- `@tab` = top-level group (required)
- `@section` = subsection within tab (optional but recommended)
- `@style` = adds ruleset to text editor dropdown (optional, text styles only)

---

## 6. SAME SF Account Quick Reference

| Item | Value |
|---|---|
| Audience ID | `9d174b3762` |
| Plan | Free (forever_free) |
| Subscribers | ~927 active |
| Newsletter template ID (mc:edit) | `11869800` — 7 sections: welcome_note, spotlight, section2, section3, section4, section5, events_calendar |
| Event Announcement template ID | `11869797` — 9 sections: preview_text, subtitle, event_image, eyebrow, headline, body_copy, event_details, signoff, cta_button. Source: `campaigns/05-may-2026/event-announcement-template-v2.html` |
| Event Reminder template ID | `11869798` — 8 sections: preview_text, subtitle, eyebrow, headline, body_copy, event_details, signoff, cta_button. Shorter body, no bullets. Source: `campaigns/05-may-2026/event-reminder-template-v2.html` |
| Know Before You Go template ID | `11869799` — 10 sections: preview_text, subtitle, eyebrow, headline, body_intro, logistics, schedule, what_to_bring, contact, signoff. No cta_button. Needs New Builder rebuild. |
| Welcome Email template ID | `11869770` — 0 mc:edit sections. Content is hardcoded. Needs full rebuild before automation can be set up. |

### Segmentation on Free Plan

Segmentation **does not work** for campaign sends on the Free plan. All sends go to the full audience. Pre-built segments and advanced segmentation require Standard plan.

### Automation on Our Account

Free plan gives us: one-click welcome email (single email, signup trigger). Multi-step welcome series requires Essentials or higher.

### Classic Builder Deprecation

Mailchimp Classic Builder was deprecated May 31, 2026. All templates need New Builder versions. Know Before You Go template still needs to be rebuilt for New Builder.

---

_Sources: mailchimp.com/help/about-mailchimp-pricing-plans/, mailchimp.com/help/classic-automation-types/, mailchimp.com/help/all-the-classic-automation-triggers/, mailchimp.com/developer/marketing/api/automation/, templates.mailchimp.com/getting-started/template-language/_
