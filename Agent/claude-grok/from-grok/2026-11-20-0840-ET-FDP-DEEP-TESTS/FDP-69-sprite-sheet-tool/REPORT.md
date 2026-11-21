Sent: 2026-11-21 15:35 ET

# FDP-69 Sprite Sheet Generator & Splitter (sprite-sheet-tool): deep test report for Claude

- **Written:** 2026-11-21 15:33 EST (box `date`, ET). Testing ran 2026-11-21 15:17–15:32 EST.
- **Tool:** https://www.freedailypro.com/tool/sprite-sheet-tool
  - TEST-ORDER row 69: **Premium Application**, Design & Marketing. Plan note "test-plan (unranked): GSC top-50 SEO backfill 12". No duplicate group.
  - "Premium application · 2 trial uses a day · $3 day pass or $9.99 a month"; trial strip "Trial: 2 uses/day"; Quick Buy Day Pass $3 / Monthly $9.99 (all 6 geo contexts, desktop and phones).
  - Video zmLP5t8sXPo (embedded, 124 s, uploaded 2026-09-23). Blogs /blog/sprite-sheet-tool "Pack 12 UI Icons Into One Sprite Sheet and Split It Again" (200), /blog/avatar-builder (200).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `SpriteSheetTool-CUkSyUBC.js`):**
  - **Combine:** drop frames (`deferUsageLog`), set Columns, Padding, Extrude, optional JSON atlas → **Generate Sprite Sheet** calls `logUsageNow()` (the charge), then shows the PNG and Download PNG / Download JSON atlas.
  - **Split:** drop one sheet (drop zone `gateAtDownload`), Columns/Rows/Padding → **Split into Frames** (no usage call) shows every frame as a full-size `<img src=blob:>`; **Download All as ZIP** packs the same blobs (`frame_01.png` …).
  - Also: Open from Google Drive (sign-in), Take photo with camera.
- **Testers:**
  - Desk: page copy (7 FAQs, how-to, when/when not, tips, limits, privacy), JSON-LD, blog, JS.
  - Playwright, guest contexts; test PNGs generated in testfiles/ (8 numbered 32×32 frames with alpha, 4×2 sheet, 4×2 sheet with 2 px gutters, odd-size sheet, mixed sizes, non-image, 4096² image).
    - `zero.json` (at 2/2), `cases.json` (at 2/2), `ctx.json` (frame tiles saveable), `left-b.json` (the one context in ~40 that loaded with uses left), `quickbuy.json`, `drive.json`.
    - Outputs compared pixel by pixel with the expected sheet/frames in Python; ZIP entries and on-page frame blobs compared by md5.
  - Video frame sheet; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered (Quick Buy stopped at the email box and at Stripe). No ad clicks. No site or repo changes. Downloads parsed, never executed.
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup, closed); paid-pass output. Rows added to SIGNIN-NEEDED.md.
- **RERUN-AFTER-RESET:** one row added (mixed-size combine, gated after reload in the only context with uses).

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for a game or web developer who packs or unpacks sprite frames, and whether the page is set up to turn that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Per-page-load charging is P1; a full-quality result at 0 is a pending owner question; a real save or download at 0 is P1 (Nov 21, corrected 1:19 PM).

**P0:** none.

**P1:**
1. **Split mode gives every frame away at 0 trial uses.**
   - Fresh page at 2/2 (zero.json): Split into Frames runs with no usage call, no POST, no dialog, and shows all 8 frames as full-size PNG `<img src=blob:>` tiles (Z05-split.png). The tiles accept the context menu, are draggable and have normal pointer events (ctx.json), so "Save image as" works on each one.
   - The fetched tile blobs are **byte-identical** to the files inside the paid `sprite-frames.zip` (md5 16bf90a3ab4d … 71149f3cf4b9 for frame_01–08, left-b L10 vs zero Z06) and pixel-identical to the source frames.
   - Only "Download All as ZIP" is gated. Gate Split into Frames (or show reduced thumbnails until a use is taken).
2. **Charging is once per page load; after it, everything in that page is free, even at 2/2.**
   - left-b.json (start 0/2): Generate → one `usage.log` POST, counter **2/2** (the device's server count). Then in the same page: Download PNG ×2, Download JSON ×2, a **new** Generate with other settings (3 cols, padding 4, extrude 2), and Split + **Download All as ZIP**: no POST, no dialog, all files saved.
   - After a reload the gate works again (L11 cap dialog). Charge per new result (each Generate, each ZIP), not per page load.

**Owner question:**
- None beyond the P1s. (Combine at the cap is gated before any preview; Generate at 2/2 on a fresh page opens the cap dialog.)

**P2 — where to look:**
- **Blog is out of date:** "Press Open / Save Sprite Sheet. The PNG opens in a new tab and you save it from the browser's menu" (now Download PNG) and "The tool gives you the image, not the coordinates" (the JSON atlas exists, TexturePacker Hash format). Its CSS-offset maths is still correct.
- **Video zmLP5t8sXPo:** old UI (no Padding/Extrude/JSON atlas, "What is this tool?" layout); the demo combines photos rather than sprite frames; title "Free Step-by-Step Walkthrough", description "Try … free", tags "free online tools", "PDF tools", end card "200+ Free Productivity Tools".
- **Split with a non-image file** (not-image.png): nothing happens and no message appears (the image load promise never settles). Combine shows "Couldn't read not-image.png" correctly.
- **Too-wide message gives the wrong advice:** 2 frames with Columns 999 → "That sheet would be 31968 x 32 px … **Use more columns**, fewer frames or smaller frames." It should say fewer columns.
- **Cap dialog** mentions removing the mark "from your PDFs and images"; this output has no mark (verified pixel-identical), so the line confuses.
- **Locale pages:** chrome, strip and Quick Buy translated; title, meta, H1, modes, labels and FAQ stay English (all 9 locales).
- **SEO:** title "Sprite Sheet Maker Online - Combine or Split | FreeDailyPro" good; meta 76 chars without padding/extrude/JSON atlas/ZIP. Generic OG image.

**P3:**
- Split Columns −3 / Rows 0 silently become 1×1 (whole sheet as one frame); say so.
- Single frames can't be downloaded alone (documented), but the tiles can be saved by hand (see P1).
- iPhone SE 9 px overflow (header action button); ja desktop 1369 px; axe desktop label-content-name-mismatch (serious), region (moderate); Pixel 7 color-contrast ×2 on the ad caption (keep reserved ad slots; fix the caption colour).
- de-DE/fr-FR consent banner (screenshot) partly covers the Feedback button.

## Intent

A game or web developer packs animation frames into one texture (with padding/extrude and an atlas) or recovers frames from a sheet. The output is exact and engine-ready; the gate leaks in Split mode and after the first charge in a page.

## What works (verified)

- **Combine accuracy:** 8 frames, 4 columns → 128×64 sheet **pixel-identical** to the expected sheet; alpha kept. 3 columns, padding 4, extrude 2 → 116×116; every frame rect in the JSON atlas matches the source pixels exactly and the 2 px extrusion repeats the edge rows.
- **JSON atlas:** TexturePacker Hash layout (frame, rotated, trimmed, spriteSourceSize, sourceSize, meta with padding/extrude).
- **Split accuracy:** 4×2 and 4×2 with 2 px gutter (padding 2) → 8 frames pixel-identical to sources; odd 130×65 sheet shows "The sheet size does not divide evenly …".
- **Guards:** 999 columns / padding 500 → "more than a browser can draw (16384 px on a side)"; non-image frame in Combine → "Couldn't read …".
- **Gate on a fresh page at 2/2:** Generate and Download All as ZIP open the cap dialog. Quick Buy: Day Pass → email dialog (stopped), Monthly → Stripe (stopped).
- **Layout:** mode buttons and drop zone above the fold on all devices; Firefox/WebKit/iPad fine.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | Combine + split, padding, extrude, atlas. |
| 2 | Completeness | PASS (minor) | No trim/rotate (documented). |
| 3 | Ease of use | PASS | Clear modes; silent fail on non-image split. |
| 4 | Layout | PASS (minor) | SE overflow. |
| 5 | Payment process | PASS | Premium strip + Quick Buy; email/Stripe reached (stopped). |
| 6 | Information correct | PARTIAL | Blog outdated; wrong "more columns" advice; cap dialog mark line. |
| 7 | Indexing | PASS | 200, canonical self, 10 hreflang + x-default. |
| 8 | SEO | PARTIAL | Meta 76 chars; generic OG. |
| 9 | Blog | PARTIAL | "Open / Save" button and "no coordinates" outdated. |
| 10 | YouTube video | PASS | zmLP5t8sXPo embedded. |
| 11 | FAQ / guide correct | PASS | Page FAQs match the live tool. |
| 12 | Video shows current capability | FAIL | Old UI; photo demo; "free" wording. |
| 13 | Storage | N/A | No cloud save on this page. |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | PASS | PNG, JSON, ZIP correct and exact. |
| 16 | Usage count | **FAIL (P1)** | Split frames free at 0; one charge per page load. |
| 17 | Categorization in section | PASS | Design & Marketing / Premium. |
| 18 | Correct section of site | PASS | Related links 200. |
| 19 | AI need and demand | PASS | "sprite sheet maker", "sprite sheet splitter". |
| 20 | Merge better? | No | Distinct job. |
| 21 | Remove? | No | GSC top-50 backfill; working tool. |
| 22 | Duplicates | None | No duplicate group. |

## After fixes, rerun

- `px69-live.js zero` (Split at 2/2 should hit the gate or show reduced tiles) and `px69-ctx.js`.
- `TRIES=40 px69-live.js left` (each Generate / ZIP charged) and `mixed` (RERUN row).
