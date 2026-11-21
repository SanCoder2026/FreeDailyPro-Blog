Sent: 2026-11-21 07:23 ET

# Live functional findings (Chromium, guest, 2026-11-21 EST)

- **zero.json (at 10/10):**
  - Convert works (3 pages); thumbnails 92×120.
  - Download → cap dialog ($1 Day Pass / $4.99 monthly, mentions the badge). Day Pass → email field (stopped). Quick Buy monthly → Stripe Checkout (stopped).
  - Save to Google Drive → cap dialog. Save to my cloud storage → sign-in dialog. Open from Google Drive → Google popup.
  - Keyboard reaches the drop zone (28 tabs).
- **left.json:** 13 downloads for one charge; see REPORT "Why". Toasts:
  - L05 "2 files can't be used here… Skipped: P08.tiff, P23_document.pdf"
  - L11 duplicate warning
  - L10a/b "The page must be between 1 in and 200 in on each side." Comma decimals are accepted.
- **gps.json:**
  - G01 keeps GPS, Make and Model in the embedded JPEG.
  - G02 is a re-download in the same load (counter stays at 1).
- **Output checks:**
  - Letter default (en-US); A4 595.2×841.92.
  - L07 930×1315.5 pt (dpi lost); L08 15000×600 pt.
  - L09 A4 landscape, 4 pages, Fill crops.
  - CMYK colours correct; 16-bit/HEIC/AVIF/SVG/GIF render; orientation upright.
  - Badge bottom-right on every page; Creator/Producer FreeDailyPro; Title = first file name.
- **Preview first page at 0:** a 489×633 image (Z03-preview-at0.png). Low resolution, not a full-quality result.
- **Firefox subset:** S01–S03 convert correctly (3 receipts, 5 mixed formats incl. HEIC/AVIF, 300 dpi Original size). S04: the harness couldn't find the "Pair" checkbox by role in Firefox (harness, not judged a bug).
- **WebKit subset:** the tab crashed twice on Convert with a JPG.
  - ip-wk.js: PNG converted, then a JPG crashed.
  - ip-wk2.js: the same JPG decodes and draws fine in a blank WebKit page.
  - Real Safari is unverified.
- Sign-in-only items are untested.
