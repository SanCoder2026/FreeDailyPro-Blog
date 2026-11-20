Sent: 2026-11-20 08:40 ET

# FDP-09 Income Tax Calculator: test cases (IT-01…IT-44)

- **Written:** 2026-11-19 13:22:23 EST.
- **Status meanings:**
  - "Currently" is the live result on 2026-11-19 (ET).
  - **FAIL** cases should pass after the fix.
  - **Re-run** cases need a context with uses left (after midnight UTC, 7:00 PM ET).
- **Calc cases:** run `node scripts/it-live.js <ids>` (the T-ids are in brackets) and compare with `python3 scripts/ref_federal.py <income> <status> <pretax> [se]`.

## Federal + FICA (employee)
| ID | Case | Expected | Currently |
|---|---|---|---|
| IT-01 | [T01] Single 85,000 | fed 9,870, FICA 6,503, take-home 68,628 | PASS |
| IT-02 | [T02] 0 income | all zero, no error | PASS |
| IT-03 | [T03] income = std deduction | fed 0 | PASS |
| IT-04 | [T04] HoH 50,000 | matches ref (std 24,150) | PASS |
| IT-05 | [T05] MFJ 120,000, 401(k) 10,000 | matches ref | PASS |
| IT-06 | [T06] Single 250,000 | SS capped at 184,500; Addl Medicare over 200k | PASS |
| IT-07 | [T07] MFJ 300,000 | Addl Medicare over 250k | PASS |
| IT-08 | [T08] Single 800,000 | 37% bracket | PASS |
| IT-09 | [T09] MFS 400,000 | Addl Medicare over 125k | PASS |
| IT-10 | [T28] Biweekly view | annual ÷ 26 | PASS |
| IT-11 | [T26] 401(k) age 60–63 | limit 35,750 accepted | PASS |

## Self-employed
| ID | Case | Expected | Currently |
|---|---|---|---|
| IT-12 | [T10] SE 100,000 | matches ref incl. QBI | PASS |
| IT-13 | [T11/T12] SE 230k / 232k | matches ref | PASS |
| IT-14 | [T35] SE 240,000 single | fed ≈ 33,082 (QBI phase-in) | **FAIL**: 43,415 |
| IT-15 | [T36–T38] SE 245k / 246k / 260k | 34,780 / 35,123 / 40,060 | **FAIL**: 44,994 / 45,309 / 49,729 |
| IT-16 | [T39] SE 300,000 | 60,519 | **FAIL**: 62,725 |
| IT-17 | Monotonic: take-home(240k) > take-home(232k) | yes | **FAIL**: 167,085 < 171,522 |
| IT-18 | [T13] SE 300 (below 400 SE floor) | SE tax 0 | PASS |
| IT-19 | [T14] SE MFJ 250k / [T40] SE 100k + 20k pre-tax | match ref | PASS |

## State
| ID | Case | Expected | Currently |
|---|---|---|---|
| IT-20 | [T17] MD 85k single | state + county (≈3.2%), or a clear "county tax not included (~$2,510)" note | **FAIL**: $3,674, no note |
| IT-21 | [T16/T33/T34] NY / IN / OH 85k | a local-tax note (NYC, county, municipal) | **FAIL**: none |
| IT-22 | [T19] CA HoH 85k | ≈ $1,636 (Schedule Z, std 11,412) | **FAIL**: $3,660 |
| IT-23 | [T18] PA 85k with 10k 401(k) | $2,609.50 | **FAIL**: $2,303 |
| IT-24 | [T15] CA single 85k | $3,660 + SDI $1,105 | PASS |
| IT-25 | [T20] TX | state 0 | PASS |
| IT-26 | Age 65+ single 85k | extra std / senior deduction applied or disclosed | **FAIL**: no control, not disclosed |
| IT-27 | "Effective rate" label | says whether it includes FICA | **FAIL**: unlabelled (19.3% incl. FICA) |

## Validation
| ID | Case | Expected | Currently |
|---|---|---|---|
| IT-28 | [T21/T24/T31] "abc", "85k", "1e12" | "Enter an income as a number" | PASS |
| IT-29 | [T22/T23/T25/T27/T32] negative, "1,000,000", 401(k) over limit, pre-tax > income, decimal | error / parsed / IRS-cited error / error / accepted | PASS |

## Trial cost (display-only counters)
| ID | Case | Expected (per Terms/FAQ) | Currently |
|---|---|---|---|
| IT-30 | Read results at 0 | visible, no use | PASS |
| IT-31 | Copy result, 10 left | no use | **FAIL**: 10 → 9 (repeats free) |
| IT-32 | Copy result at 0 | copies | **FAIL**: cap dialog |
| IT-33 | Ctrl+C of a selected figure at 0 | copies | **FAIL**: cap dialog, clipboard empty |
| IT-34 | Save as text first, 10 left | no use | **Re-run** (`it-gate4.js`) |
| IT-35 | Print first, 10 left | no use | **Re-run** (`it-gate4.js`) |
| IT-36 | Save / Print at 0 | works | **FAIL**: cap dialog |

## UI, a11y, devices, content
| ID | Case | Expected | Currently |
|---|---|---|---|
| IT-37 | Tab order | logical, focus visible | PASS |
| IT-38 | aria-live on the result | announced | **FAIL**: none |
| IT-39 | iPhone SE 320 px | no horizontal scroll | **FAIL**: 353 px |
| IT-40 | Flat rate 150% / −5% | rejected (0–100) | **FAIL**: accepted |
| IT-41 | Flat-rate currency select | has an accessible name | **FAIL** (DOM read) |
| IT-42 | Locale titles | localized, no "gratis"/"free" | **FAIL**: es "gratis"; 8 locales in English |
| IT-43 | Blog QBI sentence | matches the tool | **FAIL** |
| IT-44 | Video | current UI, no personal bookmarks | **FAIL** |
