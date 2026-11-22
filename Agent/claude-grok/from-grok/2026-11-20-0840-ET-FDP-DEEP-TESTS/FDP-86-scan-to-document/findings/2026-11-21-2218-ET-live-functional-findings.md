Sent: 2026-11-21 22:19 ET

# Live functional findings (FDP-86)

Evidence: evidence/json/{zero,left,casesdl,quickbuy,probe}.json, analysis-xlsx.json, analysis-docx.json, evidence/files/, evidence/screens/cases/.

## Usage
- **zero:** every export path (Word, .txt, Copy, Excel, Drive, after reload) shows the cap dialog with 0 POSTs. Copy leaves the clipboard unchanged ("CLIPBOARD-EMPTY" marker kept).
- **left:** POSTs at X02 (Word) and X08 (Copy first after reload) only, among X01–X10. Then one POST per reloaded S case until the counter jumped 7/10 → 10/10 (S12→S14). S14 and S19 were then blocked (each reloaded).
- **casesdl:** 1 POST for 17 downloads. The counter went from 1/10 to 10/10 between S15 and S19 with no POST from this page. S19–S22 still downloaded.
- Fresh profiles: 6–7 in a row at 10/10 before one with uses (twice).

## Outputs
- xlsx: clean exact with types (int, `"$"#,##0.00`, `0.0%`, dates); de Menge 1.2 `0.000`; parts joined in 8 rows; dmy `dd/mm/yyyy`; tilt 6×2; letter+clean → one sheet "Table 1 (p2)".
- docx: page breaks right; rot180 + picture portrait with a 688×1500 picture; wide pictures give landscape pages.
- txt: UTF-8 without BOM, paragraphs separated by blank lines, pages by an extra blank line; photo.txt 0 bytes.

## Switching
- S21: Text → Excel → Word → Text in 4.9 s, status unchanged ("about 95%"), the edited text kept in Word and Text. Excel showed "Put each line of text in its own row".
