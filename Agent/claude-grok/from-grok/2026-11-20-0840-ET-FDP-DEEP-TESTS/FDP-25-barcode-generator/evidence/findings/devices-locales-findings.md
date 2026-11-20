Sent: 2026-11-20 08:40 ET

# FDP-25 Barcode Generator: devices, locales, geo

- **Matrix (18:23–18:30 EST, `json/matrix-results.json`):** 10 device profiles all 200, no horizontal overflow on load. 10 locales 200 (/es, /pt, /fr, /de, /ja, /hi, /zh, /ko, /id translated; console noise only ads `no_div` / unload policy). ja desktop 3 px overflow (site-wide). /ar 404 (not in hreflang — expected). Geo: prices $1 / $4.99 in all 6; consent banner in de-DE and fr-FR.
- **P2 – phone layout breaks after choosing Code 128:** the Format trigger does not truncate its label "Code 128 (letters, numbers and symbols, no accents)", so it grows to ≈453 px and the whole page scrolls sideways: iPhone 13 WebKit 390 → 469 px, Pixel 7 412 → 471, iPhone SE 320 → 470 (`screens/live/overflow-iphone13-webkit.png`, `json/browsers.json`). Code 128 is the first item in the list. Other formats' labels fit.
- Preview canvas scales to width on phones (324×89 on iPhone 13) — readable.
