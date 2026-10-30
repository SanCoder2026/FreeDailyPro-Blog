Sent: 2026-10-30 15:32 ET

# B-0299 Brochure & Flyer Maker: PDF is one flat image; no folded brochure layout
Priority: P2 · Estimated effort: M · Report: QA-REPORT-157 · Source: live probe 2026-10-30 ~15:28-15:31 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone searching "brochure maker" gets a brochure they can fold and print, and a PDF a print shop accepts with sharp text.

## Why
No GSC row in the analytics raw file for this page.
Checked live (15:31 ET): paper A4 → button relabels to "Download as PDF (A4)" ✔; bright-path-consulting.pdf is 595×842 pt, 1 page ✔. Print-shop PDF 613×860 pt with TrimBox inset 9 pt (0.125 in) ✔.
- Checked (pdfimages/pdftotext): the PDF is a single 2480×3507 300 ppi image; only the footer "Created with FreeDailyPro.com" is real text. Headline and contact text cannot be selected or searched, and small text prints as pixels rather than vector.
- Layouts: paper sizes Letter, A4, A5, half-letter only; no tri-fold/bi-fold or two-sided option in the control list (checked). The tool name says "Brochure" but makes a single-sided flyer.
Competitors (live search): JukeboxPrint (tri-fold, bi-fold, Z-fold with fold lines), AnyTool (true tri-fold panels, 6 templates, 2-page PDF), Adobe Express (tri-fold templates).
Title 62 characters; meta 45. Trial: 2 uses/day; two downloads reached 0 (download gating at 0 is fine). /es title English → L-189. Ad text ("Boost SEO Traffic", "Hire Designers") → L-004.

## Who uses this
Small businesses and event organisers printing handouts.

## Outcomes (ranked)
1. Text in the PDF as real (vector) text, background/photo as image.
2. A tri-fold layout (outside + inside, 2 pages, fold guides), or rename to flyer-first wording.
3. Snippet as below.

## SEO
- Now: title "Design a Flyer or Brochure Online - Print-Ready | FreeDailyPro" (62); meta 45; H1 "Brochure & Flyer Maker"
- Keywords: brochure maker, flyer maker, tri-fold brochure template, printable flyer pdf
- Suggested Title: "Flyer & Brochure Maker: Print-Ready PDF | FreeDailyPro" (54)
- Suggested Meta: "Design a one-page business flyer in Letter, A4, A5 or half-letter with headline, key points, photo and contact line, then save a PDF with 0.125 in bleed." (153)
- Suggested H1: "Flyer & Brochure Maker"
- FAQ: Can I print with bleed? · Which paper sizes? · Can I add my photo? · Can I make a tri-fold?

## Constraints
Keep the bleed PDF and TrimBox as they are.

## Test cases
1. A4 → PDF 595×842 pt (regression); bleed PDF 613×860 with TrimBox 9 pt (regression).
2. pdftotext on the PDF returns the headline and contact line.
3. Tri-fold Letter → 2-page PDF, 11×8.5 in, three panels each side with fold guides off by default.
4. Title ≤60, meta 140–160; 390 px no overflow.
