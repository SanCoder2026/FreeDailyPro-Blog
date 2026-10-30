Sent: 2026-10-30 14:25 ET

# B-0262 Agenda Builder: no preview before the gate, overlaps the Agenda and Cue Sheet Builder; add a preview and merge or link the two
Priority: P2 · Estimated effort: M · Report: #145 · Source: Playwright headless, logged out, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:23–14:25 ET. L-243: next 3 untested tools alphabetically (sitemap minus ledger/test plan). No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
An organiser should paste a schedule, see the printable programme, and decide to pay knowing what they get.
## Why (1280 px; 0 trial uses)
- Inputs: source "My project schedule" or "Type it here" (one line per item, `time | title | presenter | room`), title, subtitle, footer, colour, presenters/rooms/tracks toggles, Letter/A4.
- **Try a sample loads 6 sessions, but no programme preview is shown;** the only output is "Download programme (PDF)", which opens "You've used today's trial uses… today's 10 trial uses". The user cannot see the layout before paying.
- **Trial-uses wording clash:** this dialog says "10 trial uses"; the sibling Agenda and Cue Sheet Builder header says "Trial: 2 uses/day" → **B-0156**.
- **Overlap:** the Agenda and Cue Sheet Builder (B-0263) has the same schedule plus a "Printed agenda" step. Two near-identical pages compete for "agenda builder" searches.
- **Missing vs competitors (~14:24 ET):** AgendaForge builds an agenda and passes it to its run-of-show generator in one click; Event70 prints and copies a plain-text version for chat.
- No overflow at 390 px.
## Who uses this
Office managers, conference and offsite organisers, wedding planners.
## Outcomes (ranked)
1. Show a live programme preview before the gate.
2. Decide: merge into the Agenda and Cue Sheet Builder, or link each to the other clearly and give them different keywords.
3. One trial-uses number on both pages.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD, all images have alt. /es English → **B-0123**.
  - **Title "Agenda Builder - Printable Event Programme PDF | FreeDailyPro" is 61 chars.** **Meta 127.** H1 "Agenda Builder".
- **Keywords:** "agenda builder", "event programme template", "printable event agenda", "conference agenda pdf".
- **Suggested:**
  - Title: `Agenda Builder – Printable Event Programme | FreeDailyPro` (57)
  - Meta: `Turn your event schedule into a printable programme: times, session titles, presenters and rooms on US Letter or A4. Type it or use your project schedule.` (154)
  - H1: `Build a Printable Event Agenda`
  - FAQ: "Can I add several days?" · "Letter or A4?" · "Is my schedule saved?" → "In this tab only."
## Constraints
Keep the PDF gated per the owner's decision; the preview should be view-only.
## Test cases
1. Fresh session, Try a sample → programme preview shows 6 sessions.
2. Title ≤ 60; meta 140–160.
