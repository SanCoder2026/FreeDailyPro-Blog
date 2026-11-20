Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-11 Paycheck Calculator)

- **Written:** 2026-11-19 13:55:40 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P1 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce.** After fixing, rerun:
   - `test-cases.md`: PC-01…PC-29.
   - `node scripts/pc-live.js [ids] [outfile]`: 30 cases + blog and video cases (reading only, free).
   - `python3 scripts/ref_federal.py <income> <status> <pretax>`: independent federal/FICA reference.
   - `node scripts/pc-gate.js`: the three export actions at 0 and with uses left. Costs 1 use in a context with uses. **Pending: needs re-run after midnight UTC (7:00 PM ET)**, RERUN row 11.
   - `node scripts/pc-kbd.js`: notes, tab order, axe, phones.
   - `node scripts/run-matrix.js scripts/config.json`: devices, locales, geo and axe (about 9 minutes).
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses". Copy and export charges are intended (owner policy); only the wording is in scope.
5. **evidence/** contains:
   - `findings/`: desk, video, live functional, devices/locales.
   - `json/`: cases, blog-cases, video-case, gate, gate-run1, kbd, matrix-results.
   - `js/`: PaycheckCalculator (raw and prettified), calcChecks, useLogToolUsage.
   - `html/`: the tool and its headers, the blog, es and fr locale pages, /terms, /faq.
   - `screens/`: live, devices, locales, geo and a11y. Screens are ≤1400 px wide (PNG at 256 colours; full-page shots as JPG q70). Full-page locale shots are kept for en, es and ja only.
   - `video/`: info.json, 8 frames, 2 contact sheets, 4 crops. No mp4.
6. **RERUN-AFTER-RESET row 11** was added (first-export cost with uses left). A copy of the running list is in `scripts/`.
