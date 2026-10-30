Sent: 2026-10-30 14:10 ET

# QA-REPORT-139 ADDENDUM — admin session ~14:07–14:09 ET
Files: batch-58/downloads/. Checked on the box with pypdf, pdftotext and python-pptx. This addendum amends B-0243–B-0245 (sent files are not edited).

## powerpoint-to-pdf (B-0243, L-305)
- t.pdf is 123,355 B, and the tool reported "3 pages · searchable text added".
- pypdf: 3 pages, each 720 × 540 pt. That matches t.pptx's slide size (720 × 540 pt, 4:3). ✔
- pdftotext reads "Slide N title • Bullet on slide N" on pages 1–3, so the text layer is present. ✔
- The download is named after the deck (t.pptx → t.pdf), so B-0243 Outcome 1 (file-named download) is **already met**. Paper fit and .ppt/.odp input remain gaps.

## bates-numbering (B-0245, L-307)
- The tool works well once past the gate.
- **Remove these from B-0245's gaps, because they are already offered:** live preview, continuous numbering across files, a white box behind the stamp, and a second line.
- pdftotext on p-bates.pdf (2,521 B; 3 A4 pages) finds ABC000001, ABC000002 and ABC000003 on pages 1–3. ✔
- bates-index.csv is correct: `p.pdf,p-bates.pdf,3,ABC000001,ABC000003`, with header Document, Numbered file, Pages, Begin Bates, End Bates. ✔
- **Gaps still open:** the output is named p-bates.pdf, not by Bates range (e.g. ABC000001-ABC000003.pdf); the gate appears on file drop at 0 trial uses (Outcome 1); skip cover page; suffix/padding; upright stamp on rotated pages.

## government-forms-hub (B-0244, L-306) — NEW issue
- 'Fill in PDF Editor' on the W-4 card opens /tool/pdf-editor **empty**. The form isn't preloaded, so the user must download it from irs.gov and upload it again.
- **Add to B-0244 as Outcome 2 (ranked above search):** preload the chosen official form in the PDF Editor (fetch it from the agency URL client-side, without hosting or changing it). If that can't be done, rename the link honestly, e.g. "Download, then fill in our PDF Editor", and add a one-line how-to.
- Test case: click 'Fill in PDF Editor' on W-4. The editor should open with fw4.pdf loaded, or the label should match what happens.
