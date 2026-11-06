# NOTE — 2026-10-28-1345-hero-image-fixes-topic-relevant

**Type:** HERO IMAGE FIX (no new posts)  
**Date:** 2026-10-28 13:45 UTC (handoff docs completed 2026-11-06)  
**Count:** 36  

## Why this pack exists

Live blog heroes had drifted from the **owner original standard** (RULES.md §5 + 1-NEW-BLOG-RULES.md §10):

- Generic / non-topic stock
- Branding drift
- Missing or non-standard 1200×630 WebP

This pack regenerates **topic-specific** photoreal scenes (person + tool UI/props visible) and applies the bottom FreeDailyPro sticker only.

## Locked standard

See `HERO-IMAGE-RULE.md` in this folder and at `from-grok/HERO-IMAGE-RULE.md`.

**Do not weaken topic relevance.** A bottom bar on a generic photo is still a fail.  
Gold accepted example: `2026-10-15-1905-new-pdf-to-jpg-and-password-generator/images/password-generator-new-accounts.webp`.

## What’s in the pack

- `images/{slug}.webp` — 36 unique heroes, each 1200×630 WebP <150KB
- `APPLY-MAP.md` / `APPLY-MAP.tsv` — slug + live title + MD5 + bytes + URL
- `HERO-IMAGE-RULE.md` — immutable owner standard
- `scripts/` — branding helpers used for this batch

## Claude apply

1. Read APPLY-MAP.md  
2. Replace live `/blog/{slug}.webp` for all 36  
3. Images only  
4. After apply, live byte size should match APPLY-MAP  

## Verify after apply

For each slug: live file MD5/size matches APPLY-MAP; topic is obvious at a glance; bottom sticker only; no third-party logos.
