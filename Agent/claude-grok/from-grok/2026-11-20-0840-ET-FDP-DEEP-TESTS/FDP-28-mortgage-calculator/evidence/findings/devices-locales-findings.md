Sent: 2026-11-20 23:25 ET

# Devices, locales, geo, a11y: mortgage-calculator (matrix 2026-11-20 23:10–23:19 EST)

- **Devices:** iPhone SE, iPhone 14 Pro Max, Pixel 7, Galaxy S9+, iPad Mini, iPad Pro 11 landscape, Desktop Chromium 1366/1920, Firefox 1440, WebKit 1440. All 200.
  - Only iPhone SE overflows horizontally (scrollWidth 329 / 320; culprit `button.inline-flex…` right edge 329).
  - Inputs use a 16 px font on phones (no iOS zoom).
  - The monthly-payment card is above the fold on every device (Pixel 7 screenshot). The breakdown sits below about 20 inputs, so phones scroll a long way (doc height about 6,300–7,300 px).
  - Desktop uses a narrow single column (max-w-md) with wide empty margins (P2: two-column inputs/results on desktop).
- **Locales:**
  - es, pt, fr, de, ja, hi, zh, ko and id: 200, correct html lang, ltr, but everything is English.
  - ja desktop overflows by 3 px (1369 / 1366).
  - /ar → 404 (Page Not Found).
  - No "free" wording in the tool UI. The footer/outro wording is outside this tool.
- **Geo:** the EU consent banner text appears for de-DE and fr-FR ("We use cookies for analytics and, when ads are shown, advertising…"), not for US/IN/SA/JP. Prices are always USD (by design for a US mortgage tool).
- **axe:**
  - Desktop: label-content-name-mismatch (serious, 1, the `.right-2` floating button), heading-order (moderate, h3 "Recent calculations"), empty-table-header (minor, the 15/30 table's first th), region (moderate, 1).
  - Pixel 7: color-contrast (serious, 2, ad captions), empty-table-header, heading-order.
- **Keyboard:** logical tab order through all inputs. The date input takes 4 stops (segments), which is normal.
