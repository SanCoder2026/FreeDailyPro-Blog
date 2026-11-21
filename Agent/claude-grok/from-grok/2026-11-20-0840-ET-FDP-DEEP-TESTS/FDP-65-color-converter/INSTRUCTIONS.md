Sent: 2026-11-21 14:26 ET

# FDP-65 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`):
   - `px65-live.js <zero|left|cases> [engine]`. Env: TRIES, SUF. The clipboard is set/read from a same-origin robots.txt tab.
   - `px65-alpha.js`: alpha round trips + Firefox copy at the cap.
   - `px65-scripts.js`, `px65-expand.js`, `run-matrix.js config.json`.
3. **Evidence:** `json/` runs, `screens/cases|devices|locales|geo|a11y`, `video/`, `html/`, `js/`.
4. **Rules:** guest only. No sign-in, no payment, no ad clicks. Times are EST.
