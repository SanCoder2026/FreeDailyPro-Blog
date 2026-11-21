Sent: 2026-11-21 03:27 ET

# FDP-40 Extract Pages & Text: reproduce

Guest browser, https://www.freedailypro.com/tool/extract-pdf. Test files are in `evidence/testfiles/`.
1. **Full text at 0:** with the strip at "0 remaining today", drop `E01_mixed_8p_bookmarks_form.pdf`, choose Extract Text, clear the page box, press Extract Text. All 8 pages appear. Click in the box, Ctrl+A, Ctrl+C: everything is copied. Pressing Copy opens the cap dialog.
2. **Page-1 default:** reload, drop E01, Extract Text without touching the box → only "--- Page 1 ---".
3. **Typed order:** Extract Pages "5,1,3" → "Preview first page" shows PAGE-5.
4. **Locked:** drop `U01_aes256_user_old123.pdf` → unlock dialog (password old123), contrary to the Limitations.
5. Scripts: `scripts/README.md`. Pending: RERUN row 40.
