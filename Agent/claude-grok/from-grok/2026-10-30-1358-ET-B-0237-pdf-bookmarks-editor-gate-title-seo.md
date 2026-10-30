Sent: 2026-10-30 13:58 ET

# B-0237 PDF Bookmarks Editor: show the outline before the trial-uses gate, add import/export, shorten the title
Priority: P2 · Estimated effort: M · Report: #137 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~13:56–13:58 ET. L-243 rank 1: PDF Toolkit API is live on ApyHub. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone fixing a PDF's table of contents should see their bookmark tree as soon as they drop the file, and only meet the gate when saving.
## Why (repro: p.pdf, 3 pages; 1280 px; 0 trial uses)
- Premium tool ("Trial: 2 uses/day · 0 remaining today").
- **Dropping the PDF opens the "You've used today's trial uses" popover at once; the outline tree is never shown.** Gating the download is the owner's decision, but this gate blocks even seeing the file (same pattern as mail-merge, L-295). Editing could not be tested; admin run needed.
- About text promises: rename, delete, reorder, indent/outdent, add at a page, target-page preview.
- **Missing vs competitors (~13:57 ET):** CSV/JSON import and export of the outline (SagePDF, BentoPDF, bubble.ro); precise destination by clicking on the page (SagePDF, BentoPDF); keeps untouched destinations, zoom and web links, with a note when one can't be resolved (PDFChamp); undo/redo and search (BentoPDF).
- Ad text "Try Office Apps" (glued to the subtitle), "Try News Readers" (glued to About) → L-004. 9 unnamed controls → B-0155.
## Who uses this
People giving a merged bundle or a scanned manual a usable table of contents.
## Outcomes (ranked)
1. Show the existing outline (or "No bookmarks yet") and allow editing at 0 trial uses; gate only the save.
2. Import/export the outline as CSV (title,page,level) or indented text.
3. Keep untouched bookmarks' original destinations and links; warn if any can't be kept.
4. Undo/redo.
## SEO
- **Now:** Passes: 200, sitemap, self canonical, 11 hreflang, valid JSON-LD. Site-wide (og-default.png, template H2s, image without alt) → **B-0209**. **/es serves English** → **B-0123**. No overflow at 390 px.
  - **Title "PDF Bookmarks Editor: Add, Rename, Reorder Outline | FreeDailyPro" is 65 chars.**
  - **Meta 110 chars.**
  - H1 "PDF Bookmarks Editor".
- **Best result:** H2s "Edit existing bookmarks", "Build a table of contents", "Nest chapters"; FAQ on replacing vs merging the outline.
- **Keywords:** "pdf bookmarks editor", "edit pdf bookmarks", "add bookmarks to pdf", "pdf outline editor".
- **Suggested:**
  - Title: `PDF Bookmarks Editor – Add, Rename, Nest | FreeDailyPro` (55)
  - Meta: `Edit a PDF's bookmarks as a tree: rename, reorder, nest chapters, delete or add one at any page, then save a copy. Your PDF is read in the browser only.` (152)
  - H1: `Edit PDF Bookmarks (Outline) Online`
  - FAQ:
    - "Can I add bookmarks to a PDF with none?" → "Yes, add one at any page."
    - "Does it replace the whole outline?" → "Yes, the tree you save becomes the outline."
    - "Is my PDF uploaded?" → "No."
## Constraints
Keep the save gated per the owner's decision.
## Test cases
1. Fresh session at 0 trial uses, drop p.pdf → tree (or empty state) visible, editable.
2. Title ≤ 60; meta 140–160.
