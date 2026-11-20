Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-04 Compress PDF)

- **Written:** 2026-11-19 11:25:55 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P0 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce** with REPRODUCE.md or the scripts. After fixing, rerun:
   - `test-cases.md`: CP-01…CP-43. "Currently: FAIL" cases should pass after the fix. "Re-run" cases need an uncapped context (after midnight UTC, 7:00 PM ET).
   - `scripts/make-testpdfs.py [dir]` to regenerate all 17 inputs. A (18 MB), I (10 MB) and J (72 MB) are not in the zip; the script reproduces them.
   - `scripts/inspect-output.py <pdf>...` for bytes, pages, sizes, /Rotate, outline, links, AcroForm, images, encryption, metadata and stamped text. Set `OUT_JSON` to choose the output file.
   - `node run-matrix.js scripts/config.json` for the device, locale, geo and axe matrix (about 12 minutes). See `scripts/README.md` for the WebKit library setup.
   - `node scripts/cp-battery.js [maxTry] [S1_...,S9_...]`: **the download battery** (9 scenarios, about 10 trial uses) in one uncapped fresh context. It skips capped contexts, up to maxTry. `ENGINE=webkit` is optional.
   - `node scripts/cp-explore.js [names]`: the 31 compress-only and validation scenarios (free).
   - `node scripts/cp-capped.js` / `cp-capped2.js`: the gate, cap dialog, batch, Run anyway, Compare and Quick Buy (stops at email and Stripe).
   - `node scripts/cp-ui-dump.js`: Target size, Several files and password controls.
   - `node scripts/cp-kbd.js`: keyboard, focus, axe on the result view, level-row widths, phone overflow, cloud dialog (Not now).
   - `node scripts/cp-target-invalid.js`: invalid targets.
   - `node scripts/cp-probe.js`: starting count.
4. **Rules while retesting:**
   - Guest or fresh contexts only.
   - No sign-in, no email or card entry, no ad clicks, no API/MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: desk, video, live functional, devices/locales.
   - `json/`: matrix, probe, capped, capped2, ui-dump, explore, battery, kbd, target-invalid, input-inspection.
   - `screens/`: devices, locales, geo, a11y, live. Screenshots are downscaled to ≤1400 px wide (PNG 256 colours; full-page shots as JPG q70) to keep the zip under 24 MB. For size, the full-page locale shots are kept only for en, es and ja (fold shots for all), and the a11y full-page shots (identical to the device ones) are left out; all of them are on the box in `/workspace/deep/04-compress-pdf/`.
   - `video/`: info.json, captions, 17 frames and the contact sheet. No .mp4.
   - `js/`: the tool bundles read during the desk review.
   - `html/`: curl captures of the tool, 9 locales, blog, headers and sitemap.
   - `testfiles/`: the small inputs used. The 3–4 MB inputs (C, D, E, F, G, H) are in the separate `FDP-04-compress-pdf-2026-11-19-testfiles.zip`.
   - No downloads/ folder: no output could be downloaded today.
6. **Not covered:**
   - **Downloaded outputs:** structure, text, the mark, ZIP, bytes vs. target, per-download counting. **Needs re-run after midnight UTC.**
   - Open from / Save to Google Drive and Save to my cloud storage (sign-in, https://www.freedailypro.com/tool/compress-pdf).
   - Real iOS and Android hardware (emulation only); a real EU IP.
   - Current GSC figures (not available).
   - The /developers compress API (out of scope).
7. **This package is frozen.** Corrections go into a new `-v2` file.
