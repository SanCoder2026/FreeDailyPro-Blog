Sent: 2026-11-21 09:19 ET

# FDP-52: how to reproduce (guest, fresh profile, no sign-in)

**Setup:** open https://www.freedailypro.com/tool/magazine-maker.

## P2: WebKit crash, Combine + JPG
1. Use Safari/iOS (or Playwright WebKit). Open Combine files → Issue Title → drop img_wide.jpg → Assemble Issue.
2. The tab crashes ("Target crashed"). memo_A4.pdf, ceo_letter.docx and article_plain.txt each assemble fine (wk-checks-webkit.json).

## P2: WebP blocks Combine
1. Combine files → add ceo_letter.docx, memo_A4.pdf and img_wide.webp → Assemble Issue.
2. Toast: "img_wide.webp isn't a supported file type …". No issue is built. Without the WebP file it builds (F-C02: 15 pages).

## P2: phone width
1. Open the page on a 320–412 px phone. The page is 442 px wide.
2. The culprit is the "Contents page style" select trigger (overflow.json).

## P2: video
1. Play AEV2y69z1t0. Check t≈15 s (old header, "10 free uses daily", "0 free uses remaining today") and t≈34 s (personal macOS file picker).
2. The end card says "200+ Free Productivity Tools".

## P2: Combine cover / blog
1. Combine files: the Front Matter has Cover Page, Masthead, Contributors, TOC and List of Images; there's no cover image input.
2. Assemble → page 1 is a white page with the title and editor.
3. The blog /blog/assemble-magazine-or-newsletter-pdf-with-toc says "Upload the cover image".

## Trial counting (PASS, for regression)
1. Fresh context with uses left: Write one article → Build → Download (+1).
2. Download again (no change). Edit → Build → Download (+1). At 2/2 → the cap dialog.

## P3 items
- **Non-Latin:** load article_unicode.txt as an article → Build/Download → pdftotext page 6. The Hindi, Japanese and Arabic lines are empty; the render shows them as shapes.
- **TOC folio:** Combine with Masthead + Contributors + TOC + List of Images. Front-matter folios run ii, iii, (none), v.
