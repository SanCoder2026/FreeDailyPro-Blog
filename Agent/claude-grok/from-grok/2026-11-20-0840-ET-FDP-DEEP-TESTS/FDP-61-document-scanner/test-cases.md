Sent: 2026-11-21 13:02 ET

# FDP-61 test cases (guest). Inputs in evidence/testfiles; scripts in scripts/

| ID | Input / steps | Expected | Today |
|---|---|---|---|
| G01 | At cap: Download PDF / PNG / searchable | Cap dialog, no charge | PASS |
| G02 | Uses left: first Download PDF | +1 use, file | PASS |
| G03 | Same scan: PNG + searchable after PDF | Same use (no extra) | PASS |
| G04 | New scan in same load after a charge | +1 use or cap | **FAIL** (free, no cap) |
| G05 | After reload at cap | Cap dialog | PASS |
| G06 | Quick Buy Day / Monthly | Email prompt / Stripe (stop) | PASS |
| F01 | p1-tilted (dark desk) | Auto corners, straight clean page | PASS |
| F02 | p4-shadow | Shadow evened | PASS |
| F03 | p5-lightdesk | Corners found or fallback message | PASS (found) |
| F04 | p7-exif-orient6 | Upright at Crop | **FAIL** (sideways) |
| F05 | p8-small-300px | Small-photo warning | PASS |
| F06 | p9-lowcontrast | Low-contrast message | PASS |
| F07 | p10-darkpage | Dark-page handling | PASS |
| F08 | p11-big-6000 | Completes | PASS (~12 s) |
| F09 | notanimage.jpg | Error message | **FAIL** (empty Crop) |
| M01 | 3 pages, move page 2 up, Letter | PDF order 2,1,4; 612×792 | PASS |
| M02 | Searchable PDF of 3 pages | Text layer for all pages | PASS |
| M03 | ID card front + back | One page, card 85.6 mm wide | PASS (named _2pages) |
| M04 | Edit as Word / Excel | Opens converter with pages | **FAIL** (404) |
| M05 | Touch drag crop (Pixel 7), iPhone flow | Works | PASS |
| A01 | Keyboard: reach corner handles | Focusable | **FAIL** |
