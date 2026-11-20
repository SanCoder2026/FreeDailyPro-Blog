Sent: 2026-11-20 08:40 ET

# Devices, platforms, locales, geo and a11y: unit-converter

- **Run:** `scripts/run-matrix.js scripts/config.json`, 2026-11-19 14:02:18–14:08:32 EST, plus `scripts/uc-kbd.js` at 14:01 EST. Results: `json/matrix-results.json`, `json/kbd.json`. Screens: `screens/devices|locales|geo|a11y|live`.

## Devices (10 profiles)

| Device | Engine | Status | Horizontal overflow | CLS | Notes |
|---|---|---|---|---|---|
| iPhone SE (320) | WebKit | 200 | **9 px** (header menu button, right = 329; same as #11, site-wide header) | n/a | 15 tabs wrap to 156 px; Value at y≈644, answer at y≈818: both below the fold (P1) |
| iPhone 14 Pro Max | WebKit | 200 | No | n/a | |
| Pixel 7 | Chromium | 200 | No | 0 | Tabs 126 px; answer at y≈669 of 839 |
| Galaxy S9+ | Chromium | 200 | No | 0 | |
| iPad Mini, iPad Pro 11 landscape | WebKit | 200 | No | n/a | |
| Desktop 1366×768, 1920×1080 | Chromium | 200 | No | 0 / 0.011 | The 15 tabs wrap to 2 rows; the second row (Fuel economy, Cooking) is stretched across the full width (cosmetic) |
| Desktop 1440×900 | Firefox, WebKit | 200 | No | n/a | Load ~25 s headless (one sample each) |

No ad overlaps with the tool. Console errors are ad-script only (`adsbygoogle no_div`).

## Keyboard and screen reader (`json/kbd.json`)

- **Tab order:** From → Value → Swap → To, then the popular-conversion links.
- Radix tabs and selects work by keyboard.
- **No aria-live or role=status:** an sr-only sentence "1 milligram = 0.001 gram" exists but isn't announced (P2).

## axe (main)

- **`aria-valid-attr-value`** (critical) on the active tab trigger: aria-controls points to a missing panel. Shared Radix pattern (seen in #11).
- **Desktop:** `label-content-name-mismatch` (serious, 1) and `region` (moderate, 1).

## Locales

| Locale | Status | lang | Content |
|---|---|---|---|
| en | 200 | en | English |
| es | 200 | es | **Translated** (title "Convertidor de unidades gratis: métrico, EE. UU. y UK") |
| pt, fr, de, ja, hi, zh, ko, id | 200 | pt/fr/de/ja/hi/zh/ko/id | **English content under a non-English `lang`** (P2) |
| /ar | 404 | en | Not in hreflang (consistent) |

## Geo / browser locale (6 contexts)

- All return 200. No prices or trial strip are shown on this tool (ungated). No consent banner was observed (headless, no EU IP, so unverified for real EU visitors).
- **Number formatting follows the browser locale:** en-US/hi-IN/ja-JP "0.001"; de-DE/fr-FR "0,001".
- **ar-SA:**
  - The English page shows results in **Arabic-Indic digits** (٠٫٠٠١, ١٬٠٠٠) next to a Latin-digit input and labels (`screens/geo/geo-ar-sa-asia-riyadh-desktop-1366x768-fold.png`).
  - Copy and Save carry those digits too.
  - Consider formatting numbers in the page language rather than the browser locale, or using `numberingSystem: 'latn'` (P2).
