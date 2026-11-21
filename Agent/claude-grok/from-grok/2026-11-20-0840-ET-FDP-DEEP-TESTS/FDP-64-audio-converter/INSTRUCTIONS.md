Sent: 2026-11-21 14:10 ET

# FDP-64 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`):
   - `px64-live.js <zero|left|batch|cases|quickbuy> [engine]`. Env: TRIES, ANY=1, SUF, CAP=1 (batch at the cap), DLT.
   - `px64-extra.js` (quality lines, OGG→OGG, cap paths: Drive, cloud storage, Trimmer), `px64-big.js` (size limit), `px64-drive.js`.
   - `make64.sh` builds the test files. `px64-scripts.js`, `px64-expand.js`, `run-matrix.js config.json`.
3. **Evidence:** `json/` runs, `outputs/` converted files, `testfiles/`, `screens/cases|devices|locales|geo|a11y`, `video/`, `html/`, `js/`.
4. **Rules:** guest only. No sign-in, no payment (stop at the email prompt and Stripe), no ad clicks. Times are EST. Fresh contexts are usually at 10/10; use TRIES=30–40.
