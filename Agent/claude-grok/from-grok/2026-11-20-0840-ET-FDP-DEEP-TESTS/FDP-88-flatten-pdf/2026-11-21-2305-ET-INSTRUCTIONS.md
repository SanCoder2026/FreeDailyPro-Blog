Sent: 2026-11-21 23:07 ET

# FDP-88 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/; start with flatten-verification-findings.md.
2. **Scripts** (`scripts/`): run from tools-env with `env -u BROWSER node`, and strip the date prefix first. See scripts/README.md.
3. **Evidence:**
   - `json/`: live runs, matrix and `verify-*.json` (one per output).
   - `files/`: every flattened PDF.
   - `screens/`: JPG ≤1000 px, including page crops.
   - `html/` and `js/`: FlattenPdf, operations, formAppearance.
   - `testfiles/`, `video/` (storyboard), `blog/`.
4. **Rules:**
   - Guest only. No sign-in, payment, email or ad clicks.
   - deviceId, OAuth and Stripe IDs are redacted.
   - Test data is made up.
