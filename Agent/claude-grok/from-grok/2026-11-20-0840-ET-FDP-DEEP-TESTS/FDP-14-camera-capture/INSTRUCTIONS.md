Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-14 Camera Capture)

- **Written:** 2026-11-19 14:45 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P1 → P2). Each item points to a repro in REPRODUCE.md.
3. **Rerun after fixing** (from a folder with `playwright`, `axe-core` and Pillow; see `scripts/README.md`):
   - `node scripts/cc-ui.js`: camera list, capture pixel check, JPG crop, Cancel/Retake, no camera (no trial use).
   - `node scripts/cc-cameras.js`: the 2-camera picker and the Front/rear toggle (no trial use).
   - `node scripts/cc-kbd.js`: keyboard, focus, axe, notices, phone layout and touch crop (no trial use).
   - `node scripts/cc-denied-ff.js`: the permission-denied message in Firefox (no trial use).
   - `node scripts/cc-cloud.js`: the Drive and cloud-storage buttons for a guest (stops at the cap or sign-in dialog).
   - `node scripts/cc-probe.js <tag> [cameraCount]`: full flow plus Download Full, Download Crop and Copy. **This costs trial uses when any are left.** Then `python scripts/cc-inspect.py live/<tag>-camera-*` for the badge check.
   - `node scripts/run-matrix.js scripts/config.json`: devices, locales, geo and axe (about 8 minutes).
   - `test-cases.md`: CC-01…CC-24.
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: live-functional, desk, video, devices-locales.
   - `json/`: desk-probe, ui, ui-cameras, kbd, cloud, matrix-results.
   - `js/`: CameraCapture (raw and prettified), mediaPermissions, CameraNotice, useExportGate, useShareGate.
   - `html/`: tool page (html and text), headers, es locale, blog (html and text).
   - `screens/`: live (dialogs, layouts, cameras, errors, the fake-camera reference), devices, locales (fold for all; full-page for en, es, ja), geo, a11y. Screens are ≤1400 px wide (PNG at 256 colours; full-page shots as JPG q70).
   - `video/`: info.json, contact sheet, 2 crops, 2 frames. No mp4.
6. **RERUN-AFTER-RESET row 14** is pending: costs and the badge with uses left. A copy of the running list is in `scripts/`.
