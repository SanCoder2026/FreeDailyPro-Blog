Sent: 2026-11-21 11:31 ET

# FDP-57 test cases (guest)

| ID | Input / steps | Expected | Today |
|---|---|---|---|
| G01 | Assemble at 0 left | allowed, no charge | PASS |
| G02 | Download at 0 left | cap dialog | PASS |
| G03 | First Download with uses | +1 | **0→2** (display) |
| G04 | Download same result again | no charge | PASS |
| G05 | Same load: re-assemble + Download at 2/2 | dialog or +1 | **FAIL**: free |
| G06 | After reload: Download at 2/2 | dialog | PASS |
| G07 | Save to Google Drive at 0 | dialog / sign-in | cap dialog |
| G08 | Save to my cloud storage | sign-in | email sign-in + $4.99 add-on (stopped) |
| G09 | Save project at 0 | allowed? | cap dialog (owner question) |
| G10 | Quick Buy day / month | email / Stripe | PASS |
| V01 | Assemble with no files | message | PASS |
| V02 | Cover on, no title | message + focus | PASS |
| V03 | .webp + .doc | skipped, named | PASS |
| V04 | fake.docx / empty.txt | named error | PASS |
| V05 | renamed text .png | named error | PARTIAL ("could not be read") |
| V06 | damaged.pdf | skipped + Repair | PASS |
| V07 | password PDF skip / wrong / u123 | named toast / retry / unlocked | PASS |
| V08 | Duplicate file | warning, added | PASS |
| O01 | Packet: cover+TOC+PDF+docx+JPEG | TOC = footers; bookmarks; links | PASS |
| O02 | .docx Unicode | all scripts | PARTIAL (Hindi broken) |
| O03 | Front-matter roman numerals | i, ii | FAIL (none) |
| C1 | Mixed full set + LOI (8 files) | fit, rotate, form flattened, cp1252 | PENDING reset |
| C2 | A4 plain, tiny PNG | no cover/TOC, no upscale | PENDING reset |
| C3 | 6×9, 60 pages, reorder, Unicode title | TOC font, speed | PENDING reset |
