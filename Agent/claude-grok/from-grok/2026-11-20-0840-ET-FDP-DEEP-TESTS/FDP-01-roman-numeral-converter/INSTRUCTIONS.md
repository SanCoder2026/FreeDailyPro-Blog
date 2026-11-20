Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-01 Roman Numeral Converter)

- **Written:** 2026-11-19 09:46:50 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, the evidence and the outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P0 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce** with REPRODUCE.md or the scripts. After fixing, rerun:
   - `test-cases.md`: RN-01…RN-37. Cases marked "currently expected to FAIL" should pass after the fix.
   - `cd /workspace/deep/tools-env && node run-matrix.js <path>/scripts/config.json` for the device, locale, geo and axe matrix (about 8 minutes). See `scripts/README.md` for the WebKit library setup.
   - `node scripts/edge-usage.js [url] [outDir]` for edge inputs, two-context usage counting, CSVs, FAQ, links and share.
   - `node scripts/edge-date-vinculum-probe.js` and `node scripts/edge-copy-table-probe.js` for targeted checks.
4. **Rules while retesting:** guest or fresh contexts only. No sign-in, no card entry (stop at the Stripe page), no ad clicks, no API/MCP calls. Counters are display-only evidence. Each fresh context is a new guest device. Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: the desk, live desktop, video, devices/locales and edge/usage reports
   - `json/`: raw matrix and edge results
   - `csv/`: the downloaded files
   - `screens/`: curated device, locale, geo, a11y, edge and desktop-Chrome screenshots
   - `js/`: the site bundles read during the desk review (index bundle excluded)
6. **Not covered:**
   - Real iOS and Android hardware (emulation only)
   - A real EU IP
   - Signed-in behaviour
   - Print/PDF layout
   - Current GSC figures (not available)
7. **This package is frozen.** Corrections go into a new `-v2` file.
