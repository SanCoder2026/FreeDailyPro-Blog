Sent: 2026-11-21 13:21 ET

# FDP-61 Document Scanner (document-scanner): deep test report for Claude

- **Written:** 2026-11-21 12:59 EST; **-v2 correction:** 2026-11-21 13:18 EST (box `date`, ET). Testing ran 2026-11-21 12:33–12:57 EST.
- **Tool:** https://www.freedailypro.com/tool/document-scanner
  - TEST-ORDER row 61: **Premium Application**. tools.csv category Image Tools; breadcrumb "Premium Applications". Plan note "test-plan (unranked): SEO backfill 8 (GA top)". Duplicate group C06 (the map already says it is distinct from the OCR family).
  - Premium terms on the page: 2 trial uses a day, $3 Day Pass or $9.99 a month.
  - Video fILxNjJP3ZY (embedded, 98 s, uploaded 2026-09-23). Blog /blog/document-scanner (Sep 23, updated Oct 15, 2026).
  - **GSC data is not available.** No API/MCP testing.
- **How it works:** 5 steps, all in the browser:
  1. Add a photo (drop zone, "Take photo with camera" = file input with `capture=environment`, "Open from Google Drive").
  2. Crop: drag a box, then Continue.
  3. Straighten: the page edge finder places 4 corner handles; Straighten (perspective fix), Skip, or Rotate 90.
  4. Enhance: Grayscale / Keep Color, Remove shadows, Contrast 0–120, Rotate, PDF page A4 / US Letter / Fit (150 dpi).
  5. Download PDF / Download PNG / Add page & scan next / New. A second box has a text language list (8), Download searchable PDF (in-browser OCR), Edit as Word and Edit as Excel.
  - An "ID card or two-sided card" tick puts front + back on one page at true size. Pages can be moved up/down or removed.
- **Testers:**
  - Desk: page copy (19 FAQs, how-to, limits, privacy), JSON-LD, blog, JS (`DocumentScanner-D0BCo7Kc.js`, `ToolPage-DwLoDncN.js`, `useDownloadedResult`, `ocrText`).
  - Playwright, Chromium unless noted:
    - `zero.json`: at the cap (2/2). Full flow, every gated button, Add page, Edit as Word.
    - `quickbuy.json`: Day Pass (stopped at the email prompt) and Monthly (stopped at Stripe).
    - `left.json` + `left-firefox.json`: contexts with 2 uses left. 3 pages with reorder, Letter, then PDF, PNG and searchable PDF.
    - `leftB.json`: ID card attempt (script used the wrong button label) plus searchable PDF of a new scan.
    - `idcard-firefox.json`: ID card front + back.
    - `perload.json`: 4 different scans in one page load, then a reload.
    - `msgs.json`: small photo, low contrast, dark page, light desk, EXIF orientation, 6000 px photo, shadow, not-an-image.
    - `orient.json`: EXIF orientation on Chromium, Firefox and WebKit.
    - `misc.json`: camera input, Drive (stopped at Google sign-in), handles, Edit as Excel.
    - `mobile.json`: iPhone 13 (WebKit) and Pixel 7 (Chromium touch crop) flow at the cap.
  - Downloads checked with pdfinfo, pdfimages, pdftotext and renders.
  - Video frame sheet and frames reviewed. Matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout, locale and overlay findings were checked against the screenshots, not the script flags.**
- **Test inputs:** synthetic photos from `make61.py`: tilted pages on a dark desk, shadow, light desk, EXIF 6, 300 px, low contrast, dark page, ID card front/back, 6000×4500, and a text file named .jpg.
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested):** Open from Google Drive opens the Google sign-in popup (verified, closed). Paid-pass output was stopped at the email prompt and at Stripe. Both are added to SIGNIN-NEEDED.md.
- **RERUN-AFTER-RESET:** none. Behaviour with uses left and at the cap was observed today.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for a person who just photographed a page and needs a clean PDF now — and whether the scan makes them want the Premium pass.

**Owner context:** copy and results count as trial uses (Oct 30). Barcode/Invoice charge on every Download (Nov 20). Per-page-load charging and full-quality results at 0 trial uses are P1 gate gaps (Nov 21). The "Created with FreeDailyPro.com" mark is intentional.

**P1 — where to look:**

1. **Edit as Word and Edit as Excel go to a 404.**
   - Both buttons navigate to `/tools/image-to-word` and `/tools/image-to-excel` (plural "tools"), which show "Hmm, we couldn't find that page" (Z08, Z09). The real pages are `/tool/…` (200).
   - The FAQ promises "Edit as Word and Edit as Excel send your scanned pages to the scan converters".
   - In code: `le = t => { …ct("scan-convert", files); Ce(`/tools/${t}`) }`. Use the `/tool/` route.
   - Then check that image-to-word and image-to-excel pick up the "scan-convert" handoff. This couldn't be verified because the link is broken.
   - The handoff is not gated. Decide whether it should take a Premium trial use, since it exports the cleaned scan.
2. **Phone photos with EXIF rotation come out sideways.**
   - A JPEG stored sideways with Orientation = 6 (normal for many phone cameras) is shown at the Crop step turned 90° the wrong way. This happened on Chromium, Firefox and WebKit (orient.json; `orient-*.png`). The scan and PDF are sideways (M05.png: canvas 1124×1008 for a portrait page).
   - Cause, from the code: the upload handler reads the EXIF tag and applies its own transform to `createImageBitmap(file, {imageOrientation: "none"})`. Current browsers already apply EXIF there ("none" is treated as from-image), so the rotation is applied twice.
   - Fix: drop the manual transform (or use `imageOrientation: "from-image"` and no matrix). Re-test with orientation 3, 6 and 8.
   - Users can recover with Rotate 90, but the first impression is a sideways page.
3. **Per-page-load charging: one trial use unlocks unlimited scans in that page load.**
   - perload.json (Chromium, fresh context 0/2): scan 1 → Download PDF → POST usage.log, count 2/2. Then New → scans 2, 3 and 4 each downloaded a full PDF with **no charge and no cap dialog**.
   - After a reload, the next Download PDF showed the cap dialog.
   - Same in leftB.json: after the counter reached 2/2, a new scan downloaded as a searchable PDF and a PNG.
   - Matches the Nov 21 rule (per-page-load charging = P1). In `nr()` the first `tryUse` logs once per tool per load, and later calls return allowed.
   - Decide the unit: one use per new result (PDF/PNG/searchable of the same scan stay one use). Today PDF + PNG + searchable PDF of the same scan cost 1 use (left.json L05–L07), which seems right.

4. **Full-quality scan preview at 0 trial uses (corrected in -v2, was P2 owner question).** At the cap the whole crop/straighten/enhance flow runs and the finished scan is shown on the page at full resolution, without the "Created with FreeDailyPro.com" mark (zero.json Z05: canvas 1002×1131; Z01-enhance.png). Only the PDF/PNG files are gated. Per the Nov 21 owner rule, full-quality results/previews at 0 trial uses are a P1 gate gap. Suggest a scaled-down or marked preview at 0 (the step-by-step flow can stay).

**P2 — where to look:**
- **Copy contradicts the tool:**
  - FAQ "Does this automatically detect and straighten the document's edges? **No** — the straighten step needs the four corners placed manually". Live: "Page found automatically. Check the corners…" on every test photo, with handles on the page corners (straighten-handles.png, mobile-straighten-webkit.png).
  - Privacy: "Nothing is uploaded and **no engine is downloaded**". The searchable-PDF FAQ and the tool's own status text say the first run downloads language data.
  - How-to says "press Crop"; the button is **Continue**.
  - Fix the FAQ and privacy lines. Today they undersell the best feature.
- **Video fILxNjJP3ZY is outdated:**
  - It shows the old one-step page ("Image Tools" breadcrumb, "10 free uses daily" badge, "Use Camera Instead", one "Download Scanned Image" button).
  - The burned-in captions describe "Black & White or Enhanced Grayscale, threshold", modes that no longer exist. The captions also sit on top of the UI.
  - No crop/straighten steps, PDF, multi-page, ID card or searchable PDF.
  - Title "Free Step-by-Step Walkthrough", description "Try Document Scanner free" / "Free daily uses", tag "PDF tools", end card "200+ Free Productivity Tools".
  - The recording shows the full browser chrome (tabs, "Ask Gemini", profile avatar).
- **The tool starts below the fold on desktop.** On 1366×768 the hero picture plus the step strip push the drop zone to ~1,150 px (desktop full screenshot).
  - The hero (`/blog/document-scanner-launch.webp`, alt "Document Scanner preview") shows a filter strip (Original/Auto/Black & White/Grayscale) and "Edge detected" that the tool doesn't have.
  - Suggest a smaller hero or the drop zone first.
- **Locale pages:** H1, badges and the trial strip are translated. The subtitle, "Premium application · 2 trial uses a day · $3 day pass or $9.99 a month", "Day pass / Monthly", the breadcrumb "Premium Applications" and all tool controls stay English (es, ja screenshots). The EU consent banner shows in de-DE/fr-FR (screenshots).
- **Competitive gaps:** one photo per pick (`multiple=false`), so a 10-page stack means 10 round trips. No "magic colour" auto-enhance. No file-size choice. Grayscale pages are stored as RGB JPEG at ~126 ppi on Letter.

**P3:**
- **Corner overlay is clipped:** the blue page outline and fill cover only the top-left ~300×150 px of the photo (default SVG size). The handles themselves are right (straighten-handles.png, mobile-straighten-webkit.png). Give the SVG the image's width/height.
- **Corner handles can't be reached by keyboard:** 4 divs, `tabIndex -1`, no role or label (misc.json). Add focusable handles with arrow-key nudging.
- **A not-an-image file** (text renamed .jpg) goes to the Crop step with an empty box and no error (orient.json: naturalWidth 0; M08).
- **Stale cap message:** after a cap dialog, the status "Today's trial uses are used up…" stays on screen through the next photo and every later step (Z07).
- **ID card naming and list:** a one-page front + back PDF is named `scanned_id-back_2pages.pdf`. In ID mode the list still offers Up/Down for the single front.
- **Counter jump (observation):** two fresh contexts showing "2 remaining today" went straight to 2/2 after one download (one usage.log POST, B03 and P1), while others went 0→1. The server appears to pool counts by network/browser. A user on a shared office network may see "2 remaining" then 0 after one scan. Consistent with earlier tools; owner awareness only.
- **Blog** says to stack pages with Image to PDF and capture both sides of a card as two images. The tool now does multi-page PDF and one-page ID copies itself.
- **axe:**
  - Desktop: label-content-name-mismatch (serious, `.right-2`) and region (moderate).
  - Pixel 7: color-contrast on an ad caption (keep reserved ad slots; fix the caption colour).
  - iPhone SE scrollWidth 329 at 320 (premium badge row; site-wide pattern). ja desktop 1369 px (site-wide).

## Intent

Someone has a receipt, signed form, ID card or notebook page and only a phone. They want a straight, clean, readable PDF to attach or upload. No app to install, nothing uploaded, done in a minute. If the first scan looks like a real scanner made it, the Premium pass is an easy yes.

## What works (verified)

- **Scan quality is excellent.**
  - Tilted pages on a wood desk → straight, white, crisp pages (pages-L05.png). The shadow test page came out evenly lit.
  - Auto corners were right on every desk photo, including the light desk (p5) and a 6000×4500 photo (12 s).
- **Multi-page:** 3 pages, page 2 moved up → PDF order 2, 1, 4 (pdftotext), 3 Letter pages. The button reads "Download PDF (3 pages)".
- **Searchable PDF:** OCR text layer read all 3 pages ("Searchable PDF ready (3 pages read)"), in both Chromium and Firefox. 8 languages (eng, eng+hin, hin, spa, fra, deu, por, ita).
- **ID card:** front + back on one Letter page at true size (923 px at 274 ppi = 3.37 in = 85.6 mm). Label "Download PDF (front + back, one page)".
- **Page sizes:** US Letter default for en-US, A4, Fit (150 dpi).
- **Status messages** for a small photo ("This photo is small (300 x 390 px)…"), a low-contrast sheet and a dark page work as written.
- **Gate at the cap:** PDF, PNG and searchable PDF each open "Today's trial uses are done" (Monthly $9.99 / Day Pass $3). No charge at the cap.
- **Quick Buy:** Day Pass → email prompt (stopped); Monthly → Stripe Checkout (stopped).
- **Mobile:** iPhone 13 (WebKit) and Pixel 7 run the full flow. Touch-drag crop works (Pixel 7) and buttons are large.
- **Mark:** "Created with FreeDailyPro.com" bottom-right on trial PDFs/PNG (intentional).
- **SEO:**
  - Title 52, meta 154 (specific), canonical self, hreflang 10 + x-default.
  - JSON-LD: SoftwareApplication (offer 9.99 USD), VideoObject, FAQPage (19), BreadcrumbList.
  - In sitemap; robots allow. OG image is the generic og-default.png.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PARTIAL | Scan, multi-page, ID, searchable PDF excellent. EXIF photos come out sideways (P1). Edit as Word/Excel 404 (P1). |
| 2 | Completeness | PARTIAL | Strong vs Adobe Scan / Genius Scan for one page. Missing multi-select import, auto colour enhance and size choice. |
| 3 | Ease of use | PASS (minor) | Clear 5-step strip, auto corners. Handles not keyboard-reachable. Overlay clipped. |
| 4 | Layout | PARTIAL | Tool below the fold on desktop (hero). Phones fine. iPhone SE 9 px overflow (site-wide). |
| 5 | Payment process | PASS / stopped | Cap dialog → Day Pass email prompt (stopped); Quick Buy Monthly → Stripe (stopped). |
| 6 | Information correct | FAIL | FAQ says no auto edge detection (it has it). Privacy says no engine is downloaded (OCR downloads one). "press Crop". |
| 7 | Indexing | PASS | 200, index, in sitemap, canonical self. |
| 8 | SEO | PASS | Title/meta/H1/H2, hreflang, 4 JSON-LD types. Generic OG image. |
| 9 | Blog | PARTIAL | Exists (Sep 23/Oct 15). Recommends Image to PDF and two images for cards instead of the built-in features. |
| 10 | YouTube video | PASS | fILxNjJP3ZY embedded + VideoObject. |
| 11 | FAQ / guide correct | PARTIAL | 19 FAQs mostly right. Edge-detection FAQ wrong; Edit as Word/Excel promise broken. |
| 12 | Video shows current capability | FAIL | Old one-step UI, removed modes, "10 free uses daily", "Free". |
| 13 | Storage | N/A | No save/history in this tool (verified). Drive import is sign-in only. |
| 14 | Sharing | N/A (tool link) | "Share this tool" shares the page link; no result share. |
| 15 | Downloads | PASS | PDF (multi-page, Letter/A4/Fit), PNG, searchable PDF, ID PDF all valid. |
| 16 | Usage count | FAIL (P1) | Charged once per page load: later new scans download free and with no cap (perload.json). Full-resolution preview at 0 (-v2). |
| 17 | Categorization in section | PASS | Premium Applications; tools.csv Image Tools. |
| 18 | Correct section of site | PASS | Premium hub + Document Operations Desk ladder; next step OCR PDF. |
| 19 | AI need and demand | PASS | High demand ("scan document to PDF", phone scanner apps). In-browser, no-upload is a strong angle. |
| 20 | Merge better? | No | Distinct from camera-capture/image-to-pdf/OCR family; it hands off to them. |
| 21 | Remove? | No | Useful and Premium-worthy. |
| 22 | Duplicates | None | C06 map already marks it distinct. |

## After fixes, rerun

- `px61-misc.js` (Edit as Word/Excel should land on `/tool/…` with the pages loaded).
- `px61-orient.js` on 3 engines (EXIF 6 upright at Crop).
- `TRIES=40 px61-live.js perload` (expect a charge per new scan, cap dialog on scan 3 with 2 uses).
- `px61-live.js zero` (gates unchanged).
