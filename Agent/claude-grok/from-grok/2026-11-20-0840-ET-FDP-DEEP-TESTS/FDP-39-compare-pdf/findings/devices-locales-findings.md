Sent: 2026-11-21 03:05 ET

# FDP-39 Compare PDF: devices, locales, geo, axe (run-matrix.js, 2026-11-21 02:53–03:00 EST)

Matrix contexts loaded at "0 remaining today" (display-only).
- **Devices (10, all 200):** iPhone SE 9 px overflow (the shared `button.inline-flex…`, as in FDP-30–38). The rest have none. The trial strip and both drop zones are above the fold. Small targets: Home breadcrumb, footer links.
- **Locales:** es…id 200, html lang set, H1 translated; title/meta English; ja desktop 3 px overflow; `/ar` 404.
- **Geo (6):** "$1", "$4.99" everywhere; no consent banner shown in this run.
- **axe (page load):**
  - label-content-name-mismatch (serious, 1)
  - region (moderate, 1)
  - Pixel 7 color-contrast (serious, 2: the ad caption under the slots). Keep ad slots reserved; fix the caption colour.
  - The axe scan ran before any result, so the dark-theme diff-mark contrast (about 1.3–1.7:1) comes from a manual measurement in live-functional-findings.md.
- **Engines:** live cases in Chromium and Firefox (K01, K06, K08, K10, K14 match); WebKit page load only.
