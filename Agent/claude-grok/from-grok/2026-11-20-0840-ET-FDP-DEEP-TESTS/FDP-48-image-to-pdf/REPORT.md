Sent: 2026-11-21 07:23 ET

# FDP-48 Image to PDF (image-to-pdf): deep test report for Claude

- **Written:** 2026-11-21 07:21 EST (box `date`, ET). Testing ran 2026-11-21 06:49–07:19 EST.
- **Tool:** https://www.freedailypro.com/tool/image-to-pdf. Row 48 of TEST-ORDER.md: **Professional Tool**, PDF Tools, plan note "test-plan (unranked): GA top-traffic". No duplicate group.
  - Pair landing pages: /tool/image-to-pdf/{png,jpg,heic,webp,gif}-to-pdf.
  - Video: VeWJoEkv8Kk. Blog: /blog/image-to-pdf ("Turn Eight Receipt Photos Into One Clean PDF…").
  - **GSC data is not available.**
- **Offer:** 10 trial uses a day, charged at Download (`gateAtDownload: true`). Adding, ordering, rotating, page setup and Convert are open, with a 92×120 thumbnail strip and a 489×633 "Preview first page". $1 Day Pass / $4.99 monthly.
  - Everything runs in the browser: HEIC/WebP/AVIF/GIF/BMP/SVG converted to PNG/JPEG on add, then pdf-lib. Page size Letter (en-US/CA/es-MX) or A4 by default, custom (1–200 in/mm/cm), or the image's own size; orientation; margins none/small/normal; fit or fill; two per page.
- **Testers:**
  - **Desk review:** copy, FAQ (10), Details, JSON-LD, 5 pair pages, blog, JS chunks ImageToPdf + imagePdf.
  - **Headless Playwright (Chromium):** at the cap (zero.json), one long page load with uses left (left.json, 15 cases), a GPS check (gps.json), pair pages (pairs.json), preview at 0.
  - **Subsets:** Firefox (S01–S03) and WebKit.
  - **Checks:** every PDF opened (pypdf/pdfinfo/pdfimages/pdftoppm); the matrix (10 devices, 11 locales + /ar probe, 6 geo contexts, axe); the video, frame by frame.
- **Constraints kept:** guest only; no sign-in, card or email; stopped at the Day Pass email prompt and the Stripe Checkout page; no ad clicks; no API/MCP calls; no site or repo changes.
- **Sign-in (untested):**
  - Save to Google Drive (Google sign-in popup with uses left; cap dialog at 0)
  - Save to my cloud storage ("Sign in with your email first", $4.99/month add-on)
  - Open from Google Drive (Google popup)
  - paid-pass output (no badge)
- **Nothing pending a usage reset**, so there's no RERUN-AFTER-RESET row.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Push back where the product intent differs.

**Owner context:** Santosh treats per-page-load charging and full-quality results at 0 trial uses as P1 gate gaps. The "Created with FreeDailyPro.com" badge is intentional.

**Code to look at:**
- **ToolPage gated download** (`vt` / DownloadButton): charges once per tool per page load and doesn't re-check the cap later in the load. Same root cause as FDP-44 to FDP-47.
- **`imagePdf-Dtz8PQyf.js`:**
  - **normalize `M()`:** returns the original JPG/PNG bytes untouched when EXIF orientation is 1. They go to `embedJpg` with EXIF, GPS and camera data intact. Other orientations are re-drawn through `createImageBitmap(…, {imageOrientation:"from-image"})` and re-encoded at JPEG 0.95, which drops EXIF and the stored dpi.
  - **Page size:** "Original size" uses the dpi only when it is between 50 and 1200, otherwise 96, and has no 200 in (14,400 pt) cap.
  - **Format messages:** the TIFF and PDF hints exist but are unreachable, because the drop-zone filter rejects those files first.
- **`ImageToPdf-DEeXBJ-z.js`:** result actions (Download, Save to Google Drive, Save to my cloud storage, Continue with OCR PDF, Preview first page).

**After you ship:**
- Rerun `scripts/ip-live.js left` (TRIES=30). Expect +1 per new PDF, and the cap dialog at 10/10 without a reload.
- Rerun `ip-live.js gps` and check the extracted JPEG has no GPS.
- Work through test-cases.md.

## Intent

Someone has photos (receipts, documents, phone shots, screenshots) and needs one tidy PDF to send or file, without installing anything and without uploading private images.

The core delivers that well:
- **Inputs:** every format the page lists works, including iPhone HEIC, AVIF, 16-bit PNG, CMYK JPEG, animated GIF (first frame, with a clear "Good to know") and SVG.
- **Orientation:** phone photos come out upright.
- **Page setup:** Letter/A4/custom/original, Fit and Fill, and two-per-page all give correct page sizes.
- **Scale:** 60 images in one go gives 30 pages in 3.3 MB, quickly. A 6000×4000 batch gives 16 MB.
- **Messages:** clear errors for a bad custom size, duplicates and skipped files.
- **Uploads:** nothing is uploaded.

What undercuts it:
- **Charging per page load:** 13 PDFs came out of one trial use, and 2 more after the counter showed 10/10.
- **Location leaks into the PDF:** a phone JPG with GPS that needs no rotation keeps its GPS coordinates and camera make/model inside the PDF. That matters for a page that sells privacy ("Your images never leave your device") to people sending receipts and documents to others.
- **"Free" wording:** the video and the five pair pages still say "Free".

## Why: what the evidence says

- **P1, per-page-load charging (gate gap).**
  - left.json: after 26 fresh contexts at 10/10, one had 0 used.
  - L01 Download: 0→1.
  - L02 through L10c then gave 10 more different PDFs in the same load with the counter at 1, including a 6-image CMYK/16-bit/HEIC set, an 8-format set, a 300 dpi scan, a panorama and a 7-receipt Fill layout.
  - At L11 the counter synced to 10/10. Even so, L12 (8 × 6000×4000, 16.7 MB PDF) and L13 (60 images, 30 pages) downloaded with no dialog.
  - Only after a reload (L14) did the cap dialog appear.
  - That makes 13 downloads for 1 trial use.
- **P1, privacy: GPS and camera EXIF embedded in the PDF.**
  - gps.json G01: `P25_gps_orient1.jpg` (GPS 40°44′54.36″N 73°59′8.5″W, Make TestCam, Model X, orientation 1) → Download.
  - `pdfimages -j` on the PDF → the extracted JPEG still has the full GPS IFD, Make and Model.
  - Code: `M()` passes orientation-1 JPEGs through byte for byte. Most phone photos taken in the default orientation, and most photos that were already rotated by an editor, fall in this group.
  - By contrast, `P02_orient6_gps.jpg` (L02) was re-encoded and lost its EXIF.
  - The PDF Title is the first file name (e.g. "IMG_4821" or a client's name). That is a minor related point.
  - The FAQ promises that images "never leave your device", but the PDF does leave it, and it carries the location. Recipients of a receipts PDF can read where the photos were taken.
- **Gate at 0: OK.**
  - At 10/10, Convert still runs (Professional Tool, gate at Download). The user sees only 92×120 thumbnails and a 489×633 preview of page 1.
  - Download and Save to Google Drive open the cap dialog ($1 / $4.99, mentions the badge).
  - Day Pass → email prompt (stopped). Quick Buy monthly → Stripe Checkout (stopped).
  - No full-quality result is reachable at 0.
- **P2 items:**
  - **Video (check 12 FAIL):** VeWJoEkv8Kk, 80 s, uploaded 2026-09-30.
    - Old light UI with no page setup steps, orientation, Fill or pairing.
    - Overlays "10 free uses daily!" and "FREE · PRIVATE · NO LOGIN".
    - It shows the creator's **macOS Downloads folder** (about 0:15–0:18, file names such as "project mtect cse+cyb…list.xlsx") and **Chrome's downloads list** (about 0:46: document.pdf, apples.html, sample_registration_form.pdf, …).
    - About 20 s end card "200+ Free Productivity Tools". The description says "Try … free" and "Free daily uses".
  - **Pair pages:** all 5 titles read "X to PDF Converter - Free, No Upload | FreeDailyPro", and the metas say "Convert X to PDF free…". The on-page body shows the trial strip, and no visible "free" (pairs.json).
  - **Locale pages:** H1 and some labels are translated. The title, meta, "About …", "How to use it", "Common questions", "HOW IT WORKS", "Take photo with camera", "Share this tool" and the video title stay English on all 10 locales.
  - **WebKit (needs a real Safari check):** Playwright's Linux WebKit crashed the tab on Convert with a JPG, twice. A PNG converted fine, and the same JPG decodes and draws fine in a blank WebKit page.
    - This could be the test build rather than Safari (unverified).
    - Please check on a real iPhone/Mac Safari, given that iPhone users are the HEIC audience.
- **P3 items:**
  - **dpi lost on rotated JPGs (Original size):** `P24_orient6_300dpi.jpg` → a 930×1315.5 pt page instead of about 298×421 pt (L07).
  - **No 200 in cap:** a 20,000 px panorama gives a 15,000 pt wide page, over the PDF 14,400 pt limit (L08). Some viewers clamp or refuse it.
  - **TIFF/PDF drops** get the generic toast "2 files can't be used here… Skipped: P08.tiff, P23_document.pdf", not the helpful hints in the code.
  - **A truncated JPEG** is accepted silently and gives a mostly blank page (L05).
  - **Blog:** says images are "embedded as they are", but rotated phone photos are re-encoded at quality 0.95.
  - **Copy and markup:**
    - The meta is 83 chars and generic, with og-default.
    - The JSON-LD VideoObject title ("How to Convert Images to PDF Online – JPG PNG Multi-Image", 2026-08-22) differs from the embedded video ("How to Use Image to PDF – Free Step-by-Step Walkthrough", 2026-09-30).
  - **Layout:**
    - iPhone SE has 9 px horizontal overflow (button row, "right=329/331"), and /ja desktop has 3 px.
    - axe: link-in-text-block (4), label-content-name-mismatch (1), color-contrast on the ad label (2), region (1).
- **Owner question:** the badge sits bottom-right on every page, including scans with content to the edge, so it can overlap the content. That is intentional; it is the owner's call.

## Outcomes we want

1. Each new PDF takes one trial use, a re-download of the same PDF stays free, and at the cap the dialog shows without needing a reload.
2. No EXIF/XMP/GPS in output PDFs, whatever the orientation. The privacy copy can then say so.
3. "Trial uses" wording on the pair pages and in a re-recorded video, made on a clean profile with no personal files on screen.
4. Translated titles, metas and tool strings on locale pages.
5. Original size keeps the dpi and caps at 200 in. TIFF/PDF hints reach the user, and broken JPEGs get a warning.
6. Real Safari confirmed for JPG convert.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | All listed formats, page sizes, fit/fill, pairing, rotate and reorder work; 60 images → 30 pages. |
| 2 | Completeness vs competitors | PASS | Compared with Smallpdf, iLovePDF, Adobe JPG to PDF: same core plus HEIC/AVIF, Fill, pairing, Original size, no upload. Lacks a "compress images" option (16 MB for 8 large photos). |
| 3 | Ease of use | PASS | Clear steps, thumbnails, good messages, locale-aware default page size. |
| 4 | Layout attractiveness | PASS (minor) | Clean; iPhone SE 9 px overflow. |
| 5 | Payment process | PASS / stopped | Cap dialog → Day Pass $1 email prompt (stopped); Quick Buy monthly → Stripe (stopped). Geo: $1/$4.99 in all 6 contexts. |
| 6 | Information correct | PARTIAL | Privacy copy omits that JPG EXIF/GPS is kept; blog's "embedded as they are" isn't true for rotated photos. The rest is accurate. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default; pair pages 200 self-canonical. |
| 8 | SEO | PARTIAL | Title 60 OK; meta 83 generic; og-default; pair titles "Free"; English locale titles. |
| 9 | Blog exists and accurate | PASS (minor) | Detailed and practical; one inaccurate "as they are" line. |
| 10 | YouTube video exists | PASS | VeWJoEkv8Kk embedded. |
| 11 | FAQ and guide correct | PASS (minor) | 10 accurate answers; privacy answer should mention metadata. |
| 12 | Video shows current capabilities | **FAIL** | Old UI, "free" overlays, personal files on screen. |
| 13 | Storage | Sign-in untested | Save to my cloud storage needs email sign-in + add-on. |
| 14 | Sharing | PASS / sign-in untested | Share this tool works; Save to Google Drive needs Google sign-in. |
| 15 | Downloads | PASS (privacy P1) | PDFs correct in size, colour and orientation; GPS EXIF kept for orientation-1 JPGs. |
| 16 | Usage count | **FAIL (P1)** | Per page load: 13 PDFs for one charge, 2 after 10/10. |
| 17 | Categorization in section | PASS | PDF Tools / Professional Tools. |
| 18 | Correct section of site | PASS | PDF Tools breadcrumb; cross-links to PDF to JPG, Merge, Compress, OCR. |
| 19 | AI need/demand | PASS | GA top-traffic; chat assistants don't build PDFs from a user's photos locally. |
| 20 | Merge better? | No | Pair pages already funnel format searches here. |
| 21 | Remove? | No | Top traffic. |
| 22 | Duplicates | None | No duplicate group; pair pages are landing pages on the same tool (self-canonical, distinct titles). |
