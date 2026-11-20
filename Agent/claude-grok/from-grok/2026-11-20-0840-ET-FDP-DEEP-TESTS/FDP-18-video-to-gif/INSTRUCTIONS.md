Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-18 Video to GIF)

- **Written:** 2026-11-19 16:18 EST (box `date`, ET).

1. **Read REPORT.md first.** It covers intent, evidence, outcomes and the 22 checks.
2. **Work from PRIORITIES.md.** Each item links to a repro in REPRODUCE.md.
3. **Rerun after fixing** (Node + `playwright` + `axe-core`; ffprobe). Scripts write to `/workspace/deep/18-video-to-gif/live/`; edit `OUT`/`T` for your paths.
   - `node scripts/vg-battery.js [G01,...]`: cases from `vg-cases.json`. It saves each preview as `out-<ID>.gif`.
   - `node scripts/vg-gate-kbd.js`: count, keyboard, Stop, live regions, axe, Download/Drive/cloud, phones.
   - `node scripts/vg-cap.js`: at 0 remaining, cap dialog → Day Pass → email prompt (stops there). It skips itself if uses are left.
   - `node scripts/vg-browsers.js`: Firefox processing and format pre-check; WebKit harness control.
   - `node scripts/vg-probe.js`, `node scripts/vg-copy.js`: page text and expanded copy + JSON-LD.
   - `node scripts/run-matrix.js scripts/config.json`: devices, locales, geo, axe.
   - **After the 7:00 PM ET reset:** `node scripts/vg-reset.js` (RERUN-AFTER-RESET row 18).
   - `test-cases.md`: VG-01…VG-24.
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **Sign-in-blocked (untested), all on https://www.freedailypro.com/tool/video-to-gif:**
   - "Save to Google Drive" opens Google sign-in.
   - "Save to my cloud storage" opens a sign-in dialog.
   - "Open from Google Drive" (in the drop zone) was not clicked.
6. **evidence/** contains:
   - `findings/`: live-functional, desk, video, devices-locales.
   - `json/`: batteries (`battery-run1-settings-carried-over.json` is kept only for G02/G07), gate-kbd, cap, browsers, reset, probe, matrix-results, JSON-LD.
   - `js/`: the VideoToGif chunk (raw and pretty), plus operations and ffmpegEngine (pretty).
   - `html/`: tool, expanded text, es, ar (404), both pair pages, blog, category.
   - `screens/`: live results/dialogs/phones, devices, locales, geo, a11y. All ≤1400 px wide; tall shots are JPG.
   - `video/`: info.json, contact sheet, crops.
   - `testfiles/`: `INPUTS.txt`, `clip.avi` (refused), `truncated.mp4`, and outputs G02 (smallest), G08 (over cap), G16 (no upscale), G23 (clean source).
7. **RERUN-AFTER-RESET:** row 18 was added; a copy is in `scripts/`.
