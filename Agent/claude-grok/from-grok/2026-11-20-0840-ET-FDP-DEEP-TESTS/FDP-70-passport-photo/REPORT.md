Sent: 2026-11-21 15:54 ET

# FDP-70 Passport Photo Maker (passport-photo): deep test report for Claude

- **Written:** 2026-11-21 15:52 EST (box `date`, ET). Testing ran 2026-11-21 15:34–15:50 EST.
- **Tool:** https://www.freedailypro.com/tool/passport-photo
  - TEST-ORDER row 70: **Professional Tool**, Image Tools. Plan note "test-plan (unranked): GSC top-50 SEO backfill 13". No duplicate group.
  - Trial strip "Trial: 10 uses/day"; Quick Buy Day Pass $1 / Monthly $4.99 (all 6 geo contexts). "NEXT STEP: PREMIUM APPLICATION Document Scanner" card.
  - Video Q7Sx8-jE-w4 (embedded, 92 s, uploaded 2026-09-23). Blogs /blog/passport-photo "Make a Passport Photo From a Phone Picture, Sized and Printable" (200) and /blog/resize-crop (200).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `PassportPhoto-DjC3QAJh.js`, `jpegDpi-c8DPdZxl.js`, shared `ToolPage` save path):**
  - Drop a photo (drop zone `gateAtDownload`), pick one of 12 templates, frame with Zoom 100–400 % and two Position sliders, check the head against two guide ovals (preview only, a 300 px wide `<canvas>`).
  - Optional **Make background white + auto-fit head**: a 4,574,861-byte `/models/u2netp.onnx` cut-out model (+ onnxruntime wasm) runs on the device; no upload, no usage call.
  - **Download Single Photo**: template size at 300 DPI (`round(mm/25.4*300)`), JPEG quality searched (8 steps between 0.2 and 0.95) to fit the File size limit, then the JFIF density is set to 300 DPI and the toast shows "W x H px, 300 DPI, N KB".
  - **Download Print Sheet (4x6")**: 1200×1800 or 1800×1200, whichever fits more copies, thin grey cut lines, JPEG 0.95.
  - Both downloads go through the shared save function. For trial users it draws the "Created with FreeDailyPro.com" badges (intentional) and **re-encodes the JPEG with `canvas.toBlob(type, 0.92)`** (ToolPage-badge-excerpt.pretty.js, last lines).
  - Also: Open from Google Drive (sign-in), Take photo with camera (`<input capture="environment">`, native picker).
- **Testers:**
  - Desk: page copy (14 FAQs, how-to, when/when not, tips, limitations, privacy), JSON-LD, blog, JS.
  - Playwright, guest contexts. Test photos in testfiles/ (two openly licensed Wikimedia portraits: FDR passport photograph, public domain; Álvaro Santos Pereira, OGL v1.0) plus derived busy-background, no-person, tiny and non-image files (make-testfiles.py).
    - `zero.json` (at 10/10), `cases.json`, `fit.log` (auto-fit on 3 photos × 2 templates, at 10/10), `left-firefox.json` (start 0/10, 13 downloads), `limits.json` (Chromium, start 0/10, 6 size-limit downloads), `quickbuy.json`, `drive.json`, `camera.json`.
    - Every saved file checked in Python (Pillow + JFIF header parse): pixel size, DPI fields, bytes.
  - Video frame sheet; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout, overlay and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered (Quick Buy stopped at the email box and at Stripe). No ad clicks. No site or repo changes. Downloads parsed, never executed.
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup, closed); paid-pass output (no badge, so the re-encode below may not happen there). Rows added to SIGNIN-NEEDED.md.
- **RERUN-AFTER-RESET:** none needed (zero, left, limits and cases all ran).

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for someone making a passport or visa photo at home for an online form or a 4x6 print, and whether the page is set up to turn that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Per-page-load charging is P1; a full-quality result at 0 is a pending owner question; a real save or download at 0 is P1 (Nov 21, corrected 1:19 PM).

**P0:** none.

**P1:**
1. **The File size limit is broken for trial users, and the toast reports the wrong size.** For an online application this is the reason to pick a limit.
   - The tool fits the JPEG under the limit, then the shared save path draws the badge and **re-encodes at quality 0.92**. The saved file is larger than the limit, while the toast still shows the pre-badge size:

     | Template / limit | Toast | Saved file | Engine |
     |---|---|---|---|
     | US / Under 50 KB | "50 KB" | **63,162 B** | Chromium |
     | US / Under 100 KB | "89 KB" | **80,033 B** (fits) | Chromium |
     | UK / Under 50 KB | "50 KB" | **51,312 B** | Chromium |
     | Canada / Under 100 KB | "100 KB" | **101,400 B** | Chromium |
     | India / Under 50 KB | "49 KB" | **79,577 B** | Firefox |
     | UK / 240, Canada / 500 | 61 / 123 KB | 54,551 / 108,633 B (fit) | Chromium |

   - Four of five 50/100 KB tries are over the limit. A portal with a hard limit rejects the upload.
   - **Fix direction:** keep the badge, but run the size search (and `jpegDpi`) on the final badged image, or badge before `Re()`. Then show the real saved size in the toast.
2. **The promised 300 DPI is lost in every download.** All 17 saved JPEGs (single and sheets, both engines) have JFIF `units=0, density 1:1` (no DPI), because the badge re-encode drops the APP0 segment that `jpegDpi` wrote.
   - The toast, the FAQ ("300 DPI at the selected template's real physical dimensions") and the blog all say 300 DPI.
   - Print apps that honour the density will print a 600×600 file at 72/96 DPI (6–8 in wide), not 2×2 in. The blog's "print at 100 percent scale" advice makes this worse.
   - Same fix: set the density after the badge step. Then check: `PIL Image.open(f).info['dpi'] == (300, 300)`.
3. **Charging happens once per page load; after it, everything in that page is free.**
   - left-firefox.json (start 0/10): the first Download Single Photo sends one `usage.log` POST (0→1/10). Then in the same page these were all saved with no POST: Print Sheet, UK single + sheet, Canada sheet, India 50 KB, China single, auto-fit + US single, **Upload Different Photo** + new download.
   - After a reload, one more POST (1→2/10); then a Print Sheet was free again. That is 13 files for 2 uses.
   - limits.json: after the first charge, the local counter jumped to **10/10** (server count). The page kept downloading 5 more files at 10/10 with no dialog.
   - **Fix direction:** charge per download (or per new photo + template), not per page load.

**Owner question:** none.
- At 10/10, the preview is a 300 px wide canvas with guide ovals on by default. That is below output size for every template (US 600, UK 413), so it is not a full-quality result.
- Auto-fit runs at 0 (cut-out + white background shown in that 300 px preview). It is a framing step; the downloads stay gated.

**P2 — where to look:**
- **Auto-fit misjudges head size but always says "the head sized to the middle of the allowed range".** Checked against the guide-oval screenshots (F-*-guides.png):
  - FDR (front-facing): US zoom 110 %, UK 167 %; the head sits **inside the green "smallest head" oval** (too small).
  - Busy-background landscape: the head is far below the minimum.
  - Pereira (3/4 view): the head is larger than the red oval and off the centre line.
  - The download L10 (US) measures about 42 % head height against a 50–69 % rule. The message does say "estimate"; consider "check the ovals" wording without claiming the middle, or a warning when the estimate looks outside the range.
- **Video Q7Sx8-jE-w4** shows an older UI: no guide ovals, auto-fit, size limit or template spec line, and the strip says "2 free uses remaining" (now 10/day).
  - The demo photo has a dark background and stays dark in the "passport-ready photo". The thumbnail carries an "APPROVED" stamp, which contradicts the page's "not a guarantee of acceptance".
  - Title "Free Step-by-Step Walkthrough", "Try … free", "10 free uses daily!", end card "200+ Free Productivity Tools". Wording should be Professional Tools / trial uses.
- **Cap dialog** says a pass removes the mark "from your PDFs and images". It is correct here, but the dialog does not mention that the badge (re-encode) also breaks the size limit/DPI; once P1 is fixed this is fine.
- **Locale pages** (es screenshot): chrome, strip, H1 and breadcrumb translated; tagline, "Runs on your device", drop-zone text, "Take photo with camera", "Ad-free: …" and the FAQ stay English.
- **Duplicate FAQs:** "Which countries' size presets are included?" / "Which photo sizes does it offer?" and "Does a correctly-sized photo mean it's guaranteed…" / "Will my photo be accepted…" (14 FAQ entries in FAQPage JSON-LD). Merge them.
- **SEO:** title "Passport Photo Maker - Size Presets & Print Sheet | FreeDailyPro" good. Meta (133 chars) doesn't name the 12 countries, 300 DPI, KB limit or white background. VideoObject name "How to Make Passport & Visa Photos Online" differs from the YouTube title.

**P3:**
- At the cap, the success toast ("600 x 600 px, 300 DPI, 89 KB" / "Print sheet ready…") fires in the DOM together with the cap dialog. It is not visible in the dialog screenshot, so the impact is low; still, show it only after a real save.
- "Take photo with camera" opens the rear camera (`capture="environment"`). A front-camera ("user") option would help people taking their own photo.
- iPhone SE 9 px horizontal overflow (header button); axe desktop label-content-name-mismatch (serious), region (moderate); Pixel 7 color-contrast ×2 on the ad caption (keep reserved ad slots; fix the caption colour).
- de-DE/fr-FR consent banner covers the bottom of the fold and the Feedback button (screenshot).
- Monthly Quick Buy goes straight to Stripe without the email step that Day Pass shows (stopped at Stripe).

## Intent

Someone at home needs a passport or visa photo: the right pixel size, the head in range, a file under the portal's KB limit, and a 4x6 sheet that prints at true size. Sizing, cropping and sheet layout are right; the trial-user save path breaks the two promises an online form and a print shop depend on (KB limit, 300 DPI), and the gate charges once per page.

## What works (verified)

- **Template sizes (Pillow on saved files):** US 600×600, UK 413×531, India 602×602, China 390×567, Canada 591×827. All match `round(mm/25.4×300)` and the on-page spec line. Head ranges match the official specs for US/UK/Schengen/AU/JP/Canada/China. NZ/IE/SG/KR show the "not yet compared with the official page" note.
- **Print sheets:** US 6 up portrait 1200×1800; UK 8 up landscape 1800×1200; Canada 4 up portrait 1200×1800. These match the toast, FAQ and blog (blog India "only 2" matches the code). Grey cut lines; badge at the sheet corners (intentional).
- **Auto-fit mechanics:** the model loads from this site (200, 4.57 MB), runs in about 3–4 s, and turns the background white. Downloads are disabled while busy ("Download is paused until it finishes"). A photo with no person gives "No person was found to position automatically - use the sliders."
- **Guards:** non-image → "could not be read as an image…"; 300×200 photo and Zoom 400 % → "Low resolution: … only about 200 px / 50 px wide, and this size needs 600 px…".
- **Gate on a fresh page at 10/10:** Download Single Photo and Print Sheet open the cap dialog; nothing saved. Quick Buy: Day Pass → email dialog (stopped), Monthly → Stripe (stopped).
- **Layout:** drop zone, Drive and camera buttons above the fold on all 10 devices; Firefox/WebKit/iPad fine.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 12 templates, framing, auto-fit, size limits, 4x6 sheet. |
| 2 | Completeness | PASS (minor) | No background colour other than white (fine for most). |
| 3 | Ease of use | PASS | Ovals + spec line help; auto-fit message overclaims. |
| 4 | Layout | PASS (minor) | SE overflow. |
| 5 | Payment process | PASS | Strip + Quick Buy; email/Stripe reached (stopped). |
| 6 | Information correct | **FAIL** | Toast KB and "300 DPI" wrong for saved files; auto-fit "middle of range". |
| 7 | Indexing | PASS | 200, canonical self, hreflang set. |
| 8 | SEO | PARTIAL | Meta thin; duplicate FAQs; VideoObject name. |
| 9 | Blog | PASS (minor) | Accurate on sizes/sheets; its 300 DPI and size-limit promises fail live (P1). |
| 10 | YouTube video | PASS | Q7Sx8-jE-w4 embedded. |
| 11 | FAQ / guide correct | PARTIAL | 300 DPI and size-limit FAQs not met by the saved file; duplicates. |
| 12 | Video shows current capability | FAIL | Old UI; dark-background demo; "APPROVED" thumbnail; "free" wording. |
| 13 | Storage | N/A (sign-in) | Drive open needs sign-in. |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | **FAIL (P1)** | Sizes right; KB limit exceeded; DPI missing. |
| 16 | Usage count | **FAIL (P1)** | One charge per page load. |
| 17 | Categorization in section | PASS | Image Tools / Professional. |
| 18 | Correct section of site | PASS | Related links 200 (compress-image, resize-crop, convert-image, document-scanner, remove-background). |
| 19 | AI need and demand | PASS | "passport photo maker", "visa photo size", "passport photo 4x6". |
| 20 | Merge better? | No | Distinct job; links to Resize & Crop / Remove Background. |
| 21 | Remove? | No | GSC top-50 backfill; high-intent tool. |
| 22 | Duplicates | None | No duplicate group. |

## After fixes, rerun

- `TRIES=40 px70-live.js limits` (every saved file ≤ limit; toast = file size) and `left` (each download charged; DPI 300 in `info`).
- `px70-live.js zero` (gate) and `fit` (auto-fit message vs ovals).
