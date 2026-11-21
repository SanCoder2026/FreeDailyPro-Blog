Sent: 2026-11-21 14:10 ET

# Devices, locales, geo, a11y (FDP-64)

- 10 devices 200 (WebKit/iPad fine). iPhone SE: 9 px overflow from the header menu button. Phones: "Tap to choose… / or tap to choose".
- Locales es/pt/fr/de/ja/hi/zh/ko/id: 200; H1 translated (e.g. "Convertidor de Audio"); subtitle, on-device note, mode toggle, drop zone, FAQ English (es screenshot). /ar 404 (no ar locale; expected). ja desktop 1369 px.
- Geo (US, DE, FR, IN, SA, JP): $1/$4.99 (+$3/$9.99 on the Premium cross-sell card). Consent banner shows in de-DE (screenshot; script flag missed it).
- axe: desktop label-content-name-mismatch (serious), link-in-text-block ×4 (serious), region (moderate); Pixel 7 color-contrast ×1 (ad caption; keep reserved ad slots), link-in-text-block ×4.
