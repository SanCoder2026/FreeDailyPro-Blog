Sent: 2026-11-21 23:07 ET

# FDP-88 devices, locales, geo, a11y (matrix-results.json)

- **Devices:** 10/10 returned 200. iPhone SE scrollWidth is 329 vs 320 (9 px); the others are fine.
- **Locales:** 10 hreflang pages return 200; /ar returns 404.
  - **H1 "Flatten PDF", title, meta, subtitle, dropzone and FAQ are English in every locale.** Only the nav, breadcrumbs, the "never stored" chip and Quick Buy labels are translated (see `locale-de-desktop-1366x768-fold.jpg`). **P2.**
  - ja desktop overflows by 3 px.
- **Geo** (6 contexts): $1 / $4.99 everywhere, all 200.
- **Axe:**
  - Desktop: `label-content-name-mismatch` (serious, 1) + `region` (moderate).
  - Pixel 7: `color-contrast` ×2 (ad label, sitewide).
