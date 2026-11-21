Sent: 2026-11-21 18:56 ET

# FDP-82 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md. `make-testfiles.py` rebuilds the inputs (seeded, byte for byte except ffmpeg version differences in encoded files); `analyze.py` lists beep times and pitch (clip identity), rate, channels, codec and bitrate.
3. **Evidence:** `json/` (zero, left, cases, analysis-cases, fmtdup, big, quickbuy, matrix, logs), `outputs/` (result-player bytes for every case), `downloads/` (files saved through Download in `left`), `testfiles/` (the 60 MB big WAVs are left out; see REPRODUCE step 4), `screens/…`, `video/`, `html/`, `blog/`, `js/` (tool, operations excerpt, ToolPage download-button excerpt, reorder list).
4. **Rules:** guest only. No sign-in, payment, email or ad clicks. Times are EST. Chromium found 0/10 on try 9.
