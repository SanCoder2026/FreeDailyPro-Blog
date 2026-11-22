Sent: 2026-11-21 23:35 ET

# Reader verification (created forms)

Created form `files/left-2-fillable-form-fillable.pdf` (L01) inspected with pikepdf:

| Field | FT | Flags | DA | Widgets / states |
|---|---|---|---|---|
| zip_code | /Tx | – | /Helvetica 17 Tf | 1, AP stream |
| full_name | /Tx | Required | /Helvetica 17 Tf | V "José Müller" |
| notes | /Tx | Multiline | **/Helvetica 69 Tf** | 1 |
| agree | /Btn | Required | – | /Yes /Off, AS /Yes |
| country | /Ch | Combo | /Helvetica 17 Tf | Opt India, United States, Germany (dup removed), V Germany |
| plan | /Btn | Required, Radio | – | /0 /Off and /1 /Off, Opt [Basic, Pro] |

- Page: no `/Tabs`; widget order zip_code, full_name, notes, agree, country, plan, plan (placement order). No StructTreeRoot. No `/TU`, `/MaxLen`, `/AA`.
- AcroForm: `/Fields` only (no `/DR`, `/DA`, `/NeedAppearances`).

## pdf.js 4.10 (json/pdfjs.json)
- Controls: input full_name (required, 20.5 px), textarea notes (**77.9 px**), checkbox agree (required, checked), select country (Germany), 2 radios plan (required), input zip_code.
- Real Tab order: full_name → notes → agree → country → plan → zip_code (pdf.js sorts by position).
- Radios: click Basic → [true,false]; click Pro → [false,true]. Exclusive.
- Typed Jonathan Reed / Hindi + 2 lines / Москва; selected India; saved → re-read values correct. Render: notes shows only the first line.
- L02: `Group` and `Group_2` are separate groups (both can be on); Q1 pair exclusive.

## PDFium (pypdfium2 form-fill API, files/pdfium-typed-L01.pdf)
- Typed zip_code "Jonathan Reed" (shows), full_name "राम कुमार" (**blank**), notes "Москва" (**blank**). The regenerated fields also lose their borders.
- Values are stored (PyMuPDF re-read shows them).

## PyMuPDF / pypdf fill by script (json/verify-*.json → fill)
- All created forms: every text/checkbox/dropdown/radio set and re-read. pypdf with auto_regenerate works.

## Site tools
- Fillable Forms: lists 6 fields, `*` on required, radio as Basic/Pro; with the required radio unset, "Fill form" gave no download and no message I could capture; after choosing Pro it filled; download OK; Hindi/Cyrillic shown via its own font; notes "Line".
- Flatten PDF on that file: 0 widgets left; text layer of Notes = "Line".
