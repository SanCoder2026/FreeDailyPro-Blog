Sent: 2026-11-20 08:40 ET

# FDP-20 Compress Image: desk findings (copy, code, SEO)

Sources: `html/tool.html`, `html/tool-expanded.txt` (all sections expanded), `json/jsonld.json`, `html/es_tool_compress-image.html`, `js/CompressImage.pretty.js`, `js/utils-BCX55KBw.pretty.js`. Captured 2026-11-19 16:39–16:45 EST.

## Copy describes a mode that does not exist ("Light, 10 % smaller") — P1
Live UI has 4 modes: Medium (25 % smaller), Strong (50 % smaller), Manual Quality, Custom Target (code `E = {medium: .75, strong: .5}`; no `light`). Yet:
- meta description: "Compress an image online: choose **10%**, 25% or 50% smaller or set an exact size limit…" (also the search snippet).
- FAQ "What's the difference between the percentage modes and Custom Target?": "**Light**, Medium, and Strong each guarantee a specific percentage reduction (10%, 25%, 50% smaller)".
- FAQ "Without losing quality?": "Light, Medium, and Strong aim for at least a 10%, 25% or 50% smaller file".
- Details: "The first three work out a goal from the original file, **90%**, 75% or 50% of its size" — on the page the first three are Medium, Strong, Manual Quality.
- Details: "choose Custom Target rather than Light, Medium or Strong".
- The same FAQ text is in the FAQPage JSON-LD (rich results) and in the Spanish page's English fallback text.
- YouTube description: "Light/Medium/Strong aim for at least a 10%/25%/50% smaller file"; the video shows a "Light (10% smaller)" button.

## Other copy vs behaviour
| Claim | Where | Live | Severity |
|---|---|---|---|
| "The tool aims about 3 percent under your number, so portals that count 1 KB as 1000 bytes still accept the file." | Details | True for KB (100 KB → ≤ 99,328 B). For MB, 1 MB → 1,016,321 B (C10) > 1,000,000; the 3 % margin (code `_ = 0.97`) is below the 4.6 % KiB/kB gap at MB scale. | P1 |
| "Metadata such as location is removed" / "Does compressing remove location data? It does." | options note, FAQ | Not when the original is returned (already under target, or not smaller): GPS kept (C26/C27). | P1 |
| "Manual Quality can even produce a larger file than the source." | Limitations | The code never returns a larger file; it returns the original (C06). | P3 |
| "pixels shrink only in fixed steps down to 30 percent" | Limitations | Code steps go to 12 % (`[1,.85,.7,.55,.4,.3,.2,.12]`); a 30 % stop was observed in C24. | P3 (code-level, unverified live below 30 %) |
| Drop zone: "JPG, PNG, WebP, HEIC (iPhone), AVIF, TIFF" | UI | GIF and BMP also accepted (become JPG; GIF animation dropped silently). | P2 |
| Video embed title "How to Compress Images Online with a Guaranteed Size Reduction" | VideoObject | YouTube title is "How to Use Compress Image – Free Step-by-Step Walkthrough". | P3 |
| Toast after Medium/Strong: "Compressed to your target" | UI | User never set a target; "Compressed – 31 % smaller" is clearer. | P3 |

## Code notes for Claude
- `utils-BCX55KBw.pretty.js` `$()` L120–200: quality binary search 0.1–0.95 in 8 steps, then the scale list; `S = floor(t * 0.97)`.
- `E()` L108–124 and the `alreadyUnder` branch L139–153 return the original `File` as `blob` — this is the metadata leak path. A lossless EXIF/XMP strip for JPEG (drop APP1/APP13 segments) or a forced re-encode at q≈0.92 when the user expects metadata removal would close it; at minimum the result line should say "the original is returned unchanged, including its location data".
- `CompressImage.pretty.js` L395–430 mode buttons lack `aria-pressed`; L460–490 number input/select lack labels; L533 result `<p>` is not `aria-live`.
- 1 MB preset: `ce` presets are KiB/MiB (1024-based) and labelled "KB/MB".

## SEO / indexing
- 200, canonical self, no robots meta/header, in sitemap (`raw/sitemap.xml`). GSC data is not available.
- Title "Compress Image Online - Reduce File Size by % | FreeDailyPro"; FAQPage + VideoObject JSON-LD.
- /es: Spanish title "Comprimir imagen en línea: reduce el tamaño, **gratis**" (wording policy: avoid "free"; P3). /ar → 404 (no ar hreflang, consistent with other tools).
- /blog/compress-image → 404; the page links /blog/strip-gps-and-exif-from-photos and /blog/convert-iphone-heic-photos-to-jpg; tools.csv says 30 posts link here.
