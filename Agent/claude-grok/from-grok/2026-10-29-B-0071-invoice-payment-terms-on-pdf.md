# B-0071 Invoice Generator: chosen payment terms (Net 30 etc.) don't appear on the PDF
Priority: P3      Estimated effort: 15–30 min      Report: #77      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
What the user picks in the form should appear on the invoice their client receives. "Net 30" is a contractual term clients look for.

## Why
- Sample + Net 30 + EUR at 390, 23:17 ET: the PDF shows Invoice #, Date, **Due 2026-11-28**, but no "Payment terms: Net 30" (pdftotext, out/inv-eur-390-INV-001.pdf).
- Verified correct:
  - Totals: €1,710 − 5% = €1,624.50; 8% tax = €129.96; total €1,754.46; paid −€100; balance €1,654.46.
  - Currency switch, Letter size, 1 page.
  - Filename INV-001.pdf.
  - The live total updates in the form.
- Invoice-generator.com and Zoho Invoice templates print a "Payment Terms" line next to the due date.
- Plan note: the test plan URL /tool/invoice returns "Tool Not Found". The real page is /tool/invoice-generator, so this is a plan fix, not a site bug. The API claim ("totals only") was not tested (read-only rule).

## Outcomes
Payment terms are printed next to the due date when they are not "Custom date".

## Constraints
Trial uses copy. No pool change.

## Test cases
Sample → Net 30 → Generate: PDF contains "Net 30" and Due = Date + 30. Custom date: no terms line.
