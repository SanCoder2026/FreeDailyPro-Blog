Sent: 2026-11-21 06:49 ET

# FDP-47: devices, locales, geo, a11y (matrix-results.json)

- **Devices (10):** all 200. iPhone SE scrollWidth 329 vs 320 (a button row, 9 px; P3). Others fit. CLS ≤ 0.025. Small targets: delay buttons (None/2s/5s/10s), "Premium application: what does this mean".
- **Phones:** the layout renders, but Android browsers have no `getDisplayMedia` (P1, see live findings).
- **Locales:** es/pt/fr/de/ja/hi/zh/ko/id all 200 with html lang set; H1 and tool name translated; title, meta, Take Screenshot / Capture whole page / delay help, How to use, Common questions and the video title stay English. /ja 3 px overflow. /ar is a 404 probe (not in hreflang).
- **Geo (6 contexts):** $3 / $9.99 everywhere.
- **axe:** desktop label-content-name-mismatch (1, serious), region (1); Pixel 7 clean.
