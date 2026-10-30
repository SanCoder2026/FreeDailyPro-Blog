Sent: 2026-10-30 14:06 ET

# B-0243 PowerPoint to PDF: a strong converter; add .ppt/.odp, paper-size fit and a file-named download, fix the meta
Priority: P2 · Estimated effort: M · Report: #139 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:03–14:05 ET. L-243 rank 1 (PDF Toolkit, live on ApyHub), then alphabetical. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone turning a deck into a handout should get one clean PDF page per slide, searchable, named after the deck, on the paper they need.
## Why (repro: t.pptx, 3 slides, 29.2 KB; 1280 px; 0 trial uses)
- Good: dropping the file shows "3 slides, first slide shown above", Quality (Fast/Default/Sharp), "Include hidden slides" and "Make the text searchable and copyable" **before** the gate. The gate appears only on "Convert to PDF" (owner's decision; not a gap).
- Output could not be checked at 0 trial uses; admin run needed (page count, slide size, text layer, file name).
- Accepts .pptx only (page copy says .pptx).
- **Missing vs competitors (~14:04 ET):** .ppt and .odp input (KovaPDF, DocHub, Adobe); fit to A4/Letter/Legal, portrait or landscape (KovaPDF, Compix); edit a slide before saving (Compix); several decks at once (PaperWingPDF); compress/merge the result as a next step (KovaPDF).
- Unnamed controls → B-0155. No overflow at 390 px.
## Who uses this
Students, teachers and staff sending slides as handouts or uploading them to a portal that only takes PDF.
## Outcomes (ranked)
1. Keep options visible before the gate (already done); download named `<deck>.pdf`.
2. Paper option: slide size (default) or A4/Letter fit, never cropped.
3. Accept .ppt/.odp, or say clearly on drop how to save as .pptx.
4. "Next: Compress PDF / Merge PDF" after download.
## SEO
- **Now:** 200, sitemap, self canonical, 11 hreflang, valid JSON-LD. Site-wide items (template H2s, image without alt) → **B-0209**. **/es serves English title** → **B-0123**.
  - Title "Convert PowerPoint to PDF Online - Free, Keeps Charts" (53): OK but no brand.
  - **Meta 97 chars**, too short.
  - H1 "PowerPoint to PDF".
- **Best result:** H2s "One page per slide", "Searchable text", "Hidden slides and notes"; FAQ below.
- **Keywords:** "powerpoint to pdf", "pptx to pdf", "convert ppt to pdf", "slides to pdf".
- **Suggested:**
  - Title: `PowerPoint to PDF – PPTX to PDF, Searchable | FreeDailyPro` (58)
  - Meta: `Convert a PowerPoint (.pptx) to PDF with one page per slide at the deck's own size. Charts, pictures and backgrounds kept; text stays searchable. In-browser.` (157)
  - H1: `Convert PowerPoint (PPTX) to PDF`
  - FAQ:
    - "Are speaker notes included?" → "No, only slides."
    - "Can I select the text?" → "Yes, with 'searchable text' on."
    - "Are hidden slides included?" → "Only if you tick the option."
## Constraints
Keep the convert step gated per the owner's decision.
## Test cases
1. Admin: convert t.pptx → 3-page PDF, page size = slide size, text extractable ("Slide 1 title").
2. Hidden-slides tick on/off changes page count on a deck with a hidden slide.
3. Title ≤ 60; meta 140–160.
