Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-05 Split PDF)

- **Written:** 2026-11-19 11:46:52 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P0 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce** with REPRODUCE.md or the scripts. After fixing, rerun:
   - `test-cases.md`: SP-01…SP-47. "Currently: FAIL" cases should pass after the fix. "Re-run" cases (SP-31…SP-41) need an uncapped context (after midnight UTC, 7:00 PM ET).
   - `scripts/make-testpdfs.py [dir]` regenerates all 14 inputs (they're small and also included in `evidence/testfiles/`).
   - `scripts/inspect-output.py <pdf>...` reports pages, order markers, sizes, /Rotate, outline, links, AcroForm, images, encryption, metadata, stamped text and non-Latin text. Set `OUT_JSON` to choose the output file.
   - `node run-matrix.js scripts/config.json` runs the device, locale, geo and axe matrix (about 8 minutes). See `scripts/README.md` for the WebKit setup.
   - `node scripts/sp-battery.js [maxTry] [S1_...,S9_...]` is **the download battery**: 9 scenarios, about 12 downloads, recording usage before and after each. It runs in one uncapped fresh context, skips capped contexts up to maxTry, and unzips ZIPs for inspection. `ENGINE=webkit` is optional. **Not run today**; it's listed in `/workspace/deep/RERUN-AFTER-RESET.md`.
   - `node scripts/sp-explore.js [names]` runs the 12 split scenarios plus the bad files and invalid ranges (free).
   - `node scripts/sp-ranges-rows.js` checks what lenient range inputs actually produce (free).
   - `node scripts/sp-kbd.js` covers thumbnails, the "1-" range, keyboard, focus, live regions, axe on the result view, row widths, capped Download/ZIP dialogs, the cloud dialog (Not now) and Pixel 7 overflow.
   - `node scripts/sp-probe.js` reads the starting count.
4. **Rules while retesting:**
   - Guest or fresh contexts only.
   - No sign-in, no email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: desk, video, live functional, devices/locales.
   - `json/`: matrix, probe, explore, kbd, ranges-rows.
   - `screens/`: devices, locales, geo, a11y and live (explore x-*.png, kbd, capped ZIP click, phone result). Screenshots are downscaled to ≤1400 px wide (PNG at 256 colours; full-page shots as JPG q70).
   - `video/`: info.json, captions, 16 frames, the contact sheet and the yt-dlp logs. No .mp4.
   - `js/`: the SplitPdf, PdfPageThumbnails, UsageAndUpgradeStrip and operations bundles.
   - `html/`: curl captures of the tool, 9 locales, /ar, the blog, headers and the sitemap.
   - `testfiles/`: all 14 inputs.
   - There is no downloads/ folder, because no output could be downloaded today.
6. **Not covered:**
   - **Downloaded outputs and per-file vs per-ZIP counting. Needs re-run after midnight UTC.**
   - Open from / Save to Google Drive and Save to my cloud storage (sign-in, https://www.freedailypro.com/tool/split-pdf).
   - Quick Buy, which is the same strip as FDP-02 to FDP-04 and was not re-clicked.
   - Real iOS and Android hardware (emulation only), and a real EU IP.
   - Current GSC figures (GSC data is not available).
   - The RapidAPI / /developers split endpoint (out of scope).
7. **This package is frozen.** Corrections go into a new `-v2` file.
