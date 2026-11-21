Sent: 2026-11-21 09:19 ET

# Devices, locales, geo, a11y (matrix-results.json, 2026-11-21 EST)

## Devices
- All 10 profiles return 200, with the trial strip and the Quick Buy buttons above the fold.
- **Phones overflow to 442 px:**

  | Device | Viewport | scrollWidth |
  |---|---|---|
  | iPhone SE | 320 | 442 |
  | iPhone 14 Pro Max | 430 | 442 |
  | Pixel 7 | 412 | 442 (layout zoomed out) |
  | Galaxy S9+ | — | 442 |

  - Culprit: the "Contents page style" select trigger (nowrap, 409 px) and the "Column template" trigger (overflow.json).
- iPads and desktops: no overflow. CLS 0 where measured.
- **Desktop 1366×768:** the hero image fills the fold; the builder starts below it.

## Locales
- es, pt, fr, de, ja, hi, zh, ko and id all return 200 with the correct `lang`, and translated H1s ("Creador de Revistas", "Magazin-Ersteller", "雑誌作成ツール", "मैगज़ीन मेकर"…).
- These stay English: the title, meta, subtitle, "Premium application · 2 trial uses a day · $3 day pass or $9.99 a month", "Day pass $3 / Monthly $9.99", the breadcrumb "Premium Applications" and the builder.
- /ar returns 404.

## Geo
- All 6 contexts show $3 / $9.99. No consent banner seen.

## axe
- Desktop: label-content-name-mismatch (1), region (1).
- Pixel 7: color-contrast (2) on the ad label.
