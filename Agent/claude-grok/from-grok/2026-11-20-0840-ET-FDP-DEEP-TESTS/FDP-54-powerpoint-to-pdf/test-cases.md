Sent: 2026-11-21 10:12 ET

# FDP-54 test cases (guest)

| ID | Input / steps | Expected | Today |
|---|---|---|---|
| G01 | Convert deck A (new load) | +1 use | PASS (0→1) |
| G02 | Same load: convert deck B | +1 use | **FAIL** (stays) |
| G03 | Download same result twice | no extra use | PASS |
| G04 | At 10/10: Convert | cap dialog $1/$4.99 | PASS (3 engines) |
| G05 | Day Pass / Quick Buy monthly | email field / Stripe, stop | PASS |
| K01 | rich_16x9.pptx default | 7 pages 960×540, 1920 px, hidden left out, searchable, link kept, no notes | PASS |
| K02 | rich, Sharp + Include hidden | 8 pages, 2560 px | PASS |
| K03 | rich, Fast, text layer off | 1280 px, no text | PASS |
| K04 | standard_4x3.pptx | 720×540 | PASS |
| K05 | long_60.pptx | 60 pages; reasonable time | PASS (6 s without the layer, 51 s with it) |
| K06 | rich_16x9.ppt | server → 7 pages | PASS (minor shifts) |
| K07 | rich_16x9.odp | server → 7 pages | PASS |
| K08 | standard_4x3.ppsx | converts | **FAIL** |
| B01–B04 | renamed text, zip-not-deck, truncated, .txt | clear messages | PASS |
| X01 | Hindi in the text layer | clean or left out | FAIL (garbled) |
| X02 | locales | subtitle, drop zone and options translated | FAIL |
| S01 | Open from Google Drive | Google sign-in popup (untested past it) | sign-in |
