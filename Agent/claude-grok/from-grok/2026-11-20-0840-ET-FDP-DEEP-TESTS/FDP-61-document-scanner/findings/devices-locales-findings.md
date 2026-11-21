Sent: 2026-11-21 13:02 ET

# Devices, locales, geo, a11y (FDP-61), checked against screenshots

- **Devices (10):** all 200.
  - Phones show "Ad-free: $3 day pass · $9.99/month" instead of Quick Buy buttons.
  - iPhone SE scrollWidth 329 at 320 (button + premium badge row).
  - Desktop 1366×768: the drop zone is below the fold (~1,150 px) under the hero and step strip.
- **Full flow on phones** (mobile.json): iPhone 13 WebKit and Pixel 7 work; Pixel 7 touch crop works.
- **Locales:** html lang correct, ltr. Translated: H1 (e.g. "Escáner de Documentos"), badges, trial strip, Quick Buy ("Compra rápida"). English: subtitle, Premium line, Day pass/Monthly, breadcrumb, controls, FAQ (es, ja screenshots). ja desktop 1369 px. /ar → 404 (expected).
- **Geo:** prices $3/$9.99 everywhere (USD). The EU consent banner is visible in the de-DE and fr-FR fold screenshots (the script flag said false; the screenshot wins). None elsewhere.
- **axe:** desktop label-content-name-mismatch (serious), region (moderate); Pixel 7 color-contrast (serious, ad caption ×2).
