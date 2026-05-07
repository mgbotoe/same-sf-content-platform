# Email 2 — Registration Opens (May 18, 2026)

**Campaign:** To be created in Mailchimp
**Template:** Event Announcement (11869797)
**Send date:** Monday, May 18, 2026 — 7:00 AM PDT
**Audience:** Full list (~914 subscribers)
**Status:** Draft — blocked on registration URL

---

## ⚠️ MISSING BEFORE PUSH

- [ ] **Registration URL** — separate form from abstract submission, being set up by Kate Garufi / EPA. Required for cta_button section and body_copy link.

---

## Subject / Preview

- **Subject:** Registration is open: Mine Cleanup Info Exchange, June 16
- **Preview:** EPA Region 9 × SAME SF | Three spots per firm — register before spots fill.

---

## Sections

### `preview_text`
```
EPA Region 9 × SAME SF | Three spots per firm — register before spots fill.
```

### `subtitle`
```html
<p style="margin:0 0 6px 0;font-family:Georgia,'Times New Roman',Times,serif;font-size:18px;color:#374151;line-height:1.4;">EPA Region 9 × SAME San Francisco Post</p>
<p style="margin:0;font-family:Georgia,'Times New Roman',Times,serif;font-size:14px;color:#6B7280;font-style:italic;line-height:1.4;">Strengthening community through service, leadership, and collaboration.</p>
```

### `eyebrow`
```
Registration Now Open
```

### `headline`
```
Mine Cleanup Info Exchange | June 16, 2026
```

### `body_copy`
```html
<p style="margin:0 0 16px 0;font-family:Arial,Helvetica,sans-serif;font-size:16px;color:#374151;line-height:1.6;">Registration is now open for the Mine Cleanup Info Exchange. Each firm registers once and selects up to three attendees. Presenters and poster contributors count toward your firm's three spots — plan accordingly.</p>

<p style="margin:0 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:16px;color:#374151;line-height:1.6;">The day runs three practitioner-led sessions, each followed by open poster sessions where you can go deeper with presenters:</p>

<ul style="margin:0 0 16px 0;padding-left:20px;font-family:Arial,Helvetica,sans-serif;font-size:16px;color:#374151;line-height:1.8;">
<li>Residential Mine Cleanup Projects</li>
<li>Geomorphic and Natural Reclamation-Focused Repository Design and Construction</li>
<li>Large-Scale Mine Waste Excavation and Consolidation in Remote and Challenging Terrain</li>
</ul>

<p style="margin:0 0 16px 0;font-family:Arial,Helvetica,sans-serif;font-size:16px;color:#374151;line-height:1.6;">The morning closes with 50 minutes of facilitated breakout discussion before closing remarks at 1:20 PM.</p>

<p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:16px;color:#C41E3A;font-weight:bold;line-height:1.6;">Abstract submissions close tomorrow, May 19. If you plan to present or contribute a poster, submit before registering so you can reserve the right spot for your team.</p>
```

### `event_details`
```
📅 Date: Tuesday, June 16, 2026
🕘 Time: 9:00 AM – 1:30 PM PDT (Check-in 8:45 AM)
📍 Location: EPA Region 9 Office, San Francisco, CA
👥 Registration: 3 attendees per firm, family-style
```

### `signoff`
```html
<p style="margin:0 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:16px;color:#374151;line-height:1.6;">We look forward to seeing you there.</p>
<p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:16px;color:#374151;line-height:1.6;"><strong>The SAME San Francisco Post</strong></p>
```

### `cta_button`
```
⚠️ MISSING: Registration URL needed from Kate Garufi / EPA before this can be pushed.

Button text: Register Now →
Button URL: [REGISTRATION URL — TBD]
```

### `add_to_calendar`
```html
<p style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:13px;color:#6B7280;text-align:center;line-height:1.6;">Add to calendar: <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Mine+Cleanup+Info+Exchange&dates=20260616T160000Z%2F20260616T203000Z&location=EPA+Region+9+Office%2C+San+Francisco%2C+CA&details=SAME+SF+%2B+EPA+Region+9" target="_blank" style="color:#003478;text-decoration:underline;">Google Calendar</a> &nbsp;&middot;&nbsp; <a href="https://github.com/mgbotoe/samesf-graphics/releases/download/calendar-files/mine-cleanup-june16.ics" style="color:#003478;text-decoration:underline;">Outlook / Apple</a></p>
```

---

## Push Script Notes

When registration URL is confirmed:
1. Create new campaign in Mailchimp using template 11869797
2. Push all sections above via API
3. Replace `[REGISTRATION URL — TBD]` in cta_button with confirmed link
4. Schedule for May 18, 2026 at 14:00 UTC (7:00 AM PDT)
