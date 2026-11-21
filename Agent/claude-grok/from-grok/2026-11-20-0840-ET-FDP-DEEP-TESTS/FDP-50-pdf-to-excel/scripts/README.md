Sent: 2026-11-21 08:14 ET

# Scripts (Playwright 1.65, Node 24; run with `env -u BROWSER node`; WebKit needs GIO_EXTRA_MODULES)

- **px-make.js:** builds test PDFs T01–T15 with Chromium `page.pdf` (real text layer). T08 is an image-only copy of T01 page 1 (about 100 dpi).
  - T09 (user password u123) and T16 (truncated) are copied from FDP-49 B04/B12.
- **px-scripts.js / px-expand.js:** JS chunks, expanded page text, JSON-LD, links.
- **px-probe.js:** DOM and options dump after one extraction (no download).
- **px-live.js `<zero|left|subset> [engine]`:**
  - **zero:** at the cap (preview, dialogs, Drive/cloud, Day Pass stops at email, Quick Buy stops at Stripe, keyboard).
  - **left:** L01–L21 in one load, plus a reload.
  - **subset:** S01–S03.
  - TRIES env = fresh contexts to try. Toasts are polled from `[data-sonner-toast]`.
- **run-matrix.js + config.json:** devices, locales, geo, axe.
- **check-xlsx.py:** sheets, dimensions, cell types and formats, formula count, autofilter.
- **ocr-compare.txt:** generated inline. It compares L08 (OCR) with L16 sheet Page 1, cell by cell.
- No sign-in, no payment and no ad clicks in any script. The scripts redact deviceId and OAuth parameters. The only password typed is the test file's own password (u123).
