Sent: 2026-11-21 06:22 ET

# Scripts: FDP-46 Mail Merge to PDF (guest QA)

**Intent:** let anyone rerun the live checks behind this report without signing in or paying.
**Why:** the P1 (per-page-load charging) and the P2 output slips (hidden rows, Hindi) should be reproducible after a fix ships.
**Outcome:** the same JSON, screenshots, PDFs and ZIPs as in `evidence/`.

**Setup:**
- Playwright 1.65. Run with `env -u BROWSER node <script>`.
- WebKit on Linux: set `GIO_EXTRA_MODULES` to the Playwright giomods dir.
- Python 3 + openpyxl/python-docx (make-files.py); poppler for checking PDFs; list ZIPs with Python zipfile (don't execute contents).
- Paths point to `/workspace/deep/46-mail-merge-pdf/`; change `BASE`/`OUT`/`TF` if needed.

| Script | What it checks |
|---|---|
| make-files.py | M02–M14 test files |
| mm-scripts.js / mm-expand.js | JS chunk list; page text with accordions open, JSON-LD, links |
| mm-live.js `zero` | At 0: example, preview, Download one PDF / ZIP dialogs, Day Pass (stops at email), Quick Buy (stops at Stripe), keyboard |
| mm-live.js `left` (`TRIES=45`) | With uses left: 18 cases in one page load with Download (per-page-load check, names, options), reload + Download; privacy request scan |
| mm-live.js `subset <engine>` | Firefox/WebKit at 0: example, M02, M03, M07, M06 |
| mm-next.js | At 0: preview stepping for M02 (misspelled field, blank cell) and M03 (hidden row), corrupt xlsx message |
| run-matrix.js + config.json | Devices, locales, geo and axe (about 10 min) |

**Safety:**
- The scripts never type an email, card or password, never click "Continue" on a pass, and never click ads.
- mm-live.js now uses an exact "Next" selector (the run in left.json failed L02b/L03 on a two-match selector; mm-next.js covers them).
- Nothing is reset-pending, so there's no RERUN-AFTER-RESET row.
- **Size:** full-page Pixel 7 locale shots are kept for en/hi/ja only. The raw video file is left out.
