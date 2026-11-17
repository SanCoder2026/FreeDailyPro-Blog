#!/usr/bin/env python3
"""
Brand a generated hero image for FreeDailyPro.com blogs.

ORIGINAL owner sticker (blog-agent/scripts/brand_image.py, Aug 2026).
Rules (RULES.md §5 / site-blog-pack/1-NEW-BLOG-RULES.md §10):
- Output exactly 1200×630 WebP, <150 kB
- Bottom stripe with logo F. (#4FD8C4) + FreeDailyPro.com
  (only the first F of Free is teal; rest white)
- No other copyright logos/text in the image
- Scene must already be topic-relevant (person + props/UI) BEFORE branding
"""
from __future__ import annotations
import argparse
import io
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

TEAL = (79, 216, 196)  # #4FD8C4
WHITE = (255, 255, 255)

HERE = Path(__file__).resolve().parent
BRANDING = HERE / "branding"


def _font(name: str, size: int):
    # SpaceGrotesk preferred when valid; many copies in this environment are corrupt → DejaVu.
    candidates = [
        BRANDING / name,
        Path("/workspace/artifacts/blog-agent/fonts") / name,
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf") if "Bold" in name else Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for cand in candidates:
        if not cand or not Path(cand).exists():
            continue
        try:
            return ImageFont.truetype(str(cand), size)
        except Exception:
            continue
    return ImageFont.load_default()


def get_space_grotesk(size):
    return _font("SpaceGrotesk-Bold.ttf", size)


def get_space_grotesk_med(size):
    return _font("SpaceGrotesk-Medium.ttf", size)


def make_brand_mark(height=70):
    """icon + F(teal)reeDailyPro.com (white)"""
    icon_path = BRANDING / "logo_f_icon.png"
    if not icon_path.exists():
        icon_path = Path("/workspace/artifacts/blog-agent/logo_f_icon.png")
    if not icon_path.exists():
        return None

    icon_size = int(height * 0.78)
    icon = Image.open(icon_path).convert("RGBA").resize((icon_size, icon_size), Image.Resampling.LANCZOS)

    font_f = get_space_grotesk(int(height * 0.48))
    font_rest = get_space_grotesk_med(int(height * 0.48))

    f_text = "F"
    rest = "reeDailyPro.com"

    dummy = Image.new("RGBA", (10, 10))
    d = ImageDraw.Draw(dummy)
    bf = d.textbbox((0, 0), f_text, font=font_f)
    br = d.textbbox((0, 0), rest, font=font_rest)
    fw = bf[2] - bf[0]
    th = max(bf[3] - bf[1], br[3] - br[1])

    pad_x = 16
    gap = 10
    total_w = pad_x + icon_size + gap + fw + (br[2] - br[0]) + pad_x + 8

    brand = Image.new("RGBA", (total_w, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(brand)

    iy = (height - icon_size) // 2
    brand.paste(icon, (pad_x, iy), icon)

    tx = pad_x + icon_size + gap
    ty = (height - th) // 2 - 2

    for dx, dy in [(1, 1), (0, 1)]:
        draw.text((tx + dx, ty + dy), f_text, font=font_f, fill=(0, 0, 0, 120))
        draw.text((tx + fw + dx, ty + dy), rest, font=font_rest, fill=(0, 0, 0, 120))

    draw.text((tx, ty), f_text, font=font_f, fill=TEAL + (255,))
    draw.text((tx + fw, ty), rest, font=font_rest, fill=WHITE + (255,))
    return brand


def brand_image(input_path: str, output_path: str, target_size=(1200, 630), max_kb=145):
    img = Image.open(input_path).convert("RGBA")
    tw, th = target_size

    src_w, src_h = img.size
    scale = max(tw / src_w, th / src_h)
    new_w = int(src_w * scale)
    new_h = int(src_h * scale)
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - tw) // 2
    top = (new_h - th) // 2
    img = img.crop((left, top, left + tw, top + th))

    stripe_h = 78
    stripe = Image.new("RGBA", (tw, stripe_h), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(stripe)
    for i in range(stripe_h):
        alpha = int(40 + 200 * (i / stripe_h) ** 0.85)
        sdraw.line([(0, i), (tw, i)], fill=(6, 10, 18, alpha))
    for i in range(8):
        alpha = int(30 * (1 - i / 8))
        sdraw.line([(0, i), (tw, i)], fill=(0, 0, 0, alpha))

    img.paste(stripe, (0, th - stripe_h), stripe)

    brand = make_brand_mark(height=int(stripe_h * 0.72))
    if brand:
        bx = 28
        by = th - stripe_h + (stripe_h - brand.height) // 2
        img.paste(brand, (bx, by), brand)
        adraw = ImageDraw.Draw(img)
        adraw.rectangle([0, th - 5, tw, th], fill=TEAL + (230,))
    else:
        # Fallback lockup if icon missing (still original text rules)
        adraw = ImageDraw.Draw(img)
        font_f = get_space_grotesk(22)
        font_rest = get_space_grotesk_med(22)
        y0 = th - stripe_h + 22
        adraw.text((36, y0), "F", font=font_f, fill=TEAL + (255,))
        try:
            fw = font_f.getlength("F")
        except Exception:
            fw = 14
        adraw.text((36 + fw, y0), "reeDailyPro.com", font=font_rest, fill=WHITE + (255,))
        adraw.rectangle([0, th - 5, tw, th], fill=TEAL + (230,))

    final = Image.new("RGB", (tw, th), (255, 255, 255))
    final.paste(img, mask=img.split()[3] if img.mode == "RGBA" else None)

    out = Path(output_path)
    if out.suffix.lower() != ".webp":
        out = out.with_suffix(".webp")

    quality = 82
    while quality >= 40:
        buf = io.BytesIO()
        final.save(buf, "WEBP", quality=quality, method=6)
        size_kb = len(buf.getvalue()) / 1024
        if size_kb <= max_kb:
            out.write_bytes(buf.getvalue())
            print(f"Branded WebP saved: {out}  ({tw}x{th}, {size_kb:.1f} kB, q={quality})")
            return str(out)
        quality -= 6

    final.save(out, "WEBP", quality=35, method=6)
    print(f"Branded WebP (high compression): {out}  ({out.stat().st_size/1024:.1f} kB)")
    return str(out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()
    brand_image(args.input, args.output)
