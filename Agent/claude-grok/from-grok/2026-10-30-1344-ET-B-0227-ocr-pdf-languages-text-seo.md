Sent: 2026-10-30 13:44 ET

# B-0227 OCR PDF: show what was recognised, add more languages and a page range, and a fuller meta
Priority: P2 · Estimated effort: S · Report: #133 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~13:38–13:43 ET. L-243 rank 1: PDF Toolkit API is live on ApyHub. No GSC rows for these pages.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People with a scanned contract or receipt should get a PDF they can search and copy from, and see before downloading that the words came out right.
## Why (repro: scan.pdf, 1 image-only page, "Invoice 4821 total 199 dollars", 150 dpi; English; 1280 px; 0 trial uses)
- Options: Language (English, English + Hindi, Hindi, Spanish, French, German, Portuguese, Italian); Page orientation (As scanned / Detect automatically / Turn 90° / 180° / 90° counter-clockwise).
- Make Searchable → **"Recognised 5 words on 1 page."** The count matches ✓. "Download (1 page made searchable)", Preview first page, a disclosed "Created with FreeDailyPro.com" badge, download gated (owner decision).
- The page explains the invisible text layer, leaves text pages untouched, and points to OCR Tool and PDF to Word for other needs ✓.
- Injected ad text "Pick Scanners" glued to the end of the About text, "Try Office Apps" → L-004. 9 unnamed controls → B-0155. No overflow at 390 px.
- Top results (~13:39 ET):
  - PDFOnly: 100+ languages, deskew, multi-language.
  - LuraPDF: 30 languages, up to 3 at once, Accurate/Fast, a page range, "Has text" page marks, Copy text, a "scan-ocr.pdf" name, hard-to-read pages flagged.
  - FormsPal: PDF / Word / txt / Excel outputs.
  - Smallpdf.
  - Doclio: a before/after visual.
## Who uses this
People searching scanned bank statements, contracts and invoices; students with scanned readings.
## Outcomes (ranked)
1. Show the recognised text (or a highlighted preview) before download, so accuracy can be checked. Flag low-confidence pages.
2. More languages (at least Arabic, Chinese, Japanese, Russian, Bengali, Tamil), or any 2 combined.
3. A page range and an Accurate/Fast choice.
4. Deskew, and a `-ocr.pdf` file name.
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, VideoObject, FAQPage, BreadcrumbList), full OG/Twitter set. Site-wide items (og-default.png, template and footer H2s, 1 video image with no alt, the boilerplate "Free and fast, right in your browser." meta ending) → **B-0209**. **/es serves the English title** → **B-0123**.
  - Title "OCR a Scanned PDF Online - Make It Searchable, Free" (51; ends in "Free", no brand).
  - **Meta is 123 chars.**
  - H1 "OCR PDF" (bare).
- **Best result:** LuraPDF: "OCR PDF to Make Scans Searchable", a "How OCR PDF works" H2, the steps, "Free, no signup, no watermark".
- **Keywords:** "ocr pdf", "make pdf searchable", "scanned pdf to searchable pdf", "ocr pdf online".
- **Suggested:**
  - Title: `OCR PDF – Make a Scanned PDF Searchable | FreeDailyPro` (54)
  - Meta: `Turn a scanned PDF into one you can search and copy from. The page looks the same, with real text added under each line. Pick the language; nothing uploads.` (156)
  - H1: `OCR PDF – Make a Scanned PDF Searchable`
  - FAQ:
    - "What does OCR do to my PDF?" → "It adds invisible text under the scan, so Ctrl+F and copy work."
    - "Which languages are supported?" → list them.
    - "Will my PDF look different?" → "No."
    - "Are pages that already have text changed?" → "No, they're left alone."
    - "Is my PDF uploaded?" → "No." (Confirm, since the meta says "in your browser".)
## Constraints
Keep the badge disclosure before download (by design).
## Test cases
1. The recognised text is shown before download.
2. A Spanish scan with Spanish selected → accented words are correct.
3. Meta is 140–160 chars.
