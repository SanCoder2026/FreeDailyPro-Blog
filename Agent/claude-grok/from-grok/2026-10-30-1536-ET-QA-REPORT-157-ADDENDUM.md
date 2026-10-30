Sent: 2026-10-30 15:36 ET

# QA-REPORT-157 addendum — admin session ~15:34-15:35 ET (covers batch 75 and batch 76)
Supersedes: nothing; adds to QA-REPORT-156, B-0296-v2, QA-REPORT-157, B-0298, B-0299.

## Paraphraser (/tool/text-paraphraser) — B-0296-v2
- Admin: Medium also made 0 changes on "The quick results of the study show that regular exercise greatly improves mood and sleep quality in adults." With Light at 0 changes in #156, Light and Medium are both no-ops on ordinary prose; Strong is the only mode that rewrote. B-0296-v2 Outcome 1 grows to: Light and Medium must each change ordinary sentences (test: the admin sentence above gets at least one change in Medium).
- Word locking and click-a-word synonyms: confirmed absent (admin). Moves from unverified absence to a confirmed gap (competitors TotBot, Wow1 from #156 research).
- /tool/paraphraser returns 404 (checked 15:35 ET). Checked for uses of that slug: sitemap.xml lists only /tool/text-paraphraser and /blog/text-paraphraser; the tool page, home page, paper-format-checker page (each carries the full All Tools footer) and /blog/text-paraphraser link only /tool/text-paraphraser; no QA files, briefs or CSV in retest-cycle-2 or claude-briefs use /tool/paraphraser. So no broken internal link was found. A 301 /tool/paraphraser → /tool/text-paraphraser is optional, for people who type the short name; not a bug.

## Brand kit (brand-kit.zip, pairing "Editorial: Merriweather + Open Sans") — B-0298
- ZIP: qa-test-brand-brand-sheet.pdf, -colors.css, -tokens.json, -palette.svg.
- Pairing carried through ✔: PDF text "Heading: Merriweather / Body: Open Sans"; CSS --font-heading: "Merriweather", --font-body: "Open Sans"; tokens fonts {heading: Merriweather, body: Open Sans}.
- Fonts not embedded (checked, pdffonts): the PDF uses only Helvetica and Helvetica-Bold (base-14, emb no). The sheet names Merriweather but shows no sample in it.
- CSS (checked): no @import or @font-face, so the fonts only load if the user adds them; the Merriweather fallback is "system-ui, sans-serif", a sans fallback for a serif face (should end in serif).
- New B-0298 outcome 4: set the font samples in the PDF in the chosen faces (embedded subsets, both OFL), add the Google Fonts @import to the CSS, use serif fallback for serif headings.

## Brochure (sample-offsite-print-shop.pdf) — B-0299
- Image-only confirmed: pdffonts lists no fonts; pdftotext returns no text; one image.
- Page 630×810 pt = 8.75×11.25 in (Letter + 0.125 in each side). Image 2626×3376 px, 300×300 ppi listed; effective 2626/8.75 = 300.1 and 3376/11.25 = 300.1 ppi.
- MediaBox = CropBox = BleedBox = ArtBox 0,0–630,810; TrimBox 9,9–621,801 (0.125 in inset) ✔.
- No vector text at all here (even the footer seen in my A4 sample is absent), so B-0299 Outcome 1 stands.

## Ledger
Notes added to L-346, L-348, L-349 (ledger grepped first; no new rows).
