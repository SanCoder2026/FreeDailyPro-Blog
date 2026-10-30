Sent: 2026-10-30 11:22 ET

# B-0147 Catalog maker: labelled layout controls, templates, product links/QR
Priority: P2 · Estimated effort: S–M · Report: #110 · Source: QA sweep + live competitor fetch 2026-10-30 11:20 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Make the builder accessible and help sellers produce a catalog buyers can act on.

## Why
Title, company and the layout dropdowns have no accessible name (same pattern as L-208). Canva leads with templates. A PDF catalog with no way to order loses buyers.

## Who uses this
Small wholesalers and makers sending line sheets.

## Outcomes (ranked)
1. Label Catalog Title, Company Name, Currency, Columns, Page size and Accent colour. 2. 2–3 starter templates. 3. An optional URL per product, printed as a link and a small QR code.

## Constraints
Keep the CSV import behaviour (quoted commas, header detection) and the price validation.

## Test cases
get_by_label("Company Name") works. The CSV with "Widget, large" still parses into 2 rows → 4 pages. A product URL appears as a clickable link in the PDF.
