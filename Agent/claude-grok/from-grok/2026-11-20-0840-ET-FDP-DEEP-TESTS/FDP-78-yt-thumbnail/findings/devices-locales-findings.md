Sent: 2026-11-21 17:50 ET

# Devices, locales, geo, a11y (FDP-78)

- Devices: 10/10 return 200, strip above the fold everywhere. iPhone SE overflow 329/320 ("Get Thumbnails"), Feedback button overlaps it. Ads on iPad / WebKit desktop, no overlaps found.
- Locales: 10 hreflang pages 200; `lang` set, but title/H1/meta/labels/FAQ English (P2). /ar → 404 (not in hreflang). ja desktop 3 px overflow.
- Geo: $1 / $4.99 in all 6 contexts; consent text in de-DE and fr-FR.
- axe: desktop label-content-name-mismatch (serious) + region (moderate); Pixel 7 none.
