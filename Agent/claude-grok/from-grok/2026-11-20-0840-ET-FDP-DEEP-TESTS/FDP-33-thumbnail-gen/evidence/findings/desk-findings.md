Sent: 2026-11-21 01:26 ET

# FDP-33 Video Thumbnail Generator: desk findings (2026-11-21 00:57–01:14 EST)

## Page and SEO
- 200, canonical self, in the sitemap with `/blog/thumbnail-gen`. Title "Generate a Video Thumbnail Online - Any Frame | FreeDailyPro"; H1 "Video Thumbnail Generator".
- **Meta description is 68 chars and generic** ("Generate video thumbnails and previews. Fast, right in your browser.") — no YouTube/Shorts sizes, title text, Suggest frames, JPG/PNG (P2).
- JSON-LD: SoftwareApplication (Offer 4.99), VideoObject, Organization, FAQPage (6), BreadcrumbList. The video thumbnail img (i.ytimg.com) has no alt (P3).
- Locales: es, pt, fr, de, ja, hi, zh, ko, id → 200, `/ar` 404. The server HTML H1 is English; in the browser the H1 and buttons translate ("Generador de Miniaturas de Video", "Compra rápida"), but the title, meta description and section headings ("About…", "How to use it", "Common questions") stay English (see devices-locales-findings.md).
- C42 name collision (DUPLICATES.md): `yt-thumbnail` (fetches an existing YouTube cover) vs `thumbnail-gen` (makes one from your video). The page's "When not to use it" already points to the YouTube thumbnail tool — good. Keep both; consider clearer names ("Video Frame → Thumbnail" vs "YouTube Thumbnail Downloader").

## Copy vs behaviour
- **Outdated size list (P2):** FAQ "Sizes are the video's own size, 1280 x 720, 1080 x 1920 or 1080 x 1080", Details "Choose a Size: Original size, YouTube 1280 x 720, Shorts / Reels 1080 x 1920 or Square 1080 x 1080" and Limitations "There are four output sizes". Live has six, including "YouTube 4K 3840 x 2160 (recommended)" and "YouTube Shorts 4K 2160 x 3840 (recommended)". The blog lists all six.
- Nothing on the page says a single Download costs a trial use while the ZIP doesn't (the per-image note says "Download uses 1 trial use").
- Privacy copy matches the network evidence (no upload; CDN engine only for unplayable videos).
- "A file that is not a video is rejected with a message" (blog) — true for .txt; a non-video with a video extension gets the HEVC message.

## Blog `/blog/thumbnail-gen` ("Pick a Sharp Video Frame and Add a Title for a Thumbnail", Oct 17, 2026)
- Accurate and specific (six sizes, Fill/Fit maths checked: 32 % / 56 % width kept, 1080×608 fit; Suggest timings; file naming). Issues: "Keep the title toward the left" — the title is always centred with no position control (P3); says nothing about the badge or trial uses.

## Completeness vs competitors (desk; e.g. Canva/Adobe Express thumbnail makers, Kapwing, online "video to thumbnail" tools — general knowledge, not re-verified live)
- Strong for a browser tool: frame-exact capture, presets, title, batch ZIP, Suggest frames, HEVC fallback, no upload.
- Missing vs design-oriented competitors: text position/alignment, second text line/subtitle, text background box, image/logo overlay, face/subject-aware crop for vertical, brightness/contrast/saturation, templates, "export under 2 MB" size target (pairs with Compress Image), sprite sheet / contact sheet of frames. Text position + a size target are the cheapest high-value adds for a Premium Application.

## Code notes (`evidence/js/`)
- `ThumbnailGen-BeEuZmFi.pretty.js`: sizes list `te` (incl. yt4k/short4k "(recommended)"); `K()` draws Fill/Fit and the title; `V()` names files; `me` capture (ffmpeg fallback when unplayable); `ue` Suggest (10 samples, Laplacian sharpness, skip mean < 20 or > 240); `pe` = Download all as ZIP → `be(...)` (generic download helper); per-image Download uses the gated download component `xe` (label "Download uses 1 trial use"). The ZIP path's charging behaviour should be checked in the shared helper (live: blocked at 0, not charged with uses left).
- Step buttons use a fixed 1/30 s.
- Header copy "The first use downloads a processing engine, which your browser then keeps" — live, V1–V3 (H.264/WebM) made no engine request; the engine loads only for an unplayable video (P3, the Privacy section has it right).
- "Open from Google Drive" (under the drop zone) was not clicked; it presumably needs a Google sign-in (unverified, untested).
