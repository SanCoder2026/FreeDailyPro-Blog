Sent: 2026-11-20 08:40 ET

# Compress PDF (compress-pdf): desk findings

- **Written:** 2026-11-19 11:11:11 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/compress-pdf. TEST-ORDER row 4 and tools.csv line 241.
- **Classification:** Professional Tool, PDF Tools. 10 trial uses per day. **Compress is free; each Download spends 1** (live, see `live-functional-findings.md`). $1 day pass / $4.99 monthly.
- **TEST-ORDER note:** test-plan rank 6, 119 views, "4 API levels model" (cited, not refreshed). **Current GSC data is not available.** The /developers compress endpoints (balanced/aggressive/extreme/size/lossless-bw/smallest-bw/greyscale) are out of scope: no API testing.
- **Method:** read-only curl of the tool, 9 locale variants, the blog and sitemap.xml; the JS bundles in `js/` (CompressPdf, operations, UsageAndUpgradeStrip); YouTube metadata, captions and frames; WebSearch.

## SEO (check 8)

| Element | Live value | Note |
|---|---|---|
| Title | "Compress PDF to a Target Size (1 MB, 200 KB) \| FreeDailyPro" (60) | Good keyword fit ("compress pdf to 1mb / 200kb") |
| Meta | "Reduce PDF file size on your device: pick Balanced, Aggressive or Extreme, or type a target like 1 MB or 200 KB. Balanced keeps text selectable. No upload." (155) | Accurate. No "no watermark" claim (unlike merge-pdf). It doesn't mention that downloads carry a mark (see live findings) |
| H1 | Compress PDF – Reduce PDF File Size to a Target | OK |
| H2/H3 | How it works · Watch… · About · How to use it · Common questions · Details · Guides and next steps; H3 "How to compress a PDF to 1 MB", "Which mode should I use?", "Compressing scanned PDFs", "Is my PDF uploaded?" | Strong long-tail coverage |
| Canonical / robots | self / indexable | OK |
| hreflang | 11 | **/es** is server-localized: title "Comprimir PDF a un tamaño objetivo: **gratis**, sin registro" ("free", off-brand), Spanish H1 and meta. **pt, fr, de, ja, hi, zh, ko, id** serve the **English title, meta and H1** in the server HTML. /ar returns 404 |
| JSON-LD | WebSite, Organization, SoftwareApplication (Offer 4.99 USD, no billing period), VideoObject ("How to Compress PDF File Size Online", uploadDate 2026-09-22), FAQPage (8 Q&As, matching the visible FAQ), BreadcrumbList (Home › PDF Tools › Compress PDF) | Offer has no period (LOW) |
| OG | og-default.png | generic |
| Images | 1 `alt=""` (video thumbnail) | LOW |
| Internal links | /blog/compress-pdf ✔, "Next: Add Password to PDF", Merge/Split/Rotate PDF, bundle "Finishing a Self-Published Document" | good |

## Indexing (check 7)

- sitemap.xml: the tool has lastmod 2026-11-19 with a video block; the blog has lastmod 2026-10-17.
- The sitemap video title is "How to Compress PDF File Size **Free** Online". That makes **three different titles** for the same video (YouTube, JSON-LD, sitemap).
- The sitemap publication_date 2026-09-22 vs. the YouTube upload of 2026-09-23 01:31 EDT (LOW).
- WebSearch "freedailypro compress pdf" (2026-11-19): the tool ranks first. No impression data (GSC not available).

## FAQ and usage guide vs. live behaviour (check 11)

8 FAQ questions plus long Details. Live results (`live-functional-findings.md`):

**Confirmed:**
- Gentlest first; levels each a complete file.
- Target stops when it fits (1 MB → 1002.6 KB; 200 KB → 193.7 KB).
- An unreachable target shows the smallest result plus the reason.
- An already-under-target file is left alone ("already under 2.00 MB. No compression needed").
- Text-only file: "Only the file's structure was tidied".
- Password unlock dialog.
- Batch of up to 5, counted as one use.
- The "What is making this file big" breakdown and hint.

**Contradicted or unclear:**
1. **CMYK file misdiagnosed.** A 10.26 MB PDF with CMYK JPEG photos got "This PDF is a scan that is already compressed: its pages are stored as scanner pictures (**JBIG2 or JPEG 2000**)… nothing was changed". The breakdown above it said "Most of this file is pictures, so Balanced should shrink it a lot". The Limitations line ("CMYK images… are left as they are by Balanced") is true, but the message names the wrong cause (MEDIUM).
2. **Extreme never reached grey or black-and-white.** The copy says "every page becomes grey at 70 dots per inch, then pure black and white". On the 6-page photo PDF:
   - Extreme first stopped at Balanced level 2 ("Stopped at level 2… Run anyway").
   - After **Run anyway** it ended at "Level 3: Photo and shaded areas at 70 dpi" (colour), with no grey or B/W level and **no note** explaining why it stopped (MEDIUM). This may be correct engine behaviour (grey not smaller?), but the user isn't told.
3. "Can compressing make my file bigger? Not any more: if a result isn't noticeably smaller… keeps your original": consistent with the CMYK case. Not tested on a file that would grow.
4. "Will compressing blur my text? In Balanced, no… links, bookmarks and form fields are kept": **unverified**. Outputs could not be downloaded (every fresh context capped); **needs re-run after midnight UTC** with `scripts/cp-battery.js`.
5. Owner-restricted PDF (no open password, editing/extraction disallowed) compressed silently with no notice (LOW).

## Blog (check 9)

- /blog/compress-pdf returns 200, self canonical, "Compress a PDF So Email and Portals Finally Accept It", 2026-10-17.
- Links: tool, Rotate, Split, Merge. It embeds the video ✔. It uses trial-uses wording ("10 trial usages a day").
- **Stale or misaligned:**
  - FAQ "Can I compress password-protected files? Unlock or work on an authorized copy first": the tool now unlocks inline.
  - It never mentions the four modes, Target size (the tool's headline feature), levels, Compare, or Several files.
  - "Compression loop: run once… one mild second pass" is generic.
- Good workflow content (portal ceilings, worked numbers, notary case) (MEDIUM: update to show Target size and levels).

## Competitors (check 2)

WebSearch 2026-11-19, "compress PDF to target size in browser no upload": SquashTools (Ghostscript WASM), PDFWrangle, pdfnex, ToolRush, CLEKARA. All are browser-only with a target size.

| Feature | FreeDailyPro | Competitors |
|---|---|---|
| Target size + presets | ✔ (500 KB, 1, 2, 5, 10 MB chips) | ✔ all |
| Levels list, any level downloadable | ✔ (unique) | ToolRush/pdfnex show a step log |
| Side-by-side compare | ✔ page by page | pdfnex: page 1 at 100% with a slider |
| Size breakdown before compressing | ✔ (unique) | — |
| Batch | ✔ 5 per batch on trial, one use, ZIP | rare |
| Password unlock | ✔ inline | ToolRush reports only |
| Offer to **split into parts that fit** when the target is unreachable | unverified absence | pdfnex |
| Decimal-MB guarantee ("MB = 1,000,000 bytes") | unverified (target 1 MB gave "1002.6 KB", which is 1,026,662 bytes if KB = 1024) | pdfnex states it |
| Destination presets (Gmail 25 MB, portal 5 MB…) | absent from the live UI (chips are sizes only) | pdfnex |
| "No watermark" | **No:** downloads carry the "Created with FreeDailyPro.com" mark (cap dialog) | SquashTools, CLEKARA: none |

## Category, placement, duplicates, AI and demand (checks 17–22)

- **Placement:** PDF Tools, Professional Tool. It is in the freelance-close-out, job-application-kit and scan-to-searchable-pdf bundles and the paralegals solution. 38 blog posts link here. Correct.
- **Duplicates:** none for PDF compression. Sibling compressors (compress-image, audio-compressor, compress-powerpoint) are different file types. Keep.
- **AI fit:** not needed. P2 idea: "detect the destination from the user's words (e.g. 'for Gmail') and set the target".
- **Demand:** high (rank 6, 38 inbound posts). Keep.
