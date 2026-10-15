#!/usr/bin/env python3
"""Resize to 1200x630, add FreeDailyPro bottom stripe only, save WebP <150KB."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import sys

W, H = 1200, 630
STRIPE_H = 48
TEAL = (79, 216, 196)  # #4FD8C4
WHITE = (255, 255, 255)
DARK = (20, 28, 36)

def brand(src: Path, dst: Path):
    im = Image.open(src).convert("RGB")
    # cover crop to 1200x630
    sw, sh = im.size
    scale = max(W / sw, H / sh)
    nw, nh = int(sw * scale), int(sh * scale)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - W) // 2
    top = (nh - H) // 2
    im = im.crop((left, top, left + W, top + H))
    draw = ImageDraw.Draw(im)
    # bottom stripe
    y0 = H - STRIPE_H
    draw.rectangle([0, y0, W, H], fill=DARK)
    # teal accent bar
    draw.rectangle([0, y0, 8, H], fill=TEAL)
    # text "F." teal + FreeDailyPro.com
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
        font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except Exception:
        font = ImageFont.load_default()
        font_sm = font
    # F. logo circle
    cx, cy = 36, y0 + STRIPE_H // 2
    draw.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=TEAL)
    draw.text((cx - 6, cy - 10), "F", fill=DARK, font=font_sm)
    # brand text: first F teal, rest white
    text_x = 58
    draw.text((text_x, y0 + 12), "F", fill=TEAL, font=font)
    # measure F width
    try:
        fw = font.getlength("F")
    except Exception:
        fw = 12
    draw.text((text_x + fw, y0 + 12), "reeDailyPro.com", fill=WHITE, font=font)
    # save webp under 150KB
    quality = 82
    for q in range(82, 40, -4):
        im.save(dst, "WEBP", quality=q, method=6)
        if dst.stat().st_size < 150_000:
            break
    print(f"{dst.name}: {dst.stat().st_size} bytes {im.size}")

if __name__ == "__main__":
    brand(Path(sys.argv[1]), Path(sys.argv[2]))
