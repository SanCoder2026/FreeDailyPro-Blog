Sent: 2026-11-21 06:06 ET

# Scripts: FDP-45 HTML to PDF (guest QA)

**Intent:** let anyone rerun the live checks behind this report without signing in or paying.
**Why:** the P1s (per-page-load charging, the WebKit hang) and the P2 output slips should be reproducible after a fix ships.
**Outcome:** the same JSON, screenshots and PDFs as in `evidence/`.

**Setup:**
- Playwright 1.65. Run with `env -u BROWSER node <script>`.
- WebKit on Linux: set `GIO_EXTRA_MODULES` to the Playwright giomods dir.
- Python 3 + Pillow (make-files.py); poppler and pikepdf for checking outputs.
- Paths point to `/workspace/deep/45-html-to-pdf/`; change `BASE`/`OUT`/`TF` if needed.

| Script | What it checks |
|---|---|
| make-files.py | H02–H14 test files (H02b = H02 without the external image) |
| hp-scripts.js / hp-expand.js | JS chunk list; page text with accordions open, JSON-LD, links |
| hp-live.js `zero` | At 0: sample convert, preview, Download/Drive/cloud dialogs, Day Pass (stops at email), Quick Buy (stops at Stripe), keyboard |
| hp-live.js `left` (`TRIES=45`) | With uses left: 17 cases in one page load with Download (per-page-load check, file names, options), reload + Download; privacy request scan |
| hp-live.js `subset <engine>` | Firefox/WebKit at 0: sample, invoice, scripts, mixed scripts, >200 pages |
| hp-preview.js | At 0: saves the on-page "Preview first page" image per case |
| hp-webkit.js `[engine]` | WebKit hang on an external image, and Stop behaviour |
| run-matrix.js + config.json | Devices, locales, geo and axe (about 10 min) |

**Safety:**
- The scripts never type an email, card or password, never click "Continue" on a pass, and never click ads.
- Nothing is reset-pending, so there's no RERUN-AFTER-RESET row.
- **Size:** full-page Pixel 7 locale shots are kept for en/hi/ja only (none for the /ar 404 probe). The raw video file is left out (frames, sheets and info.json are kept).
