Sent: 2026-10-30 13:17 ET

# B-0208 Image Splitter: grid overlay preview, bigger grids, and an H1 that matches searches
Priority: P2 · Estimated effort: S · Report: #127 · Source: QA sweep + SEO curl check + live Google top-3 (WebSearch) 2026-10-30 13:14 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People cutting an image for an Instagram grid should see exactly where the cuts fall before downloading.
## Why
- The upload shows "300 × 200 px"; presets work; "3 × 2" → "6 tiles of about 100 × 100 px" ✓
- It has PNG/JPEG output and an Instagram order option.
- Split and download ZIP → the trial-uses dialog at 0 (limit kept by owner), so the ZIP is untested.
- Top Google results (13:14 ET):
  - freeimagesplitter: up to 20×20, draggable cut lines, paste from clipboard, WebP, PDF pages, carousel presets.
  - Vizua and MultiKit: a live grid overlay, 1–20 rows/columns, batch.
  - pixellize: overlay plus presets.
## Who uses this
Instagram creators, poster printers, puzzle makers.
## Outcomes (ranked)
1. Draw the grid lines over the preview, live.
2. Columns/rows up to 20 (state the max).
3. Paste an image from the clipboard; WebP output.
4. Say how leftover pixels are handled ("the last tile takes the remainder").
## SEO
- **Now:**
  - Title "Split an Image into a Grid - Instagram Grid and Tile Maker" (58, good, but no brand).
  - Meta is 120 chars.
  - H1 "Image Splitter" (fine). Valid JSON-LD.
  - (site-wide items: generic OG image, generic H2s, boilerplate meta, empty video alt → B-0209; English metadata on locale pages → B-0123/L-189)
- **Best result:** H1 "Free image splitter", with a "How to split an image in three steps" H2 and a spec table (formats, max grid, naming).
- **Suggested:**
  - Title: `Image Splitter – Split an Image into a Grid Online | FreeDailyPro` (60)
  - Meta: `Split any photo into a 3×3 Instagram grid, a carousel strip or poster tiles. Pick rows and columns, preview the cuts, and download every tile as a ZIP.` (152)
  - H1: `Image Splitter – Split an Image into a Grid`
  - FAQ: "How do I split an image into 9 pieces for Instagram?" / "What happens if the size doesn't divide evenly?" / "Is my image uploaded?"
## Constraints
Keep the presets and the Instagram order option.
## Test cases
1. Upload, then 3×3 → the overlay shows 9 cells before download.
2. 20×20 accepted; 21 → inline error.
3. A 1000 px width at 3 columns → tiles 333/333/334, stated.
