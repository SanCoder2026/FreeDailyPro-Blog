Sent: 2026-11-21 00:18 ET

# FDP-30 JWT Decoder: instructions

- **Read first:** REPORT.md, then PRIORITIES.md, then `evidence/findings/`.
- **Folder map:**
  - `evidence/findings/`: 4 write-ups.
  - `evidence/json/`: cases, cases-extra, gate, share, misc, probe, matrix-results (+ matrix.log), jsonld.
  - `evidence/js/`: tool chunks, raw and prettified.
  - `evidence/html/`: tool, expanded copy, headers, es/ja samples, ar 404, both blog texts.
  - `evidence/screens/`:
    - `live/`: probe, cases (incl. the J13 error page), share, blog tops.
    - `devices/`, `locales/`, `geo/`, `a11y/`.
  - `evidence/testfiles/`: tokens.json (synthetic J01–J23). `outputs/` holds the saved result .txt and the print PDF. Never executed.
  - `evidence/video/`: metadata, sheets, zoom.
  - `scripts/`.
- **Sign-in blocked / untested:** none. No cap dialog, pass or Stripe prompt appeared, so the payment path was not reachable (check 5 N/A).
- **Pending:** RERUN-AFTER-RESET row 30. A context with uses left (after 7:00 PM ET) must show whether decoding or any result action is charged. Report it as FDP-30 -v2.
- **Trial uses spent:** 0. Every context loaded at 0 remaining (display-only).
- **Retest:** `env -u BROWSER node scripts/jd-live.js` (J13 must not crash; `leaks` must stay empty), then `jd-gate.js`, `jd-misc.js`, `jd-share.js` and `run-matrix.js config.json`.
- **Wording:** Professional Tools, "trial uses". The "Calculated with FreeDailyPro.com" line in exports is intentional. Never click ads; reserve ad slots rather than removing them. GSC data is not available. Counters are display-only evidence.
