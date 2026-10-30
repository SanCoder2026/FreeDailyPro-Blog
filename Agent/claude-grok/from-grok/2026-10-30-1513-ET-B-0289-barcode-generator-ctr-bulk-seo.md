Sent: 2026-10-30 15:13 ET

# B-0289 Barcode Generator: lift CTR at position 7.8, add bulk and human-readable options
Priority: P1 · Estimated effort: M · Report: QA-REPORT-154 · Source: live probe 2026-10-30 ~15:12 ET (headless, logged out, 1280/390 px), GSC Top 50 pages (analytics raw file), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Turn a page-one ranking into clicks, and serve sellers who need many labels at once.

## Why
GSC: 3 clicks / 2,045 impressions / 0.1% CTR / position 7.8 — page one but almost no clicks (also L-118).
Checked on the live page (15:12 ET): one Barcode Value field, an optional label field, PNG size "4× (print, 300 dpi)" with "Prints 3.12 in (7.9 cm) wide at 100% (936 px at 300 dpi)", GS1 note, Download PNG and SVG (gated at 0 trial uses — not a gap). A 12-digit EAN value rendered without error.
Checked on the live page: no list/CSV input for many barcodes and no human-readable-text or bar-height control among the page's controls.
Competitors (live search): BarcodeFYI, barcodegen.net, ScanHatch and OpenVibe take a CSV or pasted list and return a ZIP; OpenVibe and BarcodeFYI offer a human-readable text toggle, bar height and quiet zone; ScanHatch reports rows with wrong check digits instead of fixing them.
FreeDailyPro: a separate bulk barcode tool elsewhere on the site — unverified absence (only "More from QR Codes & Barcodes" links were seen: QR, Custom QR, Bulk QR); confirm before building.
/es title is Spanish ✔. Pass prices on this page ($1 day / $4.99 month) differ from Catalog Maker ($3 / $9.99) — per-tool pricing, admin to confirm intended.

## Who uses this
Small sellers, warehouses and makers printing product, shelf or carton labels.

## Outcomes (ranked)
1. Snippet that names the formats and the auto check digit (below); FAQ answering "free GS1 barcode?" honestly.
2. Paste-a-list / CSV mode producing a ZIP of PNG or SVG files, with per-row errors.
3. Human-readable text toggle and bar-height control.

## SEO
- Now: title "Barcode Generator: EAN-13, UPC-A, Code 128, Check Digit" (55, no brand); meta 151; H1 "Barcode Generator"
- Keywords: barcode generator, EAN-13 barcode generator, UPC barcode generator, Code 128 generator
- Suggested Title: "Barcode Generator: EAN-13, UPC-A, Code 128 | FreeDailyPro" (57)
- Suggested Meta: "Make scannable EAN-13, UPC-A, EAN-8, Code 128, Code 39 and ITF-14 barcodes with the check digit added for you. Download a 300 dpi PNG or SVG for labels." (152)
- Suggested H1: keep "Barcode Generator"
- FAQ: Is this barcode valid for Amazon or shops (GS1)? · Is the check digit added? · What size should I print? · PNG or SVG?

## Constraints
Keep the GS1 note and validation (L-119 verified). Download gating unchanged.

## Test cases
1. EAN-13 "590123412345" → check digit 7 appended, scans as 5901234123457.
2. Wrong check digit "5901234123458" → clear error (not silently corrected).
3. List of 5 values → ZIP of 5 files named by value; a bad row listed with its reason.
4. Human-readable toggle off → SVG omits the text element.
5. Title ≤60, meta 140–160; 390 px no overflow.
