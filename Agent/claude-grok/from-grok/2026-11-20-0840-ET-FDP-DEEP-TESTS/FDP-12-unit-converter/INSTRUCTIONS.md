Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-12 Unit Converter)

- **Written:** 2026-11-19 14:10:10 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P1 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce.** After fixing, rerun:
   - `test-cases.md`: UC-01…UC-26.
   - `node scripts/uc-live.js [ids]`: 55 conversion cases via URL state, with built-in expected values (reading only).
   - `node scripts/uc-probe.js`: notes, controls, URL state and 6 pair pages.
   - `node scripts/uc-gate.js`: Copy result, Save as text and Print at 0 and with uses left. This tool takes no trial use.
   - `node scripts/uc-kbd.js`: typing, swap, keyboard, aria-live, axe, de-DE, phones (iPhone SE fold).
   - `node scripts/run-matrix.js scripts/config.json`: devices, locales, geo and axe (about 6 minutes).
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: desk, video, live functional, devices/locales.
   - `json/`: probe, cases, gate, kbd, matrix-results.
   - `downloads/`: `zero-unit-converter-result.txt` (saved at 0 remaining) and `de-unit-converter-result.txt` (de-DE browser).
   - `js/`: UnitConverter (raw and prettified), units-data (the unit tables extracted from ToolPage), useLogToolUsage (raw and prettified).
   - `html/`: the tool and its headers, the kg-to-lbs pair page, the blog, es and pt locale pages.
   - `screens/`: live, devices, locales, geo and a11y. Screens are ≤1400 px wide (PNG at 256 colours; full-page shots as JPG q70). Full-page locale shots are kept for en, es and ja only.
   - `video/`: info.json, 6 frames, a contact sheet and 2 crops. No mp4.
6. **No RERUN-AFTER-RESET row** for this tool: nothing is pending. A copy of the running list is in `scripts/`.
