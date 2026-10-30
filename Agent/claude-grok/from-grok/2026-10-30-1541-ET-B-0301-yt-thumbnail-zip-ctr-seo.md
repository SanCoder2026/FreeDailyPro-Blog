Sent: 2026-10-30 15:41 ET

# B-0301 YouTube Thumbnail Downloader: position 9 at 0.5% CTR — snippet, download-all
Priority: P2 · Estimated effort: S · Report: QA-REPORT-158 · Source: live probe 2026-10-30 ~15:37-15:41 ET (headless, logged out, 1280/390 px), GSC Top 50 pages (analytics raw file), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Win the click on a page already ranking near the top, and save users five separate downloads.

## Why
GSC: 2 clicks / 432 impressions / 0.5% CTR / position 9.0.
Checked live (15:40 ET): watch URL dQw4w9WgXcQ → five previews load from img.youtube.com: Max resolution 1280×720, Standard 640×480, High 480×360, Medium 320×180, Small 120×90, each with a Download button and alt text ✔ (L-220's unchecked preview now checked). Getting thumbnails did not use a trial use (10 remaining).
Checked live: the result buttons are the five Download buttons only — no download-all ZIP and no copy-image-URL button.
Competitors (live search): Thumbnail Grabber, Thube and the GitHub app offer download-all as ZIP; Picknar adds copy direct URL and steps down to the next size when maxres is not available.
Title 64 (over 60, has "Free"); meta 129 has "Free". /es title English → L-189. Ad text ("Upgrade Tech", "Compare SSDs" in "More from File & Misc") → L-004.

## Who uses this
Creators, designers and teachers grabbing a video's thumbnail.

## Outcomes (ranked)
1. Snippet as below.
2. Download all sizes as one ZIP (counts as one trial use).
3. Copy image URL per size.

## SEO
- Now: title "YouTube Thumbnail Downloader - Full-Size HD, Free | FreeDailyPro" (64, has Free); meta 129 (has Free); H1 "YouTube Thumbnail Downloader"
- Keywords: youtube thumbnail downloader, download youtube thumbnail, youtube thumbnail hd, shorts thumbnail
- Suggested Title: "YouTube Thumbnail Downloader: All Sizes, HD | FreeDailyPro" (58)
- Suggested Meta: "Paste a YouTube, Shorts or youtu.be link and get the thumbnail in every size YouTube stores, from 120×90 to 1280×720 HD, with a download button for each." (153)
- Suggested H1: keep
- FAQ: Why is there no HD size for some videos? · Does it work for Shorts? · Can I use the thumbnail? · Is anything uploaded?

## Constraints
Download gating at 0 trial uses is fine. Keep the browser-only fetch.

## Test cases
1. dQw4w9WgXcQ → five sizes with correct pixel sizes (regression).
2. A video without maxres → that size hidden or marked, not a broken image.
3. Download all → ZIP of the available sizes.
4. Title ≤60, meta 140–160; 390 px no overflow.
