Sent: 2026-10-30 13:26 ET

Supersedes 2026-10-30-1326-ET-B-0213-thumbnail-gen-frames-text-seo.md (removes the stray length note from the suggested title; nothing else changed).

# B-0213-v2 Thumbnail Generator: suggested frames you can see, text styling, and an H1 people search
Priority: P2 · Estimated effort: S · Report: #129 · Source: Playwright headless 0 trial uses 1280/390 + curl server HTML + Google top-5 (WebSearch) 2026-10-30 ~13:22–13:27 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Creators should be able to get a click-worthy YouTube or Shorts thumbnail from their own video in one place, without opening a design app.
## Why (repro: v.mp4 320×240 3 s, 1280 px, 0 trial uses)
- It has frame stepping (±1 s / ±1 frame), Time, JPG option, size presets (Original, YouTube 4K/HD, Shorts 4K, Reels 1080×1920, Square), an optional Title, Capture, Suggest frames and Reset.
- Capture → `v_00m00.00s.png` preview, the badge notice, then "0 remaining today, Get a Day Pass to download". That's expected under the owner decision; the badge is disclosed (by design).
- Injected ad text "Get Photo Storage" sits inside the About text → L-004.
- Unnamed controls → B-0155. No 390 px overflow.
- Top results (13:24 ET):
  - stack0: text overlay with position/size/colour/shadow, 16:9 / 9:16 / 1:1.
  - openclip: a batch of 10 evenly spaced frames to pick from.
  - Vidocu: AI picks frames, 6 style templates.
  - Clipy: JPG/PNG/WebP, sub-second timestamp.
  - ThumbGen: batch ZIP.
## Who uses this
YouTubers, Shorts/Reels creators, course makers.
## Outcomes (ranked)
1. "Suggest frames" shows a strip of 6–10 candidate frames to click, like the batch mode in openclip/Vidocu. Needs a browser check of what it shows today.
2. Title text styling: font size, colour, outline/shadow, position, plus a 1280×720 safe-area guide.
3. WebP output.
4. Upscaled presets (a 320×240 source → 3840×2160) should warn "the source is smaller than this size".
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, FAQPage, BreadcrumbList, VideoObject), full OG/Twitter set. The site-wide items (og-default.png, template/footer H2s, the boilerplate meta "Free and fast, right in your browser.", empty video alt, unrelated nav category links) are covered by **B-0209**. English on locale pages → **B-0123**.
  - Title "Generate a Video Thumbnail Online - Free, Any Frame" (51, no brand).
  - **Meta is 77 chars**, all boilerplate.
  - **H1 "Thumbnail Generator"** doesn't say "video" or "YouTube".
  - No GSC rows in the approved sources.
- **Best result:** H1 "Video Thumbnail Generator" / "YouTube Thumbnail Generator from Video". FAQ: "Will the thumbnail be lower resolution?", "Can I grab an exact moment?", "Which format is best?".
- **Suggested:**
  - Title: `Video Thumbnail Generator – Any Frame, YouTube Sizes` (52)
  - Meta: `Pick any frame from your video, frame by frame, and save it as a YouTube, Shorts or square thumbnail with your title on it. Your video stays on your device.` (154)
  - H1: `Video Thumbnail Generator – Make a Thumbnail from Any Frame`
  - FAQ:
    - "How do I make a thumbnail from my video?" → "Load the video, step to the frame, choose a size and click Capture."
    - "What size is a YouTube thumbnail?" → "1280 × 720 (16:9). Shorts use 1080 × 1920."
    - "Is the thumbnail full quality?" → "It's captured at the size you choose. Pick Original to keep the source size."
    - "Is my video uploaded?" → "No."
## Constraints
Keep the existing presets and keep the badge disclosure.
## Test cases
1. Suggest frames → 6 or more clickable candidates.
2. Title with outline at 1280×720 → stays readable at 320 px wide.
3. A 320×240 source with the 4K preset → warning shown.
