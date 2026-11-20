Sent: 2026-11-20 08:40 ET

# Devices, locales, geo and a11y: Grammar Checker (FDP-13)

- **Matrix run:** 2026-11-19 14:14:38 → 14:21:55 EST, `scripts/run-matrix.js scripts/config.json`; raw data `json/matrix-results.json`; screens `screens/devices|locales|geo|a11y/`. Plus `scripts/gc-kbd.js` (14:16:33–14:16:53 EST, `json/kbd.json`, `screens/live/layout-*.png`).

## Devices (10 profiles, all HTTP 200)
| Profile | Engine | Load ms | Horizontal overflow | Notes |
|---|---|---|---|---|
| iPhone SE | WebKit | 7,632 | **yes, 9 px** (header button right=329 at 320 px; site-wide, seen on earlier tools) | English select's "Auto-detect" text renders very pale on a white control (`screens/devices/iphone-se-fold.png`); 4 small targets (breadcrumb Home 20 px tall, Check Grammar 36 px tall) |
| iPhone 14 Pro Max | WebKit | 8,626 | no | |
| Pixel 7 | Chromium | 24,581 | no | slow load in this run (ads); CLS 0.0003 |
| Galaxy S9+ | Chromium | 7,354 | no | 2 console errors (ads `no_div`) |
| iPad Mini / iPad Pro 11 | WebKit | 8,328 / 25,840 | no | |
| Desktop 1366 / 1920 Chromium | Chromium | ~6,300 | no | CLS ≈0.065 (below 0.1) |
| Desktop 1440 Firefox / WebKit | | 6,919 / 24,992 | no | |

- **First screen:** the input and Check Grammar are above the fold on every profile. On a 568–584 px phone the output starts at y≈577 after Check (`json/kbd.json`, iPhone SE: vh 584, outputTop 577), so the corrected text is just below the fold and the page does not scroll to it. On mobile an ad container sits right after the tool controls (y≈548 on iPhone SE) before the output area; keep ads in reserved slots **after** the results block, never between the button and the output.
- The input textarea is one line (42 px) until typed into: fine, but a taller default would signal "paste a paragraph".

## Accessibility
- axe (wcag2a/aa + best-practice) on `main` before Check: 0 violations. **After Check: 1 critical `label`** — the read-only output textarea has no label (`json/kbd.json` → `axeAfter`). The input textarea has only a placeholder (no `<label>`/aria-label; axe accepts the placeholder, but a visible label is better).
- Full-page axe (matrix): desktop `label-content-name-mismatch` (serious, `.right-2`, header search shortcut button) and `region` (moderate); Pixel 7 `color-contrast` (serious) on the "Advertisement" caption under ad slots.
- Keyboard: textarea → Tab → Check Grammar (focus ring visible) → English select → links; Enter runs Check. Focus stays on the button; **no aria-live/role=status** announces "N fixes made", so screen-reader users get no feedback.

## Locales (hreflang en + 9, and /ar probe)
- en, es, pt, fr, de, ja, hi, zh, ko, id: all 200 with the **English page under the locale's `lang`** (e.g. `lang="es"` with English text; title unchanged). ja desktop showed a horizontal overflow (scrollWidth 1369 at 1366).
- /ar/tool/grammar-checker: 404 (ar is not in hreflang; consistent).
- The tool is English-only by design, so the 9 locale URLs are English duplicates with a mismatched `lang`: either translate the page chrome and say "checks English text", or drop those hreflang alternates.

## Geo / browser-locale contexts (desktop)
- en-US, de-DE, fr-FR, hi-IN, ar-SA, ja-JP: all 200, `lang=en`, no prices shown, no trial strip. de-DE and fr-FR show the cookie banner ("We use cookies for analytics and, when ads are shown, advertising. The tools work either way.").
