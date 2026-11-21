Sent: 2026-11-21 17:13 ET

# Devices, locales, geo, a11y (FDP-75)

- Devices: all 10 return 200, strip above the fold. Only iPhone SE overflows (329/320, a header button). Desktop 1366 CLS 1.0 (body shift at 427 ms during boot); 1920 0.036.
- Locales: 10 hreflang pages 200 with translated nav, badges, strip, Quick Buy and "Open from Google Drive"; H1, subtitle, "Check against", drop-zone text and FAQ English (P2). /ar → 404 (not in hreflang). ja desktop overflows a few px.
- Geo: $1 / $4.99 in all 6 contexts; consent banner text in de-DE and fr-FR.
- axe: desktop label-content-name-mismatch (serious, `.right-2`) + region (moderate); Pixel 7 none.
