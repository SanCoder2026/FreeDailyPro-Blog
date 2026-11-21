Sent: 2026-11-21 02:08 ET

# FDP-35 Video Converter: desk findings (2026-11-21 01:48–02:03 EST)

## Page and SEO
- 200, canonical self, in the sitemap with `/blog/convert-video` and **11 pair pages** (avi/flv/gif/mkv/mov/webm/wmv-to-mp4, mp4-to-avi/mkv/mov/webm), all 200, self canonical.
- Title "Video Converter – MOV, WebM to MP4 Online | FreeDailyPro"; meta 158 chars, specific (PASS). JSON-LD: WebSite, SoftwareApplication (Offer 4.99; description "between MP4, WebM and MOV"), VideoObject, FAQPage (10), BreadcrumbList. og:image generic; thumbnail no alt.
- **All 11 pair titles say "Free"** ("MOV to MP4 Converter - Free, No Upload | FreeDailyPro") (P2 wording).
- Locales: 9 → 200 with translated H1 (client-side), English title/meta/headings; ja desktop 3 px overflow; `/ar` 404.

## Copy vs behaviour (the page contradicts itself)
- **Outputs:** drop zone, "Formats", About and the code offer **six** outputs (MP4, MP4 for web, WebM, MOV, MKV, AVI). But H1 subtitle and JSON-LD say "between MP4, WebM and MOV"; FAQ "converted to the four outputs"; How to use lists four; Limitations "limited to the four formats in the menu"; blog "The Output Format menu has four entries" (P2).
- **Rewrap:** live, MKV and 3GP sources and MKV targets rewrap too (code `V = ["mp4","mp4-web","mov","mkv"]`); How to use says only "For MP4 and MOV targets" (P3).
- **Size limit:** drop zone "Large files (over 5 GB) may take longer or run out of browser memory"; live and code: trial 50 MB, paid 200 MB hard limit (`ffmpegEngine` `R`/`g`); the blog has it right (P2). FAQ/Details never mention the 50 MB trial cap.
- Header "The first use downloads a processing engine" — true here (engine ~25 MB from jsDelivr, every first conversion in a fresh context).
- "Upgrade to Pro for up to 200.0 MB" — other copy says Day Pass / Monthly; "Pro" naming inconsistent (P3).
- Cap dialog's mark claim (converted video has no mark) (P3).
- Accurate: rewrap vs re-encode summary line, CRF 23 veryfast, VP8 1 Mbps 1280 cap, "_converted" suffix, audio-only rejection, "MP4 for web" = MP4.

## Blog `/blog/convert-video` ("Turn a WebM Screen Capture into an MP4 a Portal Will Accept")
- Accurate and specific on rewrap vs re-encode, 50 MB / 200 MB limits, the >25 % note, privacy. Outdated: "The Output Format menu has four entries" (six); no MKV/AVI/GIF (P3).

## Completeness vs competitors (desk; e.g. CloudConvert, FreeConvert, HandBrake web guides — general knowledge, not re-verified live)
- Strong: smart rewrap (seconds, lossless), broad input, GIF→MP4, no upload.
- Gaps: no resolution/quality/frame-rate controls, no H.265/AV1/VP9 output, no batch, no trim during convert, no audio track choice, WebM stuck on VP8 1 Mbps / 1280 px; trial 50 MB is small for phone video (a 1-minute 4K clip is larger).

## Code notes (`evidence/js/`)
- `ConvertVideo-*.pretty.js`: Convert has no usage call; Download via the shared gated button (`gateAtDownload`); `checkFileSize` (50 MB trial / 200 MB paid); preview `Q({blob})`.
- `operations-*.pretty.js`: `Rt` output list (6), `st` rewrap rule, `lt` encode args.
- Per-page-load counting: `index-*.js` `xI`/`Kt` (see FDP-34 evidence).
