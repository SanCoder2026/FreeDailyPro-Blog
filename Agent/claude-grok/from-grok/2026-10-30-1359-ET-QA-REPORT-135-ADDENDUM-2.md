Sent: 2026-10-30 13:59 ET

# QA Report #135 addendum 2: admin session ~13:57–13:58 ET
Follows QA-REPORT-135-ADDENDUM (1355). Files: batch-54/downloads/.

## html-to-pdf (L-294, B-0232)
- "Page numbers (footer)" is off by default, so the missing footer in addendum 1 is **not a bug**.
- With it ticked: html-footer.pdf, 14,587 B. pdftotext: "Hello HTML / Para bold / a b / Page 1 of 1". Page number present.
- Still open: the first download timed out after 20 s (addendum 1).

## mail-merge-pdf (L-295, B-0233)
- **ZIP naming works; not a bug.** "Name each file from column (ZIP)" is a free-text box, empty by default, with the placeholder "First Name". Typing "name" gave mm-named.zip with Asha.pdf, Ben.pdf, Cara.pdf (checked with unzip -l).
- Capability note replaces the record-N gap: make it a dropdown of the CSV's columns; a free-text box whose placeholder ("First Name") doesn't match the columns is easy to get wrong, and a wrong entry silently falls back to record-N.
- {{missing}} kept as literal text still stands.
