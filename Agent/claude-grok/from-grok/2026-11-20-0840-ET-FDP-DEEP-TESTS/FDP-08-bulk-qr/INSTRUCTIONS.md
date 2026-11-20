Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-08 Bulk QR Generator)

- **Written:** 2026-11-19 13:02:21 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P0 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce.** After fixing, rerun:
   - `test-cases.md`: BQ-01…BQ-41. "Currently: FAIL" cases should pass after the fix. "Re-run" cases need a context with uses left (after midnight UTC, 7:00 PM ET).
   - `node scripts/bq-explore.js [names]`: 14 list scenarios. It saves the preview PNGs. Free.
   - `node scripts/bq-kbd.js`: cap dialog on Generate and Save at 0, sample passes, Open-project errors, keyboard, axe, phone order. Free.
   - `node scripts/bq-sample-key.js`: sample pass key randomness. Free.
   - `node scripts/bq-probe.js`: starting count, controls and loaded bundles.
   - `node scripts/bq-battery.js [contexts]`: **the download battery** (A count trace, B names/unicode/CSV at 2000 px, C 500 codes, D passes + save, E too-long line). Contexts that load at 0 skip themselves. `DRY=1` checks the selectors for free. Then run `python3 scripts/bq-inspect.py <zip> [project.json] <out.json>`. See `scripts/RERUN-AFTER-RESET.md` row #8.
   - `node run-matrix.js scripts/config.json`: devices, locales, geo and axe (about 10 minutes). See `scripts/README.md`.
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: desk, video, live functional, devices/locales.
   - `json/`: matrix, probe, explore, decoded, kbd, sample-key, battery (dry and real), downloads-inspection.
   - `previews/`: the decoded preview PNGs (S… list scenarios, P_pass… sample passes).
   - `downloads/`: D1 `qr-codes.zip` with its extracted files, and the saved sample project with **the pass key redacted** (signatures were verified on the box before redaction).
   - `screens/`: devices, locales, geo, a11y and live. Screens are ≤1400 px wide (PNG at 256 colours; full-page shots as JPG q70). Full-page locale shots are kept for en, es and ja only.
   - `video/`: info.json, 21 frames and a contact sheet. No mp4.
   - `js/`: BulkQr, qrHelpers, passCode, csv, ProjectBar, useProject, UsageAndUpgradeStrip and cloudStorage.
   - `html/`: the tool, 10 locales plus /ar and /it (404), headers, the blog post and `locales.txt`.
   - `testfiles/`: broken project files for Open project.
6. **Not covered:**
   - **Battery A, B, C and E. Needs re-run after midnight UTC.**
   - Event Suite features in the project bar (saved projects, publish, invites). These need sign-in and an Event Suite plan; untested.
   - The QR Scanner's offline pass check (tested in its own tool later).
   - Real phone cameras: decoding used zxing-cpp.
   - Real iOS and Android hardware.
   - GSC data (not available).
   - Quick Buy (not clicked).
7. **This package is frozen.** Corrections go into a new `-v2` file.
