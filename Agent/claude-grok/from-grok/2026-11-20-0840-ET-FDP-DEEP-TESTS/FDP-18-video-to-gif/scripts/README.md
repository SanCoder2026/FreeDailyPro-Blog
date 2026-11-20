Sent: 2026-11-20 08:40 ET

# scripts/

- **Setup:** Node with `playwright` (tested with 1.65.1) and `axe-core`, plus ffmpeg/ffprobe. Playwright WebKit on our box crashes on `<video>` blobs (`vg-browsers.js` control), so verify Safari on a real device.

| Script | What it does | Costs a trial use? |
|---|---|---|
| `vg-cases.json` | G01–G25 | n/a |
| `vg-battery.js [IDs]` | Runs the cases in one context, setting every control; saves `out-<ID>.gif` from the preview | No (Create GIF is free; no Download) |
| `vg-gate-kbd.js` | Count, keyboard, Stop, live regions, axe, Download/Drive/cloud, phones | No at 0; **yes** if uses are left (it clicks Download) |
| `vg-cap.js` | At 0: cap dialog → Day Pass → email prompt (stops); skips itself if uses are left | No |
| `vg-browsers.js` | Firefox Create GIF + format pre-check; WebKit control | No |
| `vg-probe.js`, `vg-copy.js` | Page text, controls, expanded copy, JSON-LD | No |
| `vg-reset.js` | After the 7:00 PM ET reset: Download twice (count, name, bytes vs preview), Drive (stops at Google sign-in) | **Yes** |
| `run-matrix.js config.json` | Devices, locales, geo, axe | No |
| `RERUN-AFTER-RESET.md` | Copy of the running list (row 18 is this tool) | n/a |

## Test files (ffmpeg 7)
FDP-17 files (`hd1080.mp4`, `phone.mov`, `hevc.mov`, `clip.webm`, `clip.mkv`, `noaudio.mp4`, `long60.mp4`, `truncated.mp4`, `notvideo.mp4`, `big60.mp4`) are made with the commands in the FDP-17 package `scripts/README.md`. These are the same commands:
```
ffmpeg -f lavfi -i "testsrc2=s=1920x1080:r=30:d=10" -f lavfi -i "sine=f=440:d=10" -vf "noise=alls=25:allf=t" -c:v libx264 -preset veryfast -b:v 10M -maxrate 10M -bufsize 20M -pix_fmt yuv420p -c:a aac -b:a 128k -shortest hd1080.mp4
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=10" -f lavfi -i "sine=f=330:d=10" -vf "noise=alls=20:allf=t" -c:v libx264 -preset veryfast -b:v 6M -pix_fmt yuv420p -c:a aac -b:a 128k -shortest p.mov && ffmpeg -display_rotation 90 -i p.mov -c copy phone.mov
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=8" -f lavfi -i "sine=f=330:d=8" -vf "noise=alls=20:allf=t" -c:v libx265 -preset ultrafast -b:v 4M -tag:v hvc1 -pix_fmt yuv420p -c:a aac -shortest hevc.mov
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=8" -f lavfi -i "sine=f=500:d=8" -vf "noise=alls=20:allf=t" -c:v libvpx-vp9 -b:v 3M -deadline realtime -cpu-used 8 -c:a libopus -shortest clip.webm
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=8" -vf "noise=alls=20:allf=t" -c:v libx264 -preset veryfast -b:v 5M -pix_fmt yuv420p noaudio.mp4
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=8" -f lavfi -i "sine=d=8" -vf "noise=alls=20:allf=t" -c:v libx264 -preset veryfast -b:v 5M -pix_fmt yuv420p -c:a aac -shortest clip.mkv
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=60" -f lavfi -i "sine=d=60" -vf "noise=alls=30:allf=t" -c:v libx264 -preset ultrafast -b:v 6M -pix_fmt yuv420p -c:a aac -shortest long60.mp4
head -c 1500000 hd1080.mp4 > truncated.mp4 ; printf 'not a video at all\n' > notvideo.mp4
ffmpeg -f lavfi -i "testsrc2=s=1920x1080:r=30:d=45" -vf "noise=alls=40:allf=t" -c:v libx264 -preset ultrafast -b:v 12M -pix_fmt yuv420p big60.mp4
```
New for FDP-18:
```
ffmpeg -f lavfi -i "testsrc2=s=320x240:r=30:d=6" -c:v libx264 -pix_fmt yuv420p small320.mp4
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=60:d=4" -c:v libx264 -pix_fmt yuv420p -b:v 4M hfr60.mp4
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=10" -c:v libx264 -pix_fmt yuv420p flat.mp4
ffmpeg -f lavfi -i "testsrc2=s=640x360:r=25:d=5" -f lavfi -i "sine=d=5" -c:v mpeg4 -q:v 5 -c:a mp3 -shortest clip.avi
ffmpeg -f lavfi -i "testsrc2=s=640x360:r=25:d=5" -c:v wmv2 -b:v 2M clip.wmv
ffmpeg -f lavfi -i "testsrc2=s=640x360:r=25:d=5" -c:v flv1 -b:v 2M clip.flv
```
