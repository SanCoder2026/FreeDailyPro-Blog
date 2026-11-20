Sent: 2026-11-20 08:40 ET

# scripts/

- **Setup:** Node with `playwright` (tested with 1.65.1) and `axe-core`; Python 3 with Pillow (and `pillow-heif` for the HEIC input).
- **Test images:** run `python ../evidence/testfiles/make.py` in the testfiles folder. It builds photo.jpg (EXIF orientation 6 + GPS + 300 DPI), plain.jpg, alpha.png, img.webp, img.bmp, tiny.png, anim.gif, img.tiff, vector.svg, notimage.jpg and huge108mp.jpg. Then make the HEIC and AVIF:
  ```
  python -c "from PIL import Image; from pillow_heif import register_heif_opener as r; r(); Image.open('plain.jpg').resize((2000,1500)).save('photo.heic',quality=80); Image.open('img.webp').save('img.avif')"
  ```

| Script | What it does | Costs a trial use? |
|---|---|---|
| `rc-cases.json` | R01–R24, K01–K05 | n/a |
| `rc-battery.js [IDs]` | One context per case; records the result blob via a canvas hook; saves `out-<ID>.*` | No (Resize/Crop are free; no Download) |
| `rc-inspect.py <dir>` | Pillow inspection → `inspect.json` | n/a |
| `rc-gate-kbd.js` | Count, keyboard, 1:1, keyboard crop, axe, Download → Day Pass (stops at email), Drive, cloud, phones | No at 0; **yes** if uses are left (it clicks Download) |
| `rc-browsers.js` | Firefox + WebKit resize, HEIC, 1:1 crop | No |
| `rc-probe.js`, `rc-copy.js` | Page text, controls, expanded copy, JSON-LD | No |
| `rc-reset.js` | After the 7:00 PM ET reset: Download ×2 (count, name, bytes vs result), Drive (stops at Google sign-in) | **Yes** |
| `run-matrix.js config.json` | Devices, locales, geo, axe | No |
| `RERUN-AFTER-RESET.md` | Copy of the running list (row 19 is this tool) | n/a |
