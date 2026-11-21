Sent: 2026-11-21 16:53 ET

# FDP-73 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md.
2. **Scripts** (`scripts/`; run from tools-env with `env -u BROWSER node`): see scripts/README.md.
3. **Evidence:** `json/` (runs and logs), `screens/cases|devices|locales|geo|a11y`, `outputs/` (trial downloads + saved catalog JSON), `blobs/` (PDFs read from the page's Blob at the cap, for analysis only), `testfiles/`, `video/`, `html/` (page + 2 blogs), `js/`.
4. **Rules:** guest only. No sign-in, no payment, no ad clicks. Times are EST. Most fresh contexts load at 2/2; `left` needs TRIES=40 or more.
