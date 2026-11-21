Sent: 2026-11-21 12:33 ET

# FDP-60 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps in REPRODUCE.md, cases in test-cases.md.
2. **Inputs:** `evidence/testfiles/cases.json` (22 cases + a built-in 202,500-char case).
3. **Scripts** (`scripts/`, run from tools-env with `env -u BROWSER node`; WebKit needs `GIO_EXTRA_MODULES`):
   - `px60-live.js probe|left|cases [engine]`. Env: TRIES, ANY=1 (first context, whatever its count), SUF.
   - `px60-expected.mjs [cases.json]`: expected output from the site's conversion code; writes `expected-compare.json`.
   - `px60-scripts.js`, `px60-expand.js`, `run-matrix.js config.json`.
4. **Evidence:** `json/`, `outputs/` (downloads), `screens/cases|devices|locales|geo|a11y|live`, `video/`, `html/`, `js/`.
5. **Rules:** guest only, no sign-in, no payment, no ad clicks. Times are EST. Trial uses reset at midnight UTC (7:00 PM ET).
