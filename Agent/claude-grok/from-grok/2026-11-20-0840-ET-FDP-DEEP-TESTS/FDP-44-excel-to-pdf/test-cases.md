Sent: 2026-11-21 05:21 ET

# FDP-44 Excel to PDF: test cases (rerun after fixes)

Guest, fresh profile; test files in `evidence/testfiles`. "Now" is what we saw on 2026-11-21.

| ID | Case | Expected | Now |
|---|---|---|---|
| XP-01 | At 0: Convert X01 | Converts; first-page preview only | PASS |
| XP-02 | At 0: Download / Drive / cloud | Cap dialog / sign-in dialog | PASS |
| XP-03 | Day Pass / Quick Buy | Email prompt / Stripe (stop) | PASS |
| XP-04 | Uses left: Download X01, then again | +1, then no change | PASS |
| XP-05 | Same load: Download X02, X07 (new results) | +1 each | **P1 FAIL** (no change) |
| XP-06 | Counter reaches 10/10 with the page open, then Download a new result | Cap dialog | **P1 FAIL** (downloads) |
| XP-07 | Reload, Download | +1 | PASS |
| XP-08 | X01 default | Formatting, hidden data out, title once, headers repeat, badge | PASS |
| XP-09 | Include hidden data | Hidden sheet/column/rows printed | PASS |
| XP-10 | A4/Landscape/Large/no grid/no colours | Applied | PASS |
| XP-11 | X02 wide | Splits with first column repeated, note | PASS |
| XP-12 | X03 scripts | All scripts look right, or an accurate warning | **P2 FAIL** (Hindi, 🚀) |
| XP-13 | X04 formulas without saved results | Warns which cells print blank | PASS |
| XP-14 | X05 50k rows | Completes (< 15 s) | PASS (8.9 s) |
| XP-15 | X06 BOM/semicolon CSV, X07 quoted CSV | Parsed correctly | PASS |
| XP-16 | X08 empty, X09 corrupt, X10 text | Clear messages | PASS |
| XP-17 | X11 .xls | Table plus chart/picture note | **P2** (no note) |
| XP-18 | X01 picture note | "1 picture was not included" | **P2 FAIL** |
| XP-19 | X12 .ods message | Grammatical, says .ods | **P2 FAIL** |
| XP-20 | X13 .docx, X14 .xlsm, X15 LO .xlsx | Reject / convert / notes | PASS |
| XP-21 | Privacy: no cell text or file name in any request | None | PASS |
| XP-22 | Firefox/WebKit subset | Same as Chromium | PASS |
| XP-23 | iPhone SE | No horizontal overflow | P3 FAIL (9 px) |
