Sent: 2026-11-21 18:39 ET

# FDP-81 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md. `make-testfiles.py` rebuilds the inputs (all WAV inputs are left out of the zip for size; the script is seeded, so it rebuilds them byte for byte); `analyze.py` lists bursts and gaps in any output.
3. **Evidence:** `json/` (zero, left, cases, analysis-cases, quickbuy, matrix, logs), `outputs/` (Preview and result-player bytes; most WAV outputs left out for size, all measured in analysis-cases.json), `downloads/` (files saved through Download), `testfiles/`, `screens/…`, `video/`, `html/`, `blog/`, `js/` (tool, silence detector, ToolPage download-button excerpt).
4. **Rules:** guest only. No sign-in, payment, email or ad clicks. Times are EST. Chromium found 0/10 on try 16; the Firefox search was stopped as redundant.
