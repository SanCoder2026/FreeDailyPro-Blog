Sent: 2026-11-21 10:39 ET

# Devices, locales, geo, a11y (FDP-55)

- **Devices (10):** all render. iPhone SE header overflow is a known site-wide issue. Console errors are ad scripts only (adsbygoogle `no_div`, media.net CORS).
- **Locales:** html lang is right for es/pt/fr/de/ja/hi/zh/ko/id, but the title, H1, subtitle, drop zone and FAQ stay English. The trial strip and buttons are translated, and de shows "1 $ / 4,99 $" (the matrix price regex missed it; verified in the screenshot). /ar is a 404 (no ar locale, consistent with hreflang).
- **ja desktop:** page 1369 px wide at 1366 (3 px); not visible in the fold screenshot.
- **Geo:** **the consent banner shows for de-DE and fr-FR** (verified in geo-de/fr fold screenshots, despite matrix `consent:false`). No banner for en-US, hi-IN, ar-SA, ja-JP. Prices are $1/$4.99 everywhere.
- **axe:** Desktop has label-content-name-mismatch (1, serious) and region (1). Pixel 7 has color-contrast on the ad caption (2).
