Sent: 2026-11-20 08:40 ET

# Priorities: FDP-18 Video to GIF

- **Written:** 2026-11-19 16:18 EST (box `date`, ET). Repro steps are in REPRODUCE.md (R-numbers).
- **P0:** none found.

## P1
1. **AVI / WMV / FLV are listed under "Reads" but refused as "damaged" (R1).**
   - Let files that fail the browser `<video>` pre-check go to ffmpeg, or probe them with ffmpeg first. Otherwise trim the list.
   - Reword the error so a valid-but-unplayable file isn't called damaged.
   - Check MKV/WebM on real Safari.
2. **Largest file: the promised "N seconds would fit" hint never shows, and an unreachable cap ends over the limit at 200 px (R2).**
   - Show `le` (already built) with a one-click "Use N s".
   - Don't drop below 240 px / 8 fps silently. Consider shortening before cutting fps (the blog's own advice).
   - Fix FAQ, Details and blog if the behaviour changes.
3. **Copy and video describe a different tool (R3).**
   - "over 200 MB" in the drop zone vs the 50 MB trial cap (and MiB vs MB).
   - Contradictory trim advice: "Set Start and Length here rather than trimming first" vs three "trim first" lines.
   - The YouTube video shows the old UI: no settings, Pro badge, Share button, no GIF output, ≈40 s outro, "200+ Free" tools, personal bookmarks and a file-picker listing.

## P2
4. **Accessibility:** Width / Frames per second / Speed / Largest file selects have no accessible name (axe critical ×4); the "GIF size" result isn't announced; focus drops to body; the progress bar is unnamed.
5. **Next step after the result:** Universal File Converter (documents) and Video Thumbnail Generator. Offer GIF Resizer & Compressor and GIF Speed, Reverse & Crop (a "Continue with" hand-off), which also lifts Premium discovery.
6. **Capped runs drop to 6 fps** (8 MB cap → 550 px / 6 fps, 6.76 MB) and take about 2× longer with only "Estimating…" status.
7. **Completeness vs ezgif:** "use current video position" for Start, crop, text caption, loop count.
8. **The non-video file error** says "damaged or codec… re-export as MP4".
9. **Settings survive New/Reset** with no hint (could be a feature; say so).
10. **Pair pages** /tool/video-to-gif/mp4-to-gif and /mov-to-gif have "Free" in title and meta (use "trial uses").
11. **Locales:** English title, meta and tool body; /ar 404. VideoObject name ≠ YouTube title.
12. **"How to use it"** is one thin line ("Upload your video and download…"). Reuse the Details steps.
13. **Layout:** 9 px header overflow at 320 px (site-wide). On phones Create GIF needs one scroll after a file is chosen.
14. **WebKit/iOS processing is unverified** (box harness limit). Check on a real device.
