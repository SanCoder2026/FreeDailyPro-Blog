Sent: 2026-11-21 02:49 ET

# FDP-38 PDF to JPG: reproduce

Guest browser, https://www.freedailypro.com/tool/pdf-to-jpg. Test files are in `evidence/testfiles/`.
1. **Preview leak (0 trial uses):** with the strip showing 0 remaining, drop `Q01_photo_page.pdf`, choose Print, Convert. Right-click the thumbnail → Open image in new tab: 2550×3300, no badge. Download → cap dialog.
2. **Page harvest:** at 0, drop `P03_50pages.pdf`, range `37`, Convert → page 37 preview at full resolution (2550×3300 with Print kept).
3. **Badge difference:** with uses left, convert `P02_plain_1p.pdf`. Save the thumbnail image, then Download. Only the download has "Created with FreeDailyPro.com".
4. **Per page load:** with uses left, Download a P01 ZIP (−1), then Convert another → P02 → Download. The count doesn't change and the label has no "uses 1 trial use". Reload, Download again (−1).
5. **Password copy:** drop `U01_aes256_user_old123.pdf`. An unlock dialog appears (password old123), contrary to "skipped and listed".
6. Scripts: `scripts/README.md`.
