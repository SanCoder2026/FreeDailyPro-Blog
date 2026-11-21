Sent: 2026-11-21 01:50 ET

# FDP-34 Convert Image Format: instructions

- **Read first:** REPORT.md, then PRIORITIES.md, then `evidence/findings/`.
- **Folder map:**
  - `evidence/findings/`: 4 write-ups (live-functional, desk, video, devices-locales).
  - `evidence/json/`: probe, cases-chromium (C01–C32), cases-firefox, pairs, gate / gate2 / gate3, axe-loaded, misc, share, matrix-results (+ matrix.log), jsonld.
  - `evidence/js/`: tool chunks raw and prettified (`ToolPage` and `index` raw only for size; see the line refs in REPORT).
  - `evidence/html/`: tool, expanded copy, headers, es/ja samples, ar 404, 2 pair pages, blog text.
  - `evidence/screens/`: `live/` (probe, cases, batch, dialogs, Day Pass, Quick Buy, share), `devices/`, `locales/`, `geo/`, `a11y/`.
  - `evidence/testfiles/`: T01–T16 except T14 (recreate with `make-files.py`). `outputs/`: result previews, gate downloads (single, frames ZIP, batch ZIP), print-preview.pdf. Never executed.
  - `evidence/video/`: metadata, sheets, zooms.
  - `scripts/`.
- **Sign-in blocked / untested:** Save to Google Drive (Google sign-in popup), Save to my cloud storage (email sign-in dialog). Open from Google Drive and Take photo with camera not clicked. All on https://www.freedailypro.com/tool/convert-image.
- **Payment:** stopped at the Day Pass email prompt and at Stripe Checkout (session id redacted). Nothing typed.
- **Pending:** none needing the reset (no RERUN-AFTER-RESET row). Unverified: AVIF output in a real desktop Chrome/Firefox.
- **Trial uses spent:** 6 (display-only).
- **Retest:** `env -u BROWSER node scripts/cim-gate2.js`, `cim-gate3.js`, `cim-gate.js`, `cim-live.js`, `cim-pairs.js`, `cim-axe-loaded.js`, `run-matrix.js config.json`.
- **Wording:** Professional Tools / Premium Applications, "trial uses". Never click ads; reserve ad slots rather than removing them. GSC data is not available. Counters are display-only evidence.
