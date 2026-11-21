Sent: 2026-11-21 10:39 ET

# FDP-55 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md, and cases in test-cases.md.
2. **Test PDFs:** `evidence/testfiles/`, built by `make55.py` (reportlab + pikepdf). damaged.pdf and password_u123.pdf (password u123) come from FDP-52.
3. **Scripts** (tools-env, `env -u BROWSER node`; WebKit needs `GIO_EXTRA_MODULES`):
   - `px55-live.js probe|left|cases [engine]`. Env: TRIES (fresh contexts to try), CASES=B01,B08 (subset), SUF (suffix).
   - `px55-ovf.js` (overflow hint screenshots, no run).
   - `px55-drive.js` (Drive popup).
   - `run-matrix.js config.json`.
4. **Evidence:**
   - `outputs/`: every downloaded PDF/CSV/ZIP plus unzipped folders.
   - `screens/render/`: page renders and crops.
   - `json/`: all run results.
   - `video/`: sheet, crops, info.
   - `screens/devices|locales|geo|a11y`: the matrix.
5. **Rules:** guest only, no sign-in, stop at the email field or Stripe, no ad clicks. Times are EST.
