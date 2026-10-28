# NOTE — 2026-10-28-1300-hero-image-fixes-topic-relevant

**Type:** HERO IMAGE FIX (no new posts)  
**Date:** 2026-10-28 13:00 UTC  
**Count:** 36 replacement heroes  

## Why this pack exists

Audit of `from-grok/2026-10-28-1200-hero-image-fixes` (the pack that only re-striped live heroes):

| Check | 1200 pack result |
|-------|------------------|
| 1200×630 WebP <150KB | Pass (brand bar applied) |
| Bottom FreeDailyPro sticker | Pass (via `brand_hero.py`) |
| **Topic relevance (CRITICAL)** | **Fail** — many abstract neon tech panels, floating F logos on the photo body, generic stock that could fit any post |
| Person + tool UI/props | Fail on most |

Per locked `HERO-IMAGE-RULE.md` / `RULES.md` §5 / `1-NEW-BLOG-RULES.md` §10:

> If the image could fit any blog, it is wrong — regenerate until the topic is obvious at a glance.

**This pack regenerates every scene first**, then applies the owner sticker. Do not “fix” by only re-striping a still-generic photo.

## Gold standard (do not deviate)

- Scene: people in a real workflow with **visible tool UI/props**  
  Example: `from-grok/2026-10-15-1905-new-pdf-to-jpg-and-password-generator/images/password-generator-new-accounts.webp`
- Sticker: bottom only via `Agent/scripts/brand_image.py`  
  (gradient strip ~78px, real F icon + FreeDailyPro.com with first F teal, teal hairline)

## What Claude should do

1. Read `APPLY-MAP.md` (slug → title → live URL → file).
2. For each row, replace live `https://www.freedailypro.com/blog/{slug}.webp` with `images/{slug}.webp` from **this** folder.
3. Images only — do not change post Markdown in this batch.
4. After apply, each hero must show: topic-obvious scene + bottom FreeDailyPro sticker only.

## Method used (non-negotiable)

1. Imagine text-to-image: **topic-specific photoreal** scene (person + tool UI/props). Prompt forbids FreeDailyPro logo in the photo.
2. Brand with owner script:
   ```bash
   python3 scripts/brand_image.py src/<slug>.jpg images/<slug>.webp
   ```
3. Verify: 1200×630, <150KB, bottom sticker, topic unique to slug.

## Files

- `images/*.webp` — 36 branded heroes, named exactly as live slug  
- `src/*.jpg` — unbranded source scenes (for re-brand if sticker script updates)  
- `scripts/brand_image.py` + `scripts/branding/` — sticker used  
- `APPLY-MAP.md` / `apply-map.json` — Claude apply table  
- `HERO-IMAGE-RULE.md` — locked rule (copy of owner standard)  
- `NOTE.md` — this file  

## Verification (2026-10-28)

All **36/36** pass: 1200×630 WebP, each <150KB, teal hairline + FreeDailyPro.com on bottom stripe.

## Immutable rule reminder

Grok must **push back** if Claude or the owner asks to weaken topic relevance, skip `brand_image.py`, reuse one photo across slugs, or ship abstract-only heroes. The rule does not change.
