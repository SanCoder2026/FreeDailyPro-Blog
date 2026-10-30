Sent: 2026-10-30 15:13 ET

# B-0288 Catalog Maker: spreadsheet import, photo matching and a stronger snippet
Priority: P2 · Estimated effort: M · Report: QA-REPORT-154 · Source: live probe 2026-10-30 ~15:12 ET (headless, logged out, 1280/390 px), GSC Top 50 pages (analytics raw file), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let a small seller go from the product spreadsheet they already have to a shareable catalog PDF without retyping.

## Why
GSC: 4 clicks / 379 impressions / 1.1% CTR / position 61.4 — the page ranks too low to be seen; the snippet and on-page depth need work.
Checked on the live page (15:12 ET): manual product rows (name, SKU, price, minimum order, category, description, photo), "Paste CSV" and "Import CSV file", and layout controls for currency, columns, page size, accent colour, cover page, price list page and contents page. Earlier run verified CSV quoted-comma import and a 4-page build (L-215).
Checked on the live page: the import accepts CSV paste or a CSV file only; no XLSX or Google Sheets option among the controls. Photos are added per product ("Photos are added per product above").
Competitors (live search): CatalogLeaf and Katalog import XLSX and match photos by filename or product code; Katalog offers 42 templates and an "update by key" re-import; Tendeta imports a public Google Sheet; CatalogLeaf offers Compact/Standard/HD file sizes.
FreeDailyPro: template styles beyond columns/accent colour and a PDF size option — unverified absence (only the default layout panel was seen; dropdown contents not opened); confirm before building.
Several layout controls have no accessible name (B-0155 / L-215). Ad text shows inside page copy ("Read Economics") → L-004. /es title served in English → L-189.

## Who uses this
Small wholesalers, makers and shop owners sending a line sheet or price catalog to buyers.

## Outcomes (ranked)
1. Import XLSX as well as CSV, with a column-mapping step.
2. Bulk photo upload matched to products by filename = SKU.
3. Snippet and on-page FAQ as below; /es localised.
4. Label the layout controls (B-0155).

## SEO
- Now: title "Create a Product Catalog PDF Online | FreeDailyPro" (50); meta 120 (under 140); H1 "Catalog Maker"
- Keywords: product catalog maker, catalog PDF from CSV, line sheet maker, price list maker
- Suggested Title: "Product Catalog Maker: CSV to PDF Catalog | FreeDailyPro" (56)
- Suggested Meta: "Build a product catalog PDF from a CSV or by hand: photos, SKUs, prices, cover page, price list and a contents page with page numbers, made in your browser." (156)
- Suggested H1: "Product Catalog Maker – CSV or Manual to PDF"
- FAQ: Can I import from Excel? · How do I add photos for many products? · Does it make a price list and contents page? · Which page sizes?

## Constraints
Download gating unchanged. Keep CSV header auto-detection and price validation.

## Test cases
1. CSV with a quoted comma in a description → one product, text intact (regression).
2. XLSX with columns Name, SKU, Price, Category → mapped and imported.
3. 10 photos named by SKU → each attached to the right product.
4. Build with cover + price list + contents → contents page numbers match pages.
5. Every layout control has an accessible name; title ≤60, meta 140–160; 390 px no overflow.
