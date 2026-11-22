Sent: 2026-11-21 22:51 ET

# FDP-87 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/; start with true-redaction-findings.md.
2. **Scripts** (`scripts/`): run from tools-env with `env -u BROWSER node`, and strip the date prefix first. See scripts/README.md.
3. **Evidence:**
   - `json/`: live runs, matrix and `verify-*.json` (one per output PDF).
   - `files/`: every redacted PDF and summary .txt produced.
   - `screens/`: JPG, ≤1000 px wide.
   - `html/`, `js/`: RedactPdf, redactApply, redactSearch.
   - `testfiles/`: secrets/scan/enc/corrupt/curve PDFs.
   - `video/`: storyboard frames + info.
   - `blog/`: guide text.
4. **Rules:**
   - Guest only. No sign-in, payment, email or ad clicks.
   - deviceId, OAuth and Stripe IDs are redacted.
   - The test PDFs contain only made-up data (Jonathan Reed, 123-45-6789, test card 4111…).
