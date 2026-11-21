Sent: 2026-11-21 16:05 ET

# FDP-71 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md.
3. **Evidence:** `json/` runs and logs, `screens/cases|devices|locales|geo|a11y`, `outputs/` (paid downloads `L*`, player blobs `*player-blob*`, player-menu download `zero-player-menu-*`), `testfiles/`, `video/`, `html/`, `js/` (tool chunk + shared player/save excerpts).
4. **Rules:** guest only. No sign-in, no payment, no ad clicks. Times are EST. Most fresh contexts load at 10/10; `left` needs TRIES=40.
