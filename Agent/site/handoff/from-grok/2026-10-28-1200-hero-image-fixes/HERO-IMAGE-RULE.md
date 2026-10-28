# HERO IMAGE RULE (LOCKED — DO NOT DEVIATE)

This rule is mandatory for every Grok (and any agent) blog hero from 2026-10-28 forward.

## Gold standard
- Post: `from-grok/2026-10-15-1905-new-pdf-to-jpg-and-password-generator/posts/password-generator-new-accounts.md`
- Image: `password-generator-new-accounts.webp`
- Live: https://www.freedailypro.com/blog/password-generator-new-accounts.webp

If a new hero does not match this standard, it is **rejected**.

## Required output
| Property | Value |
|----------|-------|
| Size | **1200 × 630** exactly |
| Format | **WebP** |
| Max file size | **< 150 KB** |
| Content | Realistic **people-in-context** photo (or clear tool-in-use scene). Not abstract blobs, not text posters, not pure UI screenshots as the only content. |
| Branding | **Bottom stripe only** (see below). Nothing else. |

## Required branding (bottom stripe only)
Use **only** `Agent/scripts/brand_hero.py`. Do not hand-draw a different bar. Do not invent a new logo lockup.

The script applies:
1. Cover-crop resize to 1200×630
2. Dark full-width bar: height **48px**, color RGB **(20, 28, 36)**
3. Left teal accent: **8px** wide, color **#4FD8C4** / RGB (79, 216, 196)
4. Teal circle (~28px) with dark **F**
5. Text **FreeDailyPro.com** — first **F** teal, remainder white
6. WebP quality step-down until size **< 150KB**

### Forbidden (automatic reject)
- No bottom stripe
- Dark bar without FreeDailyPro.com text / F circle
- Floating F logo on the photo body without the dark bar
- Full-height teal side bar
- Top watermark / diagonal watermark
- Wrong dimensions (not 1200×630)
- File ≥ 150KB after branding
- Overwriting brand_hero.py colors or layout “for this batch”

## Process (every new blog hero)
1. Obtain a suitable base photo (people in context preferred).
2. Run:
   ```bash
   python3 Agent/scripts/brand_hero.py INPUT.jpg OUTPUT.webp
   ```
3. Verify: 1200×630, dark bar, teal F circle, FreeDailyPro.com visible, size < 150KB.
4. Name the file to match the post slug: `{post-slug}.webp`
5. Place under the batch `images/` folder and set frontmatter `image: "../images/{post-slug}.webp"`

## Process (fixing live heroes)
1. Download live `/blog/{slug}.webp`
2. If incomplete brand marks sit in the bottom ~90px, crop them off the source first
3. Run the same `brand_hero.py`
4. Ship in a `from-grok/YYYY-MM-DD-HHMM-hero-image-fixes/` folder with `APPLY-MAP.md` (slug + title + live URL + file)

## Script location
`Agent/scripts/brand_hero.py` (canonical). The pixel layout must stay identical to this file.

## Self-check before commit
```bash
python3 - <<'PY'
from PIL import Image
from pathlib import Path
p = Path("images/SOME.webp")
im = Image.open(p).convert("RGB")
assert im.size == (1200, 630)
assert p.stat().st_size < 150_000
assert im.getpixel((600, 620))[0] < 50   # dark bottom
assert im.getpixel((3, 620))[1] > 150    # teal left accent
print("hero OK", p)
PY
```
