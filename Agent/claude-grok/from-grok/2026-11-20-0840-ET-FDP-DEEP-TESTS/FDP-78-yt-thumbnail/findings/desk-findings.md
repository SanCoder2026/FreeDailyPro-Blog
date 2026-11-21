Sent: 2026-11-21 17:50 ET

# Desk findings (FDP-78)

- Title "YouTube Thumbnail Downloader - Full-Size HD | FreeDailyPro"; meta "Download a YouTube thumbnail in full size: paste the video link and save the image…"; canonical self; hreflang 10 + x-default. Strip "Trial: 10 uses/day", Quick Buy $1 / $4.99.
- 7 FAQs, accurate except: "counts as one download" (ZIP is free after the first charge on a page load) and "Save image… gives the same file" (download is badged).
- Code (`YtThumbnail-BluoGDJ4.js`): single Download calls `logUsageNow()` then the ToolPage downloader; ZIP relies on the downloader's gate. The charge is remembered per page load, so later downloads are free (P1).
- Preview `<img>` is the img.youtube.com URL itself (pretty line 234), so save-as gives the clean original.
- Blogs: /blog/yt-thumbnail describes "five cards… Not available, button disabled" (old UI, no ZIP). /blog/yt-thumbnail-downloader-creators is current and uses "trial usages".
