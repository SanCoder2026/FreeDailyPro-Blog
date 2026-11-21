Sent: 2026-11-21 15:54 ET

# FDP-70 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md.
3. **Evidence:** `json/` runs and logs, `screens/cases|devices|locales|geo|a11y`, `outputs/` (every saved JPEG + the 300 px preview canvas), `testfiles/`, `video/`, `html/`, `js/` (tool chunk, jpegDpi, shared badge excerpt).
4. **Rules:** guest only. No sign-in, no payment, no ad clicks. Times are EST. Most fresh contexts load at 10/10; `left`/`limits` need TRIES=40.
