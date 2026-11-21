Sent: 2026-11-21 00:40 ET

# FDP-31 UUID Generator: instructions

- **Read first:** REPORT.md, then PRIORITIES.md, then `evidence/findings/`.
- **Folder map:**
  - `evidence/findings/`: 4 write-ups.
  - `evidence/json/`: cases, gate, try, share, misc, probe, matrix-results (+ matrix.log), jsonld.
  - `evidence/js/`: tool and gate chunks, raw and prettified.
  - `evidence/html/`: tool, expanded copy, headers, es/ja samples, ar 404, blog text.
  - `evidence/screens/`:
    - `live/`: probe, the 1,000 batch, uppercase, share, the try at 0, blog top.
    - `devices/`, `locales/`, `geo/`, `a11y/`.
  - `evidence/testfiles/outputs/`: generated-sample.txt (1,000 UUIDs from the run) and the print PDF. Never executed.
  - `evidence/video/`: metadata, sheets, zooms.
  - `scripts/`.
- **Sign-in blocked / untested:** none. No cap dialog, pass or Stripe prompt appeared, so the payment path was not reachable (check 5 N/A).
- **Pending:** RERUN-AFTER-RESET row 31. A context with uses left (after 7:00 PM ET) must show whether Generate and each copy are charged. Report it as FDP-31 -v2.
- **Trial uses spent:** 0. Every context loaded at 0 remaining (display-only).
- **Retest:** `env -u BROWSER node scripts/ug-gate.js`, then `ug-live.js`, `ug-misc.js`, `ug-share.js` and `run-matrix.js config.json`.
- **Wording:** Professional Tools, "trial uses". Never click ads; reserve ad slots rather than removing them. GSC data is not available. Counters are display-only evidence.
