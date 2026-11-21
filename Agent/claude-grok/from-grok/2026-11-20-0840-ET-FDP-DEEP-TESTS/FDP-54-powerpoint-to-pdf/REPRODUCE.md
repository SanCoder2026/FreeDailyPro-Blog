Sent: 2026-11-21 10:12 ET

# FDP-54: how to reproduce (guest, fresh profile with trial uses left)

## P1: per-page-load charging
1. Open https://www.freedailypro.com/tool/powerpoint-to-pdf. Note the "Trial: 10 uses/day · N remaining" strip (or localStorage `fdp-usage-v1`).
2. Drop rich_16x9.pptx → Convert to PDF. The count goes +1, with one `usage.log` POST.
3. Convert another file → standard_4x3.pptx → Convert. No change.
4. Repeat with long_60.pptx and rich_16x9.ppt. Still no change.
5. Reload, then convert any deck. The count goes +1.

## P2: .ppsx
Drop standard_4x3.ppsx. It's uploaded to `/api/trpc/presentation.convert`, then the alert reads "standard_4x3.ppsx: This file is already PowerPoint (.pptx). Pick a different format to convert to." There's no way to convert it.

## P2: blog
Open /blog/convert-powerpoint-slides-to-pdf-for-handouts and read "Common mistakes" and "FAQ-style notes".

## P3: Hindi text layer
1. Convert rich_16x9.pptx with the text layer on.
2. Run `pdftotext` on the PDF, page 6: "नम ते" and "िह दी पाठ यहाँ है".
3. Ctrl+F for "हिन्दी" fails.

## P3: text layer speed
long_60.pptx with "Make the text searchable" on takes about 51 s; with it off, about 6 s.

## P3: .ppt fidelity
Convert rich_16x9.ppt and compare page 2 (pale link) and page 5 (centred caption) with the .pptx output.
