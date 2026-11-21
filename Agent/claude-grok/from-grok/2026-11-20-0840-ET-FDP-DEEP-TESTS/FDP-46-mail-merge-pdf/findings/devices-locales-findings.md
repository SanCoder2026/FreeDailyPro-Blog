Sent: 2026-11-21 06:22 ET

# FDP-46: devices, locales, geo, a11y (matrix-results.json)

- **Devices (10):** all 200. iPhone SE scrollWidth 329 vs 320 (a button row, 9 px; P3). Others fit. CLS ≤ 0.015. Small targets: breadcrumb Home, "Use an example", Letter/Certificate.
- **Locales:** es/pt/fr/de/ja/hi/zh/ko/id all 200 with html lang set; title, meta, tool labels ("1. Your table…", "Download one PDF"), About and FAQ headings stay English; header items are translated. /ja 3 px overflow. /ar is a 404 probe (not in hreflang).
- **Geo (6 contexts):** $1 / $4.99 everywhere.
- **axe:** desktop label-content-name-mismatch (1, serious), region (1); Pixel 7 color-contrast on the ad label (2). Keep the ad slot; fix the label contrast.
- **Ads:** in-content slot after the tool on mobile (y≈1600 on iPhone SE); no overlap with controls.
