Sent: 2026-11-20 08:40 ET

# FDP-19 Resize & Crop (resize-crop): deep test report for Claude

- **Written:** 2026-11-19 16:38:54 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/resize-crop. Row 19 of TEST-ORDER.md: Pro, Image Tools, test-plan rank 17 (62+68 views). The TEST-ORDER note "API ignores fit mode" concerns the API, which was not tested. **GSC data is not available.**
- **Classification:** Professional Tool, Image Tools (+ home, professional-tools, web-designer solution, eBay photo-spec page). Trial-gated at Download (`gateAtDownload`). Resizing and cropping are not charged.
- **Testers:**
  - **Desk review:** page (expanded), es, /ar, blog, category; ResizeCrop / operations / utils / convertCore code; iloveimg as competitor reference.
  - **YouTube video:** metadata, 36 frames.
  - **Headless Playwright:**
    - 29 image × setting cases, outputs inspected with Pillow
    - gate and dialogs, keyboard crop, axe, phones
    - Firefox and WebKit
    - matrix: 10 profiles, 10 locales + /ar, 6 geos, axe
- **Constraints kept:**
  - Guest only, no sign-in, nothing typed into the email or card prompts.
  - No ad clicks, no API or MCP calls, no site or repo changes.
  - No file was downloaded or executed: every context was at 0, and results were read from memory.
- **Sign-in:** URLs and status are listed in INSTRUCTIONS.md.
  - Untested: "Save to my cloud storage" (sign-in dialog), "Open from Google Drive" (not clicked).
  - Save to Google Drive hit the trial cap before any Google sign-in. "Take photo with camera" was not tested (no camera; see FDP-14 for the camera path).
- **Pending:** the cost of Download with uses left, a second-download charge, download bytes/name, and whether the downloaded image carries a "Created with FreeDailyPro.com" mark. **Needs re-run after midnight UTC (7:00 PM ET).** RERUN-AFTER-RESET row 19 has been added.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the code, restate the problem, push back where we're wrong, and choose fixes that fit how FreeDailyPro ships image tools.

Code to look at (`evidence/js/`):
- `ResizeCrop-CdC5XPx7.pretty.js`:
  - the success toast L224 and "Preview at" line L779, which use the typed size
  - `fitCanvas` call L166
  - default fit `fill` L93
  - limits L58–59, L191, L214–218
  - ratio buttons without `aria-pressed`
  - the unlabeled unit value box
- `operations-ISiPxXUp.pretty.js` `X` L564–571: toBlob with the input mime; GIF/BMP fall back to PNG.
- `convertCore-pdjQ6UTb.pretty.js`: the DPI writers (`setPngDpi`, JPEG density L419/L489), not used by this tool.

After you ship, rerun `scripts/rc-battery.js` + `scripts/rc-inspect.py` and `scripts/rc-gate-kbd.js`, then `test-cases.md` (RC-01…RC-24).

## Intent

Someone needs an image at an exact size or shape: a 1200×1200 marketplace square, a 1080×1920 story, a banner width, a print size. They want to get it right the first time on their own device. The size they're told must be the size they get. They should leave impressed and see the pass as the obvious way to download more.

The engine is strong:
- Every fit mode produces the right pixels.
- EXIF orientation is honoured, and EXIF/GPS is stripped (a privacy plus).
- Crop presets give a centred square in one click. Exact X/Y/W/H boxes make keyboard-only cropping work. Crop → scale and "Resize this crop" chain cleanly.
- HEIC, AVIF, TIFF, SVG and a 108 MP JPEG all open.
- Inline validation stops impossible sizes. Firefox and WebKit work.

Trust is lost in what the page *says* happened:
- the success message and preview report the typed size even when the file is a different size
- the FAQ promises GIF/BMP stay GIF/BMP (they become PNG)
- the video shows a much older tool

## Why: what the evidence says

- **P1: the reported size isn't the real size.**
  - Inside 1080×1080 on a 4:3 photo makes **1080×810**; Outside makes **1440×1080**. Both say "Preview at 1080 x 1080px" and "Resized to 1080x1080".
  - With "Never make it bigger than the original" on, a 50×50 image stays **50×50** while the page says "Resized to 500x500".
  - Marketplace and form users rely on that message. They'd upload, get rejected, and blame the tool.
  - Fix: report the canvas size and say why it differs.
- **P1: copy and video describe a different tool.**
  - FAQ "What happens to the file format?" and Details → Limitations say GIF and BMP are re-encoded as the same type. Live they become PNG, and the name changes to .png. The blog has it right for GIF.
  - FAQ "Can I preview…" says the preview shows "the actual output dimensions". It shows the typed ones.
  - The FAQ and Details list 5 crop ratios; 9 exist.
  - The YouTube video (107 s, 10 views):
    - shows the old Resize (width/height only) and Crop (drag only) UI, with no presets, fit modes, rotate or print units
    - has a "10 **free** uses daily!" caption covering the controls
    - has ≈53 s of outro and a "200+ Free" end card
- **P2 (selected; full list in PRIORITIES.md):**
  - **Accessibility:** the unit value box has no label (axe critical); the ratio buttons don't say which is selected; the result is announced only by a toast; focus drops to body.
  - **Default fit when unlocking is Fill** (stretch), the most damaging choice.
  - **Print:** the cm/inch flow writes no DPI tag, even though the DPI writers exist in convertCore.
  - **Next steps:** Document Scanner (Premium) and Flip & Rotate (already built in) are weak next steps.
  - **Missing:** named marketplace/social size presets and a JPEG quality choice. No share/print button on the result.
  - **Locales:** English title, meta and body; /ar 404.
  - **Layout:** 9 px header overflow at 320 px; Apply Crop needs a scroll on phones.

## Outcomes we want

1. The size in the toast, the preview line and the result card always equals the file's real pixel size. When the fit mode or Never-enlarge changes it, the page says why.
2. FAQ, Details, blog and video say what the tool outputs (GIF/BMP/AVIF/TIFF → PNG, HEIC → JPG), list all 9 ratios, and show today's controls.
3. Print users get a file tagged with the DPI they entered.
4. Screen-reader users can name every control, hear the result, and know which ratio is on.
5. After the result, the next step is something an image user needs next (compress to a KB limit, convert format, remove background).

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PASS** | — | All 29 cases produce the correct pixels (Inside/Outside/Never-enlarge files are right; only the messages are wrong, see #6). `findings/live-functional-findings.md`, `json/inspect.json` |
| 2 | Completeness | **PARTIAL** | LOW | 5 fit modes, 9 ratios, exact boxes, crop→scale, rotate/mirror/B&W, print units, HEIC/AVIF/TIFF/SVG. Missing: named size presets, JPEG quality, DPI tag, batch (sent to Convert Image), share/print. |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Clear two-mode UI and good validation. The success message misreports the size (R06/R07/R09). Unlocking defaults to Fill (stretch). Apply Crop needs a scroll on phones. |
| 4 | Layout | **PASS** | LOW | Clean. 9 px header overflow at 320 px (site-wide). `screens/devices/` |
| 5 | Payment process | **PASS** | — | At 0: Download → "Today's trial uses are done" → "Buy Day Pass — $1" → email prompt (stopped; nothing typed). Drive at 0 → same dialog. Cloud dialog: $4.99/month, sign-in needed. `json/gate-kbd.json`, `screens/live/dlg-*.png` |
| 6 | Information correct | **FAIL** | HIGH | The toast/preview report the typed size, not the output. The FAQ's GIF/BMP output claim is wrong, the preview claim is wrong, and the ratio list is understated. `findings/desk-findings.md` |
| 7 | Indexing | **PASS** | — | 200, self-canonical, in the sitemap, not noindex. GSC data is not available. |
| 8 | SEO | **PARTIAL** | LOW | Strong title/meta/JSON-LD (15-question FAQPage, VideoObject). Locale titles/meta in English; /ar 404. |
| 9 | Blog | **PASS** | LOW | /blog/resize-crop (Oct 24, 2026) is accurate on every point checked. "Every output… original format" is inexact for BMP/AVIF/TIFF. |
| 10 | YouTube video | **PASS (low reach)** | LOW | RLVYl39EfcQ embedded; 107 s, 10 views. |
| 11 | FAQ / guide | **PARTIAL** | MEDIUM | 15 FAQs + Details, mostly right. File-format and preview answers are wrong; ratios understated. |
| 12 | Video shows current tool | **FAIL** | MEDIUM | Old UI, "free" caption, ≈53 s outro. `findings/video-findings.md` |
| 13 | Storage | **PARTIAL (sign-in)** | — | Cloud storage needs sign-in. Drive was capped at 0, so its sign-in was not reached. Open from Google Drive was not clicked. Untested. |
| 14 | Sharing | **N/A** | — | No share-result button; "Share this tool" is site-wide. |
| 15 | Downloads | **PARTIAL / pending** | — | Name logic `resized_`/`cropped_` + original base, with the extension switching to .png for GIF/BMP (code + blog). No actual download yet: all contexts were at 0. RERUN row 19. |
| 16 | Usage count | **PARTIAL / pending** | — | Resize and Crop free (≈35 runs, no change). Download cost with uses left is unobserved; needs re-run after midnight UTC (7:00 PM ET). Counters are display-only evidence. |
| 17 | Category placement | **PASS** | — | Image Tools; also surfaced on home, the web-designer solution and the eBay spec page. |
| 18 | Site section | **PASS** | — | Correct. |
| 19 | AI need / demand | **PASS** | — | Evergreen need; 62+68 views in the test plan; 22 blog posts link here (tools.csv). GSC data is not available. |
| 20 | Merge candidate | **N/A (keep)** | — | Core tool. Flip & Rotate overlaps the built-in rotate/mirror (see that tool's test). |
| 21 | Remove? | **N/A (keep)** | — | High demand. |
| 22 | Duplicates | **PASS** | — | Not listed as a duplicate (DUPLICATES.md). The batch resize in Convert Image is a different job. |
