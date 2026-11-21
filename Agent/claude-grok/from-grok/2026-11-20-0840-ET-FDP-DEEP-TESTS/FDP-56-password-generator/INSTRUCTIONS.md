Sent: 2026-11-21 10:59 ET

# FDP-56 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md, and cases in test-cases.md.
2. **Scripts** (tools-env, `env -u BROWSER node`; WebKit needs `GIO_EXTRA_MODULES`):
   - `px56-live.js probe|left [engine]`. Env: TRIES (fresh contexts to try), SUF (suffix).
   - `px56-stats.js`: Node desk test of the site's generator functions.
   - `run-matrix.js config.json`.
3. **Evidence:**
   - `json/`: probe, probe-firefox, left tries, matrix.
   - `desk/stats.json`.
   - `screens/cases`: P00–P13 plus the P07 crop.
   - `screens/devices|locales|geo|a11y`.
   - `video/`: sheet, crops, info.
   - `html/`: page, blog, password-strength head.
   - `js/`: bundles.
4. **Rules:** guest only, no sign-in, no payment, no ad clicks. Times are EST.
5. **No test files:** this tool takes no file input.
