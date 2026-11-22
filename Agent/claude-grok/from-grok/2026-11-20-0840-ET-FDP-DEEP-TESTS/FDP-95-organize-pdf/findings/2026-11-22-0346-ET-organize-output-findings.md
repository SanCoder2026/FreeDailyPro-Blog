Sent: 2026-11-22 03:49 ET

# FDP-95 findings: what the saved file contains (verify95 / recover95)

| Case | Edit | Pages ok | Rotation ok | Hidden /Page | Links | Secret recoverable | Bookmarks | Size |
|---|---|---|---|---|---|---|---|---|
| O01 book | remove p5 | 19/19 | ✓ | 4 | p1 ×2, p8 ×1 → NOT-A-PAGE | **PAGE-5-SECRET, 4000-0000-0000-0005, gone_ssn value** | "Part B p5" → p6 (should drop); Only p5 dropped ✓; Named dest p10 lost; /Fit | 2.73 → 3.05 MB |
| O02 book | reverse | 20/20 | ✓ | 5 | 3/3 broken | – (nothing removed) | all follow ✓; Named dest lost; /Fit | → 3.19 MB |
| O03 book | blank, dup, rot, move | 22/22 | ✓ (p4 90) | 6 | 3/3 broken | – | follow ✓; Named dest lost | → 3.33 MB |
| O04 toc-links | remove p7 | 11/11 | ✓ | 11 | 11/11 broken | **PII-PAGE-7 … SSN 078-05-1120** | – | 8.3 → 14.3 KB |
| O05 split-field | remove p3 | 2/2 | ✓ | 2 | – | **p3_secret = P3-FIELD-SECRET** | – | 2.8 → 3.4 KB |
| O06 rotated-inherit | rot 1,2,3 ×1, 4 ×2 | 6/6 | ✓ 180/270/90/270 | 0 | – | – | – | trial mark only |
| O07 doc | drag, bulk rot, undo/redo | 6/6 | ✓ | 6 | 2/2 broken | – | follow ✓; /Fit; PageLabels, Lang lost | 11 → 15 KB |
| O08 form | dup p1, remove p2 | 3/3 | ✓ (p3 90) | 3 (copies of kept pages) | – | p2field gone ✓ | – | OCProperties, PageMode lost |
| O09 cropped | rot p1 | 3/3 | ✓, CropBox kept | 0 | – | (HIDDEN text outside crop = same as original, not a leak) | – | |
| E03 300 p | reverse, remove 1 | 299/299 | ✓ | 0 | – | – | – | 2.87 → 2.77 MB |
| E04 heavy 73.6 MB | remove 1, rot 1 | 29/29 | ✓ | 0 | – | – | – | 71.2 MB, no trial mark |

Root cause (code, `operations` `kn()`): `for entry of list: copyPages(src,[entry.index])`. pdf-lib copies each page's whole object graph. A link /Dest or widget /P on that page pulls the *target page* along as a separate object, so every target gets an extra copy outside the page tree. When the target was removed, that copy is the only one left: P0. When it was kept, the link points at the copy, not the visible page: P1.

MuPDF check (json/fitz-links.txt): original book p1 links → page index 4 and 9; reversed output p20 links → index 0, 0. toc-links output p1: eleven links → 0.

Widgets: in every output with fields, each widget's /P points to a hidden page (`widget_pages: NOT-IN-TREE`). Fields still show and fill in viewers.
