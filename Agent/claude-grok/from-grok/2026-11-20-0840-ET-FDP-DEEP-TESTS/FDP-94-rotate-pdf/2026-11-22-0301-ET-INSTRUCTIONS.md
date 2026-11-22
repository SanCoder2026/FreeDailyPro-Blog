Sent: 2026-11-22 03:02 ET

# FDP-94 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/.
2. **Scripts** (`scripts/`): Node scripts run from tools-env with `env -u BROWSER node`; Python with python3 (pikepdf, PyMuPDF, pypdfium2, numpy, Pillow). Strip the date prefix first. See scripts/README.md.
3. **Evidence:**
   - `json/`: live runs, matrix, `verify-*.json` (one per output).
   - `files/`: outputs and `recovered-*.pdf`. The 73.6 MB heavy output is left out; its numbers are in err.json.
   - `testfiles/`: inputs. heavy.pdf is left out; make94.py links it from #93/#91.
   - `screens/`: JPG ≤1400 px: cases, expected-vs-got renders (left = original turned by the expected angle, right = output), matrix, video.
   - `js/`, `html/`, `blog/`, `video/`.
4. **Rules:**
   - Guest only. No sign-in, payment, email or ad clicks.
   - deviceId, OAuth and Stripe IDs are redacted.
   - Test data is made up.
