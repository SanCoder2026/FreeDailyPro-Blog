# NOTE — 2026-10-28-1200-hero-image-fixes

**Type:** HERO IMAGE FIX (no new posts)
**Date:** 2026-10-28 12:00
**Count:** 36 replacement heroes

## What this is
Audit of **all live** FreeDailyPro.com blog heroes (324 downloadable `/blog/{slug}.webp` files).

**Finding:** 36 live blogs were missing the **standard FreeDailyPro bottom brand bar** (dark stripe + teal F circle + `FreeDailyPro.com` text). Common failure modes:
- Floating teal “F” logo on the photo with **no dark bar**
- Plain dark bar with **no logo/text**
- Incomplete brand marks not matching the gold-standard post

**Gold standard (do not deviate):**
https://github.com/SanCoder2026/FreeDailyPro-Blog/blob/main/Agent/site/handoff/from-grok/2026-10-15-1905-new-pdf-to-jpg-and-password-generator/posts/password-generator-new-accounts.md
Hero: `password-generator-new-accounts.webp` — 1200×630, people-in-context photo, **bottom stripe only** with teal F logo + FreeDailyPro.com.

## What Claude should do
1. Read `APPLY-MAP.md` (slug → title → live URL → which file to drop on site).
2. For each row, replace the live hero `https://www.freedailypro.com/blog/{slug}.webp` with `images/{slug}.webp` from this folder.
3. Do **not** change post Markdown in this batch (images-only handoff).
4. After apply, heroes must show the dark bottom bar + teal F circle + FreeDailyPro.com.

## Files
- `images/*.webp` — 36 branded heroes, named **exactly** as the live blog slug
- `APPLY-MAP.md` — table for Claude
- `HERO-IMAGE-RULE.md` — locked process Grok must follow forever
- `NOTE.md` — this file
- `apply-map.json` — machine-readable map

## Method used (non-negotiable)
`Agent/scripts/brand_hero.py` only:
- 1200×630 cover crop
- Bottom stripe height 48px, color RGB(20,28,36)
- Left teal accent 8px #4FD8C4
- Teal circle + “F” + text FreeDailyPro.com (first F teal, rest white)
- WebP quality loop until **< 150KB**
- Bottom stripe **only** — no full-height side bars, no watermarks on the photo body
- When fixing incomplete live heroes, crop ~90px off the old bottom first to remove floating incomplete logos, then brand

## Audit numbers
- Live blog URLs in sitemap: 332 (minus topic/page noise)
- Heroes downloaded: 324
- Already standard: 288
- Fixed in this batch: 36
