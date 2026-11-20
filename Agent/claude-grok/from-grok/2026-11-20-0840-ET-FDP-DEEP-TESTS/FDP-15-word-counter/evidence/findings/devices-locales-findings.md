Sent: 2026-11-20 08:40 ET

# Devices, locales, geo and a11y: Word & Character Counter (FDP-15)

- **Matrix:** 2026-11-19 ≈14:49 → 14:55:30 EST, `scripts/run-matrix.js scripts/config.json`. Raw data `json/matrix-results.json`; screens in `screens/devices|locales|geo|a11y/`.
- **Phone layout:** `scripts/wc-gate-kbd.js` (`json/gate-kbd.json`, `screens/live/layout-*.png`).

## Devices
| Profile | Status | Notes |
|---|---|---|
| iPhone SE (WebKit) | 200, 7,470 ms | 9 px header overflow (site-wide); first ad slot at y≈1,555 |
| iPhone 14 Pro Max (WebKit) | matrix run: "Page crashed" (harness) | Retried 3× at 14:55:46 EST: 200, counts correct each time (`json/webkit-retry.json`). Not a site defect. |
| Pixel 7 / Galaxy S9+ | 200 | CLS 0 |
| iPad Mini / iPad Pro 11 | 200 | ad slots after the tool (y≈1,085–1,101) |
| Desktop 1366 / 1920 Chromium | 200 | CLS 0 |
| Desktop 1440 Firefox / WebKit | 200 | 160×600 side-rail ad at x=1,280 beside the tool (not between controls) |

- **Text box:** renders about 38 px tall (one line) at idle on desktop (matrix `inputs` h=38; `screens/devices/desktop-1440x900-firefox-fold.png`). The component asks for `min-h-[200px]`, but the computed min-height is 0px with `field-sizing: content` (checked 14:57 EST). It grows as text is typed (162 px on iPhone SE with the sample). P2: a tall empty box signals "paste here".
- **iPhone SE with the sample typed:** the stats grid starts at y≈612 against a 584 px viewport, so the Words count sits just below the fold (worse with the on-screen keyboard). Pixel 7: stats at y≈490 (visible).
- A compact sticky "words · characters" line on phones would fix this.

## Accessibility
- **Full-page axe (matrix):**
  - Desktop: `label-content-name-mismatch` (serious, header search button) and `region` (moderate).
  - Pixel 7: `color-contrast` (serious) on the ad captions.
- **Tool `main`:** 12 serious color-contrast nodes on the green "OK: N left" platform texts after typing. No aria-live for the counts.

## Locales
- es: translated title, meta and H1 (with "gratis"); English body.
- pt, fr, de, ja, hi, zh, ko, id: English under a foreign `lang`. ja desktop shows a horizontal overflow.
- /ar: 404.

## Geo
- en-US, de-DE, fr-FR, hi-IN, ar-SA, ja-JP: all 200, `lang=en`, identical. Cookie banner on de/fr.
