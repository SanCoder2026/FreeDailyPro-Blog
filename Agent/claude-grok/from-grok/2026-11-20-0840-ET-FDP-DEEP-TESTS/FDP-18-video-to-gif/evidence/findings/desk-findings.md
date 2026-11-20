Sent: 2026-11-20 08:40 ET

# Desk findings: code, page copy, blog, SEO (Video to GIF)

## Code (`evidence/js/VideoToGif.pretty.js`, `operations-P8Ty5WBe.pretty.js` `St` L766–804)

- **Pipeline:** `-ss/-t` input seek, then `setpts=PTS/speed`, `fps`, `scale='min(W,iw)':-2:flags=lanczos`, then `palettegen=stats_mode=diff` → `paletteuse=dither=bayer:bayer_scale=4`.
  - `-loop -1` when "Play once" is ticked.
  - Two passes: palette, then encode.
  - No upscaling. Rotation is honoured (ffmpeg autorotate).
- **Largest file (`Ce` L54–80, `J` L42–53):**
  - It encodes a sample of up to 1.5 s from the middle of the range and estimates with ×1.1 margin, stepping fps 20→12→8→6 and width ×0.75 (min 160).
  - The final encode retries up to 2 more steps.
  - **`le` (L151, L184) builds "A clip of about N s would fit in X MB at W px and F fps." but is never displayed.** The over-cap toast (L205–208) only says "Use a shorter clip". FAQ, Details and the blog all promise that hint.
- **File acceptance (L234–248, L485, L503):** `accept: "video/*"`, then the file must load in a browser `<video>` element.
  - `onError` sets "couldn't be read as a video… Try re-exporting it as MP4" and disables Create GIF.
  - ffmpeg.wasm could read AVI/WMV/FLV, but the browser pre-check rejects them first. The page lists them under "Reads".
- **Limits:** `checkFileSize` 50 MiB trial / 200 MiB Pro (`ffmpegEngine` L217–218). The drop zone says "Large files (over 200 MB) may take longer…". The messages say "MB" for MiB values (68.3 "MB" for a 71.7 MB file).
- **Controls:**
  - Width 240–800, fps 5–20, speed 0.5–2x, Largest file No limit / 2 / 5 / 8 (chat apps) / 10 MB.
  - Only Start and Length have `htmlFor` labels.
  - Settings survive New and Reset.
- **Static copy `q` (L95–99):** "How to use it: Upload your video and download the resulting animated GIF." This is thin next to the Details guide.

## Page copy vs tool

| Claim | Where | Live / code | Verdict |
|---|---|---|---|
| "If nothing fits, it reports how many seconds would." | FAQ "What does the Largest file setting actually do?" | never shown (G08) | **Wrong** |
| "If Largest file cannot be met, the tool says how long a clip would fit." | Details → Limitations | never shown | **Wrong** |
| "When nothing fits, it tells you how many seconds of the clip would" | blog | never shown | **Wrong** |
| Reads "MP4, MOV, MKV, WebM, AVI, WMV, FLV" | Formats box | AVI/WMV/FLV refused (G13–G15, Chromium + Firefox) | **Wrong** |
| "Large files (over 200 MB) may take longer…" | drop zone | trial uses stop at 50 MB | Misleading for trial users |
| "Set Start and Length here rather than trimming first" | Details → Tips | the >20 s warning says "Trim it down first with the Trim Video tool"; the Formats box says "Trim Video: cutting the clip down before making the GIF"; the blog says "cut it with Trim Video first" | Contradiction |
| "Some phone .mov files use a codec this tool can't read — if processing fails right away…" | tip, FAQ | the failure happens at file load, with the wording "re-exporting it as MP4" | OK, slightly dated |
| Length min 0.5, defaults 480 px / 12 fps / 0 / 5 s | Details | matches | OK |
| "Output is never wider than the source" | Limitations | G16 | OK |
| "Speed 2x turns the same stretch into a GIF half as long" | Tips | G04 | OK |
| "steps down up to two more times" | FAQ, blog | code `++ce > 2` | OK |

## SEO (`evidence/html/`)

- **Title:** "Convert Video to GIF Online - Short Clips | FreeDailyPro". Meta description is good; canonical is self.
- **hreflang:** 10 locales + x-default. H1 "Video to GIF".
- **JSON-LD:**
  - SoftwareApplication (offers 4.99 USD), VideoObject, FAQPage, BreadcrumbList.
  - VideoObject name "How to Convert Video to GIF Online" ≠ YouTube title "How to Use Video to GIF – Free Step-by-Step Walkthrough"; uploadDate 2026-09-23.
- **Pair pages** /tool/video-to-gif/mp4-to-gif and /mov-to-gif (200, self-canonical, in the sitemap): titles "MP4 to GIF Converter - **Free**, No Upload" and "MOV to GIF Converter - **Free**, No Upload". Their metas say "Convert MP4 to GIF free…". This conflicts with the "trial uses" wording policy.
- **Locales** (es, pt, fr, de, ja, hi, zh, ko, id: all 200; /ar 404):
  - H1 and site chrome are translated.
  - `<title>`, meta and the tool body (drop zone, controls, copy) stay in English.
  - No EU consent banner seen in de-DE / fr-FR geo contexts. Prices are USD everywhere.
- **Sitemap:** /tool/video-to-gif, both pair pages and /blog/video-to-gif are listed. robots is not noindex. **GSC data is not available.**
- **Alt text:** the YouTube thumbnail `<img alt="">` (decorative, OK). The result image has alt "Result preview".

## Blog (/blog/video-to-gif, "Turn a 6-Second Screen Demo Into a Lean Looping GIF", Oct 17, 2026)

- **Accurate:** step order, control ranges, the 20 s warning, palette method, Play once, Stop, the "earlier result is cleared" note.
- **Inaccurate:** the "tells you how many seconds of the clip would [fit]" hint.
- **Inconsistent:** recommends Trim Video first (the tool page says not to).
- A second linked post, "Turn Short Video Clips Into GIF Loops for Social Posts", was not opened (unverified).

## Competitor reference (ezgif.com/video-to-gif, fetched 2026-11-19)

- Reads MP4, WebM, AVI, MOV, MKV, FLV, WMV, MPEG, M4V, OGV, 3GP, TS. Max 200 MB.
- Offers a URL input, "Use current video position" for start/end, a loop count, transparent video → transparent GIF, and chained crop/resize/optimise tools after conversion.
- FreeDailyPro wins on privacy (in-browser), speed control, Play once, and the size cap.
- It lacks:
  - crop and a text/caption overlay (live controls list verified: none)
  - "use current position" (none in the control list)
  - a hand-off to its own GIF tools
