Sent: 2026-11-21 00:40 ET

# FDP-31 UUID Generator: devices, locales, geo, a11y (run-matrix, 2026-11-21 00:21:34–00:34:38 EST)

Raw: `json/matrix-results.json`, `json/matrix.log`; screenshots in `screens/devices/`, `screens/locales/`, `screens/geo/`, `screens/a11y/`.

## Devices (10)
- All 10 loaded 200. **iPhone SE (320 px): 9 px horizontal overflow**, culprit a `button.inline-flex…` with right edge 329 px (same as FDP-30; looks like a shared header/action-row button). Other devices: none.
- Mobile small targets: Count input and Generate are 36 px tall; the Hyphens/Uppercase checkboxes are 24×24 px (below 44 px); breadcrumb 20 px; "Share this tool" 32 px. Tablets/desktop: favorites/share/add-to-home icons 16 px.
- Ads: slots keep reserved space; axe on Pixel 7 flags the ad caption contrast (2 × color-contrast, serious) — fix the caption colour, keep the slots.

## Locales (10 hreflang + /ar probe)
- en/es/pt/fr/de/ja/hi/zh/ko/id → 200; /ar → 404 (no ar hreflang).
- es: translated title/H1 ("Generador de UUID: hasta 1000 identificadores aleatorios por lote"; title "…en línea gratis…"), English body. The other 8 show the English title/H1/meta under their `lang`, self-canonical and hreflang.
- ja Desktop 1366: 3 px horizontal overflow (scrollWidth 1369).
- Locale pages' search placeholder says "Search 300+ tools…".

## Geo (6)
- en-US, de-DE, fr-FR, hi-IN, ar-SA, ja-JP: all 200, English, no prices. de/fr show the cookie consent banner. Output is locale-neutral (UUIDs), so nothing to localise in results.

## Accessibility (axe)
- Desktop: `label-content-name-mismatch` (serious, 1, `.right-2`), `region` (moderate, 1).
- Pixel 7: `color-contrast` (serious, 2) on the ad captions.
- Count has a proper label and `aria-describedby` to the message area; errors are `role=alert`; each copy icon has "Copy UUID n" (good). Keyboard order: breadcrumb → favorites → share → Count → Generate → Hyphens → Uppercase → Copy UUID 1…n → Copy All → video (`json/misc.json`). With 1,000 rows, keyboard users must tab through 1,000 copy buttons to reach Copy All (P3: put Copy All above the list).
