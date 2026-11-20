Sent: 2026-11-20 08:40 ET

# FDP-25 Barcode Generator: test cases (guest, fresh context)

| ID | Input | Action | Expected after fix |
|---|---|---|---|
| BC-01 | EAN-13 400638133393 | preview + 4× PNG | Decodes 4006381333931; right quiet zone ≥ 7X, left ≥ 11X |
| BC-02 | EAN-13 4006381333932 | type | "Check digit should be 1, not 2…"; Download off |
| BC-03 | EAN-13 40063813339 / 40063813339A / "4006 3813 3393" | type | Length / digits-only messages |
| BC-04 | EAN-8 9638507 | preview | 96385074; quiet zones ≥ 7X both |
| BC-05 | UPC-A 03600029145 | preview | 036000291452; ≥ 9X |
| BC-06 | ITF-14 1540014128876 | preview + SVG | 15400141288763; ≥ 10X; bearer bars |
| BC-07 | Code 128 full printable ASCII | preview | Decodes exactly; ≥ 10X |
| BC-08 | Code 128 Café / tab | type | "standard keyboard characters only" |
| BC-09 | Code 39 abc-123 | preview | Note "encodes ABC-123"; decodes ABC-123; ≥ 10X |
| BC-10 | Code 39 ABC*123 | type | Allowed-characters message |
| BC-11 | Code 128, 400 chars | type | Warning or cap before a 118 in PNG |
| BC-12 | Long caption on EAN-13 | preview/PNG | Caption fully visible (wrapped/widened) or warning |
| BC-13 | Sample value untouched | Download | Not charged / disabled until changed |
| BC-14 | List: 8-line sample (dup, bad check digit, letters, short) | A list | "2 ready, 3 problems, 2 repeated"; ZIP has 2 files + index.csv |
| BC-15 | List: 201 lines | A list | "Only the first 200 are made." |
| BC-16 | With uses: Download ×N different values + ZIP | Download | Counts per Santosh's decided policy |
| BC-17 | At 0 remaining | Download PNG | Cap dialog → Day Pass $1 → email prompt (stop) |
| BC-18 | iPhone 13 / Pixel 7 / SE | choose Code 128 | No sideways scroll |
| BC-19 | Firefox, WebKit | BC-01/05/07 | Same as Chromium |
| BC-20 | FAQ "What size should I print?" | read | 100% size and GS1 80–200% range stated |
