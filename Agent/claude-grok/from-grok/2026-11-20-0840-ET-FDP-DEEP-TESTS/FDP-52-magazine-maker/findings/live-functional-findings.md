Sent: 2026-11-21 09:19 ET

# Live functional findings (2026-11-21 EST, guest)

## At the cap (zero.json, 2/2 Premium)
- **Keyboard:** 33 Tabs reach Magazine Title, via the template buttons.
- **Options:**
  - Column templates: Custom, Classic, Narrow, Wide reader, Compact.
  - Contents styles: List, Dotted leaders, Two-column grid.
  - Columns 1/2/3; US Letter/A4.
- **Z-W01:** full issue built in 0.46 s ("Magazine ready!", "Download Magazine (7 pages)").
  - Download and Save to Google Drive open the cap dialog ("To keep using Premium Applications, pick Monthly for $9.99, or a Day Pass for $3 … removes the 'Created with FreeDailyPro.com' mark").
  - Buy Day Pass goes to "Premium Day Pass, $3 | Email | Continue to payment". Stopped there.
- **Result area at 0:** the badge notice, Download, "Get a Day Pass to download", Save to Google Drive / my cloud storage, Edit, and "Preview first page". Only page 1 is previewable, so this isn't a gate gap.
- **Save issue:** 185 KB .issue.json, no charge. After a reload and reopening it, the title, articles and 3 pictures were restored.
- **Messages:**
  - Bad JSON: "That file is not a saved issue (it could not be read as JSON)."
  - Wrong app: "…not a saved FreeDailyPro magazine issue."
  - Guessed brand file: "…not a FreeDailyPro profile or brand kit."
  - Bad picture: "That image couldn't be read. Try a JPG or PNG."
  - Empty issue: "Add at least one article with a title and text, then press Build Magazine."
- **Z-W02:** 3 columns, A4, dotted contents: 6 pages.
- **Templates (focus.json):**
  - Feature issue: From the editor / Cover story / Back page; 2 columns, Letter.
  - Photo feature: 2 sections; 1 column.
  - Report: Summary / Details / Next steps; 2 columns, A4.
  - Each shows a toast.
- **Combine (Z-C01):**
  - The password PDF opens the unlock dialog → 'Unlocked "password_u123.pdf"'.
  - damaged.pdf gets the "looks damaged … Repair PDF" toast.
  - The WebP file is listed, but Assemble fails with "isn't a supported file type". There's no output (90 s wait).
  - Without the WebP (F-C02): 15 pages in 9.2 s. WebP alone (F-C03): the same failure.
- **Open from Google Drive:** Google sign-in popup. **Save to my cloud storage:** "Sign in with your email first", $4.99/mo for 1 GB.
- **Quick Buy:** Day goes to the email dialog; Monthly goes to Stripe Checkout (cs_live_REDACTED).

## With uses left
- **left-run2:**
  - L01 7-page issue downloaded. The strip showed 0/2 → 2/2 after one `usage.log` POST (display sync).
  - L01b re-download was free.
  - L02/L03 (edited) and L04 (Combine) at 2/2 opened the cap dialog.
- **left-attempt1-crash:** L01 went 0→1 and the re-download stayed at 1. Then the script hit an ambiguous "Edit" locator (my script bug, since fixed).
- **left3:** E01 went 0→1 (3-page issue), and E02 (title edited) went 1→2. Two POSTs. **Per-export charging is confirmed.**
- **left4:** K01 Combine, 20 pages, downloaded.
  - Cover / Masthead ii / Contributors iii / TOC (no folio) / List of Images v.
  - Body numbered 1–15. TOC: CEO 1, column 3, memo 6, deck 7, img 11, plain 12, password 13. All correct.

## Output checks (pdfinfo, pdffonts, pdftotext, renders)
- **L01:**
  - Letter, 7 pages. Producer FreeDailyPro, Title = issue title.
  - Helvetica family (standard 14, not embedded) plus a DejaVuSans subset.
  - Images: cover 1700×2200 JPEG, logo on every page, the article pictures.
  - Badge "Created with FreeDailyPro.com" on every page.
  - TOC title cut at 60 characters with "…".
  - Hindi, Japanese and Arabic render correctly, but pdftotext gives blank lines (drawn as outlines). Arabic is left-aligned, with the period on the right.
- **Network:** no POST carried document text or image bytes. The GETs were fonts and chunks from freedailypro.com.

## Browsers
- **Firefox (subset):** both modes build, and Download at 2/2 opens the cap dialog.
- **WebKit:**
  - S01-write at 2/2 downloaded with no dialog (a context with server-side uses; unverified).
  - Combine then crashed the tab.
  - wk-checks: 3 fresh contexts at 2/2 all got the cap dialog. Combine: memo PDF, .docx and .txt assemble; img_wide.jpg alone crashes the tab.
