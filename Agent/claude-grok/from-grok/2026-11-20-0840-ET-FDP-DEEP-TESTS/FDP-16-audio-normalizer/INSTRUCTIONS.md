Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-16 Audio Volume Normalizer)

- **Written:** 2026-11-19 15:26 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P1 → P2). Each item links to a repro in REPRODUCE.md.
3. **Rerun after fixing** (Node with `playwright` and `axe-core`; ffmpeg for measuring). Scripts write to `/workspace/deep/16-audio-normalizer/live/`; edit `OUT`/`T` at the top for your paths.
   - `node scripts/an-battery.js [N01,N09,...]`: file × target cases from `an-cases.json`. It saves each preview blob as `out-<ID>.bin`; measure them as described in `scripts/README.md`.
   - `node scripts/an-gate-kbd.js`: starting count, Drive, cloud, Share, Download → Day Pass (stops at the email prompt), Continue with, keyboard, live regions, axe, phones.
   - `node scripts/an-browsers.js`: Firefox/WebKit processing and the keyboard path to the drop zone.
   - `node scripts/an-webkit-retry.js`, `an-webkit-control.js`: the WebKit harness check.
   - `node scripts/an-se-overflow.js`: the 320 px overflow culprit.
   - `node scripts/run-matrix.js scripts/config.json`: devices, locales, geo, axe (about 8 minutes).
   - **After the daily reset (7:00 PM ET):** `node scripts/an-reset.js` (RERUN-AFTER-RESET row 16).
   - `test-cases.md`: AN-01…AN-24.
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: live-functional, desk, video, devices-locales.
   - `json/`: live-cases (merged and measured), battery runs, probe, gate-kbd, browsers-kbd, webkit-retry/control, se-overflow, matrix-results.
   - `js/`: the AudioNormalizer chunk (raw and pretty), plus prettified operations and ffmpegEngine.
   - `html/`: tool (html, visible text, headers), es, blog (html, text), category.
   - `screens/`: live (dialogs, result, phones, failures), devices, locales, geo, a11y. All ≤1400 px wide; tall shots are JPG.
   - `video/`: info.json, captions, contact sheet, 2 crops (no mp4).
   - `testfiles/`: `INPUTS.txt`; outputs N01/N09/N22 as FLAC (same samples as the tool's WAV, for true-peak checks); the failing `quiet.opus` and a working `voicenote-opus16k.ogg`.
6. **RERUN-AFTER-RESET:** row 16 was added (download cost with uses left). A copy of the list is in `scripts/`.
