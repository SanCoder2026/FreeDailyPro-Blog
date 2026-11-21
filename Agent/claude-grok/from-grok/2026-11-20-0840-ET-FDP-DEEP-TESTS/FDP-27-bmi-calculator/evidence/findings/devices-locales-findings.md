Sent: 2026-11-20 23:05 ET

# FDP-27 BMI Calculator: devices, locales, geo, accessibility

Matrix: `scripts/run-matrix.js` + `scripts/config.json`, 2026-11-20 22:46–22:55 EST (`evidence/json/matrix-results.json`, screenshots in `evidence/screens/devices|locales|geo|a11y`). Page loads and typing only; no exports, ads never clicked.

## Devices (10 profiles, all HTTP 200)
| Profile | Engine | Horizontal overflow | Result above fold | Notes |
|---|---|---|---|---|
| iPhone SE 320×568 | WebKit | **yes (329 > 320)**, header button | no (result at y≈983) | H1 wraps to 6 lines; inputs 16 px (no iOS zoom) |
| iPhone 14 Pro Max | WebKit | no | no | |
| Pixel 7 | Chromium | no | yes | |
| Galaxy S9+ | Chromium | no | no | |
| iPad Mini / iPad Pro 11 landscape | WebKit | no | yes | |
| Desktop 1366 / 1920 Chromium, 1440 Firefox, 1440 WebKit | — | no | yes | CLS 0 where measured |

Phones: the result card sits below the 4 inputs and the Asian checkbox, so it can't be seen while typing (P2: show a sticky mini result, or put the result first on mobile). The 320 px overflow is the shared header (seen on earlier tools too).

## Locales (en + 9 hreflang + /ar probe; Pixel 7 and desktop)
- All 200 except **/ar 404** (not in hreflang).
- `html lang` matches the locale; `dir=ltr` everywhere (no RTL page exists).
- **Translated content: es only** (title, meta, H1, breadcrumb). Its title says "gratis". The tool UI ("Weight (kg)", "Your BMI", "Normal", WHO table, FAQ) is English in every locale. pt/fr/de/ja/hi/zh/ko/id use the English title and description, and their H1 is the short "BMI Calculator". The header chrome is translated ("Kategorie", "Für Ihre Arbeit"); the badge "Ihre Dateien werden niemals gespeichert" (files) is translated but wrong for a calculator.
- Number formats: results always use en-US "24.2". Input accepts "70,5" (B23), which helps de/fr/es users. No currency on the page. No date fields.
- ja desktop: 3 px horizontal overflow (1369 > 1366).

## Geo (en-US baseline, de-DE, fr-FR, hi-IN, ar-SA, ja-JP)
- Same English page; `htmlLang` en (geo does not switch the locale).
- **EU consent banner shown for de-DE and fr-FR** ("We use cookies for analytics and, when ads are shown, advertising…"); none for US/IN/SA/JP. Not clicked.
- No prices on the page in any geo (no strip, no pass buttons).

## Accessibility (axe-core, desktop 1366 and Pixel 7)
- serious: `label-content-name-mismatch` (1, `.right-2`); Pixel 7: `color-contrast` (2, the ad-slot caption text).
- moderate: `heading-order` (the WHO h3 before any h2), `region` (1).
- The gauge has `role=img` with a full sentence label and a sr-only figcaption (good). Measure errors are plain `<p>` (not `role=alert`); the age and target errors are `role=alert`.
- Keyboard: every control is reachable in order (see live findings §6). The WHO table scroll region is focusable.
