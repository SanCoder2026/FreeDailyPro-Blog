Sent: 2026-11-21 04:17 ET

# FDP-42 Find & Replace: devices, locales, geo, accessibility (matrix 04:03–04:12 EST)

- **Devices:** all returned 200: iPhone SE, iPhone 14 Pro Max, Pixel 7, Galaxy S9+, iPad Mini, iPad Pro 11 landscape, and Desktop 1366/1920 Chromium, 1440 Firefox, 1440 WebKit.
  - P3: iPhone SE has 9 px of horizontal overflow (329 vs 320), from a full-width `button.inline-flex…` (same as #40/#41).
- **Engines:** Firefox and Playwright WebKit gave the same results as Chromium on 10 key cases, including .docx and the 6.4 MB file.
- **Locales** (/es /pt /fr /de /ja /hi /zh /ko /id): all 200 with html lang set and LTR.
  - P3: the title, meta and **H1 "Find & Replace"** stay English everywhere, and so do the tool UI strings (seen on /de).
  - /ja has 3 px of overflow; /ar returns 404.
- **Geo** (locale + timezone emulation, with a US IP): all 200. No prices shown (this page has no pass offer). No EU consent banner for de-DE/fr-FR, which is an unverified absence because the IP wasn't in the EU.
- **axe:**
  - Desktop: label-content-name-mismatch (serious, 1: `.right-2`) and region (moderate, 1).
  - Pixel 7: color-contrast (serious, 2) on the small "Advertisement" caption under filled ad slots. Fix the caption contrast; the reserved slots stay as they are.
