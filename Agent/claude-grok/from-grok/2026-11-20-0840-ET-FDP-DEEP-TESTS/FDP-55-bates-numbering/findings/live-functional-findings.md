Sent: 2026-11-21 10:39 ET

# Live functional findings (FDP-55)

- **Charging (P1):** left-firefox.json shows L01 0→1, L02 1→1, L03 1→1, reload, L04 1→2, with `usage.log` POSTs at 10:18:41 and 10:19:09 EST only. cases-firefox.json: 12 runs, 0→1, one POST at 10:20:42 EST.
- **Outputs:** all PDFs open (pdfinfo); stamps verified with pdftotext and renders (`screens/render/crop-*.png`).
  - B04 output page size is 512×692 (the CropBox), with the stamp inside.
  - B03 Rotate values [90, 270, 180] are kept.
  - Metadata: Producer becomes pdf-lib, ModDate is updated, and Title/Author/Creator are kept.
- **ZIP:** STORE method; contains the PDFs plus `bates-index.csv`. Duplicate names become `-bates-2`.
- **CSV:** header `Document,Numbered file,Pages,Begin Bates,End Bates`; formula prefix escaped with `'`; no BOM.
- **Unicode stamp (B08):** renders (crop-B08-unicode.png); pdftotext finds no stamp text.
- **Dark page with the box off (B05):** the black stamp is barely visible (crop-B05-dark.png).
- **Password flow:** dialog "This PDF is password-protected … your result won't have a password". Choices are Skip this file (toast "Skipped … password-protected") or Unlock (toast "Unlocked"). The output isn't encrypted.
- **Ad creative:** a fake-looking "Download / Tap to Download" ad appeared in the in-content slot (add-dialog-*-firefox.png). Not clicked.
- **Cap:** a run at 10/10 opens "You've used today's trial uses" (Chromium, WebKit). Quick Buy Day Pass stops at the email field; Monthly reaches Stripe (redacted).
