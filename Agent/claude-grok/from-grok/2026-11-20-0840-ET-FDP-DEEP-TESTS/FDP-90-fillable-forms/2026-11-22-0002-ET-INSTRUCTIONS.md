Sent: 2026-11-22 00:04 ET

# FDP-90 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/; start with crosstool-retest-findings.md.
2. **Scripts** (`scripts/`): Node scripts run from tools-env with `env -u BROWSER node`; Python with python3 (pikepdf, PyMuPDF, pypdf, pypdfium2). Strip the date prefix first. See scripts/README.md.
3. **Evidence:**
   - `json/`: live runs, matrix, `verify-*.json` (one per output), `pypdf-values.json`.
   - `files/`: every downloaded output.
   - `testfiles/`: inputs, including real IRS W-9 / W-4 / 8822.
   - `screens/`: JPG ≤1000 px (case shots, MuPDF vs PDFium renders, matrix, video frames).
   - `js/`, `html/`, `blog/`, `video/`.
4. **Rules:**
   - Guest only. No sign-in, payment, email or ad clicks.
   - deviceId, OAuth and Stripe IDs are redacted.
   - Test data is made up (the IRS forms are blank public forms).
