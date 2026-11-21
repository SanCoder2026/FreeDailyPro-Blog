Sent: 2026-11-21 01:50 ET

# FDP-34 Convert Image Format: desk findings (2026-11-21 01:25–01:43 EST)

## Page and SEO
- 200, canonical self, in the sitemap with `/blog/convert-image` and **13 pair pages** (`/tool/convert-image/png-to-jpg` … `png-to-ico`), all 200 with self canonicals.
- Title "Convert Image Format Online - JPG, PNG, WebP, ZIP Batch" (no brand suffix, unlike other tools); meta description 135 chars and specific (PASS). H1 "Convert Image Format". JSON-LD: WebSite, SoftwareApplication (Offer 4.99), VideoObject, FAQPage (**20** questions), BreadcrumbList. og:image is the generic `og-default.png`. Video thumbnail img has no alt.
- **Pair page titles all say "Free"**: "PNG to JPG Converter - Free, No Upload | FreeDailyPro" (13 pages). Suggest "Online, No Upload" (P2, wording rule).
- Locales: es, pt, fr, de, ja, hi, zh, ko, id → 200; `/ar` 404. In the browser the H1 is translated from the **old name** ("Convertir Formatos", "Formate Konvertieren", "形式変換" = "Convert Formats"); title and section headings stay English ("About Convertir Formatos", "How to use it"). ja desktop 2 px overflow.

## Copy vs behaviour
- Accurate on: fill colour (white default), ICO sizes, BMP 24/32-bit, EXIF kept only JPEG→JPEG, SVG 300×150 default, animated GIF first/all frames (≤500), animated WebP first frame, multi-page TIFF first page, no fixed batch count, Stop keeps finished files, width validation, no upload.
- "the batch counts as one use" (FAQ) — true, but live **every** Download after the first in the same page load is also free (see live findings). Other tools' copy limits trial batches ("up to 5 at a time on the trial, counted as one use" — compress-image, listing photos); this tool has no trial batch limit (P1 policy, with the per-page-load counting).
- "The slider … starts at 92" — single mode 92 %, batch mode 80 % (P3).
- "AVIF output depend[s] on your browser … use a current Chrome or Firefox desktop" — AVIF was disabled in both Playwright Chromium and Firefox; whether desktop Chrome/Firefox can encode AVIF from a canvas is **unverified** here. AVIF is in the title-level description "Convert images between PNG, JPG, WebP, AVIF…" (P2: say "AVIF where your browser supports it" or ship an encoder).
- Header "Files never stored / Runs on your device" and Privacy section match the network evidence.
- FAQ duplicates: "Can I convert many images at once?" and "Can I convert multiple images at once?" both present (P3, also in FAQPage JSON-LD). Several FAQs point to "the FreeDailyPro API" for lossless WebP, progressive JPEG, animation (fine as upsell; the API was not tested).
- Cap dialog says passes remove the "Created with FreeDailyPro.com" mark from images; converted images carry no mark (P3 copy).
- "Open from Google Drive" and "Take photo with camera" were not clicked (Drive presumably needs Google sign-in — unverified).

## Blog `/blog/convert-image` ("Convert Image Formats Before the Upload Form Rejects You", Oct 17, 2026)
- Sensible workflow advice (masters vs derivatives, convert → resize → compress). Errors: FAQ "SVG? Vector paths are a different tool path than raster convert" — the tool converts SVG to PNG and has an svg-to-png page; "Batch? Use bulk tools" — this tool batches; never mentions ICO, fill colour, EXIF removal or HEIC (P2). "10 trial usages a day" OK. "GIF is for simple animation" while the GIF output here is a still (P3).

## C05 duplicates
- `heic-to-jpg` and `webp-converter` are presets of this tool (DUPLICATES.md). The page's "Which tool should I use?" box already explains them. Keep convert-image as the hub; keep the presets only if they rank (GSC data is not available).

## Completeness vs competitors (desk; e.g. CloudConvert, Squoosh, iLoveIMG, Convertio — general knowledge, not re-verified live)
- Strong: 9 inputs incl. HEIC/AVIF/TIFF/SVG, 8 outputs, ICO multi-size, EXIF control, DPI, resize/rotate, batch ZIP, no upload.
- Gaps: AVIF output in common browsers, lossless WebP / progressive JPEG / PNG palette (API only), PDF output (Image to PDF exists), target file size (Compress Image), animated GIF/WebP output, per-file before/after preview in batch, colour profile (CMYK→RGB) note.

## Code notes (`evidence/js/`)
- `ConvertImage-*.pretty.js`: single Convert has no usage call; Download goes through the shared download button (`ToolPage-*` → `logUsageNow("download")`); batch `X()` calls `logUsageNow()` once, then downloads the ZIP with a plain helper.
- `index-*.js` `xI(e,…)`: `if (Kt.has(e)) return "allowed"`; `Kt` gains the tool id after the first allowed use and is cleared only by `wI` → one logged use per tool per page load.
- Preview: `<img alt="Result preview" src=blob:…>` of the same blob that Download saves.
