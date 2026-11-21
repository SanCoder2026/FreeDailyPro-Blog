Sent: 2026-11-21 14:59 ET

# FDP-67 test cases

| ID | Input / action | Expected | Result |
|---|---|---|---|
| Z01–Z06 | At 10/10: upload, convert, Download, change file, reload + Download | Cap dialog on Download | PASS (convert shows stats only) |
| L01–L11 | Uses left: 4 conversions (cube, colour cube, sphere, "solid"-header binary) + Download; re-download same | 1 use per new result | PASS (each fresh page charged once; re-download of same result free) |
| P01–P03 | Uses left: 3 different files in one page load | 3 uses | **1 use (P1)**; at 10/10 later files still download (P1) |
| P04 / X | Save to Google Drive, Save to my cloud storage, Open from Drive | Gate / sign-in | Cap dialog at 10/10; Google sign-in popup (closed); cloud = sign-in dialog |
| B01–B05 | 4 files incl. invalid → ZIP; .stl/.STL same base; sphere binary → ASCII | ZIP of valid files | PASS; 1 use per ZIP (Owner question) |
| C01–C03 | not STL, empty, truncated binary | Clear error, buttons disabled | PASS |
| C04–C09 | CRLF, two solids, .STL, "solid" header binary, colour bytes, 14k sphere | Detect correctly | PASS |
| Accuracy | Outputs parsed vs sources | Same triangles/vertices | PASS (exact float32) |
| Q | Quick Buy Day / Monthly | Email / Stripe | Reached; stopped |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | PASS (P2/P3 above) |
