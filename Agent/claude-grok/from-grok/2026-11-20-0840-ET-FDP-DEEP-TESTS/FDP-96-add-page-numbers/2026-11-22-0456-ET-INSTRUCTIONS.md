Sent: 2026-11-22 04:57 ET

# FDP-96 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Interruption:** this run was interrupted. Testing ran 03:48–04:36 ET; the last write before the stop was `err.json` at 04:36 ET (core N01–N10, nonlatin L01–L07, err E01–E05, matrix, previews, mobile, Quick Buy, video and blog were already done). The run resumed at 04:38 ET and finished only what was missing: core N11–N15 (second load, `core-r2.json`), verification of N11–N14, E03/E04 and the non-Latin outputs, `batch` with a real ZIP download, and a new `xtra` mode (password unlock, extra range errors, 6-file batch, settings memory). No earlier result was redone.
2. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/.
3. **Scripts** (`scripts/`): Node scripts run from tools-env with `env -u BROWSER node`; Python with python3 (pikepdf, PyMuPDF, pypdfium2). Strip the date prefix first. See scripts/README.md.
4. **Evidence:**
   - `json/`: live runs (core, core-r2, nonlatin, err, batch, xtra, prevx, prevx-br, nlprev, atcap, cont, mobile-*, explore, quickbuy), matrix, and `verify-*.json` (one per output).
   - `files/`: live outputs and the batch ZIP. Left out to stay under 20 MB (their verify-*.json files are included): the 73.6 MB heavy output, the 300-page output (E03) and the book output (N12).
   - `testfiles/`: inputs, including the new mixed.pdf, rotated.pdf and crop-offset.pdf (made by scripts/make96.py). heavy.pdf and large-300p.pdf are left out (#91/#92 make them); book.pdf is left out (#93 make93.py makes it).
   - `screens/`: JPG ≤1400 px: cases, previews, non-Latin sheets, N06 p4 badge overlap, cap dialog, locales, matrix.
   - `js/`, `html/`, `blog/`, `video/` (storyboard contact sheet + frames).
   - `replica/` is not included: `rep96.js` (a local re-implementation used while every profile was at 10/10) is in scripts/ for reference only; all findings come from live outputs.
5. **Rules:**
   - Guest only. No sign-in, payment, email or ad clicks.
   - deviceId, OAuth and Stripe IDs are redacted.
   - Test data is made up.
6. **Retest after fixes:** see REPORT "After fixes, rerun". Professional Tools have 10 uses a day shared per IP; use `TRIES=40`.
Sent: 2026-11-22 04:56 ET
