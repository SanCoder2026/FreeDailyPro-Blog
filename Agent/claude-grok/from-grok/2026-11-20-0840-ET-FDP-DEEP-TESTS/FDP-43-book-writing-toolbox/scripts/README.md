Sent: 2026-11-21 05:21 ET

# Scripts: FDP-43 Book Writing Toolbox (guest QA)

**Intent:** let anyone rerun the live checks behind this report without signing in or paying.
**Why:** the P1 findings (preview watermark, EPUB 500, per-page-load charging, silent block at 0) should be reproducible after a fix ships.
**Outcome:** the same JSON, screenshots and preview files as in `evidence/`.

**Setup:**
- Playwright 1.65. Run with `env -u BROWSER node <script>`.
- WebKit on Linux: set `GIO_EXTRA_MODULES` to the Playwright giomods dir (TLS).
- Python checks need pikepdf, python-docx and Pillow, plus poppler (`pdftotext`, `pdffonts`, `pdftoppm`).
- Paths point to `/workspace/deep/43-book-writing-toolbox/`; change `BASE` if needed.

| Script | What it checks |
|---|---|
| make-files.py | Chapter .docx/.txt/.md, CJK, Arabic, a 400-paragraph book, low/high covers, an invalid project file (C07/C08 noted at the end) |
| bw-scripts.js / bw-expand.js | JS chunk list; page text with accordions open, JSON-LD, links, control list |
| bw-probe.js | Each sidebar section's text and buttons (no Download/trial clicks) |
| bw-live.js `<engine> [ids]` | B01–B14: preview, pre-flight, Download/trial dialogs (stops at sign-in), manuscript, EPUB, covers, import, CJK, RTL, project/ONIX, platforms, long book, clear/My Books. Saves the preview files the browser receives. |
| bw-live2.js `<engine> [ids]` | C01–C08: viewer and EPUB, all export gates, platforms/trims, Arabic RTL, persistence/My Books/invalid project, import splitting, cover resolution + Pre-flight, counter with uses left |
| bw-live3.js `[ids]` | D01 at 0 (manuscript preview + ONIX), D02 per-page-load charging, D03 reload persistence |
| verify.py | Preview PDFs (pages, size, watermark = text or tiling pattern, fonts), docx watermark parts, EPUB 500 count → live/verify.json |
| wm_check.py | Watermark robustness analysis on our own preview file (empties the tiling pattern). Analysis only; the output isn't distributed. |
| bw-blog.js | Rendered blog text |
| run-matrix.js + config.json | Devices, locales, geo and axe (about 10 min) |

**Safety:**
- The scripts never click "Continue to sign-in", never type an email, card or password, and never click ads.
- Nothing is reset-pending, so there's no RERUN-AFTER-RESET row.
