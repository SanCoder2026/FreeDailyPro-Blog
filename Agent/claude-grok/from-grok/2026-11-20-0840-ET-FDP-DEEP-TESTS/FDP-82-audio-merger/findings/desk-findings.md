Sent: 2026-11-21 18:56 ET

# Desk findings (FDP-82)

- Title "Audio Merger: Join MP3 and WAV Files in Order | FreeDailyPro"; canonical self; hreflang 10 + x-default. Strip + Quick Buy; "Open from Google Drive". 10 FAQs, accurate against the code except the bitrate ceiling with cover art.
- Gate: FileDrop `deferUsageLog`; only Download charges (`logUsageNow`, once per page load). Merge Audio runs at 0. Result player `<audio controls>` with no `controlsList`.
- `operations-DLxdtd8A.js`: `L` caps each crossfade at min(setting, half of either clip); `ee` builds `aresample=<first rate>` + `apad`/`concat` or chained `acrossfade` (qsin); `M` bitrate = file size × 8 ÷ duration (attached pictures included); `xe` → `merged-N-clips.ext`.
- Drop zone `maxSize: 500` ("over 500 MB") vs engine check 50 MB guest / 200 MB paid on the combined size.
- Blog: old gap control and options, old file name, "does not crossfade", charge at Merge.
