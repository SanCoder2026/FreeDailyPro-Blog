Sent: 2026-10-30 13:59 ET

# QA Report #136 addendum: admin session ~13:55–13:57 ET
Files: batch-55/downloads/. Checked on the box with pypdf and pdftotext.

## image-to-pdf (L-298, B-0236)
- Page size options: A4, US Letter (default), Original image size, Custom size…. So "pick a page size" in the B-0236 meta is accurate.
- Reorder exists: a drag handle plus ↑ / ↓ buttons. Scripted drags didn't move rows (possibly our automation), so the meta must say "reorder", not "drag".
- **B-0236 suggested meta is amended to:** `Turn JPG, PNG and other photos into one PDF. Reorder the pages, pick a page size, and phone photos stay upright. Nothing is uploaded to any server.` (verified in code: 147 chars). FAQ "Can I combine several images?" answer: "Yes, each becomes a page; use the arrows to set the order."
- Output MD-01b-d-and-2-more.pdf, 1,524,497 B: pypdf **3 pages**, all US Letter (612×792), one image per page (1366×3732, 1366×3174, 1366×3302, Flate/PNG), document title "MD-01b-d" (the first file). The page order follows the file list with the first file on page 1; the order of pages 2–3 can't be checked against the sources without them. No text layer.
- Capability notes: two images per page, fit or fill, and margins are already offered; do not list them as gaps.

## camera-capture (L-297, B-0235)
- No front/back switch is visible before the camera starts, though the About text says front and rear.
- **B-0235 FAQ amended:** drop "Can I use my phone's back camera? → Yes, switch cameras." Replace with "Which camera does it use? → Your device's camera; on phones, choose front or rear when your browser asks."
- The "switch camera after start" check needs camera permission; it stays open (with L-052, device test).

No new briefs.
