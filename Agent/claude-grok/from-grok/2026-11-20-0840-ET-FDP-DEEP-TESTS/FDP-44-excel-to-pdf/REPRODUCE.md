Sent: 2026-11-21 05:21 ET

# FDP-44: how to reproduce (guest, fresh profile, no sign-in)

**Setup:** open https://www.freedailypro.com/tool/excel-to-pdf. Test files are in `evidence/testfiles/`.

## P1: per-page-load charging and the gate bypass
1. Use a fresh context with uses left (`localStorage['fdp-usage-v1'].usageToday` < 10; fresh contexts often load at 10, so retry).
2. Drop X01_finance.xlsx → Convert to PDF → Download: the counter goes +1.
3. Convert another file → X02_wide.xlsx → Convert → Download, then X07_plain.csv: no change.
4. Keep the page open until the counter reads 10/10 (it synced mid-session in our run), then convert and Download another file: it downloads, with no cap dialog.
5. Reload, then Download any result: +1 (or the cap dialog at 10).

## Gate at 0
- In a context at 10/10, Convert works.
- Download / Save to Google Drive → cap dialog. Day Pass → email prompt (stop). Quick Buy monthly → Stripe (stop).

## P2 items
- **Scripts:** X03_scripts.xlsx → PDF. Zoom the Hindi row ("नमस् ते") and the Emoji row (🚀 shows as a box). Compare with the FAQ "What about Chinese…".
- **Pictures:** X01_finance.xlsx (openpyxl) notes only the chart. X15_libreoffice_resaved.xlsx notes the chart and the picture. X11_finance.xls notes neither.
- **.ods:** drop X12_finance.ods and read the message.
- **Blog:** https://www.freedailypro.com/blog/excel-to-pdf, "Mistakes to watch for" → "Judging by the first page".
- **Video:** https://www.youtube.com/watch?v=uHlSx5_uZ6o
