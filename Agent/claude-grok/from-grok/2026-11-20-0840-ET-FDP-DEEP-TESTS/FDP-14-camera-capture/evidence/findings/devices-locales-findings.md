Sent: 2026-11-20 08:40 ET

# Devices, locales, geo and a11y: Camera Capture (FDP-14)

- **Matrix:** 2026-11-19 14:31:52 → 14:39:39 EST, `scripts/run-matrix.js scripts/config.json`. Raw data: `json/matrix-results.json`. Screens: `screens/devices|locales|geo|a11y/`. Phone flow: `scripts/cc-kbd.js` (14:33:18–14:33:48 EST, `json/kbd.json`, `screens/live/layout-*.png`).

## Devices (10 profiles, all HTTP 200)
| Profile | Load ms | Overflow | Notes |
|---|---|---|---|
| iPhone SE (WebKit, 320×568) | 7,883 | **9 px** (header button, right=329; site-wide) | Start Camera is below the fold (see below) |
| iPhone 14 Pro Max | 8,582 | no | |
| Pixel 7 | 7,021 | no | CLS 0 |
| Galaxy S9+ | 24,805 | no | 4 console errors (ads) |
| iPad Mini / iPad Pro 11 | 8,199 / 8,382 | no | |
| Desktop 1366 / 1920 Chromium | ~6,000 | no | CLS ≈0.015–0.018 |
| Desktop 1440 Firefox / WebKit | 7,693 / 24,691 | no | |

## First screen on phones (P1)
- **iPhone SE:** the fold shows the header, title, badges, the trial line, "Ad-free: $1 day pass · $4.99/month" and the top of the "How it works" panel. **Start Camera is at y≈828**, well below the 568 px fold (`screens/devices/iphone-se-fold.png`, `json/kbd.json`).
- **iPhone SE after Start:** the preview starts at y≈616 and Capture is at y≈795, so the user must scroll to see themselves and to shoot.
- **Pixel 7:** Start Camera at y≈762 (the fold is 839), so it is just visible. The preview is at y≈570 and Capture at y≈801.
- **After Capture (iPhone SE):** Download Full Photo at y≈827, Crop Selection/Retake at y≈963, Download Crop/Copy at y≈1187. That is three screens of scrolling to finish.
- For a "take a photo online" query on a phone, the camera button should be on the first screen. The steps panel and trial and price lines come first today.

## Accessibility
- Full-page axe (matrix): desktop `label-content-name-mismatch` (serious, header search button) and `region` (moderate). Pixel 7: `color-contrast` (serious, the 50%-opacity ad caption).
- Tool-specific results (main, `json/kbd.json`): `image-alt` critical after Capture; focus lost after Start/Capture; crop not keyboard-operable; camera picker unnamed. The steps panel is aria-live polite (good).

## Locales (hreflang en + 9, and /ar probe)
- All 9 alternates return 200 with the English page under the locale `lang`. ja desktop has a horizontal overflow. /ar returns 404 (not in hreflang).

## Geo / browser-locale contexts (desktop)
- en-US, de-DE, fr-FR, hi-IN, ar-SA and ja-JP: all 200, `lang=en`, the same trial line "Trial: 10 uses/day · 0 remaining today" and USD prices. de-DE and fr-FR show the cookie banner.

## Ads
- Idle layout: the first ad container is at y≈1248 on iPhone SE (below Start Camera at y≈828) and y≈912 on iPhone 14 Pro Max. The position after Capture was not measured. Keep ads in reserved fixed-height slots after the result buttons. Never put them between the preview and Capture, or between the crop and its download buttons.
