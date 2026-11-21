Sent: 2026-11-20 22:15 ET

# FDP-26 Invoice Generator: instructions

- **Read first:** REPORT.md, then PRIORITIES.md, then `evidence/findings/` (each ends with the Nov 20 re-verification where relevant).
- **Folder map:** `evidence/findings/` (4 write-ups), `evidence/json/` (Nov 19: ui, ui2, ui.log, ui-AB.log, spend-A/B/C, spend-A-webkit, profile-D + saved profiles, probe, matrix-results, jsonld; Nov 20: `spend-1120/` spend-A, spend-B, spend-A-firefox, `probe-2026-11-20.json`), `evidence/js/` (current Nov 20 chunks, prettified; logic identical to Nov 19 apart from chunk names), `evidence/html/`, `evidence/screens/` (live incl. `*-1120.png` re-runs, devices, locales, geo, a11y, video), `evidence/testfiles/` (logo.png, clients.csv, junk.csv, bad-profile.json; `outputs/` Nov 19 files, `outputs/2026-11-20/` re-run files), `evidence/video/` (metadata), `scripts/`.
- **Sign-in blocked / untested (guest only, never signed in):**
  - https://www.freedailypro.com/tool/invoice-generator → PDF/Word/Excel at 0 → "You've used today's trial uses" → Buy Day Pass $3 → email prompt (stopped; nothing typed).
  - No Drive/cloud/account features on this tool (profile is a local file), so nothing else is sign-in blocked. The tools.csv "API returns totals only" note was not tested (no API testing).
- **Pending:** none; no RERUN-AFTER-RESET row.
- **Trial uses spent:** 10 (6 on Nov 19, 4 on Nov 20).
- **Wording:** Professional Tools / Premium Applications, "trial uses". The badge is intentional. Never click ads; reserve ad slots rather than removing them.
