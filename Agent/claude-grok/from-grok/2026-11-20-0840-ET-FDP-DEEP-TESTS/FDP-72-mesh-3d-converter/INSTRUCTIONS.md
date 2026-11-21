Sent: 2026-11-21 16:17 ET

# FDP-72 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md.
3. **Evidence:** `json/` runs and logs, `screens/cases|devices|locales|geo|a11y`, `outputs/` (all downloads, prefixed by job id), `testfiles/`, `video/`, `html/` (page + 3 blogs), `js/`.
4. **Rules:** guest only. No sign-in, no payment, no ad clicks. Times are EST. Most fresh contexts load at 10/10; `left` needs TRIES=40.
