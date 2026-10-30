Sent: 2026-10-30 08:22 ET
# B-0112 Book Writing Toolbox: keep images and tables on DOCX import
Priority: P1      Estimated effort: 1–2 days      Report: #94      Source: Testing Bot (admin session + logged-out verification)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
An author importing a manuscript should get back what they wrote. Images must never be lost silently, and tables should survive as tables (or at least as a faithful image), because buyers pay per download.

## Why
- Report #94: the table was flattened to plain lines R0C0..R2C1 and the image wasn't found in the editor (0 `<img>`). This was confirmed logged out; Chapter 2 is unchecked.
- Unicode (Chinese and Arabic) survives, so the issue is specific to tables and images.
- Competitors: Reedsy and Vellum keep images; Atticus imports images but not tables. Table support would be a differentiator.

## Who uses this
Self-publishing authors (non-fiction especially: tables, figures), workbook and cookbook creators, KDP/IngramSpark uploaders.

## Outcomes (ranked)
1. **Images preserved** in place on import (DOCX `w:drawing`/media), sized to the trim. Confirm which chapter they land in.
2. **Tables preserved** as editor tables rendered in the PDF/EPUB; fallback: render the table as an image with a notice.
3. **Import report**: "2 chapters, 1 image, 1 table imported; 0 skipped", listing anything unsupported.
4. **Clean paid download**: re-verify when the owner provides a test credit (parked; nothing bought).
5. Ads must not overlay editor buttons (B-0041).

## Constraints
Preview watermark is intentional (do not change). No changes to pricing. Draft stays in the browser.

## Test cases
| # | Input | Expected |
|---|---|---|
| 1 | book-test.docx | editor shows the 3×2 table as a table |
| 2 | same | red 1200×800 image visible in its chapter |
| 3 | same | Chinese/Arabic/accented text unchanged |
| 4 | same | import summary lists 2 chapters, 1 table, 1 image |
| 5 | preview | table + image in the preview (watermark expected) |
