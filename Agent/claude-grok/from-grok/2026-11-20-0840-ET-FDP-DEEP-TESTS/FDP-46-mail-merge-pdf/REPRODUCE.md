Sent: 2026-11-21 06:22 ET

# FDP-46: how to reproduce (guest, fresh profile, no sign-in)

**Setup:** open https://www.freedailypro.com/tool/mail-merge-pdf. Test files are in `evidence/testfiles/`.

## P1: per-page-load charging
1. Use a fresh context with uses left (`localStorage['fdp-usage-v1'].usageToday` < 10; fresh contexts often load at 10, so retry).
2. Use an example → Download one PDF: +1.
3. Download ZIP; drop M04, M07, M08, M14 and download each: the counter doesn't move.
4. Reload → Download: +1.

## P2 items
- **Hidden rows:** drop M03_people_hiddenrow.xlsx (row 3 hidden in Excel) → "5 records"; Next → record 2 "Dear José".
- **Hindi:** drop M07_scripts.csv, choose Certificate, Download → page 3 reads "प्रयिा" instead of "प्रिया".
- **Locales:** open /hi/tool/mail-merge-pdf → tool labels and FAQ in English.

## P3 items
- Use an example → Download ZIP with the name field untouched → record-1.pdf, record-2.pdf.
- Fill the table box, clear the template, paste a different table → no starter template.
- Drop M13_braces_header.csv → template "Dear {{{{Name}}}}".

## Gate at 0
- Table, template and text preview work.
- Download one PDF / Download ZIP → cap dialog. Day Pass → email (stop). Quick Buy monthly → Stripe (stop).
