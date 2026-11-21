Sent: 2026-11-21 09:47 ET

# FDP-53 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md, and rerunnable cases in test-cases.md.
2. **Scripts** (`scripts/`, run from tools-env with `env -u BROWSER node`; WebKit needs `GIO_EXTRA_MODULES=…/giomods`):
   - `px53-live.js func [chromium|firefox|webkit]`: 45-case battery.
   - `px53-live.js gate`: trial-use check (TRIES env sets how many fresh contexts to try).
   - `px53-biglist2.js`: list timing.
   - `px53-ux.js`: phones, keyboard, live region.
   - `px53-share.js`: share buttons.
   - `run-matrix.js config.json`: devices, locales, geo, axe.
3. **Evidence:**
   - `evidence/json`: all results.
   - `evidence/outputs`: downloaded .txt files.
   - `evidence/screens`: cases, devices, locales, geo, a11y.
   - `evidence/video`: frames, sheets, crops, info.json.
   - `evidence/html`, `evidence/js`.
4. **Rules:** guest only, no sign-in, no payment, no ad clicks. Times are EST.
