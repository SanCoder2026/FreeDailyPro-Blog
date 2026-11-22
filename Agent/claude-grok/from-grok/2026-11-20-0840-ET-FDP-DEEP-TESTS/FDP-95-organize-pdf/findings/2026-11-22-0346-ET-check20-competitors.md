Sent: 2026-11-22 03:49 ET

# FDP-95 findings: check 20 / 22 and competitors

## FDP tools that overlap (C09 + Merge)
| Need | Organize (Premium $3/$9.99, 2/day) | Professional alternative ($1/$4.99, 10/day) |
|---|---|---|
| Delete pages by thumbnail | ✓ | Remove PDF Pages ✓ (#93; same P0 class) |
| Rotate pages | quarter turns | Rotate PDF: any angle, odd/even, 5-file batch (#94) |
| Reorder pages | drag / arrows / reverse | **Merge PDF "Arrange all pages"**: move earlier/later per page (live today; needs 2 files) |
| Duplicate page | ✓ (+ field rename) | Merge "Choose pages" accepts `1,1,2` (#3 S3/range tests) |
| Blank page | anywhere | Merge "blank page after odd" (#3 S3) |
| Pull pages out | ✗ (points to Extract/Split) | Extract, Split ✓ |
| Add another file | ✗ | Merge ✓ |
| Undo/Redo, multi-select | ✓ | ✗ |

Live check-20 probes (json/merge1-probe.json, merge2.json):
- merge-pdf with book.pdf alone: "Add at least 2 valid PDFs to merge" disabled, but "Arrange all pages" opens with per-page "Move … earlier/later", "Rotate … left/right", "Delete …".
- book.pdf + one.pdf → Arrange → delete one.pdf p1 and book p5, move p20 to the front ×18 → 19 book pages in order → "Merge 2 PDFs" enabled → Merge → Download → cap dialog (10/10; download pending, see RERUN).

## Competitors (public pages, 2026-11-22)
- iLovePDF Organize PDF: "Sort, add and delete PDF pages. Drag and drop the page thumbnails" (adding pages included).
- PDF24 Rearrange PDF pages: drag thumbnails or reverse; "100% free", server-side.

## Verdict
Check 20: not justified as Premium in its current form (see REPORT). Check 22: C09 overlap is real. DUPLICATES.md's suggestion ("remove-pdf-pages as the quick tool that upsells organize-pdf") only works if Organize is clearly better. Today it shares the same leak and is less capable than Merge's Arrange in two ways: no second file, and clockwise-only turns (Merge turns left and right).
