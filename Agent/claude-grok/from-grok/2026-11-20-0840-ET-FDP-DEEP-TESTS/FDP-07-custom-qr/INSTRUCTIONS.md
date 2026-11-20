Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-07 QR Code Generator with Logo)

- **Written:** 2026-11-19 12:36:49 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P0 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce.** After fixing, rerun:
   - `test-cases.md`: CQ-01…CQ-48. "Currently: FAIL" cases should pass after the fix. "Re-run" cases need a context that shows 2 remaining (after midnight UTC, 7:00 PM ET).
   - `node scripts/cq-explore.js [names]`: 29 preview scenarios. It saves the canvas PNGs; then decode them with `python3 scripts/decode-previews.py <dir>`. Free.
   - `node scripts/cq-long.js`: the long-text crash check. Free.
   - `node scripts/cq-kbd.js`: keyboard, canvas a11y, axe, capped PNG/SVG/PDF dialogs, phone preview position. Free.
   - `node scripts/cq-probe.js`: the starting count and the control inventory.
   - `node scripts/cq-battery.js [contexts]`: **the download battery** (contexts A–F and H; usage recorded before and after every download). It costs trial uses. Then run `python3 scripts/inspect-qr-downloads.py <dir> <out.json>`, plus pdftoppm/pdftotext for PDFs. See `scripts/RERUN-AFTER-RESET.md` row #7.
   - `node run-matrix.js scripts/config.json`: devices, locales, geo and axe (about 9 minutes). See `scripts/README.md`.
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Premium Applications", "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: desk, video, live functional, devices/locales.
   - `json/`: matrix, probe, explore, decoded, long-frame, kbd, battery runs, downloads-inspection.
   - `previews/`: the 28 decoded canvas PNGs.
   - `downloads/`: the 15 files downloaded on 2026-11-19, plus `zip-extracted/`. Nothing in them is executable.
   - `pdf-renders/`: 150 dpi renders of the two PDFs and crops of the PNG corners.
   - `screens/`: devices, locales, geo, a11y and live. Screens are ≤1400 px wide (PNG at 256 colours; full-page shots as JPG q70). Full-page locale shots are kept for en, es and ja only.
   - `video/`: info.json, 21 frames and a contact sheet. No mp4.
   - `js/`: the CustomQr, qrHelpers, UsageAndUpgradeStrip and logoFile bundles.
   - `html/`: the tool, 10 locales plus /ar and /it (404), headers, the sitemap and `locales.txt`.
   - `testfiles/`: logos, a fake .png and a PDF.
6. **Not covered:**
   - B2 (bulk ZIP after a frame and logo) and D2 (gradient PNG 2000). **Needs re-run after midnight UTC.**
   - Whether a paid pass removes the PDF badge (no payment allowed).
   - Real phone cameras: decoding used zxing-cpp and OpenCV, so do a real-phone scan before release.
   - Real iOS and Android hardware.
   - GSC data (not available).
   - The "Lines are name,value" option (CQ-25).
   - Quick Buy (not clicked).
   - There are no sign-in features on this tool.
7. **This package is frozen.** Corrections go into a new `-v2` file.
