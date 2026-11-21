Sent: 2026-11-21 07:23 ET

# FDP-48 test cases (guest; run after fixes)

| ID | Steps | Expected | Today (2026-11-21) |
|---|---|---|---|
| T01 | Fresh context with uses left: 3 receipts → Convert → Download | +1 use, 3-page Letter PDF | PASS (L01) |
| T02 | Same load: Clear all → new images → Convert → Download | +1 use | FAIL: stays at 1 (L02–L10c) |
| T03 | Download the same PDF twice | second is free | PASS (G02) |
| T04 | At 10/10 in the same load, new PDF → Download | cap dialog | FAIL (L12, L13 downloaded) |
| T05 | Reload at 10/10 → Download | cap dialog $1/$4.99 | PASS (L14, Z02) |
| T06 | At 0: Convert, thumbnails, Preview first page | low-res only (≤ 489 px), no file | PASS |
| T07 | Day Pass / Quick Buy monthly | email prompt / Stripe (stop) | PASS |
| T08 | P25_gps_orient1.jpg → PDF → pdfimages -j → read EXIF | no GPS, no Make/Model | FAIL (G01) |
| T09 | P02_orient6_gps.jpg → PDF | upright, no EXIF | PASS (L02) |
| T10 | HEIC, AVIF, WebP, BMP, SVG, animated GIF, 16-bit PNG, CMYK JPG | all render, GIF note shown | PASS (L03, L04) |
| T11 | P08.tiff + P23_document.pdf dropped | specific hints (TIFF / use PDF to JPG or Merge PDF) | PARTIAL: generic toast only |
| T12 | P13_truncated.jpg | warning | FAIL: silent, blank page |
| T13 | A4 portrait | 595.2×841.92 pt | PASS (L06) |
| T14 | Original size, P21 300 dpi | 8.27×11.69 in | PASS |
| T15 | Original size, P24 orient6 300 dpi | about 4.1×5.8 in | FAIL: 12.9×18.3 in (L07) |
| T16 | Original size, 20,000 px panorama | ≤ 200 in wide or warning | FAIL: 208 in (L08) |
| T17 | Custom 0 / 300 in | "The page must be between 1 in and 200 in…" | PASS (L10a/b) |
| T18 | 7 receipts, A4 landscape, Fill, pair | 4 pages, cropped fill | PASS (L09) |
| T19 | 60 images | 30 pages (paired) / 60, under a minute | PASS (L13) |
| T20 | Duplicate add | duplicate warning | PASS (L11) |
| T21 | Save to Google Drive / cloud / Open from Drive | sign-in required | Untested (sign-in) |
| T22 | Pair pages titles/meta | no "Free" | FAIL |
| T23 | Locale pages | translated title/meta/tool strings | FAIL (partial translation) |
| T24 | Real Safari (iPhone/Mac): JPG → PDF | works | Unverified (Linux WebKit tab crash) |
| T25 | Firefox: S01–S03 | convert OK | PASS (subset-firefox.json; pair toggle not found by harness) |
