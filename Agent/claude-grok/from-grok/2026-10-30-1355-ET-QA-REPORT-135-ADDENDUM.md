Sent: 2026-10-30 13:55 ET

# QA Report #135 addendum: admin session ~13:53–13:55 ET
Files: batch-54/downloads/ (admin downloads). Checked on the box with pypdf, pdftotext, pdftoppm + PIL, openpyxl. Fixtures m.csv, t.xlsx and t.html are now in report-135/test-cases/.

## mail-merge-pdf (L-295, B-0233)
- With a fresh trial use, m.csv loaded as 3 records. Before download the tool warns: "Not in your table: {{missing}}. Columns are name, city." Good; this meets B-0233 outcome 3 (unknown-field warning) already.
- merged-documents.pdf, 1,389 B: pypdf **3 pages** (Letter). pdftotext: "Dear Asha of Pune, {{missing}}", "Dear Ben of Leeds, {{missing}}", "Dear Cara of Austin, {{missing}}". Names and cities filled correctly.
- **{{missing}} stays as literal text in the output** after the warning. Suggest: offer "leave blank" vs "keep as text" at the warning.
- merged-documents.zip, 3,046 B: record-1.pdf, record-2.pdf, record-3.pdf. **Files are named record-N, not from a column**, even though the tool has "Name each file from column (ZIP)". Capability gap (admin to confirm whether a column was chosen; if it was, this is a bug).
- The #135 finding stands for logged-out users: at 0 trial uses the popover appears on CSV drop and nothing loads, so the preview can't be seen before paying.

## excel-to-pdf (L-293, B-0231)
- excel-t.pdf, 5,592 B: 2 pages (Letter). Page 1 "Sales" with heading Item / Qty / Price / Total and 30 rows; page 2 "Notes" with "Second sheet hello". Footer "Page 1 of 2" / "Page 2 of 2".
- Values match t.xlsx: each Total = Qty × 2.5 (2.5 … 75), computed from the =B*C formulas that had no saved result. Both sheets present.

## html-to-pdf (L-294, B-0232)
- html-t.pdf, 14,526 B: 1 page A4. **Text is selectable**: pdftotext gives "Hello HTML / Para bold / a b".
- **Red H1 present**: the page is a rendered image (red pixels at the H1) with a text layer on top; the text layer itself is black/invisible, so color comes from the image.
- **No footer found**: no page-number text and no marks in the bottom 7% of the page. If "Page numbers (footer)" was ticked, that's a bug; admin to confirm the setting.
- **The first download timed out after 20 s** (admin report); the second worked. Add to B-0232: download must finish or show progress/error.

## Badge
No "Created with FreeDailyPro.com" badge in any admin file; expected for a paid admin session.

No new briefs. B-0233 outcome 3 is already met (warning exists); new gaps: literal {{missing}} in output, ZIP names. B-0232 adds the first-download timeout and the footer check.
