Sent: 2026-11-21 08:44 ET

# FDP-51: how to reproduce (guest, fresh profile, no sign-in)

**Setup:** open https://www.freedailypro.com/tool/pdf-to-powerpoint. The test files are in `evidence/testfiles/`.

## P1: per-page-load charging
1. Use a fresh context with uses left (`localStorage['fdp-usage-v1'].usageToday` < 10; retry contexts if needed).
2. Drop P02 → Convert to PowerPoint → Download. The count goes 0→1.
3. Click Convert another file → drop P01 → Editable text → Convert → Download. Repeat with other files. The counter stays at 1 (13 more new decks in left.json).
4. Reload → new file → Download: +1. Another new file → Download: no change (L21).

## P2: missing from the PDF Tools hub
1. Open /category/pdf-tools and search the tool grid. PDF to Word, PDF to JPG and PDF to Excel are there; PDF to PowerPoint isn't.
2. It is listed on /category/powerpoint-slides (category-hubs.json).

## P2: no video / blog
1. The tool page has no "Watch" section and no blog link.
2. Searching youtube.com/@freedailypro for "pdf to powerpoint", "pptx" or "pdf slides" returns only PowerPoint→PDF videos.

## P2: Arabic reversed in editable mode
1. Drop P08 → Editable text → Convert → Download.
2. Open the .pptx. The Arabic line reads right-to-left reversed, in presentation-form glyphs (L12; cmp-P08-src-vs-editable.png).

## P2: table text merged
1. Drop P11 → Editable text → Download. On slide 3, "Region Q3 Q4" is one text run, squeezed left over the grid.
2. Same for P12 ("Item Cost", "Laptops $4,800"). See cmp-P11p3 / cmp-P12.

## P2: locale body English
1. Open /de/tool/pdf-to-powerpoint. The header and trial strip are German; the subtitle, drop zone, badges and cross-sell card are English.

## P3 items
- **Near-black colour:** in M01, `check-pptx.py` shows text colours 272727–353535 where the source is 000000.
- **Password copy:** drop P05 → the unlock dialog appears → type u123 → it converts (L07). The "How to use it" text says to unlock first.
- **Non-PDF message:** drop P10 (a text file renamed .pdf) → "looks damaged … Try the Repair PDF tool".
- **Pass dialog mark copy:** at 10/10, click Download → the dialog mentions removing the mark. Trial .pptx outputs (L01, M01) have no mark.
- **Overflow:** iPhone SE (320 px) has scrollWidth 329 (the button row).
