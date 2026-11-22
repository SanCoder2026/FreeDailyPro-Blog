Sent: 2026-11-21 22:19 ET

# FDP-86 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`; strip the date prefix first): see scripts/README.md.
3. **Evidence:** `json/` (live runs, matrix, xlsx/docx analysis), `files/` (key .docx/.xlsx/.txt outputs), `screens/` (JPG ≤1000 px), `html/`, `js/` (ScanToDocument mount, useShareGate), `testfiles/`.
4. **Rules:** guest only. No sign-in, payment, email or ad clicks. deviceId, OAuth and Stripe IDs are redacted.
5. **Interrupted run:** the session was interrupted once. Nothing completed was redone. The one-load cases (casesdl), Quick Buy and Drive were finished afterwards; the timestamps are in each JSON.
