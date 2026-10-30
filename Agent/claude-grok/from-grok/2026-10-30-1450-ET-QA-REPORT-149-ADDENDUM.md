Sent: 2026-10-30 14:50 ET

# QA-REPORT-149 ADDENDUM — admin session ~14:48-14:49 ET
Supplements: QA-REPORT-149, B-0273–B-0275 (stamped 1447). Downloads in batch-68/downloads/. Checked with pdfinfo/pdftotext -bbox, pdftoppm + OpenCV QR, cmp/openpyxl, Pillow; on-page table re-rendered logged out with Playwright. Ledger grepped first: L-323–L-325 updated, no new rows.

## badge-pass-maker (B-0273, L-323)
- **name-badges-5392.pdf:** 1 page, US Letter 612×792 pt (Media = Bleed = Trim). Grid 2 across × 3 down, 4 in × 3 in cells (name rows at y 120/336/552 pt, 216 pt = 3 in apart; columns 4 in apart) ✔. **5 badges** (Maya Patel, Lukas Meyer, Amara Okafor, Haruto Tanaka, Fatima Al-Sayed), 6th cell empty ✔. Each shows event name, organisation and role.
- **QR codes:** OpenCV decoded **5/5** at 200 dpi, one per filled cell, e.g. `FDP1.iCYXYl.g_sample01.OEb5RM33id4EBT`: version, event id, guest id, signature. No name or email inside the QR ✔.
- **guest-list.csv / .xlsx:** byte-identical to batch 62 (`cmp`), and the XLSX cells are identical ✔. The export is the same across the shared event tools.

## bank-statement-to-csv (B-0274, L-324)
- **statement.csv:** UTF-8 with BOM (opens cleanly in Excel), `Date,Description,Amount,Balance`, ISO dates (2026-01-02…), money out negative (−4.50), in positive ✔.
- **statement.xlsx** (sheet "Transactions"): dates are real **date cells** (`yyyy-mm-dd`), amounts and balances are **numeric** (`#,##0.00`) ✔. Header row is text.
- **On-page table "empty cells":** not a bug. Date, Description and Amount are `<input>` fields, so page text omits their values. The logged-out render shows them filled on screen (2026-03-01 · Coffee Shop · −4.50 · 995.50); screenshot `downloads/bank-table.png`.
- **Date-order gap (new):** with every day ≤ 12, "Detect" silently reads 03/04 and 05/04 as month-first (2026-03-04, 2026-05-04). With a 13 present it switches to day-first ("Detect (day first)"). A UK statement for 1–12 April would be imported as wrong months and could still pass the balance check. **Gap:** when dates are ambiguous, say so and ask DD/MM or MM/DD before export (e.g. "These dates could be either — pick one").

## banner-sign-maker (B-0275, L-325)
- **banner.png:** 3600×5400 px RGBA ✔ (= 24×36 in at 150 DPI). No DPI metadata in the PNG (minor; print apps may assume 72).
- **banner-print-bleed.pdf:** MediaBox/BleedBox 1746×2610 pt = **24.25×36.25 in** ✔; TrimBox 9 pt inset = 24×36 in, i.e. 0.125 in bleed each side ✔. 3.35 MB.
- **Demand gap (new):** no **24×36 in poster preset**, the most common poster size; this file needed custom W×H. Add 24×36 (and 18×24, 11×17) presets.

## Admin checks still open (batch 68)
- Badges printed at 100% on Avery 5392 stock, and a printed QR scanned in Door check.
- Bank: a real text PDF (multi-page, card statement with flip signs).
