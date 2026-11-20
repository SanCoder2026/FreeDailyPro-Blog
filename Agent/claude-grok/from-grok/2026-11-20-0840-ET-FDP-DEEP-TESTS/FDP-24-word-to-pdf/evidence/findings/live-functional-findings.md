Sent: 2026-11-20 08:40 ET

# Live functional findings (headless Chromium, guest, 2026-11-19 18:12–18:21 EST)

Method: fresh context per case; drop; pick mode/paper; Convert to PDF; PDF captured from memory (Blob Proxy for application/pdf). Non-asset requests logged. Download not pressed in the battery. Reference: LibreOffice export of the same .docx (`outputs/ref-rich.pdf`, 3 pages).

| ID | Input / mode | Result | Time | Notes |
|---|---|---|---|---|
| W01 | rich.docx · Keep formatting | 4 pages · 291.5 KB | 1.0 s | Header, title, headings (colour), bold/italic/underline/red, link (URI annotation), bullets incl. level 2, numbered 1–3, bordered table with merged "Total" cell and 02134/00501, picture, centred/right alignment, page break, landscape last page, "Page N of 4". Fonts → Helvetica/Times (documented). **Hindi "हिन्दी" → "हि  दी" running into "emoji"**; Japanese, Arabic, emoji drawn fine; Cyrillic/Greek in DejaVu. |
| W02 | rich.docx · Exact look | 3 pages · 819.6 KB | 1.3 s | Looks like Word; Hindi correct; **bullets as ☐**; footer "Page  of" (fldSimple fields); link kept. |
| W03/W04 | rich.docx · Text only · A4 / US Letter | 2 pages each | 0.5 s | A4 595×842 / Letter 612×792; body text only (as documented); Hindi broken as in W01. |
| W05 | notes.txt | 1 page · 140.7 KB | 0.5 s | Default US Letter; emoji/CJK note shown |
| W06 | long_200p.docx · Keep formatting | 201 pages · 607 KB | 1.5 s | — |
| W07 | long_200p.docx · Exact look | 201 pages · 31.81 MB | 11.6 s | Large |
| W08–W10 | rich.doc / .rtf / .odt | "can't be used here · This tool takes .docx and .txt files." | — | Page promises a "save as .docx" message |
| W11/W12 | broken.docx / text renamed .docx | "This file is not a Word document (.docx). It may be damaged, or it may be another kind of file renamed to .docx." | — | Good |
| W13 | empty.docx | "There is no text in this file, so there is nothing to convert." | — | Good |
| W14 | cols.docx (2 columns, 80 lines) | auto Exact look · 3 pages · 946 KB | 2.0 s | Two columns kept |
| W15 | cols.docx · Keep formatting | 4 pages · 22.8 KB | 0.1 s | Note "Not carried over: 1 multi-column section (shown as one column). Use "Exact look"…" — honest |
| W16/W17 | fields.docx (complex PAGE/NUMPAGES fields, Word bullets) · Keep / Exact | 3 / 2 pages | 0.1 / 1.1 s | Page numbers right in both; Exact look bullets ☐ again |

Network: only `/fonts/DejaVuSans-subset.ttf` and `/fonts/FreeSans-devanagari-subset.ttf` from the site (documented); no POSTs except analytics.

## Gate
- With uses (18:16:56 EST, start 0): convert 0 → 0; Download → rich.pdf 301,488 B (badge "Created with FreeDailyPro.com" ×4), 0 → 1; 2nd Download free; Convert another file + same file + Download free (1 → 1).
- At cap (18:15:26 EST, start 10): Download → "WE VALUE YOUR USAGE · Today's trial uses are done · … $4.99 … Day Pass for $1 …" → Buy Day Pass → "Day Pass, $1 · Enter your email and go straight to payment" (stopped). Result kept. Save to Google Drive → same cap dialog. Save to my cloud storage → "$4.99 per month, 1 GB … Sign in" (Not now).
- Pre-convert: mode buttons expose aria-pressed; the script note is a role=alert; result summary is a role=status.
- Keyboard: 28 Tabs to the drop zone; Enter opens the chooser.
- Phones: iPhone SE and Pixel 7 convert by tap; Download at y≈820 / 713 px.

## Browsers
Firefox and WebKit: Keep formatting 4 pages, Exact look 3 pages; same Hindi break and Exact-look bullet boxes (`outputs/br-*.pdf`).
