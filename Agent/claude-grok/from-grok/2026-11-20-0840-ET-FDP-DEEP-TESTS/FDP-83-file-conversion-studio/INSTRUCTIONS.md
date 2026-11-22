Sent: 2026-11-21 19:08 ET

# FDP-83 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md. No test files were needed (a guest cannot reach the Studio).
3. **Evidence:** `json/` (live Chromium + Firefox, matrix, logs), `screens/…`, `html/` (page, headers, expanded text, JSON-LD, links), `blog/` (both guides), `js/` (Studio, paywall gate, access, CTA labels; prettified), `video/channel-videos.txt` (511 channel titles, none for the Studio).
4. **Rules:** guest only. No sign-in, payment, email or ad clicks. Times are EST.
