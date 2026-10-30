Sent: 2026-10-30 13:52 ET

# B-0232 HTML to PDF: print-CSS choice, more page sizes, and fix the meta
Priority: P3 · Estimated effort: S · Report: #135 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~13:47–13:51 ET. L-243 rank 1: PDF Toolkit API is live on ApyHub. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A developer or office user with HTML (an invoice, email template, report) should get a PDF that looks like what they designed, with clear control of layout.
## Why (repro: t.html with a styled H1; 1280 px)
- Dropping t.html fills the HTML Content box (good). Options: Page size A4/Letter/Legal, Page numbers (footer), Landscape, Margin (mm).
- Convert → Edit / Preview first page, disclosed badge (by design), download gated at 0 trial uses (owner decision).
- Clear honesty notes: scripts not run, linked images and styles still fetched from their own sites, no live URL fetching.
- **Missing vs competitors:** no "use print stylesheet vs screen CSS" toggle (pdfedit); no A3/A5/Tabloid (pdfedit); no side-by-side live preview while editing (Signegy); no .zip bundle of HTML + assets (RectoPDF); no list of unsupported CSS (OfficeIMO).
- Ad text "Compare Browsers" glued to "...browser memory", "Try Office Apps" glued to the About text, "Automate Work", "Try Cloud Tools" → L-004. 10 unnamed controls → B-0155.
## Who uses this
Developers testing invoice templates; staff saving an email or report as PDF.
## Outcomes (ranked)
1. A "Use print CSS (@media print)" toggle, on by default.
2. A live preview beside the HTML box.
3. Add A3, A5 and Tabloid.
4. After converting, list anything that didn't render (blocked fonts, cross-origin images).
## SEO
- **Now:** 200, sitemap, self canonical, 11 hreflang, valid JSON-LD. Site-wide items (og-default.png, template H2s, 1 image with no alt) → **B-0209**. **/es serves English** → **B-0123**. Unnamed controls → B-0155. No overflow at 390 px (→ B-0194 not needed).
  - Title "HTML to PDF Converter - Paste and Convert | FreeDailyPro" (56). Good.
  - **Meta 79 chars.**
  - H1 "HTML to PDF".
- **Best result:** H2s "Paste HTML", "Page size and margins", "What renders"; FAQ on scripts and images.
- **Keywords:** "html to pdf", "convert html to pdf", "paste html to pdf", "html file to pdf".
- **Suggested:**
  - Title: keep the current title.
  - Meta: `Paste HTML code or drop a .html file and save it as a PDF with page size, margins and page numbers. Scripts never run, and your HTML is not uploaded.` (149)
  - H1: `HTML to PDF Converter – Paste Code or Drop a File`
  - FAQ:
    - "Does JavaScript run?" → "No; paste the rendered HTML."
    - "Will my images show?" → "Yes, if their sites allow it; data URIs always work."
    - "Can I convert a live URL?" → "No, paste its HTML instead."
    - "Is my HTML uploaded?" → "No."
## Constraints
Keep the no-scripts and linked-assets notes.
## Test cases
1. HTML with @media print hiding a nav → nav hidden when toggle on, shown when off.
2. A3 landscape → page 1190×842 pt.
3. Meta 140–160 chars.
