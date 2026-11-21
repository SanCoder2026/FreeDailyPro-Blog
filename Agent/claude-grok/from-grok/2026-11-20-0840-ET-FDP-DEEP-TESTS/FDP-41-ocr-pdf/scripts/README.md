Sent: 2026-11-21 03:55 ET

# Scripts: FDP-41 OCR PDF (guest QA)

**Intent:** let anyone re-run the live checks behind this report without signing in or paying.
**Why:** the gate finding (P1) and the output defects should be reproducible after a fix ships.
**Outcome:** the same JSON, screenshots and downloaded PDFs as in `evidence/`.

Setup:
- Playwright 1.65. Run with `env -u BROWSER node <script>`. For WebKit on Linux, set `GIO_EXTRA_MODULES` to the Playwright giomods dir (TLS).
- Python checks need pypdf, pikepdf, reportlab and Pillow, plus poppler's `pdftoppm`/`pdftotext`.
- Paths in the scripts point to `/workspace/deep/41-ocr-pdf/`. Change `BASE` if needed.

| Script | What it checks |
|---|---|
| make-scans.py | Builds the S01–S13 image-only scans and `truth.json` (expected words) |
| ocr-scripts.js / ocr-expand.js | JS chunk list; expanded page text, JSON-LD and links |
| ocr-left.js | Reads the trial strip in 8 fresh contexts (no actions) |
| ocr-probe.js | Controls, OCR timing, notice, preview size, every request host, counter at each step |
| ocr-gate.js `12` | Part 1 (needs a context with uses left): load/reload/drop/OCR/preview/Download ×2/Drive/cloud/second file/Continue. Part 2 (at 0): keyboard, OCR, preview, Download/Drive/cloud/Continue → cap, Day Pass email prompt, Quick Buy → Stripe (stop) |
| ocr-live.js `<chromium\|firefox\|webkit> <V\|W\|K>` | V/W: many files in ONE page load with Download (per-page-load evidence + outputs). W sets language and orientation explicitly. K: edge cases at any count, no Download |
| ocr-handoff.js | At 0: Continue with Compress PDF carries the result; Compress Download stays gated |
| ocr-privacy.js | Requests after the file drop (hosts, POST sizes, file name or text leaks) |
| ocr-webkit.js | OCR in Playwright WebKit (desktop + iPhone emulation): crash or not |
| run-matrix.js + config.json | Devices, locales, geo and axe (`node run-matrix.js config.json`, about 10 min) |
| verify.py `<downloads dir> [prefix]` | Page count, /Rotate, word recall vs truth.json, visual diff vs input, badge |

Safety:
- The scripts stop at the Day Pass email field, at Stripe and at the Google sign-in popup. They never type an email, card or password (except the test PDF password `ocr123`).
- They never click ads.

No RERUN-AFTER-RESET row: nothing in this report waits for a usage reset. Open item: run S01 on a real iPhone/Mac Safari.
