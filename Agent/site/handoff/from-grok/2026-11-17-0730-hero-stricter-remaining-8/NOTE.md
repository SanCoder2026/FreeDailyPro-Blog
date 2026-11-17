# hero-stricter-remaining-8
Date: 2026-11-17 07:30
Type: HERO FIX (live replacements)

## Why
Fresh full-site audit 2026-11-17 (385 heroes):
- Prior packs already **applied on live**:
  - `2026-11-13-1330-hero-standard-upgrade-12` (12 weakest) — all MATCH
  - `2026-11-13-0745-hero-image-fixes-3-api-posts` (3 API) — all MATCH
- Technical: 0 size fails, 0 over-150KB, 0 duplicate hashes, high-risk 0
- Stricter residual: low-person / dark-scene / high-teal outliers that still look weak at a glance

## What (8 new heroes)
run-stage-countdown-and-focus-rounds, strip-gps-and-exif-from-photos, audio-compressor,
bates-stamp-production-zip-legal-desk, jwt-decoder, run-prize-draw-and-event-merch,
color-converter, build-run-of-show-cue-sheet-and-timer

## Checks
1200×630 WebP <150KB, bottom FreeDailyPro sticker only, person face + tool UI visible, unique per slug.

## Deploy
Copy images/*.webp over live blog heroes by exact slug. Optional imageAlt from APPLY-MAP.json.
