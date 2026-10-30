Sent: 2026-10-30 15:01 ET

# QA-REPORT-151 Addendum — admin session ~14:59-15:00 ET
Supplements QA-REPORT-151, B-0279 and B-0281 (sent files unchanged).

## Bill of sale — vehicle mode (batch-70/downloads/bill-of-sale.docx, bill-of-sale.pdf)
PDF: 1 Letter page; .docx text identical to the PDF.
- VIN printed: "2HGFC2F59JH123456" ✔ (17 characters).
- Odometer statement: "45210 miles … reflects the actual mileage" ✔ — but only the "actual mileage" certification exists; the other two federal options ("exceeds mechanical limits", "not the actual mileage") and a buyer acknowledgment are absent (gap already in B-0279 outcome 2). Reading printed without a thousands separator.
- Price in words: "$12,500.00 (Twelve thousand five hundred dollars and 00/100)" ✔.
- Both names: "Alex Rivera ("Seller") and Sam Lee ("Buyer")" ✔.
- Signature lines: Seller and Buyer lines each with a Date line ✔; printed names are not repeated under the lines (minor).
- Gap check vs B-0279:
  - Addresses: absent for both parties → gap holds.
  - Date: partly corrected — the document states "made on October 30, 2026" (today's date, auto-filled). There is no field to choose a different sale date, and no place of sale. B-0279 outcome 1 should read "selectable date of sale and place of sale".
  - Make/model/body as separate fields: absent (only the free-text item "2018 Honda Civic") → holds.
- New: section 5 prints "governed by the laws of [State]" — a bracket placeholder left in the final document when State is blank. Should be omitted or prompted.

## Blind CV redactor (batch-70/downloads/blind-cv.txt)
Output: "Jane Doe, [EMAIL], [PHONE], [ADDRESS], Boston. Senior engineer at Acme since 2019." — 3 items removed.
- Name kept because the name field was empty; year kept because the years option is off by default. Both by design.
- Gap (add to B-0281): auto-detect the candidate name from the first line and pre-fill the name field for confirmation (Formatix.AI does this from the top line). City "Boston" also stays; only street addresses are removed.

## Grammar checker — L-087 re-report: claimed fixed but still failing
- L-087 was claimed fixed under B-0059. At ~14:59 ET "centre's" was changed to "center's" while the page showed "UK spelling (detected)".
- Combined with the #150-addendum (plain "centre"/"colour" kept), the fault is specific to the possessive form. Fix target: UK mode must leave "centre's", "colour's", "organisation's" unchanged.

## Process
- Code check added: chk now fails a body containing its own "Sent:" line, and tchk fails any file with more than one. Scan of sent files finds two with a duplicate: QA-REPORT-151 (1458) and QA-REPORT-150 (1453; its second line reads "14:5x"). Both left unedited; their stamps (14:58 ET, 14:53 ET) are authoritative.
