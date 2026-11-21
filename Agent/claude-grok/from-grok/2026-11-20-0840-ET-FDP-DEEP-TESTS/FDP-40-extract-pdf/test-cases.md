Sent: 2026-11-21 03:27 ET

# FDP-40 Extract Pages & Text: test cases (2026-11-21 EST run)

| ID | Case | Expected | Result |
|---|---|---|---|
| EX-01 | "5,1,3" | typed order | PASS (first page = 5; rest pending download) |
| EX-02 | "2,2" | page twice | PASS (2 pages extracted; counter says 1) |
| EX-03 | "6-" | 6 to end | PASS |
| EX-04 | Odd / Even | 1,3,5,7 / 2,4,6,8 | PASS |
| EX-05 | "1; 3" and "1,,3;;5 , 7" | tolerant | PASS |
| EX-06 | "9", "0" | out-of-range message | PASS |
| EX-07 | "3-1", "abc" | clear errors | PASS |
| EX-08 | pages, empty | refused | PASS |
| EX-09 | text, default | all pages (copy) | **FAIL P2** (page 1 only) |
| EX-10 | text, empty / Select all | all pages | PASS |
| EX-11 | markers, tabs, forms, header | as documented | PASS |
| EX-12 | two columns | column order | PASS |
| EX-13 | Unicode | intact | PASS |
| EX-14 | scanned, text | OCR notice | PASS |
| EX-15 | scanned, pages | works | PASS |
| EX-16 | locked + password | copy: cannot open | PASS (unlocks; copy stale) |
| EX-17 | corrupt / fake | damaged toast, Repair link | PASS |
| EX-18 | 50 pages text | completes | PASS (3.9 s) |
| EX-19 | Firefox K subset | same as Chromium | PASS: 16/16 identical (cases-firefox-K.json) |
| EX-20 | Extract Text with uses left | policy: result counted | FAIL (0 → 0) |
| EX-21 | Copy with uses left | −1 | PASS (0 → 1) |
| EX-22 | Download A, A2 | −1 each | PENDING (rerun) |
| EX-23 | New → B / text C | −1 each | PENDING (rerun) |
| EX-24 | after reload D/E | −1 | PENDING (rerun) |
| EX-25 | full text at 0 | not available | **FAIL P1** |
| EX-26 | Copy / Download at 0 | cap dialog | PASS |
| EX-27 | pages preview at 0 | low-res first page only | PASS (489×633) |
| EX-28 | Day Pass / Quick Buy | email prompt / Stripe (stop) | PASS (stopped) |
| EX-29 | Privacy + Share | nothing sent; URL only | PASS |
| EX-30 | output content (bookmarks, forms, name, badge) | as FAQ | PENDING (rerun) |
