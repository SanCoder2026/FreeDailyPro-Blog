Sent: 2026-11-21 23:35 ET

# Non-Latin text

- Field appearance font: Helvetica WinAnsi only (per-field DR inside AP). No AcroForm /DR.
- Starting value "Москва": pdf-lib throws `WinAnsi cannot encode "М" (0x041c)`; toast "Couldn't make the fillable PDF. Please try again."; 0 POSTs.
- Latin-1 value "José Müller-Øster €": OK.
- Typing after download: pdf.js and MuPDF show Hindi/Cyrillic/CJK via fallback fonts; PDFium shows them blank.
- Field name in Hindi: shown in the editor list, saved as `Field` (regex `[^\w\-]` strips non-ASCII).
- Printed labels (pdfText): Hindi, Cyrillic, CJK, Arabic render correctly; Hindi/CJK/Arabic not extractable as text.
- Dropdown options Россия / भारत: stored; build OK when none selected.
