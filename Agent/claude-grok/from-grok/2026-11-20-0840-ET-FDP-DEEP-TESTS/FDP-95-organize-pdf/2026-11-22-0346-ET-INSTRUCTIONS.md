Sent: 2026-11-22 03:49 ET

# FDP-95 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/.
2. **Scripts** (`scripts/`): Node scripts run from tools-env with `env -u BROWSER node`; Python with python3 (pikepdf, PyMuPDF). Strip the date prefix first. See scripts/README.md.
3. **Evidence:**
   - `json/`: live runs (core, err, capload, capx, encx, mobile-*, explore, quickbuy, merge1-probe, merge2), matrix, and `verify-*.json` (one per output).
   - `files/`: outputs, plus `recovered-*.pdf` (hidden pages rebuilt from the outputs). Left out to stay under 20 MB (their verify-*.json files are included): the 71 MB heavy output, the 300-page output (E03), the O03 book output and recovered-O02.
   - `testfiles/`: inputs. heavy.pdf and large-300p.pdf are left out (#91/#92 make them).
   - `screens/`: JPG ≤1400 px: cases, recovered secret pages, cap dialog, preview at 0 uses, Merge Arrange, locales, matrix.
   - `js/`, `html/`, `blog/`, `video/` (storyboard contact sheet + frames).
4. **Rules:**
   - Guest only. No sign-in, payment, email or ad clicks.
   - deviceId, OAuth and Stripe IDs are redacted.
   - Test data is made up.
5. **Retest after fixes:** see REPORT "After fixes, rerun". Premium has 2 uses a day, so put many cases in one page load (that is the P1, but it helps testing) and use `TRIES=40`.
