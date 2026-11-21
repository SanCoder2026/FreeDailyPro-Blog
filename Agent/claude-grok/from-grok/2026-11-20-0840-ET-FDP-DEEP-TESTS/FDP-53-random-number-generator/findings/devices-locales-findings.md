Sent: 2026-11-21 09:47 ET

# Devices, locales, geo, a11y (matrix-results.json)

- **Devices:** all 10 return 200.
  - Phones: no overflow, except iPhone SE (scrollWidth 329 on a 320 px viewport; culprit is a header button, site-wide).
  - CLS 0–0.045.
  - 15–19 small targets per device (mode buttons 32 px high, switches 32×18).
- **Locales:** es, pt, fr, de, ja, hi, zh, ko and id all return 200 with the correct `lang`.
  - Title, meta, H1, subtitle and all controls are English. Only the breadcrumb and badge are translated.
  - /ar returns 404.
- **Geo:** 6 contexts, all English, with no prices on the page.
  - The EU consent banner ("We use cookies… Accept all / Reject non-essential / Choose") is visible for de-DE and fr-FR, and not for the others.
  - The matrix `consent` flag read false. The screenshots are authoritative.
- **axe:**
  - Desktop: label-content-name-mismatch (1, serious), region (1).
  - Pixel 7: none.
