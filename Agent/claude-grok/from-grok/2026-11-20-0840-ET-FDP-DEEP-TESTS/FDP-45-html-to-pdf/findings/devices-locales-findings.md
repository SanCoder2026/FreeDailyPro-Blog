Sent: 2026-11-21 06:06 ET

# FDP-45: devices, locales, geo, axe (matrix-results.json, 2026-11-21 EST)

- **Devices (10):**
  - All return 200.
  - **iPhone SE:** 9 px horizontal overflow (a button, right edge 329 of 320). /ja desktop has 3 px.
  - Small targets on mobile: Home crumb, Open from Google Drive, the Page size select and the two checkboxes.
  - CLS ≤ 0.015.
- **Locales:** all 10 return 200 with translated H1s; titles and meta stay English. /ar is 404.
- **Geo (6):** USD everywhere.
- **axe:**
  - Desktop: label-content-name-mismatch (serious ×1, the site-wide `.right-2`), region (moderate).
  - Pixel 7: clean.
  - Note: the Margin input's visible label "Margin (mm)" differs from its aria-label "Margin in millimetres" (voice-control users saying "Margin mm" may miss it; P3).
- **Ads:** in-flow reserved containers; no overlap with the tool; never clicked.
- **Lookalike ad (P2):** in the Firefox run (screens/cases/S08-firefox.png), the in-flow slot right under "Convert to PDF" served a creative reading "Start Download (Free) … Add Extension to Firefox". A user waiting for the real Download button could click it. Never clicked. Keep the reserved slot; block deceptive download/extension creatives in AdSense and keep spacing from the action buttons.
