Sent: 2026-11-21 03:05 ET

# FDP-39 Compare PDF: test cases (2026-11-21 EST run)

| ID | Case | Expected | Result |
|---|---|---|---|
| CP-01 | C01 vs C02 | 6 changes: 1 added, 1 removed, 4 edited | PASS |
| CP-02 | word marks | old struck red, new underlined green | PASS (dark contrast low) |
| CP-03 | running header changed | ignored | PASS |
| CP-04 | Side by Side | aligned rows | PASS |
| CP-05 | hide unchanged | only changes | PASS |
| CP-06 | Next/Previous | 2, 3, 2 of 6 | PASS |
| CP-07 | identical | "same text" message | PASS |
| CP-08 | restyled/rewrapped/repaginated | same text | PASS |
| CP-09 | blank page added | same text + page listed | PASS |
| CP-10 | scanned original | names file, OCR link | PASS |
| CP-11 | both scanned | names both | PASS |
| CP-12 | two-column | interleaved (documented) | PASS (limitation) |
| CP-13 | 50 pages, edit p.37 | 1 change, page 37 | PASS |
| CP-14 | Unicode | correct marks | PASS |
| CP-15 | 3,200 lines | limit message or result | Result shown; limit unverified |
| CP-16 | hyphenation | same text | PASS |
| CP-17 | locked + password | unlock dialog → compare | PASS (blog says fails) |
| CP-18 | locked + Cancel | one clear message | FAIL P3 (toast mentions "row") |
| CP-19 | corrupt / fake | damaged message, Repair link | PASS |
| CP-20 | swapped order | mirrored counts | PASS |
| CP-21 | Firefox subset | same | PASS |
| CP-22 | Compare with uses left | policy: counted (results) | FAIL (0 → 0) |
| CP-23 | Report 1 | −1 | PASS |
| CP-24 | Report again / .txt | −1 each | FAIL (free) |
| CP-25 | New Comparison → report | −1 | **FAIL P1** (free) |
| CP-26 | after reload report | −1 | PASS |
| CP-27 | full redline at 0 | not available | **FAIL P1** |
| CP-28 | reports at 0 | cap dialog | PASS |
| CP-29 | Day Pass / Quick Buy | email prompt / Stripe (stop) | PASS (stopped) |
| CP-30 | Privacy + Share | no file data sent; URL only | PASS |
