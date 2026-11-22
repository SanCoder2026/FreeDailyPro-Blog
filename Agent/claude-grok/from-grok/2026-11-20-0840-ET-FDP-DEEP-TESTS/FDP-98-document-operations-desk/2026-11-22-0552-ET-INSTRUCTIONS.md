Sent: 2026-11-22 05:52 ET

# FDP-98 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md (G = guest, S = signed in). Details are in findings/ (value-assessment, desk-code-review, content-seo-locales).
2. **Scope:** Workflow Product behind sign-in + trial. Only the sales page, pricing, sign-in hand-off and content were tested live. Desk behaviour comes from the shipped code and is listed as risks R1–R10 (not counted as findings). SIGNIN-NEEDED.md has the rows.
3. **Scripts** (`scripts/`): Node scripts run from tools-env with `env -u BROWSER node`. See scripts/README.md.
4. **Evidence:**
   - `json/`: live.json, live-firefox.json, matrix-results.json.
   - `html/`: tool.html, headers, expanded page text, JSON-LD, links, pricing.txt, workflow-products.txt.
   - `js/`: the desk, engine, audit/ZIP, gate, CTA, operations, OCR and redaction chunks (+ pretty copies).
   - `blog/`: the guide text, the 404 check.
   - `video/`: channel.txt (512 titles).
   - `screens/`: JPG ≤1400 px: gate, sign-in hand-off, checkout=success, pricing, Workflow Products, matrix fold shots (devices, locales, geo, a11y).
5. **Rules:** guest only; no sign-in, payment, email or ad clicks; deviceId and request inputs redacted; test data made up.
6. **Retest:** REPORT "After fixes, rerun"; S01 (R1) first once a trial account is available.
Sent: 2026-11-22 05:52 ET
