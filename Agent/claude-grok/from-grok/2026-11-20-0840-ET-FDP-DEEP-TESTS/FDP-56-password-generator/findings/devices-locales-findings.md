Sent: 2026-11-21 10:59 ET

# Devices, locales, geo, a11y (FDP-56)

- **Devices (10):** all render. Console errors are ad scripts only.
  - iPhone SE fold: the floating Feedback button covers the "Hide" toggle (screenshot `devices/iphone-se-fold.png`).
  - Long passwords wrap mid-string (break-all), which is fine.
- **Locales:** html lang is correct, and the breadcrumb and header are translated. The H1, subtitle, every tool control, the FAQ and the `<title>` stay English (verified in the ja/de screenshots). /ar is a 404 (no ar locale).
- **ja desktop:** flagged overflowX by the script; not visible in the fold screenshot.
- **Geo:** **the consent banner shows for de-DE and fr-FR** (verified in the screenshots; matrix `consent:false` is wrong again). None for en-US, hi-IN, ar-SA, ja-JP. No prices anywhere (the tool shows no offer).
- **axe:** Desktop has label-content-name-mismatch (1, serious, `.right-2`) and region (1). Pixel 7 is clean.
