Sent: 2026-11-21 13:37 ET

# Devices, locales, geo, a11y (FDP-63)

- 10 devices 200. iPhone SE 320 px: 9 px overflow from the header menu button (screenshot). Others fit. WebKit loads fine (no media APIs on this page).
- Locales es/pt/fr/de/ja/hi/zh/ko/id: 200; chrome and trial strip translated; H1, subtitle, drop zone, camera button, meta stay English (es screenshot). /ar → 404 (no ar locale; expected). ja desktop 1369 px (site-wide).
- Geo (US, DE, FR, IN, SA, JP): same $1 / $4.99. The EU consent banner (Accept all / Reject non-essential / Choose) shows in de-DE (screenshot; the script flag missed it, so screenshots were used).
- axe: desktop label-content-name-mismatch (serious, `.right-2`), region (moderate); Pixel 7 color-contrast on an ad caption (keep reserved ad slots; fix the caption colour).
