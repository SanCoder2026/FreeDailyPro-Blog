Sent: 2026-10-30 13:44 ET

# B-0225 Compare PDF: page and visual compare, a change summary, and a title that doesn't end in 'Free'
Priority: P2 · Estimated effort: S · Report: #133 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~13:38–13:43 ET. L-243 rank 1: PDF Toolkit API is live on ApyHub. No GSC rows for these pages.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People checking two versions of a contract or report should find every change fast and trust that nothing was missed. The tool already does text well; say clearly what it doesn't catch, and close the biggest gaps.
## Why (repro: p.pdf vs q.pdf, 3 pages each, page 2 text "Page 2 hello" → "Page 2 hello CHANGED"; 1280 px; 0 trial uses)
- The Original and Revised drop areas each take one file. The revised input appears only after the original loads.
- Compare PDFs → **"1 change | 0 added | 0 removed | 1 edited"**, "Change 1 of 1", Previous / Next change, Unified / Side by Side, Show unchanged text, a "CHANGED · P. 2" marker. Correct ✓.
- Report (PDF) is gated (owner decision); Report (.txt) is also offered.
- The page honestly says that only text is compared and that scans need OCR PDF first ✓.
- Injected ad text "Try Office Apps", glued to the end of the honesty paragraph → L-004. 10 unnamed controls → B-0155. No overflow at 390 px.
- Top results (~13:39 ET):
  - Diffchecker: rich text, plain, image (pixel) view, built-in OCR, redline export, PDF vs Word.
  - diffchecker.dev: 5 views, including a metadata "Details" table; password-protected files unlocked locally.
  - Adobe: filters by change type, summary counts.
  - diff.tools: pick pages to compare, formatting-change cards, built-in OCR.
  - PDFJar: overlay with a blend slider.
## Who uses this
Freelancers and small-business owners checking a returned contract; students comparing drafts.
## Outcomes (ranked)
1. A visual (pixel) page compare or an overlay view, so layout, image and font changes are caught. Until then, keep the honest note.
2. Run OCR inside the tool for scans, or offer a one-click "Run OCR PDF on this file" link.
3. A redline report (struck-through and underlined) in the same style as the PDF report.
4. Ask for the password when a PDF is locked (link to Unlock PDF).
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, VideoObject, FAQPage, BreadcrumbList), full OG/Twitter set. Site-wide items (og-default.png, template and footer H2s, 1 video image with no alt, the boilerplate "Free and fast, right in your browser." meta ending) → **B-0209**. **/es serves the English title** → **B-0123**.
  - Title "Compare Two PDF Files Online - See What Changed, Free" (53; ends in "Free", no brand).
  - **Meta is 113 chars.**
  - H1 "Compare PDF" (bare).
- **Best result:** diff.tools: a TL;DR answer up front, "Can I compare scanned PDFs?" and "Are my files uploaded?" FAQs, a change list described in the copy.
- **Keywords:** "compare two pdf files", "pdf compare", "pdf diff", "compare pdf for differences".
- **Suggested:**
  - Title: `Compare PDF – See What Changed in Two PDFs | FreeDailyPro` (57)
  - Meta: `Compare two PDF files and see every added, removed or edited line, page by page. Step through each change, view side by side, and nothing leaves your device.` (157)
  - H1: `Compare Two PDF Files – See What Changed`
  - FAQ:
    - "How do I compare two PDFs?" → "Drop the original and the revised file, then click Compare PDFs."
    - "Does it catch formatting or image changes?" → "No. It compares the text only."
    - "Can I compare scanned PDFs?" → "Run OCR PDF first."
    - "Are my files uploaded?" → "No."
## Constraints
Keep the honest scope note until visual compare ships.
## Test cases
1. An image-only change → caught (after outcome 1), or the note stays.
2. Edit, insert and delete fixtures → the counts match.
3. Meta is 140–160 chars.
