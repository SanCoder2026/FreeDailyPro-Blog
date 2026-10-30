Sent: 2026-10-30 13:26 ET

# B-0215 Format Converter (video): more input formats, codec choice, real file sizes, and an H1 that says "video"
Priority: P2 · Estimated effort: M · Report: #129 · Source: Playwright headless 0 trial uses 1280/390 + curl server HTML + Google top-5 (WebSearch) 2026-10-30 ~13:22–13:27 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone with a MOV, MKV or AVI should get an MP4 that plays everywhere, and see exactly what changed.
## Why (repro: v.mp4 45,682 B H.264/AAC, output MP4, 1280 px)
- Output: MP4 (widely compatible), MP4 for web, WebM, MOV.
- Convert → **"MP4 0.0 MB → MP4 0.0 MB (+0%)"**, copied without re-encoding ✓. Then the Day Pass prompt (owner decision, fine).
- **Sizes under 0.1 MB show "0.0 MB"**, which is meaningless.
- MP4 → MP4 is allowed and does nothing visible; say "Already MP4; use MP4 for web for fast start" instead.
- Unnamed controls: 9 (B-0155). No overflow.
- Top results (13:26 ET):
  - MP4Web: MOV/MKV/AVI/WMV/FLV/3GP/TS/ProRes in; WebCodecs with an FFmpeg fallback; resolution and quality presets; MP3 extract.
  - Rotato: codec choice H.264/H.265/VP8/VP9, audio AAC/Opus/MP3, resample.
  - Adobe: trim/mute.
  - FreeConvert: bitrate and resolution.
  - Media.io: 1000+ formats.
## Who uses this
People whose phone, editor or website rejects their video format.
## Outcomes (ranked)
1. Show the inputs it accepts (MOV, MKV, AVI, WebM…) and confirm each converts. Needs an admin check with MOV/MKV files.
2. Show sizes in KB under 1 MB, and explain "+0%" (stream copy).
3. Optional resolution (1080p/720p) and quality; an advanced codec choice (H.264/H.265/VP9).
4. Hand off to Extract Audio for MP3.
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, FAQPage, BreadcrumbList, VideoObject), full OG/Twitter set. The site-wide items (og-default.png, template/footer H2s, the boilerplate meta "Free and fast, right in your browser.", empty video alt, unrelated nav category links) are covered by **B-0209**. English on locale pages → **B-0123**.
  - Title "Convert Video Format Online (MP4, MOV) - Free | FreeDailyPro" (60, at the limit).
  - **Meta is 99 chars.**
  - **H1 "Format Converter"** has no "video". /es is English (B-0123).
- **Best result:** H1 "Free Online MP4 Converter" / "Video converter"; a table of input formats; FAQ "How do I convert a video to MP4?", "Is there a size limit?", "Watermark?".
- **Suggested:**
  - Title: `Video Converter – MOV, MKV, WebM to MP4 Online | FreeDailyPro` (59) — list only inputs that are confirmed
  - Meta: `Convert MOV, WebM and other videos to MP4 that plays on any phone, TV or website, or to WebM and MOV. No re-encoding when it can be avoided, so quality stays.` (156)
  - H1: `Video Converter – Convert Video to MP4, WebM or MOV`
  - FAQ:
    - "How do I convert MOV to MP4?" → "Load the MOV, choose MP4 and click Convert."
    - "Will it lose quality?" → "Not when the video can be copied as is; otherwise it's re-encoded at high quality."
    - "Which MP4 should I pick for a website?" → "MP4 for web (fast start)."
    - "Is my video uploaded?" → "No."
## Constraints
Processing stays in the browser.
## Test cases
1. A 45 KB file → "45 KB → 45 KB".
2. Admin: MOV and MKV inputs → MP4 that plays (check with ffprobe).
3. H1 contains "Video".
