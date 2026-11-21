Sent: 2026-11-21 03:55 ET

# FDP-41 OCR PDF: reusable test cases

Guest browser, https://www.freedailypro.com/tool/ocr-pdf. Inputs: `evidence/testfiles/` (`scripts/make-scans.py`, `truth.json`). Downloads are checked with `testfiles/verify.py <dir>`. "Counter" = localStorage `fdp-usage-v1.usageToday` (display-only).

| ID | Input | Steps | Expected | Result 2026-11-21 |
|---|---|---|---|---|
| OC-01 | — | Load and reload the page twice (uses left) | Counter unchanged | PASS (0 → 0) |
| OC-02 | S01 | Drop, Make Searchable, Preview first page | Counter unchanged until Download | PASS |
| OC-03 | S01 | Download | Counter +1; `searchable_S01_scan_clean_en.pdf` | PASS (0 → 1) |
| OC-04 | S01 | Download the same result again | Counter +1 (Nov 20 decision) | **FAIL P1** (stays 1) |
| OC-05 | S02 | New → drop → Make Searchable → Download in the same load | Counter +1 | **FAIL P1** (stays 1; 14 files for 1 use in V) |
| OC-06 | S01 | Reload → OCR → Download | Counter +1 | PASS (1 → 2) |
| OC-07 | S01 at 0 | Make Searchable | Runs; notice; Download shows "Get a Day Pass to download" | PASS |
| OC-08 | S01 at 0 | Preview first page | Low-res preview of the original only | PASS (489×633) |
| OC-09 | S01 at 0 | Download / Save to Google Drive | Cap dialog | PASS |
| OC-10 | S01 at 0 | Continue with Compress PDF → Compress → Download | Result handed over; cap dialog | PASS |
| OC-11 | at 0 | Cap dialog → Buy Day Pass; Quick Buy monthly | Email prompt; Stripe (stop) | PASS |
| OC-12 | S01 | Verify the output | 100% recall, visual diff 0, badge | PASS |
| OC-13 | S02 | Verify | Page 2 untouched; pages 1 and 3 OCR'd; "48 words on 2 pages" | PASS |
| OC-14 | S03 | Detect automatically | Upright output, 100% | PASS |
| OC-15 | S03 | Turn 90° clockwise | Upright output, 100% | PASS |
| OC-16 | S12 | Detect automatically | Upright output (`/Rotate 180`) | **FAIL P2** (`/Rotate 270`, sideways) |
| OC-17 | S12 | Turn 180° first | Upright, 100% | PASS |
| OC-18 | S03 then New + S05 | Set Turn 90° for S03, New, S05 with no changes | Orientation back to As scanned; upright output | **FAIL P1** (sideways, "turned 90°… reads upright") |
| OC-19 | S07 then New + S01 | English + Hindi, New, next file | Language resets or is shown | **FAIL P1** (carried over; part of OC-18) |
| OC-20 | S05 | Spanish | 100%, accents kept | PASS |
| OC-21 | S06 | German | 100% | PASS |
| OC-22 | S07 | English + Hindi | Hindi words searchable | **FAIL P2** (77%; reph/half forms lost) |
| OC-23 | S11 | English | Table digits in the text layer | **FAIL P2** (38%; QTY/PRICE missing) |
| OC-24 | S09 | English | Readable text | PASS (75%, expected for 72 dpi noise) |
| OC-25 | S10 | English; time it | 12 pages, 100%, under 15 s | PASS (7.4–10.4 s) |
| OC-26 | S04 | Make Searchable | Image page OCR'd despite the "Page 1 of 1" stamp | **FAIL P2** ("already searchable") |
| OC-27 | P02 | Make Searchable | "already searchable" notice, no file | PASS |
| OC-28 | S08 | Make Searchable | "No text found" style message | PARTIAL P3 (orientation message) |
| OC-29 | P06 / P07 | Drop | Damaged toast + Repair PDF link | PASS |
| OC-30 | S13 | Password ocr123 → OCR → Download | Unlocked, 100%, no password on output | PASS |
| OC-31 | S10 | Make Searchable, press Stop after 4 s | Stops; no download; can restart | PASS |
| OC-32 | S01 | Firefox K set; WebKit OCR | Same as Chromium; WebKit completes | Firefox PASS (11/11); **WebKit crash, unverified on real Safari** |
