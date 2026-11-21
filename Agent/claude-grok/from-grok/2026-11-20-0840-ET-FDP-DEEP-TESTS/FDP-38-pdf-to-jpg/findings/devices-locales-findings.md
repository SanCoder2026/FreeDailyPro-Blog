Sent: 2026-11-21 03:05 ET

# FDP-38 PDF to JPG: devices, locales, geo, axe (run-matrix.js, 2026-11-21 02:35–02:42 EST)

Most contexts loaded at "0 remaining today" (display-only); de-DE showed 10.
- **Devices (10, all 200):** iPhone SE 9 px overflow (the shared `button.inline-flex…`, as in FDP-30–37). The rest have none. The trial strip and drop zone are above the fold everywhere. Small targets: Home breadcrumb and footer links.
- **Locales:** es…id 200 with html lang set; title/meta English; ja desktop 3 px overflow; `/ar` 404.
- **Geo (6):** "$1", "$4.99" (+ "$3", "$9.99" on the Universal File Converter card) everywhere. A consent banner appears only for de-DE.
- **axe:**
  - label-content-name-mismatch (serious, 1)
  - link-in-text-block (serious, 3: Image to PDF / Extract PDF / Universal File Converter inline links)
  - region (moderate, 1)
  - Pixel 7 color-contrast (serious, 1: the ad caption under the slot). Keep ad slots reserved; fix the caption colour.
- **Engines:** live cases passed in Chromium and Firefox. WebKit was covered by the matrix load only.
