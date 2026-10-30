Sent: 2026-10-30 15:45 ET

# B-0304 Business Card: "bleed" PDF trim box and crop marks checked: none; text is a flat image
Priority: P2 · Estimated effort: M · Report: QA-REPORT-159 · Source: live probe 2026-10-30 ~15:42-15:44 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
The print PDF should be accepted by a print shop without fixes, and the cards should look professional.

## Why
No GSC row in the analytics raw file for this page.
Checked live (15:43 ET), default card (Jane Doe, Acme Inc.):
- Print-ready PDF: 2 pages, 270.24×162.24 pt = 3.75×2.25 in (3.5×2 + 0.125 in bleed) ✔, but TrimBox = BleedBox = MediaBox (checked, pdfinfo -box), so the printer is not told where to cut; no crop marks on the rendered page (checked).
- Each page is one 1126×676 image at 300 ppi; the only text is "Created with FreeDailyPro.com" (checked, pdftotext/pdffonts), so names and numbers are pixels, not vector.
- Front PNG 1050×600 (3.5×2 in at 300) ✔, no DPI tag.
- Filenames "business-card-print-acme-inc..pdf" and "business-card-front-acme-inc..png" have a double dot from the company name "Acme Inc.".
- One layout with six colour themes or a photo background (page About text); no logo or QR control in the control list (checked).
Competitors (live search): ToolNova (16 templates, QR, US/EU/Japan sizes, crop marks, 10-up sheet), Jasper Bernaers (40 templates, trim/bleed box, crop marks), Jarvis (10 templates, 10-per-sheet PDF), Motionshine (600 dpi, QR back).
Title 58 ✔; meta 35. /es title English → L-189.

## Who uses this
Freelancers and small businesses printing cards.

## Outcomes (ranked)
1. Set TrimBox 9 pt inside the page and add crop marks outside the trim.
2. Draw text as vector text over the background image.
3. Clean filenames (no "..").
4. Logo upload and a QR code on the back; a 10-up Letter/A4 sheet for home printing.
5. Meta as below.

## SEO
- Now: title "Design a Business Card Online - No Software | FreeDailyPro" (58); meta 35; H1 "Business Card Generator"
- Keywords: business card maker, printable business cards, business card pdf with bleed, business card template
- Suggested Title: "Business Card Maker: Print PDF with Bleed | FreeDailyPro" (56)
- Suggested Meta: "Design a business card with name, title, company, phone, email and website, pick a colour theme or photo, then download a PNG or a front-and-back print PDF." (156)
- Suggested H1: "Business Card Maker"
- FAQ: What size is a business card? · Does the PDF have bleed? · Can I add a logo? · Can I print at home?

## Constraints
Download gating at 0 trial uses is fine. Keep 300 ppi or better.

## Test cases
1. Print PDF → page 3.75×2.25 in, TrimBox 9,9–261.24,153.24, crop marks visible outside trim.
2. pdftotext on the PDF → name, title, phone, email appear.
3. Company "Acme Inc." → filename without "..".
4. Front PNG 1050×600 (regression).
5. Meta 140–160; 390 px no overflow.
