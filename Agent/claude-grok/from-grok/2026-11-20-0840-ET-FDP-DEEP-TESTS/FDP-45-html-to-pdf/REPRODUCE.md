Sent: 2026-11-21 06:06 ET

# FDP-45: how to reproduce (guest, fresh profile, no sign-in)

**Setup:** open https://www.freedailypro.com/tool/html-to-pdf. Test files are in `evidence/testfiles/`.

## P1: per-page-load charging
1. Use a fresh context with uses left (`localStorage['fdp-usage-v1'].usageToday` < 10; fresh contexts often load at 10, so retry).
2. Keep the sample → Convert to PDF → Download: +1.
3. Edit → paste H02_invoice.html → Convert → Download; repeat with H03…H07: the counter doesn't move.
4. Reload → Convert → Download: +1.

## P1: WebKit hang
1. Open the page in Safari (or Playwright WebKit). Paste H02_invoice.html (it has one external image) → Convert.
2. It stays at "Rendering page 1 of 3… keep this tab open".
3. Press Stop: nothing changes.
4. H02b_invoice_noext.html converts in about 6 s. `scripts/hp-webkit.js` automates this.

## P2 items
- **File name:** after step 3, every download is named "Invoice INV-2026-045.pdf" although each document has its own `<title>` (check `pdfinfo` Title).
- **Blank page:** paste H03_breaks.html → 5 pages, page 1 empty.
- **Links:** H02 → in the PDF, the "Anchor" link (`#top`) opens https://www.freedailypro.com/tool/html-to-pdf#top.
- **Charset:** drop H09_cp1252.html → the box shows "Caf� cr�me".
- **Video:** https://www.youtube.com/watch?v=JqeVfUR3J-g (about 0:18–0:28).

## Gate at 0
- Convert works; "Preview first page" shows page 1 as an image.
- Download / Save to Google Drive → cap dialog. Day Pass → email (stop). Quick Buy monthly → Stripe (stop).
