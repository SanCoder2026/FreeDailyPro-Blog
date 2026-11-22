Sent: 2026-11-21 20:39 ET

# Live functional findings (FDP-84)

Evidence: evidence/json/{left,zero,casesdl,casesdl-b,casesdl-c,heic,handoff,quickbuy,probe}.json, evidence/json/analysis-xlsx.json, evidence/xlsx/, evidence/screens/cases/.

## Usage
- **left** (fresh profile, uses left): X02 charges 1 (1 POST). X03 (same), X04 (edited cell), X05 (new picture), X09 (after reload + 1 download) are free. X08 after reload charges 1. Then the C cases with a reload each: one POST per case. C04 moved the counter 5/10 → 10/10 with a single POST (pooling).
- **casesdl** (one load, Start over between cases): 16 downloads, 1 POST. **casesdl-b**: 5 downloads, 1 POST. **casesdl-c**: 2, 1 POST.
- **zero**: at 0 uses, Read gives the full grid (status "Read 1 picture · about 95%", 21 numbers and 7 dates). Every save shows "Today's trial uses are done" with 0 POSTs. The gate line reads "0 remaining today Get a Day Pass to download".

## Data accuracy (openpyxl)
- clean: 56/56 cells. Qty int `0`; Price `"$"#,##0.00`; Share 0.125 `0.0%`; Date datetime `yyyy-mm-dd`; Code/ZIP strings with leading zeros.
- de (C12/C13 with numbers on): Menge 1.2 `0.000` (should be 1200); Preis 1234.5 / 89.9 / 7.25 / 1099 `#,##0.00" €"`; Rabatt 0.125 / 0.05 / 0 / 0.15.
- tilt (dark): [["item","2026-03-04"],["paper A4","2026-03-09"],…]. Code/ZIP/Qty/Price/Share lost; dates two rows off.
- tilt-light6 without Straighten: Price "40.85" for "$0.85", header "‘tem"/"iid". With Straighten: exact.
- small: 48% (left) / 62% (casesdl). Values like 5450 and 20260301 written.
- join / no-join / one-sheet: 8 rows / 5+4 / 10 rows.
- dmy auto: day-first. Month-first forced: the note says day-first was used.

## Other
- HEIC: all three engines read it (93%).
- Corrupt: 122 s, "could not be decoded.. Try a clearer picture."
- Options persisted across Start over (numbers-off from C02 carried to later cases in casesdl).
