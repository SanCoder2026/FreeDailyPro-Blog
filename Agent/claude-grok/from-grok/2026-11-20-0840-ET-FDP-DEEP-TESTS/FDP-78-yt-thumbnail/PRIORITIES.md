Sent: 2026-11-21 17:50 ET

# FDP-78 priorities

**P0:** none found.

**P1**
1. **One trial use per page load, not per download.** Chromium at 0/10: the first Download charged 0→1/10 (1 `usage.log` POST). After that, Standard + Small downloads, 2 ZIPs, a second video's High quality download + ZIP were all free (7 files, 0 POSTs). After a reload, the next Download charged 1→2/10 and the ZIP after it was free (`left.json` X02–X11). The FAQ says the ZIP "counts as one download".
2. **The clean full-size image can be saved at 0 uses (owner rule).** At 10/10, Get Thumbnails still shows the 1280×720 preview and all tiles (X01/X07, no dialog). The preview `<img>` src is the img.youtube.com original, so "Save image as" gives the clean, byte-identical file (65,324 bytes), while the gated Download gives a badged copy (89,022 bytes). Nuance for the owner: it's YouTube's public image, so you may prefer to accept this.

**Owner question**
1. Downloads stamp two "Created with FreeDailyPro.com" badges onto another creator's cover (diff box x 948–1256, y 24–696 on maxres; Small 120×90 is byte-identical/unmarked). The badge is intentional per policy; the question is only whether it belongs on third-party thumbnails that the page's FAQ calls "the same file".

**P2**
1. Re-submitting the same video (same link, or another link form of the same ID) leaves no preview and the ZIP stuck disabled on "Checking sizes…" (Chromium and Firefox, S02/S03). Another video then back recovers (S04).
2. FAQ "Save image… gives the same file" is false: the new-tab fallback is clean, the download is badged; the page never mentions the badge.
3. Blog /blog/yt-thumbnail describes old UI ("five cards… shown as Not available and its button is disabled"); no ZIP, no left-out line.
4. Video lDBgQDbgHmY: old light UI, "10 free uses daily" overlay, no ZIP.
5. Locale pages: title, H1, meta, labels and FAQ English on all 10 hreflang pages.
6. iPhone SE: "Get Thumbnails" runs 9 px off screen (329/320) and the Feedback button covers it; URL box squeezed to 139 px.

**P3**
1. Not parsed (error message): youtube.co.uk, attribution_link, gaming.youtube.com. "hello-world" (11 chars) is treated as an ID → "Video not found".
2. ja desktop overflows 3 px. axe desktop: label-content-name-mismatch (serious, `.right-2`) + region; Pixel 7 clean.
3. C42 duplicates: "YouTube Thumbnail Downloader" vs Thumbnail Generator names; suggest keeping "Downloader" in titles everywhere.
