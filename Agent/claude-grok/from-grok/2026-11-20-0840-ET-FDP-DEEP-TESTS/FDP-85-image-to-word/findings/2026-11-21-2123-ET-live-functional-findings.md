Sent: 2026-11-21 21:25 ET

# Live functional findings (FDP-85)

Evidence: evidence/json/{left,zero,casesdl,casesdl-b,handoff,quickbuy,probe}.json, analysis-docx*.json, evidence/docx/, evidence/screens/cases/.

## Usage
- **left:** X02 charges 1. X03, X04 (rewritten text) and X05 (new picture) are free. X08 after reload charges 1; X09 free. Then the W cases with a reload each: 1 POST per case until the cap. W04 moved the counter 5/10 → 10/10 with a single POST.
- **casesdl:** 22 downloads for 1 POST. **casesdl-b:** 5 for 1.
- **zero:** at 0, Read gives the full text. Every save shows "Today's trial uses are done" with 0 POSTs.
- Fresh profiles: about 20 in a row came up at 10/10 before one with uses (shared pool).

## Output (.docx via python-docx)
- Page size: Letter 11×8.5 / A4 11.69×8.27, landscape for every wide picture. Portrait only for rot180 (wrongly, since the picture was wide) and for tall pictures.
- Multi-page: 2 page breaks for 3 pictures; the reorder is kept.
- Pictures: 1 embedded with the option; picture-only page for photo.jpg; none otherwise.
- rot180 + picture: embedded picture 688×1500 (sideways) on a portrait page. rot90 / exif6 / heic + picture: upright.
- No header/footer, no FreeDailyPro mark in the text. Core title = picture name, author "FreeDailyPro".

## Text accuracy
- letter / exif6 / rot90 / lowcon / big: exact. small: a stray ‘. tilt-dark: "days:" for "days.".
- Paragraph splits on short final lines ("within 10 ¶ working days.", "jusqu'à ¶ la fin"). lines.png: each line becomes its own paragraph.
- twocol: interleaved across columns.
- fr with English: "a Genéve", "regu", "1'été", "gargon". With French: exact. de / hi: exact.
- tilt-light without Straighten: fragments out of order; with Straighten: exact.
- corrupt: 122 s, then "could not be decoded.. Try a clearer picture."
