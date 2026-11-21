Sent: 2026-11-21 13:02 ET

# FDP-61 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Inputs:** `evidence/testfiles/` (synthetic photos from `scripts/make61.py`, run with a Python that has PIL + numpy). `p11-big-6000.jpg` (2.6 MB) is left out to keep the zip small; rebuild it with make61.py. `js/ToolPage-usage-excerpt.txt` holds the usage functions from ToolPage-DwLoDncN.js (1.8 MB, left out).
3. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`; WebKit needs `GIO_EXTRA_MODULES=…/giomods`):
   - `px61-live.js <zero|quickbuy|left|leftB|idcard|perload|msgs> [engine]`. Env: TRIES (fresh contexts to try for Premium uses left), ANY=1, SUF.
   - `px61-orient.js`: EXIF orientation and not-an-image on 3 engines.
   - `px61-misc.js`: camera input, Drive (stops at Google sign-in), Share, handles, Edit as Excel.
   - `px61-mobile.js`: iPhone 13 / Pixel 7 flow at the cap.
   - `px61-scripts.js`, `px61-expand.js`, `run-matrix.js config.json`.
4. **Evidence:**
   - `json/`: all runs.
   - `outputs/`: downloaded PDFs/PNGs.
   - `screens/cases|devices|locales|geo|a11y|live`.
   - `video/`: sheet, frames, info.
   - `html/`, `js/`.
5. **Rules:** guest only. No sign-in, no payment (stop at the email prompt and Stripe), no ad clicks. Times are EST. Premium trial uses reset at midnight UTC (7:00 PM ET). Fresh contexts are usually already at 2/2; use TRIES=30–40 to find one with uses left.
