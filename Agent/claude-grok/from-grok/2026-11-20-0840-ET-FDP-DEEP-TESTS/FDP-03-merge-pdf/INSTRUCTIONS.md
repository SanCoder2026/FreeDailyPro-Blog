Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-03 Merge PDF)

- **Written:** 2026-11-19 10:52:05 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P0 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce** with REPRODUCE.md or the scripts. After fixing, rerun:
   - `test-cases.md`: MP-01…MP-39. Cases marked "Currently: FAIL" should pass after the fix.
   - `scripts/make-testpdfs.py [dir]` to regenerate the 19 inputs (the exact files used are in `evidence/testfiles/`).
   - `scripts/inspect-output.py <pdf>...` to check order markers, count, sizes, /Rotate, outline, AcroForm, encryption, metadata and stamped text.
   - `node run-matrix.js scripts/config.json` for the device, locale, geo and axe matrix (about 7 minutes). See `scripts/README.md` for the WebKit library setup.
   - `node scripts/mp-battery.js [maxTry] [S1_...,S2_...]`: 8 merge scenarios in one uncapped fresh context with downloads and a usage trace (skips capped contexts, up to maxTry).
   - `node scripts/mp-ui-probe.js`: corrupt and renamed files, .txt, password prompt (wrong and right), duplicate, form warning, range errors, single-file state.
   - `node scripts/mp-arrange-probe.js`: Arrange and Choose-pages controls.
   - `node scripts/mp-kbd-cloud.js`: keyboard, focus, axe on the result view, and the cloud-storage dialog (closed with "Not now").
   - `node scripts/mp-probe.js` / `mp-try.js`: starting-count probes in fresh contexts.
4. **Rules while retesting:**
   - Guest or fresh contexts only.
   - No sign-in, no email or card entry, no ad clicks, no API/MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: desk, video, live functional, devices/locales.
   - `json/`: matrix, probes, battery, ui-probe, arrange, kbd-cloud, output inspection.
   - `screens/`: devices, locales, geo, a11y, live. Screenshots are downscaled to ≤1400 px wide (PNG 256 colours; full-page shots as JPG q70) to keep the zip under 24 MB.
   - `downloads/`: the S1–S8 merged PDFs.
   - `video/`: info.json, captions, 17 frames and the contact sheet. No .mp4.
   - `js/`: the tool bundles read during the desk review.
   - `html/`: curl captures of the tool, /es, blog, headers and sitemap.
   - `testfiles/`: the 19 inputs used (about 400 KB, so no separate test-files zip was needed).
6. **Not covered:**
   - Open from / Save to Google Drive and Save to my cloud storage (sign-in, https://www.freedailypro.com/tool/merge-pdf).
   - Camera capture (headless).
   - Whether a pass removes the badge (no payment).
   - Real iOS and Android hardware (emulation only); a real EU IP.
   - Current GSC figures (not available).
   - A second fresh-context counting trace: **needs re-run after midnight UTC**.
7. **This package is frozen.** Corrections go into a new `-v2` file.
