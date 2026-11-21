Sent: 2026-11-21 16:53 ET

# FDP-73 reproduce

1. **0 → 2/2 (check):** guest window with uses left → https://www.freedailypro.com/tool/catalog-maker → title "Spring 2026 Product Catalog", 2 products (Blue Mug 12.50, Clay Vase 34) → Build Catalog → Download (1 `usage.log` POST; the strip shows 0 remaining). Download again (free, correct). Edit → price 13.00 → Build → Download → the cap dialog opens.
2. **Text price:** Product 1 price "Ask for quote" → "Enter a number, like 12.50", Build disabled. Or Import CSV `testfiles/unicode.csv` (row 5 "Call for price").
3. **Blank barcode page:** Combine files → add `sheet-letter-2p.pdf` → Back page code type "Real Barcode" → format EAN-13 → value 12345 → Assemble → "Catalog assembled!". The last page of the PDF is blank; the console shows "Couldn't generate a barcode: EAN-13 needs 12 digits…".
4. **WebP in Combine:** add `sheet-letter-2p.pdf` + `lamp.webp` → Assemble → toast "lamp.webp isn't a supported file type…", no catalog.
5. **One row per page:** Import CSV `linesheet-24.csv` → title → Build → 15 pages, 2 cards per product page.
