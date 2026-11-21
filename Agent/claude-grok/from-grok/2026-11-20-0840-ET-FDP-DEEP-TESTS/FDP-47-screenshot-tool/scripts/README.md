Sent: 2026-11-21 06:49 ET

# Scripts: FDP-47 Screenshot Capture & Editor (guest QA)

**Intent:** let anyone rerun the live checks behind this report without signing in or paying.
**Why:** the P1s (per-page-load charging, Android) and the editor/stitch results should be reproducible after a fix ships.
**Outcome:** the same JSON, screenshots and images as in `evidence/`.

**Setup:**
- Playwright 1.65. Run with `env -u BROWSER node <script>`. WebKit on Linux: set `GIO_EXTRA_MODULES` to the Playwright giomods dir.
- Paths point to `/workspace/deep/47-screenshot-tool/`; change `BASE`/`OUT` if needed.

**About the stub:** headless browsers on Linux can't open a real screen-share picker (see st-probe*.js). `st-live.js` and `st-check.js` replace `navigator.mediaDevices.getDisplayMedia` in the test browser only (via `addInitScript`) with a `canvas.captureStream()` that paints a known test screen (`single`), a scrolling 3,120 px page (`scroll`) or a blank page (`blank`). Nothing on the site is changed. Do one real capture by hand.

| Script | What it checks |
|---|---|
| st-scripts.js / st-expand.js | JS chunk list; page text with accordions open, JSON-LD, links |
| st-probe.js / st-probe2.js | Whether headless/Xvfb Chromium can capture for real (it can't here) |
| st-live.js `main` | One page load: capture, Download, crop Download, Copy, editor tools + PNG/JPG, rotate, whole page, blank page, countdown + stop, new capture; then reload until the cap dialog (Download, Copy, editor); Day Pass (stops at email) / Quick Buy (stops at Stripe) |
| st-live.js `mobile` | Pixel 7 / iPhone profiles with `getDisplayMedia` removed (Android behaviour) |
| st-live.js `real <engine>` | Real picker path in headless (error toast) |
| st-live.js `subset <engine>` | Firefox/WebKit: capture, editor, pixelate, download, whole page |
| st-check.js (`KINDS`, `TRIES`) | One action per fresh context: what one Download/Copy/editor Download charges; selection honoured; saves the clipboard image |
| st-peek.js | Usage object of N fresh contexts (no actions) |
| run-matrix.js + config.json | Devices, locales, geo and axe (about 10 min) |

**Safety:**
- The scripts never type an email, card or password, never click "Continue" on a pass, and never click ads.
- Nothing is reset-pending, so there's no RERUN-AFTER-RESET row.
- **Size:** full-page Pixel 7 locale shots are kept for en/hi/ja only. The raw video file is left out.
