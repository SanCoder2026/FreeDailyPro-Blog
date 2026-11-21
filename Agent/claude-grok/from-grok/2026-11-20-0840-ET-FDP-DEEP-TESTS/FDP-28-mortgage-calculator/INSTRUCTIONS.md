Sent: 2026-11-20 23:25 ET

# FDP-28 Mortgage Calculator: instructions

- **Read first:** REPORT.md, then PRIORITIES.md, then `evidence/findings/` (live-functional, desk, devices-locales, video).
- **Folder map:**
  - `evidence/findings/`: 4 write-ups.
  - `evidence/json/`: cases, cases-blog, gate, privacy, share, misc, probe, matrix-results (+ matrix.log), jsonld.
  - `evidence/js/`: tool chunks, raw and prettified.
  - `evidence/html/`: tool, locale samples, ar 404, blog text, expanded copy, headers.
  - `evidence/screens/`:
    - `live/`: probe, cases, schedule, print preview, share, favorites, blog.
    - `devices/`, `locales/`, `geo/`, `a11y/`.
  - `evidence/testfiles/outputs/`: downloaded CSV and .txt, and the print PDFs. Never executed.
  - `evidence/video/`: metadata, 4 frame sheets, zoomed crops.
  - `scripts/`.
- **Sign-in blocked / untested:** none. The tool needs no sign-in; Share copies a link; favorites are local. No cap dialog, pass or Stripe prompt appeared, so the payment path could not be reached from this tool (check 5 N/A).
- **Pending:** RERUN-AFTER-RESET row 28. A context that loads with uses left (after 7:00 PM ET) must show whether any export/result is charged. Report it as FDP-28 -v2.
- **Trial uses spent:** 0. Every context loaded at 0 remaining (display-only).
- **Retest:**
  1. `env -u BROWSER node scripts/mc-privacy.js` (expect no hits).
  2. `mc-gate.js`.
  3. `mc-live.js`; compare with test-cases.md.
  4. `mc-misc.js` (print PDFs must show the summary).
  5. `mc-share.js`.
  6. `run-matrix.js config.json`.
- **Wording:** Professional Tools, "trial uses". The "Calculated with FreeDailyPro.com" line in exports is intentional. Never click ads; reserve ad slots rather than removing them. GSC data is not available. Counters are display-only evidence.
