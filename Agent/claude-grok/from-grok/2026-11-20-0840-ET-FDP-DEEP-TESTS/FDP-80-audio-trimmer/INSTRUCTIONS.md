Sent: 2026-11-21 18:23 ET

# FDP-80 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md. `make-testfiles.py` rebuilds the inputs (the 6 and 12 min WAVs are left out of the zip for size); `analyze.py` reads any output.
3. **Evidence:** `json/` (zero, left, left-firefox, cases, analysis-*, quickbuy, matrix, logs), `outputs/` (result-player bytes per case), `downloads/` (files saved through Download), `testfiles/`, `screens/…`, `video/`, `html/`, `blog/`, `js/` (tool, operations, time fields, time format, ffmpeg engine, ToolPage download-button excerpt).
4. **Rules:** guest only. No sign-in, payment, email or ad clicks. Times are EST. Most fresh contexts load at 10/10; Chromium found 0/10 on try 25; Firefox none in 40.
