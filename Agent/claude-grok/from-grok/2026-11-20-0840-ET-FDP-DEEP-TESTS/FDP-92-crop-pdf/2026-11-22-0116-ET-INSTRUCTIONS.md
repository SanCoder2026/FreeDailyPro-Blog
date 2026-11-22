Sent: 2026-11-22 01:18 ET

# FDP-92 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/; start with crop-findings.md.
2. **Scripts** (`scripts/`): Node scripts run from tools-env with `env -u BROWSER node`; Python with python3 (pikepdf, PyMuPDF, pypdf, pypdfium2, numpy, Pillow). Strip the date prefix first. See scripts/README.md.
3. **Evidence:**
   - `json/`: live runs, matrix, `verify-*.json` (one per output; boxes, needles, region match).
   - `files/`: downloaded outputs (the 73.6 MB heavy output is left out for size; its numbers are in err.json).
   - `testfiles/`: inputs (heavy.pdf left out; rebuild with make92.py, which copies it from #91).
   - `screens/`: JPG ≤1000 px (case shots, expected-vs-got renders, matrix, video storyboard).
   - `js/`, `html/`, `blog/`, `video/`.
4. **Rules:**
   - Guest only. No sign-in, payment, email or ad clicks.
   - deviceId, OAuth and Stripe IDs are redacted.
   - Test data is made up.
5. **Competitors:** findings/competitors.md lists the sources read for check 2.
