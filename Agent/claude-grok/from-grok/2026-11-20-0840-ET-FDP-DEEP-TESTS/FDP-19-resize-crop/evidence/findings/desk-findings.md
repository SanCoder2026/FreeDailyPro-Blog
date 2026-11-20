Sent: 2026-11-20 08:40 ET

# Desk findings: code, copy, blog, SEO (Resize & Crop)

## Code (`evidence/js/ResizeCrop-CdC5XPx7.pretty.js`)

- **Limits:** 16,384 px per side (L58), 100 MP output (L59, L214), 16 MP warning (L218), live preview skipped above 4 MP output (L191).
- **Success toast L224:** `Resized to ${e}x${s}` uses the **typed** width/height, not the canvas returned by `fitCanvas` (`Mt`, L166). The "Preview at x × y" line (L779) does the same.
  - Inside, Outside and "Never make it bigger" therefore report sizes the file doesn't have.
  - The fit help text warns for Inside/Outside only.
- **Lock behaviour:** with the lock on, the fit mode is forced to `fill` (L166). With it off, the default fit is `fill` (L93), which stretches.
- **Output encode (`operations-ISiPxXUp.pretty.js` `X`, L564–571):**
  - `canvas.toBlob(input mime, 0.92 for JPEG)`.
  - Browsers can't encode GIF/BMP, so those come back as PNG, and the name switches to .png.
  - EXIF, GPS and DPI are not carried over.
- **DPI tagging:** `convertCore` exports `setPngDpi` and writes JPEG DPI (L419/L489), but Resize & Crop doesn't use them for the cm/inch flow.
- **Crop:** `jt` crops from the original file; the optional "Then scale to width" path goes through `vt`. Touch handlers exist (`touchAction: none`).

## Page copy vs tool

| Claim | Where | Live | Verdict |
|---|---|---|---|
| "Output matches the input type for JPEG, PNG, WebP, GIF and BMP" / "JPEG, PNG, WebP, GIF and BMP are re-encoded as the same type" | FAQ "What happens to the file format?", Details → Limitations | GIF and BMP come out as PNG (R13, R14) | **Wrong** (the blog correctly says GIF → still PNG) |
| "Resize mode shows a live preview of the actual output dimensions" | FAQ "Can I preview…" | the preview line shows the typed size (R06, R07, R09) | **Wrong** for Inside/Outside/Never enlarge |
| Crop presets "Freeform, 1:1, 16:9, 4:5 and 9:16" | FAQ, Details | 9 presets (adds 4:3, 3:2, 3:4, 2:3) | Understated (blog lists all 9) |
| "the same five fit modes as the FreeDailyPro API" | About, FAQ, Details | 5 modes live | OK (API not tested) |
| "the saved file carries no DPI tag" | Tips | confirmed (R21, R22) | OK, but print users lose the size |
| "Animated images keep only their first frame" | Limitations | R14 | OK |
| "iPhone HEIC, AVIF and TIFF files open as well" / "A HEIC photo is saved as JPG" | Details, FAQ | R23 JPG, R24 AVIF → PNG, R15 TIFF → PNG | OK; AVIF/TIFF output type not stated |
| 1:1 draws the largest centred square; enlarge >2× warning; inline errors disable the button | blog | gate-kbd, R10, R19/R20 | OK |
| "Can I resize larger? Yes…" + "Never make it bigger" | FAQ | works (R09/R10) | OK, but the toast misreports R09 |

## SEO

- **Title:** "Resize or Crop an Image Online - Exact Dimensions | FreeDailyPro". Good meta; self-canonical; 10 hreflang + x-default.
- **JSON-LD:** SoftwareApplication (offer), VideoObject "How to Resize & Crop Images Online", FAQPage (15 Q&A), BreadcrumbList.
- **Sitemap:** tool and /blog/resize-crop listed. **GSC data is not available.**
- **Locales:** H1 translated (e.g. リサイズ・トリミング). Title, meta and tool body are English. /ar 404. No consent banner in de/fr geo; prices USD.

## Blog (/blog/resize-crop, "Crop a 4032x3024 Phone Photo to an Exact 1200x1200 Square", Oct 24, 2026)

- Accurate on every point checked:
  - 1:1 centred square, X box, "Then scale to width", cropped_ name
  - the 9 presets, the enlarge warning
  - limits 16,384 / 100 MP / 16 MP, inline errors
  - GIF → still PNG, and "a trial use is counted at the download" (charge pending observation)
- One claim is inexact: "every output is saved again in the picture's original format" (GIF/BMP/AVIF/TIFF become PNG).

## Competitor reference

- iloveimg Resize (fetched 2026-11-19) resizes many images at once ("Change image dimensions in bulk") and by percentage or pixels.
- FreeDailyPro sends batch users to Convert Image.
- Single-image strengths here:
  - fit modes, rotate/mirror/B&W, print units
  - EXIF/GPS stripping
  - exact crop boxes and the crop → scale chain
- Missing:
  - named social/marketplace size presets (e.g. 1080×1350, 1200×1200)
  - a target file size (copy points to the compressor)
  - a JPEG quality choice
  - a DPI tag for print
