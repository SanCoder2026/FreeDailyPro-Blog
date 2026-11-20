Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-06 QR Code Generator)

- **Written:** 2026-11-19 12:05:23 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P0 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce.** After fixing, rerun:
   - `test-cases.md`: QR-01…QR-42. "Currently: FAIL" cases should pass after the fix. "Re-run" cases (QR-27…QR-35) need an uncapped context after midnight UTC (7:00 PM ET).
   - `node scripts/qr-explore.js [names]`: 30 preview scenarios. It saves the canvas PNGs, then `python3 scripts/decode-previews.py <previews dir>` decodes them. Free.
   - `node scripts/qr-logo-aspect.js`: the wide-logo distortion check. Free.
   - `node scripts/qr-kbd.js`: tabs and selects by keyboard, canvas a11y, axe, capped PNG/SVG dialogs, upsell link, phone preview position. Free.
   - `node scripts/qr-probe.js` / `qr-tabs-dump.js`: starting count and the field inventory per tab.
   - `node scripts/qr-battery.js [maxTry] [B1_...]`: **the download battery** (8 scenarios, about 12 downloads, usage recorded per download). It skips capped contexts. **Not run today**; it's listed in `/workspace/deep/RERUN-AFTER-RESET.md` (a copy is in `scripts/`).
   - `python3 scripts/inspect-qr-downloads.py <dir>`: size, quiet zone, colours, corner pixels (mark), SVG text/image and decode (zxing-cpp, OpenCV, cairosvg).
   - `node run-matrix.js scripts/config.json`: devices, locales, geo and axe (about 7 minutes). See `scripts/README.md`.
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: desk, video, live functional, devices/locales.
   - `json/`: matrix, probe, explore, decoded, kbd.
   - `previews/`: the 31 canvas PNGs that were decoded.
   - `screens/`: devices, locales, geo, a11y and live. Screens are ≤1400 px wide (PNG at 256 colours; full-page shots as JPG q70). Full-page locale shots are kept only for en, es and ja.
   - `video/`: info.json, captions, 16 frames and the contact sheet. No mp4.
   - `js/`: the QrGenerator, qrHelpers, UsageAndUpgradeStrip and index bundles.
   - `html/`: the tool, 9 locales, /ar, related blogs, the QR topic page, headers and the sitemap.
   - `testfiles/`: logos. The 2.2 MB busy photo logo is included.
   - There is no downloads/ folder, because nothing could be downloaded today.
6. **Not covered:**
   - **Downloads (size, mark, decode, per-format cost). Needs re-run after midnight UTC.**
   - Quick Buy (same strip as FDP-02 to FDP-05; not re-clicked).
   - Real phone cameras: decoding was done with zxing-cpp and OpenCV, so do a real-phone scan before release.
   - Real iOS and Android hardware.
   - GSC data (not available).
   - The QR API (out of scope).
   - There are no sign-in features on this tool.
7. **This package is frozen.** Corrections go into a new `-v2` file.
