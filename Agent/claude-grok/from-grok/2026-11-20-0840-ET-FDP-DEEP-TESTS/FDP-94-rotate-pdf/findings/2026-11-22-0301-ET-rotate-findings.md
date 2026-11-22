Sent: 2026-11-22 03:02 ET

# Rotate PDF: how it works and what the outputs show

## Code (`operations` hn)
```
for each page with extra angle c:
  l = page.getRotation().angle        // pdf-lib, inherited value included
  if c is a multiple of 90: page.setRotation(l + c)  // in place
  else: E = embedPage(page)             // content only, MediaBox; no annots, no CropBox
        insertPage(i, size from we(w,h,l+c)).drawPage(E, rotate -(l+c))
        removePage(i+1)                 // old page stays in the context → written to file
save({useObjectStreams:true})
```
- The new page has no /Rotate, so it **inherits /Pages /Rotate** → double turn (P2 #2).
- `getSize()` and `embedPage` use the MediaBox → CropBox lost (P2 #3).
- Old page refs in /Outlines and other pages' /Dest are not re-pointed (P2 #4).
- The old page stays in the file (P3 #6).

## Output table (verify94.py)
| Tag | Input / action | Size | Hidden pages | Notes |
|---|---|---|---|---|
| C01 | doc All 90 | 11,011 → 11,531 | 0 | everything kept |
| C04 | doc p1 5, p3 −3, p5 90 | → 13,210 | 2 | bookmarks p1/p3 DEAD; p5→p1 dead; p3_name widget not in tree |
| R01 | rotated-inherit All 90 | 2,813 → 6,199 | 0 | 90→180, 180→270, 0→90 ✓ |
| R02 | rotated-inherit p1 10, p2 −7 | → 7,647 | 2 | new pages inherit /Rotate 90 → wrong |
| K01 | cropped All 90 | 2,051 → 4,156 | 0 | CropBox kept |
| K02 | cropped p1/p2 3 | → 5,376 | 2 | CropBox gone; hidden text visible |
| F01 | form All 90 | 18,977 → 14,186 | 0 | 12 fields + comments kept |
| F02 | form p1 2 | → 15,246 | 1 | 11 fields orphaned with values |
| A01 | form p2 2 | → 15,258 | 1 | 4 comments + p2field lost |
| A02 | doc p2 −2 | → 12,418 | 1 | highlight + note lost; bookmark p2 dead |
| L01 | toc-links p7 2 | 8,316 → 14,174 | 1 | contents link to p7 dead |
| S01 | sideways fix 3 | 56,315 → 58,505 | 0 | 90/180/270 right; render match |
| E03 | 300p All 90 | 2,866,511 → 2,778,699 | 0 | 300/300 match |
| E04 | 300p p1 4, p300 −4 | → 2,778,793 | 2 | match |
| B01 | batch ×3 | ZIP 12,239 | 0 | 3 files correct |
