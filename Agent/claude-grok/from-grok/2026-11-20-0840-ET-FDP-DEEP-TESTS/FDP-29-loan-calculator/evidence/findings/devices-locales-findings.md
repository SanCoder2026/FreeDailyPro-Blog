Sent: 2026-11-20 23:58 ET

# Devices, locales, geo, a11y: loan-calculator (matrix 2026-11-20 23:45–23:57 EST)

- **Devices:** iPhone SE, iPhone 14 Pro Max, Pixel 7, Galaxy S9+, iPad Mini, iPad Pro 11 landscape, Desktop Chromium 1366/1920, Firefox 1440, WebKit 1440. All 200.
- **iPhone SE overflows horizontally by 70 px** (scrollWidth 390 / 320). Culprits: the "Compare extra payments" table (right edge 404) and a `button.inline-flex…` (329). Other devices: none.
- Desktop uses a two-column layout (inputs left, result cards right), so the result is visible at once. On phones the result card follows the inputs.
- **Locales:** es, pt, fr, de, ja, hi, zh, ko and id are 200 with a foreign `lang`, but the UI is English. ja desktop overflows by 3 px (1369). /ar → 404.
- **Geo:** the EU consent banner shows for de-DE and fr-FR only. Currency is user-selectable (10 currencies, INR with en-IN grouping). The default stays USD regardless of locale or geo (P3: default by locale).
- **axe:**
  - Desktop: label-content-name-mismatch (serious, the `.right-2` floating button), heading-order (h3 in Compare extra payments), landmark-unique (two "How this was calculated" regions), region.
  - Pixel 7: color-contrast (serious, ad captions), heading-order, landmark-unique.
- **Keyboard:** logical order. Scenario inputs are announced by id ("ln-scn-b", "ln-scn-c") in focus order. Their aria-label is "Scenario 2: extra each month", so the id is what the script read. Fine.
