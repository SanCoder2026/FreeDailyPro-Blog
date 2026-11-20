Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-10 State Tax Calculator)

- **Written:** 2026-11-19 13:34:02 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P1 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce.** After fixing, rerun:
   - `test-cases.md`: ST-01…ST-40.
   - `node scripts/st-live.js [S-ids]`: 31 calculation cases (reading only, free).
   - `node scripts/st-compare.js <income> <single|mfj|mfs|hoh>`: the full 51-state table. Free.
   - `node scripts/st-gate.js`: the six export actions at 0 and with uses left. Costs 1 use in a context with uses.
   - `node scripts/st-kbd.js` (compare, "85k", tab order, phones), `node scripts/st-axe.js`, `node scripts/st-blog95.js` (the blog table), `node scripts/st-probe.js`.
   - `node scripts/run-matrix.js scripts/config.json`: devices, locales, geo and axe (about 7 minutes).
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses". Copy and export charges are intended (owner policy); only the wording is in scope.
5. **evidence/** contains:
   - `findings/`: desk, video, live functional, devices/locales.
   - `json/`: cases, compare-75000-single, blog95, gate, kbd, axe, probe, matrix-results.
   - `downloads/`: the CSV and .txt from the context with uses left.
   - `js/`: StateTaxCalculator (raw and prettified), stateTaxData (raw and prettified), CalcReport, report, useLogToolUsage.
   - `html/`: the tool, the blog, and the es and ja locale pages.
   - `screens/`: live, devices, locales, geo and a11y. Screens are ≤1400 px wide (PNG at 256 colours; full-page shots as JPG q70). Full-page locale shots are kept for en, es and ja only.
   - `video/`: info.json, frames and a contact sheet. No mp4.
6. **No RERUN-AFTER-RESET row** for this tool: nothing is pending. A copy of the running list is in `scripts/`.
