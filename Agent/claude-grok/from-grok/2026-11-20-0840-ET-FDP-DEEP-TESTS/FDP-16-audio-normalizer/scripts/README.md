Sent: 2026-11-20 08:40 ET

# scripts/

- **Setup:** Node with `playwright` (tested with 1.65.1) and `axe-core`, plus ffmpeg on PATH. For WebKit on Linux, set `GIO_EXTRA_MODULES`. Playwright WebKit on our box crashes on any `<audio>` blob (see `an-webkit-control.js`), so verify Safari on a real device.

| Script | What it does | Costs a trial use? |
|---|---|---|
| `an-cases.json` | N01–N26: file, target, limiter, expected | n/a |
| `an-battery.js [IDs]` | Runs the cases in one context; saves preview blobs `out-<ID>.bin` | No (Normalize is free; no Download) |
| `an-probe.js` | First look: count, UI, Normalize, blob, Download click | No at 0 (cap dialog); **yes** if uses are left |
| `an-gate-kbd.js` | Drive / cloud / Share / Download → Day Pass (stops at email) / Continue with; keyboard, live regions, axe, phones | Same as above |
| `an-browsers.js` | Firefox + WebKit processing; keyboard path to the drop zone | No |
| `an-webkit-retry.js`, `an-webkit-control.js` | WebKit crash check (site vs harness) | No |
| `an-se-overflow.js` | 320 px overflow culprit | No |
| `an-reset.js` | After the 7:00 PM ET reset: Download cost, second download, file name/size, Drive (stops at Google sign-in) | **Yes** (1 or more) |
| `run-matrix.js config.json` | Devices, locales, geo, axe | No |
| `RERUN-AFTER-RESET.md` | Copy of the running list (row 16 is this tool) | n/a |

## Test files (ffmpeg)
```
AM="anoisesrc=color=pink:d=20:r=44100:a=1,volume=0.5*(0.6+0.4*sin(2*PI*1.7*t)):eval=frame"
ffmpeg -f lavfi -i "$AM" -af volume=-6dB -ac 2 -c:a pcm_s16le quiet.wav           # ≈ -30.3 LUFS
ffmpeg -f lavfi -i "$AM" -af volume=-22dB -ac 2 -c:a pcm_s16le vquiet.wav         # ≈ -46.4 LUFS
ffmpeg -f lavfi -i "$AM" -af "volume=16dB,alimiter=limit=0.95" -ac 2 -c:a pcm_s16le loud.wav
ffmpeg -f lavfi -i "$AM" -f lavfi -i "aevalsrc='if(between(t,10,10.002),0.99,0)':d=20:s=44100" -filter_complex "[0]volume=-8dB[a];[a][1]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo" -c:a pcm_s16le spike.wav
ffmpeg -i quiet.wav -c:a libmp3lame -b:a 128k quiet.mp3 ; ffmpeg -i quiet.wav -c:a aac -b:a 96k quiet.m4a
ffmpeg -i quiet.wav -c:a libvorbis -b:a 112k quiet.ogg ; ffmpeg -i quiet.wav -c:a libopus -b:a 64k quiet.opus
ffmpeg -i quiet.wav -c:a libopus -b:a 128k opus128.opus ; ffmpeg -i quiet.wav -ac 1 -ar 48000 -c:a libopus -b:a 16k voicenote-opus16k.ogg
ffmpeg -i quiet.wav -c:a flac -sample_fmt s32 quiet24.flac ; ffmpeg -i quiet.wav -c:a pcm_s24le quiet24.wav ; ffmpeg -i quiet.wav -ac 1 mono.wav
ffmpeg -f lavfi -i anullsrc=r=44100:cl=stereo -t 10 -c:a pcm_s16le silence.wav ; ffmpeg -i quiet.wav -t 0.3 short03.wav
printf 'this is not audio\n' > corrupt.mp3
ffmpeg -f lavfi -i "anoisesrc=color=pink:d=360:r=44100:a=0.05" -ac 2 -c:a pcm_s16le big60.wav
ffmpeg -f lavfi -i testsrc=d=10:s=320x240:r=15 -i quiet.wav -t 10 -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest clip.mp4
```

## Measuring an output
```
ffmpeg -hide_banner -nostats -i out-N09.bin -af loudnorm=print_format=json,volumedetect -f null - 2>&1 | grep -E '"input_(i|tp)"|max_volume'
ffprobe -v error -show_entries stream=codec_name,sample_fmt,sample_rate,channels,bit_rate,bits_per_raw_sample -of compact out-N16.bin
```
`input_tp` is true peak (dBTP) and must stay at or below the target's ceiling. `max_volume` is the sample peak.
