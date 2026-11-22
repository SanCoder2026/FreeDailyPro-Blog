Sent: 2026-11-21 20:39 ET

# FDP-84 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave out that prefix (e.g. "REPORT.md" means `…-ET-REPORT.md`).
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`; strip the date prefix first): see scripts/README.md. Test pictures are in evidence/testfiles/ and can be regenerated with make-testfiles.py (seed 84). analyze.py reads .xlsx with openpyxl.
3. **Evidence:** `json/` (live runs, matrix, xlsx analysis), `xlsx/` (key downloaded workbooks), `screens/{cases,devices,locales,geo,a11y}` (JPG, ≤1000 px), `html/` (page text, headers, JSON-LD, links), `js/` (prettified ScanConverter, tablesToExcel, export gate; ToolPage excerpt).
4. **Rules:** guest only. No sign-in, payment, email or ad clicks. deviceId, OAuth and Stripe IDs are redacted.
