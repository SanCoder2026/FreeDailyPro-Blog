Sent: 2026-11-20 08:40 ET

# FDP-10 State Tax Calculator: test cases (ST-01…ST-40)

- **Written:** 2026-11-19 13:33:46 EST.
- "Currently" is the live result on 2026-11-19 (ET). **FAIL** cases should pass after the fix.
- Calc cases: `node scripts/st-live.js <ids>` (S-ids in brackets). Compare table: `node scripts/st-compare.js <income> <status>`.

## Core math
| ID | Case | Expected | Currently |
|---|---|---|---|
| ST-01 | [S01] CA single 75k | $2,774.57 + SDI $975 | PASS |
| ST-02 | [S03] CA MFJ 150k | $5,549.14 | PASS |
| ST-03 | [S19] CA 10M | 12.3% + 1% MHST | PASS (≈$1,299,925) |
| ST-04 | [S04] NY single 85k | $3,993.00 + PFL $367.20 | PASS |
| ST-05 | [S02] CA HoH 75k | $1,118.19 | **FAIL**: $2,774.57 |
| ST-06 | [S27] NC HoH 75k | $2,229.41 | **FAIL**: $2,483.78 |
| ST-07 | [S05] NY HoH 85k | HoH std $11,200 + HoH brackets | **FAIL**: = single $3,993 |
| ST-08 | Compare, HoH | uses HoH rules per state | **FAIL** (same engine) |
| ST-09 | [S12] IL 75k | $3,567.71 | PASS |
| ST-10 | [S21] MA 75k | $3,530 + PFML $345 | PASS |
| ST-11 | [S22] NJ 75k | $2,596 + TDI/FLI | PASS |
| ST-12 | UT 75k single (compare row) | $3,103.45 | **FAIL**: $2,621 |
| ST-13 | [S30] OR 75k | $5,733 (−$256 credit) | **FAIL**: $5,989 |
| ST-14 | DE 75k (compare row) | $3,609 (−$110 credit) | **FAIL**: $3,719 |
| ST-15 | [S13/S14] TX / WA | $0; WA PFML $605.40 + Cares $435 | PASS |

## Input
| ID | Case | Expected | Currently |
|---|---|---|---|
| ST-16 | [S17] "85k" | error (or parsed as 85,000) | **FAIL**: $0.00, no error |
| ST-17 | [S15] "abc" | error | **FAIL**: $0.00, no error |
| ST-18 | [S16] -5000 | alert | PASS |
| ST-19 | [S18] 0 | $0 | PASS |

## Local
| ID | Case | Expected | Currently |
|---|---|---|---|
| ST-20 | [S06] NYC 85k | $2,859.69 | PASS |
| ST-21 | [S11] Yonkers 85k | $668.83 | PASS |
| ST-22 | [S07/S08/S29] MD Montgomery / Anne Arundel / Frederick MFS | $2,510.40 / $2,186.43 / $2,092.12 | PASS |
| ST-23 | [S10/S10b] Philadelphia res/non-res | $3,174.75 / $2,911.25 | PASS |
| ST-24 | Notice with a city picked | "Includes <city>" | **FAIL**: says "not included" |
| ST-25 | NY typical box | labelled NYC/Yonkers only | **FAIL**: 3.5% for all NY |
| ST-26 | [S09/S24] MD / PA typical box | +3.2% / +1.5% of state taxable | PASS |

## Exports and trial (owner policy: charging is intended)
| ID | Case | Expected | Currently |
|---|---|---|---|
| ST-27 | Reading and Compare | no use | PASS |
| ST-28 | Download CSV, 10 left | file; 1 use per visit | PASS (10 → 9) |
| ST-29 | Other 5 exports, same visit | no extra use | PASS |
| ST-30 | Any export at 0 | cap dialog | PASS |
| ST-31 | /terms wording | matches "1 use per visit for copy/save/print" | **FAIL** |
| ST-32 | /faq wording | same | **FAIL** |
| ST-33 | CSV content | BOM, numeric, no formulas | PASS |
| ST-34 | Export bars | one bar; dialog verb matches the action | **FAIL**: two bars; "Copy report" → "downloading" |

## A11y, content
| ID | Case | Expected | Currently |
|---|---|---|---|
| ST-35 | Compare rows by keyboard | focusable/operable | **FAIL** |
| ST-36 | aria-live on the result | yes | **FAIL** |
| ST-37 | Tab order of the inputs | logical | PASS |
| ST-38 | Video | current UI, correct figure, no bookmarks | **FAIL** |
| ST-39 | Blog $95k table | matches the tool | **FAIL**: NY, CA, OR |
| ST-40 | Locales and schema | localized; Offer period | **FAIL** |
