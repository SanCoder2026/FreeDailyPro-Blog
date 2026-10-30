Sent: 2026-10-30 13:58 ET

# B-0239 PDF to PowerPoint: preview editable text, offer OCR for scans, tidy the title
Priority: P3 · Estimated effort: S · Report: #137 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~13:56–13:58 ET. L-243 rank 1: PDF Toolkit API is live on ApyHub. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone turning a PDF deck back into slides should know before downloading whether the text will be editable and how it will look.
## Why (repro: p.pdf, 3 pages; 1280 px)
- Upload shows "2.2 KB · 3 pages" with page thumbnails. Two clear modes: Picture per slide (exact look) and Editable text (best effort, honest about approximate spacing).
- Convert (Picture per slide) → "p.pptx · 3 slides · 8.3 × 11.7 inches · 107.3 KB", slide preview "Slide 1 of 3". Download gated (owner decision). Slide size follows the PDF page (A4 portrait); good.
- **Missing vs competitors (~13:57 ET):** edit before export (Polotno); OCR for scanned PDFs (iLovePDF detects scanned pages and offers OCR); images/shapes as separate objects (SlidesPilot, Doclio). No "fit to 16:9" option for portrait PDFs.
- Ad text "Try Office Apps" (glued to About) → L-004. 8 unnamed controls → B-0155.
## Who uses this
People who only have a PDF of a deck and need to update it.
## Outcomes (ranked)
1. When a page has no text layer, say so and point to OCR PDF (or offer OCR).
2. A "Fit to 16:9 slides" option.
3. Preview the Editable-text result before download.
## SEO
- **Now:** Passes: 200, sitemap, self canonical, 11 hreflang, valid JSON-LD. Site-wide (og-default.png, template H2s, image without alt) → **B-0209**. **/es serves English** → **B-0123**. No overflow at 390 px.
  - Title "Convert PDF to PowerPoint Online - Editable Text, Free" (54; "Free", no brand).
  - Meta 140 chars (ends with "Free."). OK length.
  - H1 "PDF to PowerPoint".
- **Best result:** H2s "Picture per slide vs editable text", "Scanned PDFs".
- **Keywords:** "pdf to powerpoint", "pdf to ppt", "pdf to pptx editable", "convert pdf to slides".
- **Suggested:**
  - Title: `PDF to PowerPoint – Editable or Exact Slides | FreeDailyPro` (59)
  - Meta: keep the current meta.
  - H1: `Convert PDF to PowerPoint (PPTX)`
  - FAQ:
    - "Will the text be editable?" → "Choose Editable text; spacing is approximate."
    - "What about scanned PDFs?" → "Run OCR PDF first."
    - "Is my PDF uploaded?" → "No."
## Constraints
Keep both modes and their honest descriptions.
## Test cases
1. A scanned PDF in Editable text → OCR message.
2. Title ≤ 60.
