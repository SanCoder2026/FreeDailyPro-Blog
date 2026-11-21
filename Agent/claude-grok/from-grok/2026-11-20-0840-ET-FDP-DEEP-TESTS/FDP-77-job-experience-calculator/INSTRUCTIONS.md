Sent: 2026-11-21 17:36 ET

# FDP-77 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md. The harness needs only node.
3. **Evidence:** `json/` (zero, left-firefox, cases, logs, matrix), `harness/` (22 cases + blog example), `screens/cases|devices|locales|geo|a11y|blog`, `video/` (sheet, 0:40 frame, info), `html/`, `blog/`, `js/` (tool, dates and usage-hook chunks + pretty copies).
4. **Rules:** guest only. No sign-in, no payment, no ad clicks. Times are EST. Most fresh contexts load at 10/10; Firefox found 0/10 on try 6.
