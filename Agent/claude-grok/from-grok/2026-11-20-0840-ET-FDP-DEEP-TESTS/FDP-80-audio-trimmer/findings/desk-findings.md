Sent: 2026-11-21 18:23 ET

# Desk findings (FDP-80)

- Title "Audio Trimmer: Cut MP3 or WAV to Exact Times | FreeDailyPro"; canonical self; hreflang 10 + x-default. Strip + Quick Buy $1 / $4.99. 11 FAQs.
- Gate: FileDrop `gateAtDownload`; only the Download button (`logUsageNow("download")`) charges, once per page load. Trim and the result player run at 0.
- Result player (ToolPage `Al`): `<audio controls src=blob:…>`, no `controlsList`, so native download is offered.
- `TimeRangeFields`: Enter/blur re-parses both boxes; the boxes show times rounded to 0.1 s (`timeFormat.f`), so a typed 3.25 becomes 3.3 at the next blur (Trim click). Parser `we()` takes only the first two `:` parts.
- `ffmpegEngine`: guest limit 50 MB, paid 200 MB; drop zone `maxSize: 500` and "over 500 MB" text.
- Blog /blog/audio-trimmer is older than Remove selection; /blog/make-srt-vtt-subtitles-from-audio is a related guide.
