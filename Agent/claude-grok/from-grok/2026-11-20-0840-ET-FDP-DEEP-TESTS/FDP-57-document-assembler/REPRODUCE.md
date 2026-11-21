Sent: 2026-11-21 11:31 ET

# FDP-57: how to reproduce (guest; fresh profile with 2 uses left; a reset is at midnight UTC = 7:00 PM ET)

## P1: per-page-load gate
1. Open https://www.freedailypro.com/tool/document-assembler. The strip shows "2 remaining today".
2. Drop report_letter_3p.pdf, cover_letter.docx and photo_exif6.jpg; title "Left Packet"; Assemble Document; Download. The counter goes to 2/2, with one `/api/trpc/usage.log` POST.
3. Without reloading, change the title (or the files), Assemble Document, then Download. The file downloads, with no dialog and no POST.
4. Reload, assemble anything, Download. The cap dialog appears.

## 0→2 jump
Watch localStorage `fdp-usage-v1` in step 2: usageToday goes 0 → 2 after one download.

## Save project at the cap
At 2/2, click "Save project": the cap dialog ("downloading needs a pass") appears.

## Hindi in .docx
Assemble cover_letter.docx and look at the "Unicode:" line on its page: the Hindi word is broken.

## Roman numerals
Assemble with a cover and TOC: the cover and TOC pages have no page number; pdfinfo/pikepdf show no /PageLabels.
