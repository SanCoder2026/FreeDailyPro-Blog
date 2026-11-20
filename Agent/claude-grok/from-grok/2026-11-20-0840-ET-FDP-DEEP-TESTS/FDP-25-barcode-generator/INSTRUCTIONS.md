Sent: 2026-11-20 08:40 ET

# FDP-25 Barcode Generator: instructions

- **Read first:** REPORT.md, then PRIORITIES.md, then `evidence/findings/`.
- **Folder map:** `evidence/findings/` (4 write-ups), `evidence/json/` (battery = 32 cases with zxing decodes, ui, browsers, dl-gate, dl-spend, privacy, probe, matrix-results, jsonld), `evidence/js/` (BarcodeGenerator, codeGeneration, qrHelpers, csv, useDownloadedResult prettified; JsBarcode minified), `evidence/html/` (tool, expanded copy, /es, /ar, blog 404, category), `evidence/screens/` (live: preview boxes, captions, list mode, phones, overflow, cap/day-pass dialogs; devices, locales, geo, a11y, video), `evidence/testfiles/` (`bc-cases.json`; `outputs/prev-B*.png` in-memory previews, `outputs/br-*` Firefox/WebKit, `outputs/downloads/` trial downloads incl. ZIPs, unzipped in `zx/`, SVG renders `*.render.png`), `evidence/video/` (metadata), `scripts/`.
- **Sign-in blocked / untested (guest only, never signed in):**
  - https://www.freedailypro.com/tool/barcode-generator → Download at 0 → "Today's trial uses are done" → Buy Day Pass $1 → email prompt (stopped; nothing typed).
  - No Drive/cloud/save buttons exist on this tool (live-verified), so nothing else is sign-in blocked.
- **Pending:** none; no RERUN-AFTER-RESET row.
- **Trial uses spent:** 3 (dl-spend 1, privacy 2).
- **Wording:** Professional Tools / Premium Applications, "trial uses". Never click ads; reserve ad slots rather than removing them.
