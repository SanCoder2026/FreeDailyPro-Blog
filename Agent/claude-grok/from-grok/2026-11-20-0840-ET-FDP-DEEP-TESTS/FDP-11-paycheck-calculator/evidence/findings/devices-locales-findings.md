Sent: 2026-11-20 08:40 ET

# Devices, platforms, locales, geo and a11y: paycheck-calculator

- **Run:** `scripts/run-matrix.js scripts/config.json`, 2026-11-19 13:44:57–13:53:29 EST, plus `scripts/pc-kbd.js` at 13:42 EST. Results: `json/matrix-results.json`, `json/kbd.json`. Screens: `screens/devices|locales|geo|a11y|live`.

## Devices (10 profiles, Chromium / WebKit / Firefox)

| Device | Engine | Status | Horizontal overflow | CLS | Notes |
|---|---|---|---|---|---|
| iPhone SE (320) | WebKit | 200 | **Yes, 9 px** (header menu button, right = 329) | n/a | Result starts at y≈861, below the 568 px fold; the salary field is at y≈512 |
| iPhone 14 Pro Max | WebKit | 200 | No | n/a | |
| Pixel 7 | Chromium | 200 | No | 0 | Result at y≈799 of 839 |
| Galaxy S9+ | Chromium | 200 | No | 0.011 | |
| iPad Mini | WebKit | 200 | No | n/a | |
| iPad Pro 11 landscape | WebKit | 200 | No | n/a | |
| Desktop 1366×768 / 1920×1080 | Chromium | 200 | No | 0.015 / 0 | |
| Desktop 1440×900 | Firefox, WebKit | 200 | No | n/a | Firefox load 24 s (headless; one sample) |

No overlaps between ads and the tool. Ad containers sit below the tool on phones and to the side on wide desktops (reserved slots; keep it that way). Console errors are ad-script only (doubleclick frame access, adsbygoogle `no_div`); none from the tool. The 9 px overflow is the site header at 320 px (likely site-wide, not this tool).

## Keyboard and screen reader (`json/kbd.json`)

Tab order after the salary field: Filing status → Pay frequency → State → State tax rate → 401(k) → Health premium → HSA → Income Tax Calculator link → Copy result → Save as text → Print → video. Logical. **No aria-live or role=status on the result**, so screen-reader users get no update when an input changes. The Salary/Hourly tabs are a Radix tablist.

## axe (main)

- `aria-valid-attr-value` (critical) on the Salary/Hourly tab triggers: `aria-controls` points to `radix-…-content-salary`, which isn't in the DOM (desktop and Pixel 7, both tabs).
- `label-content-name-mismatch` (serious, 1, `.right-2`), `region` (moderate, 1) on desktop; `color-contrast` (serious, 1, `.text-muted-foreground/50`) on Pixel 7.

## Locales (hreflang + /ar)

| Locale | Status | Title / lang | Translated? |
|---|---|---|---|
| en | 200 | "Paycheck Calculator Online - Take-Home Pay" | n/a |
| es | 200 | "Calculadora de sueldo neto de EE. UU. en línea, gratis" | **Yes** (title, H1, meta; the title says "gratis") |
| pt, fr, de, ja, hi, zh, ko, id | 200 | English title, H1 and meta | **No** (English copies under locale URLs) |
| /ar | 404 | "Page Not Found" | Not in hreflang, so consistent |

## Geo (6 locale/time-zone contexts)

All 200, same USD prices ($1 / $4.99) and the same default result $2,368.94; number format en-US everywhere (US-only tool, so fine). No consent banner observed in any geo (headless; no EU IP, so unverified for real EU visitors). All loaded at "0 remaining today" (display-only).
