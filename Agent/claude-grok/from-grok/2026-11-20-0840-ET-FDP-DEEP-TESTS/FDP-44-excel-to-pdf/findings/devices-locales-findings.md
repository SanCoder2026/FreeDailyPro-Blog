Sent: 2026-11-21 05:21 ET

# FDP-44: devices, locales, geo, axe (matrix-results.json, 2026-11-21 EST)

- **Devices (10):**
  - All return 200, and the trial strip, drop zone and result area are visible on every device.
  - **iPhone SE:** 9 px horizontal overflow from a button (right edge 329 of 320). /ja desktop has 3 px.
  - Small targets: Home breadcrumb, "Share this tool", Quick Buy on tablet/desktop.
  - CLS ≤ 0.037.
- **Locales (10 + /ar probe):** all 200 with translated H1s; title and meta stay English. /ar is 404 (hreflang doesn't list it, so this is fine).
- **Geo (6):** USD prices everywhere ($1, $4.99, $3, $9.99). A consent banner shows for de-DE and fr-FR only.
- **axe:**
  - Desktop: label-content-name-mismatch (serious ×1, `.right-2`), region (moderate).
  - Pixel 7: colour-contrast ×2 on the ad caption. Keep the reserved ad slots and raise the caption contrast.
- **Ads:** in-flow, reserved containers; no overlap with the tool. Never clicked.
