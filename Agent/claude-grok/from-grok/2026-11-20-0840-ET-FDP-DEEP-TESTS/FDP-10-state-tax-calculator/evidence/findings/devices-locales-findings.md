Sent: 2026-11-20 08:40 ET

# FDP-10 State Tax Calculator: devices, platforms, countries and languages

- **Run:** `run-matrix.js` from 2026-11-19 13:29:13 to 13:36:44 EST. Raw data: `json/matrix-results.json`.
- **Coverage:**
  - 10 device profiles (iPhone SE, iPhone 14 Pro Max, Pixel 7, Galaxy S9+, iPad Mini, iPad Pro 11 landscape, Desktop 1366/1920 Chromium, Firefox 1440, WebKit 1440)
  - 9 hreflang locales + en, × Pixel 7 and desktop
  - /ar
  - 6 geo contexts
  - axe on desktop and Pixel 7

## PASS
- 200 on 10 of 10 profiles; load times 6–9 s (Pixel 7 run 25 s).
- 16 px inputs on phones, so iOS doesn't zoom. The income field is near the top on all phones (y 397–523 px).
- No ad overlaps on any profile. CLS ≤ 0.014.
- The same USD results in all 6 geos ($2,774 CA default). The consent banner appears in de-DE and fr-FR only.
- The wide bracket and compare tables scroll inside their own box, so the page itself doesn't scroll sideways (except the header item below).

## FAIL / PARTIAL
- **iPhone SE (320 px):** page overflow to 353 px, caused by a header button (right edge 329) and the "US-Specific" badge (353). This is the same header as #9.
- **Desktop ja:** 1369 vs 1366 (+3 px).
- **Locales:** all 9 keep the English title and H1. /ar returns 404 and is not in hreflang.
- **axe:**
  - Desktop: `label-content-name-mismatch` serious ×1 (header `.right-2`), `heading-order` moderate ×1 ("Tax by bracket" h3), `region` moderate ×1.
  - Pixel 7: `color-contrast` serious ×2 on the ad label text.
  - Gate-run axe on main (MD + compare): `scrollable-region-focusable` serious ×1 (`.max-h-96`).

## Ads
Keep the reserved fixed-height slots below the tool, as they are now. Don't place one between the inputs and the result.
