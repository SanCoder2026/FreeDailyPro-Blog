Sent: 2026-11-21 17:25 ET

# FDP-76 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md. The harness needs only node.
3. **Evidence:** `json/` (zero, left-firefox, clip, logs, matrix), `harness/` (rule-engine output for 30 cases + the blog paragraph), `screens/cases|devices|locales|geo|a11y|blog`, `video/` (sheet, 0:20 frame, About crop at 0:30, info), `html/`, `blog/`, `js/`.
4. **Rules:** guest only. No sign-in, no payment, no ad clicks. Times are EST. Most fresh contexts load at 10/10; Firefox found 0/10 on try 6.
