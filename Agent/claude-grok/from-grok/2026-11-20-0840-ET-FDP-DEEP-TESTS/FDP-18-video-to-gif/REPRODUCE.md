Sent: 2026-11-20 08:40 ET

# Reproduce: FDP-18 Video to GIF

- **Page:** open https://www.freedailypro.com/tool/video-to-gif as a guest. Create GIF costs no trial use.
- **Test files:** make them with `scripts/README.md`.
- **Measuring outputs:** take the "Result preview" blob (`[...document.querySelectorAll('main img')].filter(i=>i.src.startsWith('blob:')).pop().src`) and run ffprobe, or use `scripts/vg-battery.js`.

- **R1 (formats):**
  1. Scroll to "Formats and which tool to use", which shows "Reads MP4, MOV, MKV, WebM, AVI, WMV, FLV".
  2. Drop `clip.avi` (or `clip.wmv`, `clip.flv`).
  3. The page shows `"clip.avi" couldn't be read as a video; it may be damaged or use a codec this browser can't open. Try re-exporting it as MP4.` Create GIF is disabled.
  4. The same happens in Firefox. `ffprobe clip.avi` shows a valid file.
- **R2 (size cap):**
  1. Drop `long60.mp4`. Set Start 0, Length 30, Width 640 px, 15 fps, Largest file 2 MB. Press Create GIF.
  2. After about 17 s, the toast reads "GIF is 2.2 MB, still over 2 MB at 200 px and 5 fps. Use a shorter clip to make it smaller."
  3. "GIF size: 2.15 MB". No "a clip of about N s would fit" line appears anywhere.
  4. Compare Common questions → "What does the Largest file setting actually do?" ("If nothing fits, it reports how many seconds would") and Details → Limitations.
  5. Also: `hd1080.mp4`, Length 10, 640 px, 15 fps, Largest 8 MB → "reduced to 550 px, 6 fps to fit 8 MB", 6.76 MB, about 42 s.
- **R3 (copy and video):**
  - The drop zone reads "Large files (over 200 MB) may take longer…".
  - Drop `big60.mp4` (71.7 MB) and the page reads "trial use supports up to 50.0 MB".
  - Details → Tips: "Set Start and Length here rather than trimming first". Compare the warning shown for `long60.mp4`: "Trim it down first with the Trim Video tool".
  - In the video (https://www.youtube.com/watch?v=P9s4XBNSB10), watch 0:15–0:51: no settings, a "Pro" badge, Download/Share/New, and no GIF shown.
- **R4 (accessibility):** drop any video and run axe on `main`: `select-name` critical ×4. After Create GIF, `document.activeElement` is BODY.
