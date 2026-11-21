Sent: 2026-11-21 18:03 ET

# FDP-79 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md.
3. **Evidence:** `json/` (zero, left-firefox, cases, shift, matrix, logs), `screens/cases|devices|locales|geo|a11y|blog`, `video/` (sheets, 0:25 and 0:50 frames, info), `html/`, `blog/`, `js/` (tool chunk + pretty copy, copyText chunk).
4. **Rules:** guest only. No sign-in, payment, email or ad clicks. Times are EST. Most fresh contexts load at 10/10; Firefox found 0/10 on try 20.
