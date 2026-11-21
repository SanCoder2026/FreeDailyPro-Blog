Sent: 2026-11-21 09:19 ET

# FDP-52 test cases (guest; run after fixes)

| ID | Input / steps | Expected | Today (2026-11-21) |
|---|---|---|---|
| M01 | Write: 3 articles (long .md + wide JPG, unicode .txt + tall PNG, plain), cover JPG, logo → Build → Download | 7 pages; cover, In this issue (3/6/7), header, logo, badge | PASS (L01) |
| M02 | Download the same build again | no extra use | PASS (L01b) |
| M03 | Edit → Build → Download with uses left | +1 | PASS (E02 1→2) |
| M04 | At 2/2: Download / Save to Google Drive | cap dialog $3/$9.99 | PASS (zero, Firefox, fresh WebKit) |
| M05 | Day Pass → | email field, stop | PASS (stopped) |
| M06 | Quick Buy monthly | Stripe, stop | PASS (stopped) |
| M07 | 3 columns + A4 + Dotted contents | builds | PASS (Z-W02, 6 pages) |
| M08 | Templates Feature / Photo / Report | prefilled sections, columns, page size, toast | PASS |
| M09 | Empty issue → Build | inline alert | PASS |
| M10 | Bad picture / bad JSON / wrong-app issue / unknown brand file | specific messages | PASS |
| M11 | Save issue → reload → Open saved issue | everything restored incl. pictures | PASS |
| M12 | Combine: docx, 3 PDFs, JPG, txt, password PDF (u123), Masthead, Contributors | 20 pages; TOC numbers correct; List of Images | PASS (K01) |
| M13 | Combine with WebP | assembles | FAIL |
| M14 | Combine with JPG in WebKit/Safari | assembles | FAIL (tab crash, WebKit) |
| M15 | Damaged PDF in Combine | clear toast, others unaffected | PASS |
| M16 | Hindi/Japanese/Arabic article | renders and is selectable; Arabic right-aligned | PARTIAL (renders as shapes) |
| M17 | Emoji in article | note shown, emoji left out | PASS |
| M18 | Phones 320–430 px | scrollWidth = viewport | FAIL (442) |
| M19 | Network during builds/downloads | no document bytes POSTed | PASS |
| M20 | Locales | subtitle/offer/builder translated | FAIL |
