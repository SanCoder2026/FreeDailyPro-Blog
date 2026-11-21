Sent: 2026-11-21 12:15 ET

# FDP-59 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps in REPRODUCE.md, cases in test-cases.md.
2. **Inputs:** `evidence/testfiles/cases.json` (14 cases).
3. **Scripts** (`scripts/`, run from tools-env with `env -u BROWSER node`; WebKit needs `GIO_EXTRA_MODULES`):
   - `px59-live.js probe|left|cases [engine]`. Env: TRIES (fresh contexts to try for uses left), ANY=1 (use the first context, whatever its count), SUF.
   - `px59-expected.mjs [cases.json]`: recompute expected drafts from the site's template code (needs `textUtils.pretty.js` copied to /tmp/textUtils59.mjs) and compare.
   - `px59-scripts.js`, `px59-expand.js`, `run-matrix.js config.json`.
4. **Evidence:** `json/` (probe, cases, left-firefox, expected-compare, matrix), `screens/cases|devices|locales|geo|a11y|live`, `video/` (sheet, crops, info), `html/`, `js/`.
5. **Rules:** guest only, no sign-in, no payment, no ad clicks. Times are EST. Trial uses reset at midnight UTC (7:00 PM ET).
