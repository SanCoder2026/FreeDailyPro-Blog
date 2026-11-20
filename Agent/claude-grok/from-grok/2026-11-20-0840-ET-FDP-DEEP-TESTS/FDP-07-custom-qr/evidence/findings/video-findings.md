Sent: 2026-11-20 08:40 ET

# FDP-07 custom-qr: video findings

- **Written:** 2026-11-19 12:30:07 EST (box `date`, ET).
- **Video:** https://www.youtube.com/watch?v=-YoQA8K6x8I "How to Design a Branded QR Code with Custom QR Code | FreeDailyPro". 62 s, uploaded 2026-10-16, 9 views (yt-dlp metadata, 2026-11-19). Embedded on the page and in the sitemap video block.
- Evidence: `video/v.info.json`, `video/frames/` (21 frames, one every 3 s), `video/contact.png`. No mp4 in the zip.

## What it shows
- An older UI: a single "Content" box, no type tabs, no frame, no PDF, no bulk; Download PNG / Download SVG only.
- The strip in the video reads "Trial: 10 uses/day · 10 remaining today" and "Ads-free unlimited usage, $1 day pass / $4.99 monthly pass".
  - Live today: "Trial: 2 uses/day", $3 day pass / $9.99 monthly (Premium Application).
- Description: "10 trial usages every day." This is wrong for the current Premium tier (2/day).
- The thumbnail says "200+ professional tools"; the blog says "300+".
- QR codes in 13 of 21 frames decode with zxing-cpp (https://example.com/spring-fair and https://freedailypro.com). One partial frame ("https://examp") was mid-typing.

## Verdict
- Check 10 (video exists): PASS, low reach.
- Check 12 (shows current capabilities): **FAIL**. It shows a stale UI, a stale price and a stale trial allowance, and misses the 7 types, frame, PDF and bulk, which are the tool's main differences from qr-generator.
