Sent: 2026-11-20 08:40 ET

# FDP-24 Word to PDF: priorities

| # | Pri | Item | Evidence | Suggested outcome |
|---|---|---|---|---|
| 1 | P1 | Devanagari broken in Keep formatting and Text only ("हिन्दी" → "हि  दी", runs into next word); copy says Hindi is drawn as pictures | `screens/live/hindi-crop-1.png`, `out-W01.pdf`, `out-W03.pdf`, `br-*-Keep.pdf` | Shape Indic text (or draw it as pictures as promised); align the note |
| 2 | P2 (verify Win/Mac) | Exact look: Word's Symbol-font bullets (U+F0B7) drawn as ☐ boxes | `screens/live/w02-zoom.png`, `w17-bul.png` | Map U+F0B7 → "•" before capture |
| 3 | P2 | Exact look: `w:fldSimple` PAGE/NUMPAGES footers render "Page  of" (complex fields fine; Keep formatting fine) | `out-W02.pdf` vs `out-W17.pdf` | Resolve simple fields too |
| 4 | P2 | Exact look 200 pages → 31.8 MB (Keep formatting 0.6 MB), 11.6 s | battery W06/W07 | Lower raster resolution / JPEG; warn above N pages |
| 5 | P3 | .doc/.rtf/.odt get the generic picker message, not the "save as .docx" message the page describes (code has it, L111–121) | `json/errors.json` | Let those names through to the specific messages |
| 6 | P3 | No PDF bookmarks/outline from headings | pypdf outline | Add outline from Heading styles |
| 7 | P3 | axe: label-content-name-mismatch `.right-2`; ad-label contrast on phones (site-wide) | matrix a11y | Fix label |
| 8 | P3 | tools.csv lists share/copy; result has Download, Drive, cloud only | gate resultButtons | Update catalogue |
| 9 | P3 | /blog/word-to-pdf 404; locale titles English; /ar 404; ja desktop 3 px, iPhone SE 9 px overflow | curl, matrix | Localise; site-wide fixes |
| — | untested | Password-protected .docx | — | Add a test file |
