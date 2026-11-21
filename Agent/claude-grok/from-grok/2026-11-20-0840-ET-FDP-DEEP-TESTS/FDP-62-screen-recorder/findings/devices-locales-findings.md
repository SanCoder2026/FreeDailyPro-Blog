Sent: 2026-11-21 13:20 ET

# Devices, locales, geo, a11y (FDP-62), checked against screenshots

- **Devices:** Chromium/Firefox rows 200. Galaxy S9+ fine. Desktop: the tool is above the fold. All WebKit rows (iPhone SE, iPhone 14 Pro Max, iPad Mini, iPad Pro, Desktop WebKit) crashed at load in Playwright's Linux WebKit — env (`enumerateDevices`), see px62-wk2.js. Real Safari check needed.
- **Locales:** html lang correct, ltr. es: H1 "Grabador de Pantalla", breadcrumb "Herramientas de Video", strip and "Compra rápida" translated; subtitle, Premium line, toggles, Start Recording, FAQ English. ja desktop 1369 px. /ar → 404 (expected).
- **Geo:** $3/$9.99 everywhere. EU consent banner visible in de-DE/fr-FR fold screenshots.
- **axe:** desktop label-content-name-mismatch (serious), region (moderate); Pixel 7 color-contrast (ad caption).
