Sent: 2026-11-21 03:55 ET

# FDP-41 OCR PDF: reproduce

Guest browser, https://www.freedailypro.com/tool/ocr-pdf. Inputs are in `evidence/testfiles/`; ground truth is in `truth.json`.
1. **Per-page-load charging:** in a fresh profile showing "10 remaining today":
   1. Drop `S01_scan_clean_en.pdf` → Make Searchable → Download. The strip/`fdp-usage-v1.usageToday` goes 0 → 1.
   2. Download again → still 1.
   3. New → `S02_scan_text_scan_3p.pdf` → Make Searchable → Download → still 1. Repeat with any number of files: still 1.
   4. Reload, then do one more Download → 2.
2. **Sticky orientation:**
   1. Drop `S03_sideways_90.pdf`, set Page orientation "Turn 90° clockwise first", Make Searchable, Download (correct).
   2. Press New, drop the upright `S05_scan_spanish.pdf` without touching the menus, Make Searchable. The notice says "Page 1 was turned 90° clockwise so it reads upright".
   3. The download opens sideways (`/Rotate 90`).
3. **Auto on upside-down:** reload, drop `S12_upside_down.pdf`, choose "Detect automatically (turns sideways pages)" → "turned 270° clockwise…". The download is sideways. "Turn 180° first" gives an upright page.
4. **Stamped footer:** drop `S04_scan_digital_footer.pdf` (an image page plus "Page 1 of 1" text) → "This PDF is already searchable…". No OCR.
5. **Table digits:** `S11_scan_table.pdf`, English, As scanned → download → `pdftotext` shows "ITEM / Widget A 4 / Widget B / Cable" with QTY/PRICE missing.
6. **Hindi:** `S07_scan_eng_hindi.pdf`, English + Hindi → download → `pdftotext` shows "माच" and "शम" for "मार्च" and "शर्मा".
7. **WebKit:** Playwright WebKit (`scripts/ocr-webkit.js`) → S01 → Make Searchable → page crash. Then try a real Safari.
8. **At 0 (gated, PASS):** at "0 remaining today", Make Searchable still runs. Download, Save to Google Drive and Continue with Compress PDF → Download all open "Today's trial uses are done".
9. **Copy:** expand Common questions ("English is currently supported") and Details → Tips ("not turned for you in this tool").
