Sent: 2026-10-30 14:14 ET

# B-0249 Document Assembler: "Assemble Document" does nothing visible; add feedback, project-neutral copy and title/meta fixes
Priority: P1 · Estimated effort: M · Report: #141 · Source: Playwright headless, logged out, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:10–14:14 ET. L-243: rank 1, PDF Toolkit (live on ApyHub), first untested. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone combining a PDF, a Word file and a photo into one paginated document should press Assemble and get the PDF, or a clear message why not.
## Why (repro: p.pdf 3 pp + tbl.pdf; 1280 px; fresh session)
- Rich form, all usable before any gate: Document Title, Author, Page Size (US Letter), file list with ↑/↓ reorder, camera capture, Cover Page ✔, Table of Contents ✔, List of Images, "Add pages from my project" (Agenda, Guest list, Budget summary), Save/Open project, Try a sample.
- **Clicking "Assemble Document" (title left empty) gave no download, no gate, no error and no visible change within 20 s** (twice). Either a required title is silently blocking or the build fails quietly. → done/error state per **B-0187**; admin run needed to confirm the output.
- **Counter mismatch:** the first session showed "Trial: 2 uses/day · 0 remaining today", a fresh session "2 remaining today" with no use spent → **B-0156**.
- **Off-topic copy:** "Project: My event … The saved file includes a pass key: the secret that signs the QR codes on guest passes" — event-planner text on a document tool confuses users.
- **Missing vs competitors (~14:12 ET):** .xlsx/.pptx/.odt input (VellumPDF, FileLume, iHatePDF); sort by name/date and per-page view (VellumPDF); page thumbnails/preview before building (iHatePDF); bookmarks per section in the output; "next tool" without re-upload (iHatePDF).
- Ad text "Try Office Apps" glued to subtitle → L-004. No overflow at 390 px.
## Who uses this
Office staff, students and event organisers compiling a report or pack from mixed files.
## Outcomes (ranked)
1. Assemble always ends in a download, the gate, or an inline error ("Add a document title").
2. Show the counter consistently (B-0156).
3. Hide guest-pass/QR copy unless event pages are added.
4. Accept Excel/PowerPoint; bookmark each section.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD; site-wide → **B-0209**; /es English title → **B-0123**.
  - **Title "Assemble Multiple Documents Into One PDF Online | FreeDailyPro" is 62 chars.**
  - **Meta 93 chars.**
  - H1 "Document Assembler".
- **Keywords:** "combine pdf word and images", "merge word and pdf into one pdf", "document assembler", "combine documents into one pdf".
- **Suggested:**
  - Title: `Combine PDF, Word & Images Into One PDF | FreeDailyPro` (54)
  - Meta: `Combine PDFs, Word files and images into one document with a cover page, an automatic table of contents and real page numbers. Reorder freely; runs in-browser.` (159)
  - H1: `Combine PDF, Word and Images Into One Document`
  - FAQ: "Does it add a table of contents?" → "Yes, automatically." · "Can I reorder files?" → "Yes." · "Are files uploaded?" → "No."
## Constraints
Gating the final download is the owner's decision.
## Test cases
1. Fresh session, add p.pdf + tbl.pdf, title empty, Assemble → inline error or PDF/gate within 10 s.
2. Admin: with a title → PDF with cover + TOC + 3+ pages, page numbers present (pdftotext).
3. Title ≤ 60; meta 140–160.
