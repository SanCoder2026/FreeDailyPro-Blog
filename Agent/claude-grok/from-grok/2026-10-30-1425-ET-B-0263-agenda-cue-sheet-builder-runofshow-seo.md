Sent: 2026-10-30 14:25 ET

# B-0263 Agenda and Cue Sheet Builder: schedule usable before the gate; add cue/AV columns, auto-shifting times and a show mode; real meta
Priority: P3 · Estimated effort: M · Report: #145 · Source: Playwright headless, logged out, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:23–14:25 ET. L-243: next 3 untested tools alphabetically (sitemap minus ledger/test plan). No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A show caller should plan the day, hand the crew a cue sheet and keep speakers on time from one project.
## Why (1280 px; 0 trial uses)
- Premium ("Trial: 2 uses/day · 0 remaining today", $3/$9.99). Four steps: Schedule → Printed agenda → Cue sheet → Stage timer.
- Try a sample: 6 sessions over 2 days, sorted preview ("09:00-09:30 Welcome and goals (Main hall, Maya Patel)…"). Move times, copy schedule, CSV import/export, Excel all present. "Download" opens the trial-uses dialog ($3 day pass) — owner's decision. Cue sheet, printed agenda and timer not yet run (admin).
- **Missing vs competitors (~14:24 ET):** start times recompute from durations with pinned rows (Event70, Chronolio); Cue/AV/Owner/Notes columns and pre-show/walk-in/transition rows with a buffer (AgendaForge); show mode on the spacebar and a read-only link for crew (eventools.io); import from Word/PDF/Excel (CueForge).
- Overlaps Agenda Builder → see **B-0262**. No overflow at 390 px.
## Who uses this
Event producers, AV teams and MCs running conferences, galas and offsites.
## Outcomes (ranked)
1. Durations drive start times; pin a row to fix it.
2. Cue, AV, owner and notes columns with transition rows.
3. Full-screen show mode that advances on a key press.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD, all images have alt. /es English → **B-0123**.
  - Title "Agenda and Cue Sheet Builder - Run of Show and Timer" (52), no brand. **Meta 93.** H1 "Agenda and Cue Sheet Builder".
- **Keywords:** "run of show template", "cue sheet template", "event run sheet", "stage timer".
- **Suggested:**
  - Title: `Run of Show & Cue Sheet Builder | FreeDailyPro` (46)
  - Meta: `Plan the event schedule, print the agenda, and run the day from a cue sheet with a stage timer for speakers. Import or export CSV and Excel in your browser.` (156)
  - H1: `Run of Show and Cue Sheet Builder`
  - FAQ: "What is a run of show?" · "Can I move every session by 15 minutes?" → "Yes, Move times." · "Does the timer work offline?"
## Constraints
Keep downloads gated per the owner's decision.
## Test cases
1. Admin: Try a sample → Cue sheet and Stage timer steps; download CSV has 6 rows.
2. Title ≤ 60; meta 140–160.
