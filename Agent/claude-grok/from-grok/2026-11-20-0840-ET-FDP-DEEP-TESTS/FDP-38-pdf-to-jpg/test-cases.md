Sent: 2026-11-21 02:49 ET

# FDP-38 PDF to JPG: test cases (2026-11-21 EST run)

| ID | Case | Expected | Result |
|---|---|---|---|
| PJ-01 | P01 Standard | 918×1188 | PASS |
| PJ-02 | P01 High (default) | 1224×1584 | PASS |
| PJ-03 | P01 Maximum | 1836×2376 | PASS |
| PJ-04 | P01 Print PNG | 2550×3300 PNG | PASS |
| PJ-05 | range "3" | single JPG `-page-03.jpg` | PASS |
| PJ-06 | range "1, 3-5" on 50p | 4 images | PASS |
| PJ-07 | range "8-" | 43 images; 12 thumbnails + "…and 31 more" | PASS |
| PJ-08 | range "60" | clear error, nothing used | PASS |
| PJ-09 | range "5-3, x" | clear error | PASS |
| PJ-10 | 2 PDFs | range disabled | PASS |
| PJ-11 | 100-inch page Print | lowered-resolution notice, 4000×4000 | PASS |
| PJ-12 | mixed page sizes | each page keeps its own size | PASS |
| PJ-13 | AES user password | unlock dialog → converts | PASS (copy says "skipped") |
| PJ-14 | Skip locked + plain | toast, plain converts | PASS |
| PJ-15 | owner-only | converts silently | PASS (policy note) |
| PJ-16 | corrupt / renamed text | "couldn't be read … Nothing was used" | PASS |
| PJ-17 | duplicate names | `report/`, `report (2)/` | PASS |
| PJ-18 | 3 PDFs ZIP | per-PDF folders, `converted-images-3-files.zip` | PASS |
| PJ-19 | 50 pages Print | completes (3.4 s, 4.26 MB) | PASS |
| PJ-20 | Firefox subset | same behaviour | PASS (bigger JPGs) |
| PJ-21 | Download 1 (uses left) | −1 | PASS |
| PJ-22 | same Download again | policy: −1 per Download | FAIL (free) |
| PJ-23 | Convert another → Download | −1 | **FAIL P1** (free) |
| PJ-24 | after reload Download | −1 | PASS |
| PJ-25 | Preview at 0 trial uses | not usable as output | **FAIL P1** (full-res) |
| PJ-26 | Preview vs download | preview not cleaner than download | **FAIL P1** (no badge) |
| PJ-27 | Range harvest at 0 | blocked | **FAIL P1** |
| PJ-28 | Download at 0 | cap dialog, count unchanged | PASS |
| PJ-29 | Day Pass from cap | email prompt (stop) | PASS (stopped) |
| PJ-30 | Privacy | no file bytes/names/password in requests | PASS |
| PJ-31 | Share | tool URL only | PASS |
| PJ-32 | Pair page /pdf-to-png | PNG preselected, canonical self | PASS |
