Sent: 2026-11-21 02:24 ET

# FDP-36 Add Password to PDF: devices, locales, geo, axe (run-matrix.js, 2026-11-21 02:07:59 EST start)

All matrix contexts loaded at "0 remaining today" (display-only).
- **Devices (10, all 200):**
  - iPhone SE has 9 px overflow (shared `button.inline-flex…`, same as FDP-30–35). Others none.
  - Small targets: "Home" 39×20, One file / Several files 32 px tall on phones (P3).
- **Locales:** es, pt, fr, de, ja, hi, zh, ko, id → 200, html lang set, H1 translated, title/meta English, no "free" strings. ja desktop 3 px overflow. `/ar` 404.
- **Geo (6):** "$1", "$4.99" everywhere; no consent banner in headless.
- **axe:**
  - label-content-name-mismatch (serious, 1: the eye button `.right-2`)
  - region (moderate, 1)
  - Pixel 7 color-contrast (serious, 1: `.text-muted-foreground/50`)
  - Keep ad slots reserved; fix the contrast.
