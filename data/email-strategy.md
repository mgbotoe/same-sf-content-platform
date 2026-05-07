# Email Strategy — SAME SF Mailchimp Operations

Operational reference for email content and list management. Strategic layer lives in `identity/SOUL.md → Email Strategy`.

---

## Subject Lines

- **Under 40–50 characters.** Higher Logic association benchmark: under 9 characters performs best; under 50 is the practical ceiling. Mobile truncates at ~33–40 characters.
- **Specificity beats clever.** "Registration is open: Mine Cleanup, June 16" outperforms "Don't miss this." Personalized/specific subject lines hit 46% opens vs. 35% generic (Belkins 2024, 5.5M emails).
- **Numbers in subject lines no longer help** — 2024 data shows slight underperformance vs. no numbers. Tactic decay from older advice.
- **No first-name personalization tokens.** Now neutral or negative for associations (Higher Logic 2024–2026). Substitute job title or industry reference if personalizing.
- **ALL CAPS is a cumulative spam signal**, not an automatic killer — but avoid it. One fully-capitalized word slightly underperforms; full-subject ALL CAPS triggers spam-filter cumulative scoring when combined with other signals.
- **3 punctuation marks max per subject line** (Mailchimp official guidance).

## Preview Text

- Always write it — never leave the default "View this email in your browser."
- Treat as a 5–15% open-rate lever, not near-equal to subject line.
- Outlook desktop (primary client for government/AEC corporate inboxes) often does not render preview text — design subject line to stand alone.
- Apple Intelligence (iOS 18.1+) overwrites marketer-set preview text with AI-generated summaries for ~25%+ of Apple Mail opens. Don't rely on preview text for critical information.
- Keep under 90 characters.

## Email Length

- **400–2,000 words performs best** for association/professional content (Higher Logic 2024). "Shorter is always better" is wrong for this audience.
- Lead with value above the fold — mobile readers see ~3–4 lines before scrolling.
- Short paragraphs (3 lines max). Single column layout performs 21% better on mobile.

## CTAs

- **Primary CTA = a button.** Button CTAs outperform text links by ~127% in newsletter context (Campaign Monitor A/B).
- **Minimum 44×44 px tap target** — required for Section 508 / WCAG 2.1 compliance. Relevant for .gov subscribers where federal accessibility policy applies.
- **Action-verb microcopy:** "Register Now" / "Submit Your Abstract" / "View Event Details" — not "Learn More" or "Click Here."
- **Add a soft reply invitation in P.S.** — "Questions? Reply to this email." Captures relational responses that buttons miss. Hybrid outperforms either alone.
- Never use reply-only as the primary CTA in newsletter format.

## Frequency Thresholds

| Zone | Sends/month | Action |
|---|---|---|
| Safe | 1–4 | No monitoring needed |
| Caution | 5–8 | Watch unsubscribes and complaints closely |
| Danger | 8+ / 2+/week | Stop — B2B unsubscribes spike here |

Irregular cadence (silence → sudden burst) causes more unsubscribes than higher consistent frequency. A predictable 4/month beats a sporadic 1/month + 5 event emails.

## Unsubscribe and Complaint Benchmarks

| Metric | Normal | Yellow flag | Red flag |
|---|---|---|---|
| Unsubscribe rate | 0.05–0.25% per send | 0.5%+ (~5 people on 914-list) | Sustained >1% |
| Spam complaint rate | <0.1% | Approaching 0.1% | >0.1% — Mailchimp platform risk |

**On a 914-person list, ONE spam complaint = 0.1%.** This is the metric to watch — not unsubscribes.

Industry median unsubscribe rose from 0.08% (2024) to 0.22% (2025) due to Gmail one-click unsubscribe rollout — a doubling that reflects platform mechanics, not content failure.

Association median unsubscribe is historically 0.05% — associations run 3–5x lower than all-industry median because audiences are self-selected.

## List Health and Hygiene

**Bounce rates:**
- Hard bounce threshold: keep below 2% per send. Mailchimp warns at 5%.
- AEC/construction contacts have the highest industry bounce rate (1.32% avg, ER Marketing/MailerLite 2024) — high firm turnover causes frequent email churn.
- **Run quarterly hard-bounce cleanup on the A&E segment** (March/June/September/December — aligns with member sync cadence).

**Inactive subscribers:**
- iOS 18 (Oct 2024) sorts low-engagement senders into Promotions. Inactive subscribers on the list actively hurt inbox placement for engaged subscribers.
- Define inactive: no clicks in 180+ days (clicks only — opens are unreliable post-Apple MPP).
- Re-engagement sequence: 3 emails over 4–6 weeks. Email 1: value highlight + "still interested?", Email 2: preference/frequency change option, Email 3: "last chance — confirm to stay subscribed." Expect ~10% reactivation (Mailchimp documented rate).
- Suppress non-responders. Expect to archive 10–20% of list annually as normal churn.
- Note: Free/Essentials plan — re-engagement must be done manually via segments since Classic Automation is retired (June 2025).

## .gov and .mil Deliverability

- **Mailchimp "delivered" does not mean it reached .mil inboxes.** DoD filters silently quarantine commercial bulk email without bounce notifications. No visibility.
- DoD email runs Microsoft M365 GCC High behind multiple security layers. HTML is stripped or blocked; tracking pixels don't fire; links may be broken or rewritten.
- **Practical fix:** Collect alternate non-.mil/.gov contact emails from these subscribers. Ask them to have IT allowlist Mailchimp's sending IPs: `https://www.mailchimp.com/about/ips/`
- CISA BOD 18-01 (still enforced 2026): all federal .gov second-level domains require DMARC p=reject. Inbound .gov filters check DMARC alignment aggressively.
- Design every email to degrade gracefully: minimal images, no link shorteners, no tracking-pixel reliance, include plain-text version (verify Mailchimp's auto-generated plain-text tab before each send).

## Outlook/Desktop Design Notes

Government, military, and AEC corporate inboxes run Microsoft Outlook / M365 — not Gmail.

- Outlook blocks images by default. Always set descriptive alt text on every image.
- Outlook adds padding between sliced images — avoid all-image designs.
- Outlook 3-pane view often does not render preview text.
- Single-column layouts perform 21% better on mobile and degrade better in Outlook.
- Desktop CTR (3.4%) outperforms mobile (2.6%) for content-rich B2B — design for desktop-primary.

## Performance Benchmarks (2025–2026)

| Metric | Association median | Government vertical | Target for SAME SF |
|---|---|---|---|
| Open rate (Mailchimp-reported) | 33.54% | 28.77–46% | 33–45% (inflated by MPP) |
| Real engagement open rate | ~18–22% | ~20–28% | Not trackable directly |
| Click rate | 2.68% | 3.99–4.58% | 2.5–4% |
| Unique clicks per send (914 list) | — | — | 23–37 clicks |
| Unsubscribe rate | 0.22% | — | <0.25% per send |

Source: Higher Logic 2025–2026 Association Benchmark (2B emails, 1,500+ associations); Mailchimp official vertical benchmarks; Brevo 2025 (44B emails).
