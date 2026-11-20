Sent: 2026-11-20 08:40 ET

# FDP-21 Sign PDF: devices, locales, geo, a11y matrix

`json/matrix-results.json`, run 17:04–17:12 EST.
- 10 device profiles all 200. Overflow only iPhone SE (320 px, scrollWidth 329, header button — site-wide).
- Locales en/es/pt/fr/de/ja/hi/zh/ko/id 200; ja desktop 3 px overflow (scrollWidth 1369 / 1366); /ar 404. Console errors are ad-script / permissions-policy only.
- Geo (de, fr, hi, ar, ja): $3 / $9.99 everywhere; cookie banner in de/fr.
- axe idle: desktop `label-content-name-mismatch` (serious, `.right-2`), `region` (moderate); Pixel 7 `color-contrast` (serious) on the "Advertisement" caption of the after-tool slot (keep the slot; restyle the caption).
- Phone flow (gate script): tap placement works; field table overflows; Download 4+ screens down on iPhone SE.
