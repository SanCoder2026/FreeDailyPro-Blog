Sent: 2026-11-21 01:26 ET

# FDP-33 Video Thumbnail Generator: instructions

- **Read first:** REPORT.md, then PRIORITIES.md, then `evidence/findings/`.
- **Folder map:**
  - `evidence/findings/`: 4 write-ups (live-functional, desk, video, devices-locales).
  - `evidence/json/`: probe, cases-* (per test file), fake-mp4-hang, gate, drain, misc, share, matrix-results (+ matrix.log, config), jsonld.
  - `evidence/js/`: tool chunks, raw and prettified.
  - `evidence/html/`: tool, expanded copy, headers, es/ja samples, ar 404, blog text.
  - `evidence/screens/`: `live/` (uploads, gallery, suggest, dialogs, cap dialog, Day Pass, Quick Buy, share, blog, probe), `devices/`, `locales/`, `geo/`, `a11y/`.
  - `evidence/testfiles/`: V3_720p.webm, V4_hevc.mp4, V5_black.mp4, X1/X2; `make-videos.sh` recreates V1/V2 (not shipped). `outputs/`: captured PNG/JPGs, the gate download, the gate ZIP and its extracted images (`zipx/`), print-preview.pdf. Never executed.
  - `evidence/video/`: metadata, sheets, zoom.
  - `scripts/`.
- **Sign-in blocked / untested:** Save to Google Drive (Google sign-in popup), Save to my cloud storage (email sign-in dialog), Open from Google Drive (not clicked). All on https://www.freedailypro.com/tool/thumbnail-gen.
- **Payment:** stopped at the Day Pass email prompt and at Stripe Checkout (session id redacted). Nothing typed.
- **Pending:** RERUN-AFTER-RESET row 33. A second uses-left context must confirm the ZIP stays uncharged (1, 2, 5 frames) and Capture/Suggest are uncounted. Report as FDP-33 -v2.
- **Trial uses spent:** 1 (display-only).
- **Retest:** `env -u BROWSER node scripts/tg-gate.js`, then `tg-live.js <video>`, `tg-drain.js`, `tg-misc.js`, `tg-share.js`, `run-matrix.js config.json`.
- **Wording:** Professional Tools / Premium Applications, "trial uses". The "Created with FreeDailyPro.com" badge is intentional. Never click ads; reserve ad slots rather than removing them. GSC data is not available. Counters are display-only evidence.
