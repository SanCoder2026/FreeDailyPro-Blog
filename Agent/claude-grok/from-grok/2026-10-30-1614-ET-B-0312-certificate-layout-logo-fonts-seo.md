Sent: 2026-10-30 16:14 ET

# B-0312 Certificate Maker: one layout, no logo or signature image, half-empty page, Helvetica not embedded
Priority: P3 · Estimated effort: M · Report: QA-REPORT-161 · Source: live probe 2026-10-30 ~16:06-16:13 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
An organiser prints certificates that look finished and official, with their own logo and signatures.

## Why
No GSC row in the analytics raw file for this page.
Checked live (16:11 ET): three typed names (Ana López, Bo Chen, Zoë Ðorđević) → certificates.pdf, 3 pages, 792×612 pt US Letter landscape ✔. Toast "3 certificates in one PDF" ✔. Names with accents print correctly (DejaVuSans embedded) ✔. Wording placeholders {event}/{date} filled ✔. A warning that the event name is still "My event" ✔.
Render (page 1): the text block sits in the top half and the lower half is empty. With signers blank, no signature lines are drawn. A "Created with FreeDailyPro.com" badge sits at the bottom right over the inner border on logged-out output (owner question; same as the business-card trial badge, L-354).
Fonts: Helvetica and Helvetica-Bold are not embedded (checked with pdffonts). Some print shops reject this.
Layout choices: Border (Double line / None) and accent colour only. Logo upload, signature image, seal, certificate number and CSV/Excel import: not offered (checked: inputs are names, title, lines, event, date, two signer names/titles, colour, border, PDF/ZIP).
Competitors (live search): BulkCerts (103 templates, logo, signature, certificate numbers, CSV/XLSX, PDF/PNG/JPEG ZIP), Cert Generate (Excel/CSV, logo, QR), Make in Bulk (own PDF template + CSV), IssueBadge (PDF template + CSV fields).
Title 54 without brand; meta 140 has "Free". /es page fully English → L-189. Unnamed text inputs (checked) → B-0155.

## Who uses this
Event organisers, trainers and schools.

## Outcomes (ranked)
1. Balance the layout to fill the page, and draw signer lines.
2. Logo and signature image upload.
3. Paste or import a CSV of names; add an optional certificate number.
4. Embed the fonts.
5. Title with brand (below).

## SEO
- Now: title "Certificate Maker - Attendance Certificates for Guests" (54, no brand); meta 140 (Free); H1 "Certificate Maker"
- Keywords: certificate maker, certificate of attendance, bulk certificate generator, certificate of completion template, certificate pdf
- Suggested Title: "Certificate Maker: Attendance Certificates | FreeDailyPro" (57)
- Suggested Meta: "Make attendance, completion or appreciation certificates for every name on your list, with event, date and two signers, as one PDF or a ZIP on Letter or A4." (156)
- Suggested H1: keep
- FAQ: keep; add: Can I add my logo and signature? · Can I make certificates from a spreadsheet?

## Constraints
Downloads count against the trial; gating at 0 trial uses is fine. Keep Unicode names working.

## Test cases
1. Three names with accents → 3-page PDF, names correct, fonts embedded.
2. Upload a logo PNG → it appears on every page.
3. Two signers → two signature lines with names and titles.
4. ZIP option → three PDFs named after each person.
