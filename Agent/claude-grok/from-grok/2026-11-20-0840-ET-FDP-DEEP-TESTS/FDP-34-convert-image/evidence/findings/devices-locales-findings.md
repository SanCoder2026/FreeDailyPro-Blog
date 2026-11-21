Sent: 2026-11-21 01:50 ET

# FDP-34 Convert Image Format: devices, locales, geo, axe (run-matrix.js, 2026-11-21 01:25:28–01:34:04 EST)

All matrix contexts loaded at "0 remaining today" (display-only).

## Devices (10, all 200)
- iPhone SE: 329 px on a 320 px viewport (9 px overflow; shared `button.inline-flex…`, same as FDP-30–33) (P3). Others none.
- Small targets: breadcrumb "Home" ≈39×20; "Convert several images at once (ZIP)" 32 px tall and Drive/camera buttons 36 px on phones; 16 px icons and 84×28 "Quick Buy" on tablet/desktop (P3).
- Clean on Chromium, Firefox, WebKit. Screens `screens/devices/`.

## Locales (11 incl. /ar probe)
- es, pt, fr, de, ja, hi, zh, ko, id → 200; H1 translated client-side from the old name "Convert Formats"; title English; headings English. ja desktop 1368 px on 1366 (2 px). `/ar` 404.

## Geo (6)
- Prices "$1", "$4.99" (and Document Scanner "$3", "$9.99") in every context; no consent banner in headless.

## axe
- Page load: label-content-name-mismatch (serious, 1), link-in-text-block (serious, 4: "Which tool should I use?" links), region (moderate, 1); Pixel 7 ad-caption color-contrast (serious, 2) — keep ad slots, fix caption colour.
- Loaded state (`json/axe-loaded.json`): Quality slider has no accessible name (aria-input-field-name, serious).
