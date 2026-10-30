Sent: 2026-10-30 14:06 ET

# B-0245 Bates Numbering: show settings and preview before the trial-uses gate; add range file names, skip cover page, continuous across files
Priority: P2 · Estimated effort: M · Report: #139 · Source: Playwright headless, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:03–14:05 ET. L-243 rank 1 (PDF Toolkit, live on ApyHub), then alphabetical. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A paralegal stamping a production should set prefix, start number and position and see the stamp on a real page before deciding to pay.
## Why (repro: p.pdf, 3 pages; 1280 px; 0 trial uses)
- **Dropping the PDF opens "You've used today's trial uses" at once; no settings or preview are shown** (same pattern as L-295, L-299). Settings could not be tested; admin run needed.
- About text promises: prefix, start number, position, optional second line (e.g. CONFIDENTIAL), index CSV.
- **Missing vs competitors (~14:04 ET):** live preview on the real page (OneClickPDF, ihatepdf); files renamed to their Bates range, e.g. `DEF-000001-DEF-000015.pdf` (Essex); skip/uncount cover pages (Essex, ihatepdf); suffix and padding width 1–15 (OneClickPDF); continuous vs restart-per-file and ZIP of all files (BatesStamp, ihatepdf); white plate for dark scans (ihatepdf); upright stamp on landscape pages (Essex).
- Unnamed controls → B-0155. No overflow at 390 px.
## Who uses this
Law firms, paralegals and in-house teams producing discovery documents.
## Outcomes (ranked)
1. Show settings and a live preview at 0 trial uses; gate only the download.
2. Continuous numbering across files with a ZIP and index CSV.
3. Name files by Bates range or first number.
4. Skip cover page; suffix; padding width; upright stamp on rotated pages.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD. **/es serves English** → **B-0123**. Site-wide → **B-0209**.
  - Title "Bates Numbering for PDFs: Stamp Pages and Get an Index" (54), no brand.
  - **Meta 131 chars.**
  - H1 "Bates Numbering".
- **Best result:** H2s "Number a whole production", "Bates index CSV", "Privacy: files stay in your browser".
- **Keywords:** "bates numbering", "bates stamp pdf", "add bates numbers to pdf", "bates numbering without acrobat".
- **Suggested:**
  - Title: `Bates Numbering PDF – Stamp & Index Online | FreeDailyPro` (57)
  - Meta: `Add Bates numbers like ABC000001 to every page of one or more PDFs, with a prefix, start number, position and a CONFIDENTIAL line, plus an index CSV.` (149)
  - H1: `Add Bates Numbers to PDFs`
  - FAQ:
    - "Does numbering continue across files?" → confirm with admin run.
    - "Do I need Acrobat?" → "No."
    - "Are my files uploaded?" → "No."
## Constraints
Keep the download gated per the owner's decision.
## Test cases
1. Fresh session at 0 trial uses, drop p.pdf → settings + preview visible.
2. Admin: stamp p.pdf with prefix ABC → pages 1–3 read ABC000001–ABC000003 (pdftotext); index CSV has 1 row.
3. Title ≤ 60; meta 140–160.
