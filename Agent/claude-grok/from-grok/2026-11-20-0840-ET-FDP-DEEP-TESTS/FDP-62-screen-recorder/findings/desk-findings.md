Sent: 2026-11-21 13:20 ET

# Desk findings (FDP-62)

- **SEO:** title "Screen Recorder Online - Record and Download a Video" (52, no brand). Meta 83. Canonical self. hreflang 10 + x-default. JSON-LD SoftwareApplication (9.99 USD), VideoObject (2026-09-23), FAQPage (7), BreadcrumbList. In sitemap. og-default.png.
- **Copy:** 7 FAQs, how-to, limits and privacy match the code: mime order mp4 avc1/aac → webm vp9/vp8, 30-minute reminder, 200 MB warning, 20 px region minimum, camera asked on toggle, Pause/Resume same file.
- **Code:**
  - Download goes through the shared download button (gated, once per load).
  - The finished `<video controls>` has no controlsList.
  - Region and camera use a canvas redraw driven by a Worker at about 30 fps, capped at 3840×2160.
  - `enumerateDevices()` runs on load (mic picker).
- **Blog:** accurate help-center walkthrough; mentions tab-only sharing to avoid leaking bookmarks — which the video itself doesn't follow.
- **C17:** keep. GSC data is not available.
