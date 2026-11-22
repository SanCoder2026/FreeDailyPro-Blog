Sent: 2026-11-22 05:35 ET

# FDP-97 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/ (output-verification, strip-demo, content-video-seo).
2. **Scripts** (`scripts/`): Node scripts run from tools-env with `env -u BROWSER node`; Python with python3 (pikepdf, PyMuPDF, pypdfium2, Pillow). Strip the date prefix first. See scripts/README.md.
3. **Evidence:**
   - `json/`: live runs (explore, core, nonlatin, img, err, inputs, xl, batch, xtra, atcap, cont, mobile-iphone, mobile-iphone-wk, quickbuy, zero), matrix, and `verify-*.json` (one per output, plus `verify-strip-check.json`).
   - `files/`: live outputs and the batch ZIP. Left out to stay under 20 MB (their verify JSON is included where verified): the 73.6 MB heavy output (E04), the 300-page outputs (E03 3.99 MB, E07 107 MB), the book output (W17, 2.7 MB) and the tiled CJK doc (L08, 2.1 MB).
   - `stripped/`: the 5 stripped PDFs from strip97.py except the book one.
   - `testfiles/`: inputs incl. new scan.pdf and logos (make97.py). heavy.pdf, large-300p.pdf, book.pdf left out (#91–#93 makers).
   - `screens/`: JPG ≤1400 px: cases, non-Latin sheet, badge-clash sheet, verify renders, matrix fold shots.
   - `js/`, `html/`, `blog/`, `video/` (storyboard contact sheet + frames).
4. **Rules:**
   - Guest only. No sign-in, payment, email or ad clicks.
   - deviceId, OAuth and Stripe IDs are redacted.
   - Test data is made up.
5. **Retest after fixes:** see REPORT "After fixes, rerun". Professional Tools have 10 uses a day shared per IP; use `TRIES=60`.
Sent: 2026-11-22 05:34 ET
