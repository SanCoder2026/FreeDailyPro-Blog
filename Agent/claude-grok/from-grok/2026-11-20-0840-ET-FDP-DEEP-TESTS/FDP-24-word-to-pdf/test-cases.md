Sent: 2026-11-20 08:40 ET

# FDP-24 Word to PDF: test cases (guest, fresh context)

| ID | Input (`evidence/testfiles/`) | Action | Expected after fix |
|---|---|---|---|
| WP-01 | rich.docx | Keep formatting | All features as W01; "हिन्दी" shaped correctly |
| WP-02 | rich.docx | Exact look | Bullets "•"; "Page 1 of 3" |
| WP-03 | rich.docx | Text only, A4 | 595×842, Hindi correct |
| WP-04 | rich.docx | Text only, US Letter | 612×792 |
| WP-05 | notes.txt | Convert | 1 page, Letter (US browser) |
| WP-06 | long_200p.docx | Keep formatting | 201 pages, < 2 s |
| WP-07 | long_200p.docx | Exact look | Reasonable size (≪ 31.8 MB) or a warning |
| WP-08–10 | rich.doc / rich.rtf / rich.odt | drop | Specific "save as .docx" message |
| WP-11/12 | broken.docx / renamed.docx | drop | "not a Word document…" |
| WP-13 | empty.docx | Convert | "There is no text…" |
| WP-14 | cols.docx | drop | Auto Exact look; 2 columns |
| WP-15 | cols.docx | Keep formatting | "Not carried over: 1 multi-column section" |
| WP-16/17 | fields.docx | Keep / Exact | Page numbers; bullets "•" |
| WP-18 | rich.docx at 0 remaining | Download | Cap dialog → Day Pass $1 → email prompt (stop) |
| WP-19 | rich.docx with uses | Download ×2 | 0 → 1 then free; badge on each page |
| WP-20 | any | Save to my cloud storage | Sign-in dialog |
| WP-21 | Firefox, WebKit | WP-01/02 | Same as Chromium |
| WP-22 | password-protected .docx | drop | "could not be read… password-protected" (untested) |
