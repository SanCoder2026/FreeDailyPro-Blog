Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-17 Compress Video)

- **Written:** 2026-11-19 15:55 EST (box `date`, ET).

1. **Read REPORT.md first.** It covers intent, evidence, outcomes and the 22 checks.
2. **Work from PRIORITIES.md.** Each item links to a repro in REPRODUCE.md.
3. **Rerun after fixing** (Node + `playwright` + `axe-core`; ffprobe). Scripts write to `/workspace/deep/17-compress-video/live/`; edit `OUT`/`T` for your paths.
   - `node scripts/cv-battery.js [C01,...]`: cases from `cv-cases.json`. It saves each preview blob as `out-<ID>.mp4`.
   - `node scripts/cv-gate-kbd.js`: count, modes, Download/Drive/cloud/Day Pass (stops at the email prompt), keyboard, live regions, axe, phones.
   - `node scripts/cv-keep.js`: the larger-result path: Keep original (free) vs the larger MP4 anyway (gated).
   - `node scripts/cv-browsers.js`: Firefox processing and the WebKit harness control.
   - `node scripts/run-matrix.js scripts/config.json`: devices, locales, geo, axe.
   - **After the 7:00 PM ET reset:** `node scripts/cv-reset.js` (RERUN-AFTER-RESET row 17).
   - `test-cases.md`: CV-01…CV-22.
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: live-functional, desk, video, devices-locales.
   - `json/`: live-cases (measured), battery runs, gate-kbd, keep, browsers, matrix-results.
   - `js/`: the CompressVideo chunk (raw and pretty), plus utils, megabytes and ffmpegEngine (pretty).
   - `html/`: tool, es, blog, category.
   - `screens/`: live results C01–C15, failures, dialogs, phones; devices; locales; geo; a11y. All ≤1400 px wide; tall shots are JPG.
   - `video/`: info.json, contact sheet, crops.
   - `testfiles/`: `INPUTS.txt`, `truncated.mp4` (pre-check case), and outputs C05 (2 MB, 720p) and C07 (0.5 MB missed).
6. **RERUN-AFTER-RESET:** row 17 was added; a copy is in `scripts/`.
