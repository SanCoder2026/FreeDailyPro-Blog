Sent: 2026-11-21 21:25 ET

# FDP-85 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out (e.g. "REPORT.md" means `…-ET-REPORT.md`).
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`; strip the date prefix first): see scripts/README.md. Test pictures are in evidence/testfiles/ (make-testfiles85.py, seed 85; the table pictures come from #84's make-testfiles.py). analyze85.py reads .docx with python-docx.
3. **Evidence:** `json/` (live runs, matrix, docx analysis), `docx/` (key downloaded documents), `screens/{cases,devices,locales,geo,a11y}` (JPG ≤1000 px), `html/` (page text, headers, JSON-LD, links), `js/` (prettified ScanConverter, Word builder chunks), `video/` (channel title matches).
4. **Rules:** guest only. No sign-in, payment, email or ad clicks. deviceId, OAuth and Stripe IDs are redacted.
