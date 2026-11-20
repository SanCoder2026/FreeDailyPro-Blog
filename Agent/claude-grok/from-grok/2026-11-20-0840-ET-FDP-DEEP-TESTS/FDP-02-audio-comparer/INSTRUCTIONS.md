Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-02 Compare Two Audio Files)

- **Written:** 2026-11-19 10:28:59 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P0 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce** with REPRODUCE.md or the scripts. After fixing, rerun:
   - `test-cases.md`: AC-01…AC-44. Cases marked "Currently: FAIL" should pass after the fix.
   - `scripts/make-testfiles.sh [dir]` to regenerate the audio. The exact files used are in `evidence/testfiles/`, except the 67 MB WAV, which the script makes.
   - `node run-matrix.js scripts/config.json` for the device, locale, geo and axe matrix (about 8 minutes). See `scripts/README.md` for the WebKit library setup.
   - `node scripts/ac-functional.js pairs|usage|all` for the 20 pairs, plus the full control walk and trial-use trace in 2 fresh contexts.
   - `node scripts/ac-verify-pairs.js '<json pairs>'` for one fresh context per pair, with a usage trace.
   - `node scripts/ac-pool-probe.js [N]` to check fresh contexts for the starting trial count.
   - `node scripts/ac-capped-flow.js` for the cap dialog and Quick Buy paths. It stops at the email prompt and the Stripe page.
   - `node scripts/ac-a11y-result.js` for keyboard checks and axe on the result view.
   - The scripts write to `/workspace/deep/02-audio-comparer/live/`. Edit `OUT`/`T` at the top to change that.
4. **Rules while retesting:**
   - Guest or fresh contexts only.
   - No sign-in, no email or card entry, no ad clicks, no API/MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: desk, video, live functional (pairs, controls, counting, paywall), devices/locales.
   - `json/`: matrix, pairs, verify-pairs, usage runs, pool probe, capped flow, a11y result.
   - `screens/`: devices, locales, geo, a11y, live (pairs, verify, paywall, Quick Buy).
   - `downloads/`: the two `audio-difference.wav` files from the usage runs.
   - `video/`: info.json, captions, 15 frames and the contact sheet. No .mp4.
   - `js/`: the tool bundles read during the desk review.
   - `html/`: the curl captures of the tool, /es, blog and category pages, with headers.
   - `testfiles/`: the audio used.
6. **Not covered:**
   - "Open from Google Drive". It needs a Google login (Santosh), at https://www.freedailypro.com/tool/audio-comparer.
   - Audible playback quality (headless).
   - Real iOS and Android hardware (emulation only).
   - A real EU IP.
   - Signed-in or pass-holder behaviour.
   - Current GSC figures (not available).
   - The result view in non-English locales.
7. **Box restore:** the box was restored from a snapshot at about 10:10 EST during testing. Affected runs were repeated. AC-19's screenshot was lost and is pending a re-run.
8. **This package is frozen.** Corrections go into a new `-v2` file.
