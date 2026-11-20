Sent: 2026-11-20 08:40 ET

# Devices, locales, geo, a11y (matrix 16:20–16:31 EST; `evidence/json/matrix-results.json`)

- **Devices:** 10 profiles, all 200.
  - iPhone SE 320 px: 9 px overflow from a header button (site-wide).
  - Others: none.
  - The trial strip is above the fold everywhere. iPhone SE and iPad Mini contexts loaded with 10 remaining, the rest at 0 (display-only evidence).
- **Locales:**
  - es/pt/fr/de/ja/hi/zh/ko/id: 200, correct `lang`, ltr. H1 translated.
  - `<title>`, meta and tool body are English.
  - /ar/tool/resize-crop: 404.
- **Geo** (de-DE, fr-FR, hi-IN, ar-SA, ja-JP): html lang en, USD prices, no consent banner detected.
- **axe:**
  - Idle desktop: label-content-name-mismatch ×1, region ×1. Pixel 7: color-contrast ×2 (ad-slot label).
  - With a file in Resize: **label critical ×1** (unit value box).
  - Crop and result views: no violations, but the ratio buttons lack `aria-pressed` (manual check).
- **Browsers:** Firefox and WebKit desktop process images correctly (`browsers.json`).
