Sent: 2026-11-20 08:40 ET

# Devices, locales, geo, a11y (matrix 15:57–16:07 EST; `evidence/json/matrix-results.json`)

- **Devices** (iPhone SE, iPhone 14 Pro Max, Pixel 7, Galaxy S9+, iPad Mini, iPad Pro 11 landscape, desktop Chromium 1366/1920, Firefox 1440, WebKit 1440): all 200.
  - **iPhone SE 320 px:** 9 px horizontal overflow from a header button (right=329; site-wide, seen on earlier tools).
  - All others: no overflow.
- **Trial strip:** shown above the fold on all devices. iPad contexts loaded with 10 remaining; the rest loaded at 0 (display-only evidence).
- **Locales:**
  - es/pt/fr/de/ja/hi/zh/ko/id: 200, correct `lang`, ltr.
  - The H1 is translated (e.g. 動画をGIFに変換). Title, meta, drop zone, controls and copy are English.
  - /ar/tool/video-to-gif returns 404 (no Arabic locale; consistent with earlier tools).
  - Pair pages load (the screenshot name `locale-probe-tool-*` holds the last one).
- **Geo** (de-DE, fr-FR, hi-IN, ar-SA, ja-JP + baseline): html lang en, prices $1 / $4.99 / $3 / $9.99, no consent banner detected.
- **axe:**
  - Idle desktop: label-content-name-mismatch ×1, link-in-text-block ×3, region ×1. Pixel 7: color-contrast ×2 (ad-slot label), link-in-text-block ×3.
  - With a file loaded: **select-name critical ×4** (from `gate-kbd.json`).
