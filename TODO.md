# SAME SF — To-Do List

Last updated: 2026-05-03 (A6 done, email sequence drafted)

---

## URGENT — Before May 31

| # | Task | Why | Owner |
|---|---|---|---|
| U1 | ✅ DONE — KBYG template rebuilt with 10 mc:edit sections (May 3) | Classic Builder retires May 31 | Sage |
| U2 | ✅ DONE — Welcome Email template rebuilt with 4 mc:edit sections (May 3) | Was hardcoded, can't update via API | Sage |
| U3 | ~~Welcome automation~~ — BLOCKED by plan | Classic Automations retired June 2025. Automation Flows require paid plan. Final Welcome Email requires Double Opt-in (SAME SF uses Single Opt-in). **No free path exists.** | Backlog |
| U4 | **Test custom-coded template workflow June 1+** | 5/31/2026 may close Free-plan API workaround for custom-coded templates. Send a test campaign June 1 — if mc:edit sections still push, we're safe. If broken, accelerate Standard upgrade. | Sage |
| U5 | **Decision: Standard plan upgrade ($35/mo)** | Custom-coded templates die on Essentials 5/31/2026. Standard is the only viable upgrade path for our workflow. Tie to Golf Tournament fundraising. **Never upgrade to Essentials.** | Dina |

---

## ACTIVE CAMPAIGNS — Blocking Work

| # | Task | Blocking | Date |
|---|---|---|---|
| A1 | ✅ DONE — Registration link confirmed (May 3) | Google Form URL already live in announcement campaign 3619932539 | — |
| A2 | Update May 18 newsletter with registration link once A1 confirmed | Can't finalize newsletter until A1 done | Sage |
| A3 | Update Mine Cleanup LinkedIn post with registration link (May 18) | Same as A2 | Sage |
| A6 | ✅ DONE — Add to Calendar URL pushed to Mine Cleanup announcement (May 3) | June 16, 9AM–1:30PM, EPA Region 9 Office SF. Campaign rescheduled. | Sage |
| A7 | **Create + push Mine Cleanup email 2 (Registration Opens, May 18)** | Draft at `campaigns/mine-cleanup-2026/02-registration-opens.md` — create campaign, push sections, schedule May 18 7AM | Sage (after A1 confirmed) |
| A8 | **Create + push Mine Cleanup email 3 (KBYG, June 9)** | Draft at `campaigns/mine-cleanup-2026/03-kbyg.md` — needs venue address + schedule detail before push | Sage (needs venue info) |
| A4 | AI Summit — May 7 post: Track reveal #2 + GovGiv sponsor | Needs speaker headshots + panel graphic from external team | Dina/team |
| A5 | Confirm Golf Tournament date + venue | Brief can't move to Tier 1 without it | Dina |

---

## EMAIL TEMPLATES — Improvements

| # | Task | Why |
|---|---|---|
| T1 | ✅ DONE — Add to Calendar button added to Event Announcement (May 3) | Industry standard, reduces no-shows |
| T2 | ✅ DONE — Add to Calendar button added to Event Reminder (May 3) | Same |
| T3 | Add `event_image` section to Event Reminder template | Inconsistent with Announcement — both should have optional image |
| T4 | Rename Newsletter template sections semantically | `section2`–`section5` are meaningless — rename to `event_teaser`, `sponsor_highlight`, `member_spotlight`, `resources` or similar |
| T5 | Add sponsor acknowledgment section to Newsletter template | No dedicated sponsor slot right now |
| T6 | Review and customize plain text version of all templates | Auto-generated versions are usually garbled |

---

## MAILCHIMP — Untapped Capabilities

| # | Task | Why |
|---|---|---|
| M1 | Build welcome automation sequence (2 emails: immediate + 7-day follow-up) | Free plan allows 1 automation — not using it |
| M2 | Set up subscriber tagging structure (member / sponsor / student / general) | Enables differentiated content without paid segmentation |
| M3 | Build re-engagement campaign for ~600 non-openers | 30% open rate means ~640 subscribers haven't opened in months |
| M4 | Add UTM parameters to all CTA links | Currently no way to track which emails drive web traffic |

---

## CONTENT OPERATIONS — Infrastructure

| # | Task | Why |
|---|---|---|
| C1 | Run `/performance-review` after Mine Cleanup sends (May 12) | Establish baseline for event announcement emails |
| C2 | Run `/performance-review` on March–April posts | No baselines exist yet |
| C3 | Build Golf Tournament brief once date confirmed | Currently has 7 open blockers |
| C4 | Create event recap post for Geospatial Panel (April event) | Retroactive — still worth doing |

---

## NOTES

- **Max 2 Hero campaigns in Tier 1 at once** — AI Summit + Mine Cleanup = at capacity. Golf Tournament goes to Tier 3 until Mine Cleanup closes.
- **Mine Cleanup closes June 16** — retro.md due after event.
- **AI Summit external team owns content** — chase assets, don't write. Check calendar weekly.
- **Mailchimp Free plan limits**: no A/B testing, no behavioral triggers, no advanced segmentation, 1 automation slot.
