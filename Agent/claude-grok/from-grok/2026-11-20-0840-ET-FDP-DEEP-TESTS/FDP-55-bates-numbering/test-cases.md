Sent: 2026-11-21 10:39 ET

# FDP-55 test cases (guest)

| ID | Input / steps | Expected | Today |
|---|---|---|---|
| G01 | Run on new load | +1 use | PASS (0→1) |
| G02 | Same load: new prefix, run | +1 use | **FAIL** (stays) |
| G03 | Same load: new file, run | +1 use | **FAIL** (stays) |
| G04 | After reload, run | +1 use | PASS (1→2) |
| G05 | Download PDF/CSV/ZIP | no extra use | PASS |
| G06 | Run at 10/10 | cap dialog, no output | PASS (Chromium, Firefox, WebKit) |
| G07 | Quick Buy day / month | stop at email / Stripe | PASS |
| B01 | 2 files, continuous, legend CONFIDENTIAL | ABC000001–8; legend bottom-left | PASS |
| B02 | Continuous off | each file from DEF000001 | PASS |
| B03 | Rotate 90/270/180, Top right | upright in viewed corner | PASS |
| B04 | Offset CropBox | stamp inside visible box | PASS |
| B05 | Dark page, box off | readable | WEAK (black on near-black) |
| B06 | Footer text at margin | not covered | PASS (this file) |
| B07 | Start 999995, 12 pages, auto digits | equal width 7 digits | PASS |
| B08 | Unicode prefix/suffix | renders and is searchable | PARTIAL (renders; not in text layer) |
| B09 | Same-name files + landscape | -bates-2, CSV distinct | PASS |
| B10 | Good + locked (skip) | single PDF, label right | PASS (locked never listed) |
| B11 | Prefix `=SUM(1)` | CSV escaped | PASS (`'=SUM`) |
| B12 | Good + locked (unlock u123) | both numbered in order | PASS |
| P04 | start -1/1.5, digits 0/11, size 30, legend = number corner | message, run disabled | PASS |
| P02 | Renamed text, damaged | toast + Repair link | PASS |
| P03 | Duplicate add | warning, added | PASS |
| D01 | Open from Google Drive | Google sign-in | Sign-in untested |
