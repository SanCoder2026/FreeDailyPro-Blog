Sent: 2026-11-21 13:37 ET

# FDP-63 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`):
   - `px63-live.js <zero|left|cases|kbd|quickbuy> [engine]`. Env: TRIES.
   - `px63-debug.js` (mapping + keyboard), `px63-extra.js <chromium|firefox>`, `px63-drive.js`, `px63-camera.js`, `px63-cam2.js`, `px63-touch.js`.
   - `make63.py` builds the test images. `px63-scripts.js`, `px63-expand.js`, `run-matrix.js config.json`.
3. **Evidence:** `json/` runs, `testfiles/`, `screens/cases|devices|locales|geo|a11y`, `video/`, `html/`, `js/`.
4. **Rules:** guest only. No sign-in, no payment (stop at the email prompt and Stripe), no ad clicks. Times are EST. Fresh contexts are usually at 10/10; use TRIES=30–40.
