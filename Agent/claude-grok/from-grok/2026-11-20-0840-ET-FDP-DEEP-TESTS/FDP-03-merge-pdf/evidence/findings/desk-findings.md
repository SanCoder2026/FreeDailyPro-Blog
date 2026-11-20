Sent: 2026-11-20 08:40 ET

# Merge PDF (merge-pdf): desk findings

- **Written:** 2026-11-19 10:49:25 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/merge-pdf. TEST-ORDER row 3 and tools.csv line 252.
- **Classification:** Professional Tool, PDF Tools. 10 trial uses per day, gated **at download** (`gateAtDownload`). $1 day pass / $4.99 monthly.
- **TEST-ORDER note:**
  - Test-plan rank 5, 235 views (cited, not refreshed). **Current GSC data is not available.**
  - The note "API ignores page selection (B-0040)" is out of scope: no API testing per the rules.
- **Method:** read-only curl of the tool, /es, the blog and sitemap.xml; the JS bundles (`js/`: MergePdf, pdfBookmarks, pdfMetadata, ReorderableFileList, imagePdf, operations, PdfPageStrip); YouTube metadata, captions and frames; WebSearch.

## SEO (check 8)

| Element | Live value | Note |
|---|---|---|
| Title | "Merge PDF – Combine PDF Files, No Upload \| FreeDailyPro" (55) | OK |
| Meta | "Combine PDF files into one in seconds. Reorder files, pick the pages you need and download a clean PDF, **with no watermark**. Your files never leave your device." (158) | **False for trial-use downloads.** Each page carries a "Created with FreeDailyPro.com" badge (`live-functional-findings.md` §2) |
| H1 | Merge PDF – Combine PDF Files into One | OK |
| H2 | How it works · Watch… · About · How to use it · Common questions · Details · Guides and next steps | OK |
| Canonical / robots | self / indexable | OK |
| hreflang | 11 | **/es** is localized server-side (title "Fusionar PDF **gratis**: sin registro y sin subir archivos", H1, meta), but "gratis" means "free", which is off-brand. **pt, fr, de, ja, hi, zh, ko, id** serve the English title and meta (see devices-locales) |
| JSON-LD | WebSite, SoftwareApplication (Offer 4.99, no billing period), VideoObject ("How to Merge PDF Files Online – Combine Multiple PDFs \| FreeDailyPro.com", uploadDate 2026-08-22), FAQPage (**13** Q&As, matching the visible FAQ), BreadcrumbList (Home › PDF Tools › Merge PDF) | VideoObject uploadDate 2026-08-22 vs the YouTube upload of 2026-09-30 (LOW) |
| OG | og-default.png | generic |
| Images | video thumbnail `alt=""` | LOW |
| Internal links | /blog/merge-pdf (linked ✔), Split/Compress/Organize/Rotate PDF, Document Assembler (Premium upsell: "2 trial uses a day · $3 day pass or $9.99 a month") | good |

## Indexing (check 7)

- sitemap.xml: the tool has lastmod 2026-11-19 and a video block; the blog has lastmod 2026-10-17.
- **The sitemap video title contains a literal escape sequence**, "How to Merge PDF Files Free Online \u2013 Combine…". 24 lines in sitemap.xml contain a literal `\u2013` (site-wide, LOW). It also says "Free".
- WebSearch "freedailypro merge pdf" (2026-11-19): the tool ranks first. Indexed. No impression data (GSC not available).

## FAQ and usage guide vs. live behaviour (check 11)

13 questions. The live results (`live-functional-findings.md`) confirm most of them:
- Password prompt, unlocked output
- Duplicate warning
- Form warning, and forms not fillable
- Per-file bookmarks with nested originals
- Page sizes and /Rotate preserved
- Images on Letter, landscape for wide pictures
- Page ranges
- Arrange and Choose pages
- Output name "<first>-merged.pdf"
- Blank page for duplex printing
- Producer = FreeDailyPro

**Wrong or misleading:**
1. "Does merging add a watermark? **No.** … nothing stamped on them", and the H3 "No upload, no watermark… **no logo or text is added**". Every trial-use output page carries a "Created with FreeDailyPro.com" logo badge. **HIGH.**
2. The question "What **doesn't** carry over when I merge PDFs?" is answered "**Bookmarks do**: …". The heading and answer contradict each other; this is a copy bug (LOW).
3. "if you use Arrange all pages, only the per-file bookmarks are kept". Live, the arranged output had **no outline at all** (LOW).
4. "Is there a limit to how many PDFs…": "no fixed limit". The drop zone warns about files over 50 MB, which is consistent.

## Blog (check 9)

- /blog/merge-pdf returns 200, self canonical, "Merge Signed Pages Into One Client PDF Without Losing Order", 2026-10-17. It links the tool, Compress, Split and PDF Password. It has **no video embed**.
- It is a workflow article (legal or client packets), good for intent.
- Stale lines:
  - "Bookmarks may drop on merge": the tool now keeps them.
  - "Encrypted parts must be unlocked first": the tool unlocks inline.
- It doesn't mention Arrange all pages, Choose pages, ranges, pictures, the blank-page option, or trial uses (MEDIUM).

## Competitors (check 2)

WebSearch on 2026-11-19 found browser-only mergers: docMentis, Kortex, EmbedPDF, PDFslime and pdfhey.
- Common claims: no upload, page-level arrange, rotate, delete, **duplicate pages**, **form fields kept fillable** (EmbedPDF renames clashing fields), links kept, bookmark options (per-file on/off), sort by name / reverse, and "no watermark".
- **FreeDailyPro has:** in-merge page arranging, ranges, per-page rotate and delete, pictures, the duplex blank page, password unlock, a form warning, per-file bookmarks, and very fast merges (503 pages in 0.34 s).
- **Live-verified gaps:**
  - Form fields not kept fillable
  - No bookmark options
  - A logo badge on every trial-use page, while competitors advertise no watermark
  - No result share
- **Unverified absences:** duplicate page, sort by name/reverse, link preservation (not tested).

## Category, placement, duplicates, AI and demand (checks 17–22)

- **Placement:** PDF Tools, Professional Tool, plus many hubs (home, professional-tools, corporate-safe-tools, the freelance-close-out and job-application-kit bundles, bookkeepers and paralegals). 28 blog posts link here. Correct.
- **Duplicates:** C10 (document-assembler, mail-merge-pdf, merge-pdf). The jobs differ (assembly with TOC and numbering; data-driven letters; plain merge). Keep all three. The Document Assembler upsell card on the page is a sensible next step.
- **AI fit:** not needed for merging. P2 ideas: auto-order by detected dates or names, or "name the merged file from contents".
- **Demand:** high (rank 5 in the test plan, the most internal links). Keep.
