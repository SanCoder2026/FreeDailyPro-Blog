Sent: 2026-11-20 23:05 ET

# FDP-27 BMI Calculator: instructions

- **Read first:** REPORT.md, then PRIORITIES.md, then `evidence/findings/` (live-functional, desk, devices-locales, video).
- **Folder map:**
  - `evidence/findings/`: 4 write-ups.
  - `evidence/json/`: cases (+B39), gate, privacy, share, misc, probe, matrix-results, jsonld.
  - `evidence/js/`: the BMI chunks, raw and prettified.
  - `evidence/html/`: tool, locales, blog text, expanded copy, headers.
  - `evidence/screens/`:
    - `live/`: probe, cases, print preview, share, favorites, extreme, blog.
    - `devices/`, `locales/`, `geo/`, `a11y/`.
  - `evidence/testfiles/outputs/`: the downloaded CSV and .txt, and the print PDF; never executed.
  - `evidence/video/`: metadata, 4 frame sheets, key frames.
  - `scripts/`.
- **Sign-in blocked / untested:** none. The tool needs no sign-in; Share copies a link and favorites are local. No pass, Day Pass or Stripe prompt appears on this page, so the payment path was not reachable from the tool.
- **Pending:** none; no RERUN-AFTER-RESET row (nothing is counted; both 0-remaining and 10-remaining contexts were observed).
- **Trial uses spent:** 0.
- **Retest:**
  1. Run `env -u BROWSER node scripts/bmi-privacy.js` (it must find no hits).
  2. Run `bmi-gate.js` (per Santosh's decision).
  3. Run `bmi-live.js` and compare with test-cases.md.
  4. Run `bmi-misc.js` (print PDF must show the BMI).
  5. Run `run-matrix.js config.json`.
- **Wording:** Professional Tools, "trial uses". The "Calculated with FreeDailyPro.com" line in exports is intentional. Never click ads; reserve ad slots rather than removing them. GSC data is not available.
