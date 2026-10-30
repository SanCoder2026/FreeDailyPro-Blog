Sent: 2026-10-30 14:06 ET

# QA-REPORT-137 ADDENDUM — admin session ~14:00–14:01 ET
Files: batch-56/downloads/. Checked on the box with pypdf, openpyxl and python-pptx.

## pdf-bookmarks-editor (B-0237, L-299)
- The editor works: add, rename, indent; Download stays disabled until something changes.
- p-bookmarks.pdf (1,566 B, 3 pages), checked with pypdf. Its outline is 'Intro Renamed' → p1, with the child 'Child' → p1. ✔
- No toast or done state after download → **B-0187**.
- Not tested: a PDF that already has bookmarks (are they kept or replaced?).

## pdf-to-excel (B-0238, L-300)
- tbl.xlsx (20,908 B), sheet "Table 1 (p1)": 31 rows × 4 columns, with header Item, Qty, Price, Total. ✔
- Qty is int, Price is float, Total is int/float, all numeric. Last row: Item 30, 30, 2.5, 75. ✔

## pdf-to-powerpoint (B-0239, L-301)
- p-picture.pptx (109,902 B) and p-editable.pptx (104,825 B) each have 3 slides at 7,560,259 × 10,692,079 EMU (A4 portrait). ✔
- In the editable version, each slide has a text box ("Page 1 hello", …) over a slide-background image. ✔
- In the picture version, the page image is the **slide background** (blipFill), not a picture shape, and there are no shapes. It looks right, but users can't select or move the image. Note only, not a bug.
- **Gap:** both modes download as p.pptx, so the second file saves as 'p (1).pptx'. Add a mode suffix: `p-editable.pptx` / `p-picture.pptx`.

## Housekeeping
The run accidentally added pdf-bookmarks-editor to Favourites on the admin account, and it was removed in the same session. **Reverted; no site change remains.**
