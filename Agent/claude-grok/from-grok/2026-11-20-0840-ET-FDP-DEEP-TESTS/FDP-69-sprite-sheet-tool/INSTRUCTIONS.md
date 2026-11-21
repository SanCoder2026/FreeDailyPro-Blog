Sent: 2026-11-21 15:35 ET

# FDP-69 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md.
3. **Evidence:** `json/` runs, `screens/cases|devices|locales|geo|a11y`, `outputs/` (PNG/JSON/ZIP and fetched frame tiles), `testfiles/`, `video/`, `html/`, `js/`.
4. **Rules:** guest only. No sign-in, no payment, no ad clicks. Times are EST. Premium contexts mostly load at 2/2; `left` needs many tries.
