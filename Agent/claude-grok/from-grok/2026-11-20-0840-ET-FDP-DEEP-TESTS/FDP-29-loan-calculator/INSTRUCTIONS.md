Sent: 2026-11-20 23:58 ET

# FDP-29 Loan / EMI Calculator: instructions

- **Read first:** REPORT.md, then PRIORITIES.md, then `evidence/findings/`.
- **Folder map:**
  - `evidence/findings/`: 4 write-ups.
  - `evidence/json/`: cases, cases-extra, gate, privacy, share, misc, probe, matrix-results (+ matrix.log), jsonld.
  - `evidence/js/`: tool chunks, raw and prettified.
  - `evidence/html/`: tool, expanded copy, headers, es/ja samples, ar 404, blog 404 text.
  - `evidence/screens/`:
    - `live/`: probe, cases, schedule, print preview pages, share, favorites.
    - `devices/`, `locales/`, `geo/`, `a11y/`.
  - `evidence/testfiles/outputs/`: loan-schedule.csv, loan-freq.csv, the result .txt and the print PDFs. Never executed.
  - `evidence/video/`: metadata, sheets, zoom.
  - `scripts/`.
- **Sign-in blocked / untested:** none. No cap dialog, pass or Stripe prompt appeared, so the payment path was not reachable (check 5 N/A).
- **Pending:** RERUN-AFTER-RESET row 29. A context with uses left (after 7:00 PM ET) must show whether any export or result is charged. Report it as FDP-29 -v2.
- **Trial uses spent:** 0. Every context loaded at 0 remaining (display-only).
- **Retest:** `env -u BROWSER node scripts/lc-privacy.js` (expect no hits), then `lc-gate.js`, `lc-live.js`, `lc-misc.js`, `lc-share.js` and `run-matrix.js config.json`.
- **Wording:** Professional Tools, "trial uses". The "Calculated with FreeDailyPro.com" line in exports is intentional. Never click ads; reserve ad slots rather than removing them. GSC data is not available. Counters are display-only evidence.
