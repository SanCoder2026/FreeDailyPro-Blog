Sent: 2026-11-21 05:21 ET

# Scripts: FDP-44 Excel to PDF (guest QA)

**Intent:** let anyone rerun the live checks behind this report without signing in or paying.
**Why:** the P1 (per-page-load charging, downloads after 10/10) and the P2 conversion gaps should be reproducible after a fix ships.
**Outcome:** the same JSON, screenshots and PDFs as in `evidence/`.

**Setup:**
- Playwright 1.65. Run with `env -u BROWSER node <script>`.
- WebKit on Linux: set `GIO_EXTRA_MODULES` to the Playwright giomods dir.
- Python: openpyxl, Pillow (make-files.py), poppler (`pdfinfo`, `pdffonts`, `pdftotext`, `pdfimages`), LibreOffice for .xls/.ods.
- Paths point to `/workspace/deep/44-excel-to-pdf/`; change `BASE`/`OUT` if needed.

| Script | What it checks |
|---|---|
| make-files.py | X01–X14 test files (X15 = X11 re-saved to .xlsx by LibreOffice: `soffice --headless --convert-to xlsx X11_finance.xls`) |
| xp-scripts.js / xp-expand.js | JS chunk list; page text with accordions open, JSON-LD, links |
| xp-gate.js `2` | At 0: Convert, preview, Download/Drive/cloud dialogs, Day Pass (stops at email), Quick Buy (stops at Stripe), keyboard |
| xp-gate.js `1` | With uses left: Download, re-download, Drive/cloud, two more files in the same load, reload + Download |
| xp-live.js `<engine> [T01,..\|all] [nodl]` | T01–T18 conversions and options; downloads when the context has uses left |
| xp-net.js | Privacy: requests during drop + convert; flags cell text or the file name |
| run-matrix.js + config.json | Devices, locales, geo and axe (about 10 min) |

**Safety:**
- The scripts never type an email, card or password, never click "Continue" on a pass, and never click ads.
- Nothing is reset-pending, so there's no RERUN-AFTER-RESET row.
- **Size:** full-page Pixel 7 locale shots are kept for en/hi/ja only; fold shots are kept for every locale. The raw video file is left out (frames, sheets and info.json are kept).
