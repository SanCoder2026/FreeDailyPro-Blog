Sent: 2026-11-21 11:52 ET

# FDP-58 test cases (guest)

| ID | Input / steps | Expected | Today |
|---|---|---|---|
| G01 | Stamp on new load | +1 use | PASS (0→1) |
| G02 | Same load: new prefix, stamp | +1 use | **FAIL** (stays) |
| G03 | Same load: new file, stamp | +1 use | **FAIL** (stays) |
| G04 | After reload, stamp | +1 use | PASS (1→2) |
| G05 | Download PDF/CSV/ZIP, Save buttons | no extra use | PASS |
| G06 | Stamp at 10/10 | cap dialog, no output | PASS (Chromium, WebKit) |
| G07 | Quick Buy day / month | stop at email / Stripe | PASS |
| E01 | 3 files, letters, first page | A–C top right, ZIP + CSV | PASS |
| E02 | Numbers, "Pl. Ex. ", every page, page X of N, bottom right | "Pl. Ex. 1, page 1 of 5"… | PASS |
| E03 | Rotate 90/270/180, every page, top left | upright in viewed corner | PASS |
| E04 | Offset CropBox, bottom center | inside visible box | PASS |
| E05 | Case header at top-right, defaults | header not covered | **WEAK** (covers "Filed …") |
| E06 | Dark page, box off | readable | WEAK (black on dark) |
| E07 | 28 files | A…Z, AA, AB | PASS |
| E08 | Start Z | Z, AA | PASS |
| E09 | Numbers start 0 | 0, 1 or a message | **FAIL** (1, 2 silently) |
| E10 | "Anlage A – 証拠", every page, 12 p | renders, searchable | PARTIAL (renders; no text) |
| E11 | Same-name files + password (u123) | -exhibit-2, unlocked, A–C | PASS |
| E12 | Prefix `=HYPERLINK("x")` | CSV escaped | PASS |
| E13 | Size 36, bottom left, suffix | fits, readable | PASS |
| P01–P04 | Locked/damaged/renamed/txt/duplicate | dialog/toasts | PASS |
| P05 | Letters 1/ABCDE, numbers A/-1/123456, size 7/37/empty | message, Stamp disabled | PASS |
| D01 | Open from / Save to Google Drive | Google sign-in | Sign-in untested |
| D02 | Save to my cloud storage | sign-in + add-on | Sign-in untested |
