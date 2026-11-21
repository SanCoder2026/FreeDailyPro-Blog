Sent: 2026-11-21 05:21 ET

# FDP-44 Excel to PDF: live functional findings (guest, 2026-11-21 04:55–05:14 EST)

**Intent:** check that a guest gets a correct, readable PDF from real workbooks, and that Download is gated exactly once per result.
**Why:** this is a PDF Toolkit Professional Tool (L-243 rank 1), and the PDF is the deliverable people share with managers and clients.

## Gate and trial uses (live/gate-1.json, gate-2.json, cases-chromium.json)
- **At 0 (10/10):** Convert works, which is fine because `gateAtDownload: !0`.
  - Download / Save to Google Drive open the cap dialog ("Today's trial uses are done… $4.99 monthly / $1 Day Pass").
  - Save to my cloud storage opens "Sign in with your email first" (dlg-zero-*.png).
  - Day Pass → email prompt (stopped, nothing typed). Quick Buy monthly → Stripe Checkout title (stopped).
  - The first-page preview at 0 is a 633×489 raster image of page 1 only. Not a full-quality result.
- **P1, per-page-load charging (gate gap):**
  - gate-1: Download X01 0→1; the same file again stays 1; X02 and X07 downloads in the same page load stay 1. Reload, then X06 → 2.
  - cases-chromium: one page load, **12 distinct PDFs from 12 different workbooks (T01–T10, T14, T17) for 1 trial use**.
  - **Worse:** between T10 and T14 the counter synced to 10/10 (0 left) while the page stayed open. Downloads T14 (.xls) and T17 (.xlsm) still went through with no cap dialog. A page kept open sidesteps the gate entirely.
  - Same mechanism as earlier tools: the ToolPage trial-use wrapper (`vt`→`Sa`) remembers "already charged for this tool" per page load instead of per result.
- **Charging policy:** Excel to PDF takes a trial use on Download, so it isn't an uncounted tool and there's no policy question.

## Conversion quality (live/downloads, verified with poppler)
| Case | Result |
|---|---|
| T01 X01 default | PASS. Letter landscape (auto), 4 pages. Title printed once, headers repeat, $ and % and dates as displayed, negative red kept, long notes wrap. Hidden sheet/column/rows absent (no "secret-", "HIDDEN", Person 4/5). Badge on every page. DejaVu embedded; text selectable. |
| T02 Include hidden data | PASS. 3 sheets, 5 pages; hidden column/rows/sheet now present. |
| T03 A4 + Landscape + Large, no grid, no colours | PASS. 841.89×595.28; plain table. |
| T04/T05 X02 30×300 wide | PASS. 42 pages (A4 landscape, settings carried over from T03) / 22 pages (Small). First column repeated; note shown. |
| T06 X03 scripts | **P2.** CJK/Japanese/Korean/Arabic/Hebrew/Thai drawn as images and look right. **Hindi is drawn as font text (FreeSans) with no shaping:** "नमस्ते" prints as "नमस् ते" (broken conjunct). **🚀 prints as an empty box** (✅ is fine). The pre-convert warning says these "are drawn as pictures so they look right". |
| T07 X04 formulas with no saved result | PASS. Warned before converting: "5 formula cells … will print blank: Sheet!D2…D6 … 5 simpler formulas were calculated here". VLOOKUP column blank, SUM column calculated. |
| T08 X05 50,000 rows | PASS. 8.9 s, 1,725 pages, 11.2 MB. |
| T09 UTF-8 BOM + semicolon CSV | PASS. Delimiter detected; Zoë/Köln/São Paulo correct; no BOM artefact. |
| T10 quoted CSV | PASS. Commas, quotes and multi-line inside quotes are correct. |
| T11 empty workbook | PASS. "There is no data in this file." |
| T12 corrupt / T13 text renamed .xlsx | PASS. Clear messages; Convert disabled. |
| T14 .xls | PASS for the table. **P2:** chart and picture dropped with **no note** (the same workbook via LibreOffice has both). |
| T15 .ods | **P2 copy:** "“X12_finance.ods” looks like a OpenDocument spreadsheet file, not a spreadsheet." Wrong article, and it contradicts itself. |
| T16 .docx | PASS. "looks like a Word file, not a spreadsheet". |
| T17 .xlsm | PASS. Same as T01. |
| T18 LibreOffice-saved .xlsx | PASS. Notes "1 chart … 1 picture was not included". |

- **P2, picture note missed:** X01 (written by openpyxl, the library behind pandas `to_excel`) has a picture, but only the chart is noted. The code counts `xdr:pic` by its literal prefix, and openpyxl writes the drawing with a default namespace (`<pic>`), so the picture vanishes silently. The FAQ promises "a note telling you how many charts or pictures were left out".
- **Cross-engine (nodl subsets):** Firefox and WebKit give the same summaries and messages for T01/T06/T09/T12/T15.
- **Privacy:** live/privacy-net.json. Dropping and converting X01 sent 5 requests (site insight.hit 162 B, GA). None carried cell text or the file name, which matches "never uploaded".
- **Keyboard:** Tab reaches the drop zone; Enter opens the chooser (gate-2).
