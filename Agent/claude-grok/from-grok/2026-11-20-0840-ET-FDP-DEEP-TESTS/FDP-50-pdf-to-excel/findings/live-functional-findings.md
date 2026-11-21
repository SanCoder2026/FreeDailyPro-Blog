Sent: 2026-11-21 08:14 ET

# Live functional findings (Chromium, guest, 2026-11-21 EST)

## At the cap (zero.json, fresh context at 10/10)
- Extract runs and shows the summary and a preview of up to 8 rows per sheet.
- Download → cap dialog: "Today's trial uses are done… Monthly for $4.99… Day Pass for $1…".
- Save to Google Drive → the same cap dialog. Save to my cloud storage → the sign-in / $4.99 add-on dialog. Open from Google Drive → Google sign-in popup.
- Day Pass → email field (stopped there). Quick Buy monthly → Stripe Checkout (stopped there).
- The keyboard reaches the drop zone in 28 tabs.

## With uses left (left.json)
- **Charging:** L01 0→1; 15 new workbooks and 1 re-download in the same load at 1. After a reload, L20 went 1→2, and L21 (new) stayed at 2. Only 2 `usage.log` POSTs in total.
- **Save buttons with uses left:** Drive → Google sign-in popup; cloud → sign-in dialog.

## Output checks (check-xlsx.py)
- **T01:** joined over pages 1–3; header repeat dropped; `"$"#,##0.00`; parenthesised amounts negative; dates mm/dd/yyyy; autofilter set.
- **T02:** 5 money columns kept as text because of header words.
- **T03:** Menge 1.500 → 1.5 (×1000 error); Betrag and Anteil correct; dd.mm.yyyy dates.
- **T04:** amounts with space thousands → text.
- **T05:** only the table (prose and two-column text ignored).
- **T07:** identifiers stay text with their zeros.
- **T08 OCR:** 10 of 104 cells differ (json/ocr-compare.txt).
- **T11:** formula-like strings stay text; 0 `<f>` elements.
- **T12:** CR/DR and USD → text.
- **T13:** table not found.
- **T14:** 1,601 rows in 0.5 s.
- **T15:** ambiguous dates left as text with a clear note; Day first converts them; two-digit pivot 49.
- **Sheet modes:** per page = 3 sheets; single = "Tables"; values off = all text.
- **Damaged and password files:** the truncated file gets the damaged-file toast; the password file goes through the unlock dialog.

## Network
- No document bytes or table text were POSTed.
- For OCR, only tesseract.js, its worker and `eng` language data were fetched from cdn.jsdelivr.net, as the Privacy section says.
