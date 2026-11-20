Sent: 2026-11-20 08:40 ET

# Reproduce: FDP-19 Resize & Crop

- **Page:** open https://www.freedailypro.com/tool/resize-crop as a guest. Resize Image and Apply Crop cost no trial use.
- **Test images:** make them with `evidence/testfiles/make.py` (Pillow; `pillow-heif` for HEIC).
- **Real output size:** download it with a pass, or use `scripts/rc-battery.js`, which records the in-memory blob, then `scripts/rc-inspect.py`.

- **R1 (size message):**
  1. Drop `plain.jpg` (4000×3000). Untick Maintain aspect ratio. Choose fit **Inside**, Width 1080, Height 1080. Press Resize Image.
  2. The page shows "Preview at 1080 x 1080px" and the toast "Resized to 1080x1080". The file is 1080×810.
  3. Repeat with **Outside**: the file is 1440×1080, with the same message.
  4. Drop `tiny.png` (50×50). Tick "Never make it bigger than the original", type Width 500, press Resize Image. The toast says "Resized to 500x500"; the file is 50×50.
- **R2 (copy):**
  1. Drop `img.bmp` or `anim.gif` and resize. The result is PNG (the download name ends .png).
  2. Compare Common questions → "What happens to the file format?" ("Output matches the input type for JPEG, PNG, WebP, GIF and BMP").
  3. In Crop, count the ratio buttons (9) vs the FAQ "Are there crop shapes…" (5).
  4. Watch https://www.youtube.com/watch?v=RLVYl39EfcQ 0:15–0:51: the old controls and the caption "10 free uses daily!".
- **R3 (accessibility):** drop any image in Resize and run axe on `main`: `label` critical on `.w-24`. In Crop, the ratio buttons have no `aria-pressed`. After Apply Crop, `document.activeElement` is BODY.
- **R4 (DPI):** Or set the width in → centimetres (print), 10, DPI 300 → Set width → Resize Image. The file is 1181 px wide with no DPI tag (Pillow `info.get('dpi')` → None).
