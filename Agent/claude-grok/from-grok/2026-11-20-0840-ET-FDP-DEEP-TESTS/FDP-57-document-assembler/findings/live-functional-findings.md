Sent: 2026-11-21 11:31 ET

# Live functional findings (FDP-57)

- **left-firefox.json** (the 10th fresh Firefox context was at 0/2):
  - L01 assemble 2.3 s, 8 pages. Download 0/2 → 2/2, one usage.log POST at 11:06:17 EST, 329,894 bytes.
  - L01b same file again: free.
  - L02 retitle + re-assemble + Download at 2/2: delivered (330,016 bytes), no dialog, no POST.
  - Reload: L03 Download → cap dialog.
- **Probe (Chromium, at 2/2):**
  - P01–P11 validation and bad files, as in REPORT.
  - P12 assemble 1.7 s.
  - P13 "Preview first page" shows a 489×633 image.
  - P14 Download, P15 Save to Google Drive and P17 Save project all open the same cap dialog.
  - P16 cloud opens an email sign-in + "$4.99 per month, 1 GB" dialog.
  - QB day stops at the email field; QB month reaches Stripe.
- **password.json:** dialog text "…never uploaded — and your result won't have a password"; Skip toast; wrong-password message; Unlocked; assembled 8 pages.
- **Fresh-context availability:** Firefox 10 (left) + 12 + 15, Chromium 12, WebKit 12. Only one context had uses, so cases C1–C3 are pending.
- **Output L01:**
  - Letter 612×792 everywhere; no /Rotate.
  - Fonts: Literata (embedded) + Helvetica.
  - Outline: report (3 nested chapters, correct pages), cover letter (6), photo (8).
  - TOC links /Fit to the right pages; source URI link kept at [72,115,330,132]; badge link on every page.
  - Footer numbers 1–6 on content; cover and TOC unnumbered.
