Sent: 2026-11-21 03:55 ET

# FDP-41 OCR PDF: devices, locales, geo, accessibility (matrix 03:37–03:47 EST)

- **Devices (load and layout):** all returned 200: iPhone SE, iPhone 14 Pro Max, Pixel 7, Galaxy S9+, iPad Mini, iPad Pro 11 landscape, and Desktop 1366/1920 Chromium, 1440 Firefox, 1440 WebKit.
  - P3: iPhone SE has 9 px of horizontal overflow (329 vs 320). The culprit is a full-width `button.inline-flex…` (same as #40).
  - Small targets: the Home breadcrumb link is 20 px high; Share is 32 px.
- **OCR by engine:** Chromium PASS; Firefox PASS (11/11 K cases identical). Playwright WebKit crashed during OCR on desktop and on iPhone emulation. That's unverified on real Safari; see live findings.
- **Locales** (/es /pt /fr /de /ja /hi /zh /ko /id): all 200 with html lang set and LTR. The H1 is translated, but the title and meta stay English, and the tagline, chips and notes stay English (seen on /de).
  - Prices show as "1 $" / "4,99 $" on /de, which is a local format. That's fine.
  - P3: /ja has 3 px of overflow (1369 vs 1366).
  - /ar/tool/ocr-pdf returns 404 (no Arabic locale; hreflang doesn't list it, so this is consistent).
- **Geo** (locale + timezone emulation only, with the IP still in the US): en-US, de-DE, fr-FR, hi-IN, ar-SA and ja-JP all show $1 / $4.99 and English. No EU consent banner appeared for de-DE/fr-FR. That's an unverified absence, because the IP wasn't in the EU.
- **axe:**
  - Desktop: label-content-name-mismatch (serious, 1: `.right-2`) and region (moderate, 1).
  - Pixel 7: color-contrast (serious, 2), both on the small "Advertisement" caption under filled ad slots. Fix the caption contrast; the reserved slots stay as they are.
