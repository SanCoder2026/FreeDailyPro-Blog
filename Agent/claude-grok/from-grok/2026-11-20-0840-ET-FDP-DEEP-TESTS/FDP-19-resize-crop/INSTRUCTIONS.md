Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-19 Resize & Crop)

- **Written:** 2026-11-19 16:38 EST (box `date`, ET).

1. **Read REPORT.md first.** It covers intent, evidence, outcomes and the 22 checks.
2. **Work from PRIORITIES.md.** Each item links to a repro in REPRODUCE.md.
3. **Rerun after fixing** (Node + `playwright` + `axe-core`; Python + Pillow). Scripts write to `/workspace/deep/19-resize-crop/live/`; edit `OUT`/`T` for your paths.
   - `node scripts/rc-battery.js [R01,...]`: one fresh context per case. It records the result blob (`out-<ID>.*`).
   - `python scripts/rc-inspect.py <live dir>`: format, size, EXIF/GPS, DPI → `inspect.json`.
   - `node scripts/rc-gate-kbd.js`: count, keyboard, 1:1 preset, keyboard crop, enlarge warning, axe, Download/Day Pass (stops at the email prompt), Drive, cloud, phones.
   - `node scripts/rc-browsers.js`: Firefox and WebKit.
   - `node scripts/rc-probe.js`, `node scripts/rc-copy.js`: page text, controls, expanded copy, JSON-LD.
   - `node scripts/run-matrix.js scripts/config.json`: devices, locales, geo, axe.
   - **After the 7:00 PM ET reset:** `node scripts/rc-reset.js` (RERUN-AFTER-RESET row 19).
   - `test-cases.md`: RC-01…RC-24.
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **Sign-in-blocked (untested), all on https://www.freedailypro.com/tool/resize-crop:**
   - "Save to my cloud storage" opens a sign-in dialog.
   - "Open from Google Drive" (in the drop zone) was not clicked.
   - "Save to Google Drive" was capped at 0, so its Google sign-in was not reached.
6. **evidence/** contains:
   - `findings/`: live-functional, desk, video, devices-locales.
   - `json/`: batteries, inspect, gate-kbd, browsers, reset, probe, matrix-results, JSON-LD.
   - `js/`: the ResizeCrop chunk (raw and pretty), plus operations, utils and convertCore (pretty).
   - `html/`: tool, expanded text, es, ar (404), blog, category.
   - `screens/`: live results/dialogs/phones/browsers, devices, locales, geo, a11y. All ≤1400 px wide; tall shots are JPG.
   - `video/`: info.json, contact sheet, quad.
   - `testfiles/`:
     - `make.py` (all inputs) and the EXIF+GPS input `photo-exif-gps-input.jpg`
     - outputs R01 (GPS stripped), R06 Inside 1080×810, R07 Outside 1440×1080, R08 transparent Contain, R09 Never-enlarge 50×50, R13 BMP→PNG, R14 GIF→PNG, K02 crop+scale
7. **RERUN-AFTER-RESET:** row 19 was added; a copy is in `scripts/`.
