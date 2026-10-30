Sent: 2026-10-30 14:14 ET

# B-0250 Exhibit Stamper: show settings and preview before the trial-uses gate; add cover sheets, combined bundle, AA after Z
Priority: P2 · Estimated effort: M · Report: #141 · Source: Playwright headless, logged out, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:10–14:14 ET. L-243: rank 1, PDF Toolkit, untested. No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A paralegal labelling exhibits should set the label and position and see it on the page before deciding to pay.
## Why (repro: p.pdf + tbl.pdf; 1280 px; 0 trial uses)
- **Dropping the PDFs opens "You've used today's trial uses" at once; no settings, index preview or stamp preview are shown** — same pattern as Bates (L-307), mail-merge (L-295), bookmarks (L-299). Settings untested; admin run needed.
- About text promises: letters or numbers, first label, text before/after, first or every page, position, size, white box by default, index CSV with empty Description column, single PDF or ZIP.
- **Missing vs competitors (~14:12 ET):** optional cover sheet per exhibit (UnboundPDF, shobfree); one combined bundle with a bookmark per exhibit (shobfree, exhibitstamper.com); party presets — Plaintiff's, Defense, Joint (exhibitstamper.com, Tabzoola); AA/AB after Z (UnboundPDF, shobfree; confirm ours); rotation and colour (UnboundPDF, exhibitstamper.com); file names with the label, e.g. Exhibit-B-invoice.pdf (shobfree); page x/y in the stamp (shobfree).
- Unnamed controls → B-0155. No overflow at 390 px.
## Who uses this
Litigators, paralegals and claims handlers preparing filings.
## Outcomes (ranked)
1. Settings + live preview at 0 trial uses; gate only the download.
2. Name stamped files with the label (Exhibit-A-p.pdf).
3. Party presets; continue past Z to AA.
4. Cover sheets and a combined bookmarked bundle.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD, all images have alt. /es English → **B-0123**. Site-wide → **B-0209**.
  - Title "Exhibit Stamper: Label PDFs Exhibit A, B, C + Index" (51), no brand. Already ranks #3 in Google for "exhibit stamper PDF exhibit labels" (~14:11 ET).
  - Meta 147 ✔. H1 "Exhibit Stamper".
- **Keywords:** "exhibit stamper", "exhibit stamp pdf", "exhibit labels pdf", "plaintiff exhibit stamp".
- **Suggested:**
  - Title: `Exhibit Stamper – Label PDFs Exhibit A, B, C | FreeDailyPro` (59)
  - Meta: keep current (147).
  - H1: `Stamp Exhibit Labels on PDFs`
  - FAQ: "What comes after Exhibit Z?" · "First page or every page?" · "Are my PDFs uploaded?" → "No."
## Constraints
Keep the download gated per the owner's decision.
## Test cases
1. Fresh session at 0 trial uses, drop 2 PDFs → settings, index preview (A=p.pdf, B=tbl.pdf), stamp preview visible.
2. Admin: stamp → pdftotext finds "Exhibit A" on p.pdf p1, "Exhibit B" on tbl.pdf p1; CSV has 2 rows.
3. Title ≤ 60.
