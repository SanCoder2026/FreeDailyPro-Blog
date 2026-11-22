Sent: 2026-11-21 22:51 ET

# FDP-87 devices, locales, geo, a11y (matrix-results.json, 22:36–22:44 ET)

- **Devices:** all 10 returned 200.
  - Overflow: iPhone SE only, scrollWidth 329 vs 320 (9 px).
  - Load times 6–25 s; the iPad Pro / Firefox / WebKit desktop runs were slow on the box.
- **Locales:** es, pt, fr, de, ja, hi, zh, ko and id all return 200 with self hreflang; /ar returns 404 (not declared, fine).
  - The H1 is translated (e.g. de "PDF Schwärzen", ja "PDF情報削除", fr "Caviarder PDF").
  - The `<title>` stays "Redact a PDF Online - Permanently Remove Content | FreeDailyPro" in every locale, and the meta description is English.
  - The subtitle, the dropzone and every tool control are English (see `locale-de-desktop-1366x768-fold.jpg`). **P2.**
  - ja desktop overflows by 3 px.
- **Geo** (en-US, de-DE, fr-FR, hi-IN, ar-SA, ja-JP): prices $1 / $4.99 everywhere. A consent banner appears for de and fr. The html lang is en.
- **Axe:**
  - Desktop: `label-content-name-mismatch` (serious, 1, `.right-2`) + `region` (moderate).
  - Pixel 7: `color-contrast` (ad label, sitewide).
- **Console:** AdSense `no_div` errors, and "Permissions policy violation: unload" (sitewide).
