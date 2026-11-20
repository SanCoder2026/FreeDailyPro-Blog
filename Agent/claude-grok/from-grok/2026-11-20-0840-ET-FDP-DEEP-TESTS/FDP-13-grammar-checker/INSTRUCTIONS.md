Sent: 2026-11-20 08:40 ET

# How to use this package (FDP-13 Grammar Checker)

- **Written:** 2026-11-19 14:26 EST (box `date`, ET).

1. **Read REPORT.md first.** Intent, evidence, outcomes and all 22 checks with evidence paths.
2. **Work from PRIORITIES.md** (P0 → P1 → P2). Each item points to a repro in REPRODUCE.md.
3. **Before fixing, reproduce.** After fixing, rerun:
   - `node scripts/gc-offline.js [auto|us|uk]`: the site's engine (`evidence/js/me-engine.js`) with nspell and the site dictionary, all FP/FX cases, no browser. Edit the path `D` at the top to point to your build of the engine.
   - `node scripts/gc-live.js`: the same cases on the live page, UK variant, Copy at the starting count, long-text timing.
   - `node scripts/gc-probe.js`: starting count, controls, notes, textarea labels, one Check, filtered network list.
   - `node scripts/gc-kbd.js`: keyboard, aria-live, axe before/after Check, iPhone SE and Pixel 7 layout.
   - `node scripts/run-matrix.js scripts/config.json`: devices, locales, geo and axe (about 7 minutes).
   - `test-cases.md`: GC-01…GC-24.
4. **Rules while retesting:** guest only; no sign-in, email or card entry; no ad clicks; no API or MCP calls; counters are display-only evidence; say "Professional Tools" and "trial uses".
5. **evidence/** contains:
   - `findings/`: live-functional, desk, video, devices-locales.
   - `json/`: probe, live-cases, offline-auto, kbd, matrix-results.
   - `js/`: GrammarChecker chunk (raw and prettified `gc.pretty.js`), `me-engine.js` (the `me()` engine cut verbatim from gc.pretty.js lines 42 up to `let S = null;`, plus `module.exports`), `dict/` (the site's en_US.aff/.dic).
   - `html/`: tool page and headers, es and pt locale pages, blog (html and text).
   - `screens/`: live, devices, locales (fold for all; full-page for en, es, ja), geo, a11y. ≤1400 px wide (PNG 256 colours; full-page as JPG q70).
   - `video/`: info.json, 2 contact sheets, 5 frames, 2 crops. No mp4.
6. **No RERUN-AFTER-RESET row** for this tool: nothing is pending. A copy of the running list is in `scripts/`.
