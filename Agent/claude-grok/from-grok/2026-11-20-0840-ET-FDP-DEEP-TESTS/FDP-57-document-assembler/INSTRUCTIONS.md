Sent: 2026-11-21 11:31 ET

# FDP-57 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md, and cases in test-cases.md.
2. **Test files:** `evidence/testfiles/` (`make57.py`; damaged.pdf and password_u123.pdf from FDP-52, password u123).
3. **Scripts** (tools-env, `env -u BROWSER node`; WebKit needs `GIO_EXTRA_MODULES`):
   - `px57-live.js probe|left|cases [engine]`. Env: TRIES, CASES=C1,C3, SUF.
   - `px57-pw.js` (password flow).
   - `px57-explore.js`.
   - `px57-drive.js`.
   - `run-matrix.js config.json`.
4. **Evidence:**
   - `outputs/`: L01/L02 PDFs.
   - `screens/render/`: page sheet and crops.
   - `json/`: all runs.
   - `video/`: sheet, crop, info.
   - `screens/devices|locales|geo|a11y`.
5. **Rules:** guest only, no sign-in, stop at the email field or Stripe, no ad clicks. Times are EST. Trial uses reset at midnight UTC (7:00 PM ET).
