Sent: 2026-11-20 08:40 ET

# scripts/

- **Setup:** Node with `playwright` (tested with 1.65.1) and `axe-core`, plus ffmpeg/ffprobe. Playwright WebKit on our box crashes on `<video>` blobs (`cv-browsers.js` control), so verify Safari on a real device.

| Script | What it does | Costs a trial use? |
|---|---|---|
| `cv-cases.json` | C01–C20 | n/a |
| `cv-battery.js [IDs]` | Runs the cases in one context; saves `out-<ID>.mp4` from the preview | No (Compress is free; no Download) |
| `cv-gate-kbd.js` | Count, modes, dialogs (stops at the email prompt), keyboard, axe, phones | No at 0; **yes** if uses are left (it clicks Download) |
| `cv-keep.js` | Keep original vs larger MP4 anyway | Keep original: no. Larger: yes if uses are left |
| `cv-browsers.js` | Firefox Compress; WebKit control | No |
| `cv-reset.js` | After the 7:00 PM ET reset: Download cost, second download, name/size, Drive (stops at Google sign-in) | **Yes** |
| `run-matrix.js config.json` | Devices, locales, geo, axe | No |
| `RERUN-AFTER-RESET.md` | Copy of the running list (row 17 is this tool) | n/a |

## Test files (ffmpeg 7)
```
ffmpeg -f lavfi -i "testsrc2=s=1920x1080:r=30:d=10" -f lavfi -i "sine=f=440:d=10" -vf "noise=alls=25:allf=t" -c:v libx264 -preset veryfast -b:v 10M -maxrate 10M -bufsize 20M -pix_fmt yuv420p -c:a aac -b:a 128k -shortest hd1080.mp4
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=10" -f lavfi -i "sine=f=330:d=10" -vf "noise=alls=20:allf=t" -c:v libx264 -preset veryfast -b:v 6M -pix_fmt yuv420p -c:a aac -b:a 128k -shortest p.mov && ffmpeg -display_rotation 90 -i p.mov -c copy phone.mov
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=8" -f lavfi -i "sine=f=330:d=8" -vf "noise=alls=20:allf=t" -c:v libx265 -preset ultrafast -b:v 4M -tag:v hvc1 -pix_fmt yuv420p -c:a aac -shortest hevc.mov
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=10" -c:v libx264 -preset slow -crf 35 -pix_fmt yuv420p efficient.mp4
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=8" -f lavfi -i "sine=f=500:d=8" -vf "noise=alls=20:allf=t" -c:v libvpx-vp9 -b:v 3M -deadline realtime -cpu-used 8 -c:a libopus -shortest clip.webm
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=8" -vf "noise=alls=20:allf=t" -c:v libx264 -preset veryfast -b:v 5M -pix_fmt yuv420p noaudio.mp4
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=8" -f lavfi -i "sine=d=8" -vf "noise=alls=20:allf=t" -c:v libx264 -preset veryfast -b:v 5M -pix_fmt yuv420p -c:a aac -shortest clip.mkv
ffmpeg -f lavfi -i "testsrc2=s=1280x720:r=30:d=60" -f lavfi -i "sine=d=60" -vf "noise=alls=30:allf=t" -c:v libx264 -preset ultrafast -b:v 6M -pix_fmt yuv420p -c:a aac -shortest long60.mp4
head -c 1500000 hd1080.mp4 > truncated.mp4 ; printf 'not a video at all\n' > notvideo.mp4
ffmpeg -f lavfi -i "testsrc2=s=1920x1080:r=30:d=45" -vf "noise=alls=40:allf=t" -c:v libx264 -preset ultrafast -b:v 12M -pix_fmt yuv420p big60.mp4
```
