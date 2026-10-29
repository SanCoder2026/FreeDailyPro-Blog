# NOTE — 2026-10-29-0115-hero-topic-relevance-pass

**Type:** HERO IMAGE FIX (no new posts)  
**Date:** 2026-10-29 01:15 UTC  
**Count:** 15 replacement heroes  

## Why this pack exists (owner feedback)

Previous audits weighted **brand bar + 1200×630** too heavily and under-checked  
**topic relevance CRITICAL** (RULES §5 / HERO-IMAGE-RULE §3):

> If the image could fit any blog, it is wrong — regenerate until the topic is obvious at a glance.

Example: `assign-guests-to-tables-seating-chart` — brand was fine, but the scene did not  
make *seating assignment* obvious enough (generic planner-with-tablet look).

Also fixed: wrong props (Bates stamp shown as packing boxes), floating F logos in scene,  
abstract-only heroes, exact MD5 duplicates, and near-reused stock across unrelated posts.

## Method

1. Title → required props/UI written first  
2. Photoreal scene with **topic dominant** (tool UI/props fill the frame)  
3. `brand_image.py` bottom sticker only  
4. Verify 1200×630 WebP <150KB  

## Claude apply

Read `APPLY-MAP.md`. Images only. Prefer this pack over older 2015/1300 for overlapping slugs.

## Follow-up

Full 324 visual topic pass continues; more packs if further weak persona/generic heroes remain.
