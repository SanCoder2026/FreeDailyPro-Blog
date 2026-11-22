Sent: 2026-11-21 23:35 ET

# FDP-89 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/; start with reader-verification-findings.md.
2. **Scripts** (`scripts/`): Node scripts run from tools-env with `env -u BROWSER node`; Python with python3 (pikepdf, PyMuPDF, pypdf, pypdfium2). Strip the date prefix first. See scripts/README.md.
3. **Evidence:**
   - `json/`: live runs, charge checks, matrix, pdf.js run, `verify-*.json` (one per created form).
   - `files/`: every created PDF, plus reader-filled copies (pdf.js, PDFium, PyMuPDF, pypdf, Fillable Forms, Flatten PDF).
   - `screens/`: JPG ≤1000 px, including preview-vs-output comparisons.
   - `html/` and `js/`: CreateFillablePdf, useExportGate, pdfText.
   - `testfiles/`, `blog/`.
4. **Rules:**
   - Guest only. No sign-in, payment, email or ad clicks.
   - deviceId, OAuth and Stripe IDs are redacted.
   - Test data is made up.
