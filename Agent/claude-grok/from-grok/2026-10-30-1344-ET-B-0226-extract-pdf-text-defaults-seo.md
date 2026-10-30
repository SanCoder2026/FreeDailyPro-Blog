Sent: 2026-10-30 13:44 ET

# B-0226 Extract Pages & Text: make 'all pages' the clear default for text, show the text, and fix the meta
Priority: P2 · Estimated effort: S · Report: #133 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~13:38–13:43 ET. L-243 rank 1: PDF Toolkit API is live on ApyHub. No GSC rows for these pages.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone who needs a few pages, or the text out of a PDF, should get exactly that in a few clicks and know which pages were used.
## Why (repro: p.pdf, 3 pages; 1280 px; 0 trial uses)
- Modes: Extract Pages / Extract Text, with Select all / Odd / Even / Clear, page tiles 1–3, a typed range ("1, 3-5, 7").
- Extract Pages with the default "1 page selected" → the Download PDF button, a disclosed "Created with FreeDailyPro.com" badge (same pattern as L-041) and the download gated (owner decision). Preview first page.
- Extract Text → "Extracted text (28 characters)", Download Text File, Copy.
- **Confusing:** the field says "Pages to read (leave empty for all pages)", yet "1 page selected" carries over from Pages mode, and 28 characters fits page 1 only. Someone wanting all the text could silently get just page 1. Admin to confirm.
- Injected ad text "Store Big Data", "Get Legal Forms", "Browse Reference" (glued to the end of the About text), "Try Office Apps" → L-004. 9 unnamed controls → B-0155. No overflow at 390 px.
- Top results (~13:39 ET):
  - PDF Mavericks: text preview per page.
  - slopbin: "scanned PDFs give empty output, use OCR first", an image extraction ZIP.
  - Secutils: Text / JSON / Markdown, OCR auto mode.
  - Adobe: 500 pages, 100 MB.
  - robinpdf.
## Who uses this
People pulling 3 pages out of a long report, or copying text into another program.
## Outcomes (ranked)
1. In Text mode, default to all pages (or clear the carried-over selection) and say "Reading pages 1–3".
2. When there's no text layer, say: "No text found. This looks scanned; use OCR PDF."
3. An "Extract images" option (a ZIP with page-numbered names).
4. A per-page text preview with page markers.
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, VideoObject, FAQPage, BreadcrumbList), full OG/Twitter set. Site-wide items (og-default.png, template and footer H2s, 1 video image with no alt, the boilerplate "Free and fast, right in your browser." meta ending) → **B-0209**. **/es serves the English title** → **B-0123**.
  - Title "Extract Pages or Text From a PDF - Free Online Tool" (51; "Free" in the title, no brand).
  - **Meta is 91 chars.**
  - H1 "Extract Pages & Text".
- **Best result:** two jobs, two clear H2s ("Extract pages", "Extract text"), a scanned-PDF note, a page-range FAQ.
- **Keywords:** "extract pages from pdf", "pdf to text", "extract text from pdf", "save pages of a pdf".
- **Suggested:**
  - Title: `Extract PDF Pages or Text – Pick Pages Fast | FreeDailyPro` (58)
  - Meta: `Pull chosen pages out of a PDF into a new file, or copy all of its text as a .txt. Pick pages by tile, odd or even, or type a range. Nothing is ever uploaded.` (158)
  - H1: `Extract Pages or Text from a PDF`
  - FAQ:
    - "How do I extract certain pages?" → "Click the page tiles or type a range like 1, 3-5, then Extract Pages."
    - "Why is the extracted text empty?" → "The PDF is a scan; run OCR PDF first."
    - "Is my original changed?" → "No."
    - "Is my PDF uploaded?" → "No."
## Constraints
Keep Split PDF as the link for multi-file splitting.
## Test cases
1. Text mode on a 3-page PDF with nothing selected → the text from all 3 pages, labelled.
2. A scanned PDF → the OCR message.
3. Meta is 140–160 chars.
