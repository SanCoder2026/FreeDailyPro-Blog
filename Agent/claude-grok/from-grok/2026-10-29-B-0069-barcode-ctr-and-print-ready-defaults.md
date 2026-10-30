# B-0069 Barcode Generator: 2,045 impressions at position 7.8 but 0.1% CTR. Make the snippet and defaults match "print-ready"
Priority: P2      Estimated effort: 45–90 min      Report: #77      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
The tool is technically correct. The goal is to turn existing page-1 visibility into clicks and satisfied users: someone who needs a retail or shipping barcode should see in the snippet, and get from the defaults, a code that will print and scan at the right size.

## Why
- GSC (analytics/2026-07-10-to-now-raw.md): /tool/barcode-generator has 3 clicks / 2,045 impressions, 0.1% CTR, position 7.8. The query "barcode generator" has 1/1,516 at position 5.5. This is the largest click gap in this batch.
- Verified working (Oct 29, 23:15 ET, zxing-cpp decode):
  - EAN-13 default decodes as 5901234123457.
  - Code 128 "ABC-123 test" at 4× decodes (1416×482).
  - A wrong check digit shows "Check digit should be 7, not 8" and blocks download.
  - Five digits shows a clear length error with no use charged.
  - SVG downloads.
  - Mobile works.
- Gaps against live competitors (read Oct 29):
  - The default PNG is **1× = 234×122 px**, too small to print at the GS1 nominal 37.29×25.93 mm at 300 dpi. readbarcode.com, cleverence.com and openvibe.tools offer bar height, nominal-size/print-size presets and 300 dpi PNG.
  - Competitors also show GS1 guidance ("the number must come from GS1 to sell in stores"). Cleverence and readbarcode put this near the input.
  - barcodesready.com and barcodepress.com add UPC-E, ISBN and GS1-128.
  - The download filename is always "barcode.png", which is confusing when you make several.
- The title already lists the formats. The meta (156 characters) ends with a generic phrase. A snippet that mentions the auto check digit, print size and SVG for packaging matches what competitors win on.

## Outcomes
- Snippet (title/meta) highlights check-digit auto-fill, print-ready size and SVG. "Free" in tags is allowed.
- Default PNG suitable for print (e.g. 300 dpi at nominal size), with 1× kept as an option.
- A short GS1 note for EAN/UPC.
- Filename includes format and value (e.g. ean13-5901234123457.png).
- Optional: UPC-E / ISBN.

## Constraints
No visible "free" in UI copy (B-0019). Trial uses wording. Don't change the trial pool. Keep the existing validation messages, which are good.

## Test cases
| # | Device | Steps | Expected |
|---|---|---|---|
| 1 | 1280, logged out | default EAN-13 → Download PNG | ≥300 dpi nominal size, decodes 5901234123457, filename has value |
| 2 | 390 | UPC-A 03600029145 → PNG | decodes; print size shown |
| 3 | 1280 | 5901234123458 | check-digit error, no download, no use charged |
| 4 | — | view-source | new meta, 140–160 characters |
Outputs: report-77/test-cases/outputs/bar-*.png/svg; results bar.json.
