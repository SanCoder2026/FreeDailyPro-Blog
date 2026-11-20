Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-09 Income Tax Calculator)

- **Written:** 2026-11-19 13:23:18 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P0 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce.** After fixing, rerun:
   - `test-cases.md`: IT-01…IT-44. "FAIL" cases should pass after the fix. "Re-run" cases need a context with uses left (after midnight UTC, 7:00 PM ET).
   - `node scripts/it-live.js [T-ids]`: 40 calculation cases. It reads every result box and note. It never copies, saves or prints, so it is free.
   - `python3 scripts/ref_federal.py <income> <single|mfj|mfs|hoh> <pretax> [se]`: the independent 2026 federal + FICA/SE + QBI reference (JSON).
   - **Trial-cost scripts:**
     - `node scripts/it-gate2.js`: Copy ×3 with uses left, and Copy ×3 plus Save at 0.
     - `node scripts/it-gate3.js`: Print and Ctrl+C at 0.
     - `node scripts/it-gate4.js`: **re-run**: Save-first and Print-first with uses left.
     - `it-gate.js` is the first exploratory run. It wrote a clipboard sentinel, which itself triggers the gate, so read its copy result with that in mind.
   - `node scripts/it-flat.js`: Custom Flat Rate cases. `node scripts/it-probe.js`: starting count and controls. `node scripts/it-dbg.js`: strip and buttons for one fresh context.
   - `node scripts/run-matrix.js scripts/config.json`: devices, locales, geo and axe (about 7 minutes). See `scripts/README.md`.
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: desk, video, live functional, devices/locales.
   - `json/`: matrix-results, probe, cases-T01-T34, cases-T35-T40, gate, gate2, gate3, gate4, flat.
   - `downloads/`: the saved `income-tax-calculator-result.txt` (from a context with uses left).
   - `js/`: the bundles read for the code findings (IncomeTaxCalculator, stateTaxData, useLogToolUsage, calcChecks, k401, numberInput, RatesNote).
   - `html/`: the tool, /terms, /faq, the blog posts, and the es and ja locale pages.
   - `screens/`: live (the cap dialogs at 0, phones, flat rate), devices, locales, geo and a11y. Screens are ≤1400 px wide (PNG at 256 colours; full-page shots as JPG q70). Full-page locale shots are kept for en, es and ja only.
   - `video/`: info.json, 12 frames and a contact sheet. No mp4.
