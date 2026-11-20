Sent: 2026-11-20 08:40 ET

# FDP-09 Income Tax Calculator: devices, platforms, countries and languages

- **Run:** `run-matrix.js` from 2026-11-19 13:08:51 to 13:15:34 EST. Raw data: `json/matrix-results.json`.
- **Coverage:**
  - 10 device profiles: iPhone SE, iPhone 14 Pro Max, Pixel 7, Galaxy S9+, iPad Mini, iPad Pro 11 landscape, Desktop 1366/1920 Chromium, Firefox 1440 and WebKit 1440
  - 10 hreflang locales × Pixel 7 + desktop
  - 6 geo contexts (en-US, de-DE, fr-FR, hi-IN, ar-SA, ja-JP)
  - axe on desktop and Pixel 7

## PASS
- 200 on 10 of 10 profiles (WebKit desktop took 25 s, the others 6–9 s).
- All inputs use 16 px font on phones, so iOS doesn't zoom.
- The order on phones is inputs → result → Copy/Save/Print.
- No ad overlaps on any profile. Ads sit in static slots below the tool (y ≈ 1,560–2,340 px).
- CLS is 0–0.013.
- Geo: the same USD figures in every geo. The consent banner appears in de-DE and fr-FR only.

## FAIL / PARTIAL
- **iPhone SE (320 px):** horizontal overflow to 353 px. The culprits are a header button (right edge 329) and the "US-Specific" badge (right edge 353). On 320/375 px phones the income input starts at y ≈ 690–1030, below the first screen (P2).
- **Desktop ja:** 1369 vs 1366 (+3 px).
- **Locales:**
  - Only es is localized; its title includes "gratis" (P2 wording).
  - pt, fr, de, ja, hi, zh, ko and id keep the English title and description. Their H1 is the short "Income Tax Calculator" rather than the en H1 "2026 Income Tax Calculator — Federal, State and FICA".
  - /ar returns 404; it is not in hreflang (curl check). The matrix's /ar row is a config miss (relative URL), not a site failure.
- **axe:**
  - Desktop: `label-content-name-mismatch` serious ×1 (header `.right-2`), `region` moderate ×1.
  - Pixel 7: `color-contrast` serious ×2 on the ad label text.
  - In the gate run, axe on `main` found 0.
- **Small targets:** breadcrumb links are 20 px tall on phones (P2).

## Ads
Keep the reserved fixed-height slots below the tool, as they are now. Don't place one between the inputs and the result.
