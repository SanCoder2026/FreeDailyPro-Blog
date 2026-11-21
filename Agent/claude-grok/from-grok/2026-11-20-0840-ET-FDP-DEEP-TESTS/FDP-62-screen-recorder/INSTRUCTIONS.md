Sent: 2026-11-21 13:20 ET

# FDP-62 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`):
   - `px62-live.js <zero|quickbuy|left|perload|nodm|deny|stopcheck> [engine]`. Env: TRIES, ANY=1, SUF. Chromium runs with fake mic/camera flags; Firefox with fake-stream prefs. `getDisplayMedia` is a canvas stub in the test browser only.
   - `px62-wk.js`, `px62-wk2.js`: WebKit crash isolation.
   - `px62-scripts.js`, `px62-expand.js`, `run-matrix.js config.json`.
3. **Evidence:**
   - `json/`: runs.
   - `outputs/`: WebM files.
   - `screens/cases|devices|locales|geo|a11y|live`.
   - `video/`: sheet, frames, info.
   - `html/`, `js/`.
4. **Rules:** guest only. No sign-in, no payment (stop at the email prompt and Stripe), no ad clicks. Times are EST. Premium trial uses reset at midnight UTC (7:00 PM ET). Fresh contexts are usually at 2/2; use TRIES=30–40.
