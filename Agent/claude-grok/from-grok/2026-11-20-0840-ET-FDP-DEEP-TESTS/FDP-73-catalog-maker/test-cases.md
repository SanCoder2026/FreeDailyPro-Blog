Sent: 2026-11-21 16:53 ET

# FDP-73 test cases

| ID | Input / action | Expected | Result |
|---|---|---|---|
| Z01 | 2/2: 2 products + photos → Build → Download / Drive / cloud | Build OK; gated | 5-page PDF built; cap dialog; cloud sign-in (PASS) |
| Z02 | 2/2: Combine PDF + DOCX + PNG → Download | Gated | 7 pages; cap dialog (PASS, Chromium + WebKit) |
| X20 | 2/2: Preview first page | Not a full result | Cover only, 489×633 (PASS) |
| K01 / K16 | Empty build; cover without title | Clear errors | PASS |
| K02 | 24-SKU CSV with header words | 24 cards, contents | PASS; **1 row per page (P2)** |
| K03–K07 | No header; bad rows; quoted; BOM+semicolon; TSV | Parsed / flagged | PASS |
| K08 / X02 | "Call for price" / "Ask for quote" | Printed as typed (FAQ) | **Refused (P2)** |
| X01 | Unicode names/categories, € | Render | PASS (outlines, P3) |
| X03 | "1,299.00", "12,50" | Parsed | PASS |
| K09 / K10 | Long text; 300 rows 3-col A4 | Cut 2/4 lines; 46 pages | PASS |
| K11 | 10 px, 4000 px, WebP, fake photo | OK / error | PASS |
| K12 | 3 templates | Layout only | PASS; lookbook → A4 (P3) |
| K13 / X05 | Yen, Rupee, Dirham, ₹125000 | Formatted | PASS (Western grouping, P3) |
| K14 / X04 | Tax included 10 %; before tax 8.875 % | Correct columns | PASS |
| K15 | Cover/contents/price list off | 2 pages | PASS |
| K17 | Save → reopen; bad JSON; brand JSON | Round trip; errors | PASS |
| K18 | Logo | On cover | PASS |
| K19 | Combine: PDFs, TXT, WebP, locked, damaged, .doc, .xlsx | Skip bad files | Bad files handled; **WebP fails assembly (P2)** |
| X10–X13 | Back page: EAN-13 invalid / valid, Code 128, QR | Code or error | **Invalid → blank page (P2)**; others PASS |
| L01–L02 | 0/2: Download; re-download | 1 use; free | 1 POST; free (PASS) |
| L03–L07 | Edited / combine downloads | 2nd use available | **Cap dialog after 0→2/2 (P1 check)** |
| Q | Quick Buy day / monthly | Email / Stripe | Stopped |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | iPhone SE 9 px; locale English (P2) |
