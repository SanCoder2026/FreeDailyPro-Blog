Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-15 Word & Character Counter)

- **Written:** 2026-11-19 14:59 EST (box `date`, ET).

1. **Read REPORT.md first.** It gives the intent, evidence and outcomes, plus all 22 checks with their evidence paths.
2. **Work from PRIORITIES.md** (P1 → P2). Each item points to a repro in REPRODUCE.md.
3. **Rerun after fixing** (Node with `playwright` and `axe-core`):
   - `node scripts/wc-live.js`: 30 counting cases against `wc-cases.json`, timings, platform rows, 224k text.
   - `node scripts/wc-gate-kbd.js`: starting count, Ctrl+C, Copy stats, Clear, tab order, aria-live, axe, iPhone SE and Pixel 7 layout. Copy stats may cost a trial use if the tool becomes gated.
   - `node scripts/wc-goal.js`: word goal states.
   - `node scripts/wc-webkit-retry.js`: iPhone 14 Pro Max WebKit load and count, 3 attempts.
   - `node scripts/run-matrix.js scripts/config.json`: devices, locales, geo and axe (about 6 minutes).
   - `test-cases.md`: WC-01…WC-22.
4. **Rules while retesting:**
   - Guest only. No sign-in, email or card entry, no ad clicks, no API or MCP calls.
   - Counters are display-only evidence.
   - Say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: live-functional, desk, video, devices-locales.
   - `json/`: live-cases, gate-kbd, goal, webkit-retry, matrix-results.
   - `js/`: WordCounter and WordCounterExtras (raw and prettified).
   - `html/`: tool page (html and text), headers, es locale, blog (html and text).
   - `screens/`: live (typed stats, platform limits, phone layouts, WebKit retry), devices, locales (fold for all; full-page for en, es, ja), geo, a11y. Screens are ≤1400 px wide (PNG at 256 colours; full-page shots as JPG q70).
   - `video/`: info.json, contact sheet, 1 crop, 1 frame. No mp4.
6. **No RERUN-AFTER-RESET row** for this tool: nothing is pending. A copy of the running list is in `scripts/`.
