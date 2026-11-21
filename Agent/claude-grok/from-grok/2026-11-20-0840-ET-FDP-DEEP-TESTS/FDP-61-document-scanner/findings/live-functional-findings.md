Sent: 2026-11-21 13:02 ET

# Live functional findings (FDP-61)

- **zero.json (Chromium, 2/2):** full flow on p1 (canvas 1002×1131). PDF, PNG and searchable PDF each open "Today's trial uses are done…" with no charge. The canvas is readable at full size (Z05). Add page works at the cap (no gate). After the dialog, the status line "Today's trial uses are used up…" stays through the next photo (Z07). Edit as Word → `/tools/image-to-word` 404 (Z08).
- **quickbuy.json:** Day pass → "Premium Day Pass, $3 | Enter your email…" (stopped). Monthly → checkout.stripe.com (redacted, stopped).
- **left.json / left-firefox.json (0/2):** p1 + p2 added, page 2 moved up, p4-shadow on Letter. "Download PDF (3 pages)" took 1 use (0→1, one usage.log POST). PNG and searchable PDF then downloaded with no extra charge. PDF: 3 Letter pages, order 2,1,4, mark present. Searchable: "3 pages read", text correct.
- **leftB.json:** the ID front step failed because the script looked for "Add page" (the label is "Add front & scan back" in ID mode). The front-only PDF took the count 0→2. New scan p6 (Fit) → searchable PDF and PNG downloaded at 2/2 with no dialog.
- **idcard-firefox.json:** front + back → "Download PDF (front + back, one page)" → one Letter page, both cards at 274 ppi (85.6 mm). File `scanned_id-back_2pages.pdf`. 0→1.
- **perload.json:** p1 PDF (0→2, one POST). p2, p3, p4 PDFs at 2/2 with no POST and no dialog. After reload, a p6 PDF showed the cap dialog.
- **msgs.json:** small-photo warning, low-contrast message, dark page handled. Light desk and 6000 px (12 s) found the corners. EXIF 6 sideways (M05). Not-an-image → empty crop.
- **orient.json:** EXIF 6 sideways at Crop on Chromium, Firefox and WebKit. Not-an-image naturalWidth 0, no message, on all 3.
- **misc.json:** inputs `image/*` (single) and `image/*` capture=environment (single). Drive → accounts.google.com sign-in popup (closed). Handles tabIndex -1. Edit as Excel → `/tools/image-to-excel` 404; `/tool/image-to-word` = 200.
- **mobile.json:** iPhone 13 and Pixel 7 run the full flow; touch crop works; cap dialog at download; no overflow.
