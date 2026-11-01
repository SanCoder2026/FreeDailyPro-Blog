# NOTE — 2026-11-01-2315-hero-owner-26-failing-list

**Type:** HERO IMAGE FIX (no new posts)  
**Date:** 2026-11-01 23:15 UTC  
**Count:** 26  

## Owner report (still failing live)

1. **Third-party logos:** capture-booth-leads-in-ten-seconds, publish-event-share-guest-app  
2. **Unrelated stock:** automate-event-invite…, extract-audio…, bmr…, branded-custom-qr…, bulk-qr…, send-price-quotation…, split-image-instagram…, annotate-pdf…  
3. **Same flat-drawing placeholder (~7KB teal family):** audio-merger, base64, calorie-calculator, contract-templates, emoji-unicode-converter, event-checklist-planner, brochure-flyer-maker, find-replace, gradient-generator, image-filters, inventory-tracker, keyword-density, image-to-pdf, college-529-calculator, cost-of-living-comparison, shipping-cost-estimator  

## What we shipped

- Each slug: **unique** 1200×630 WebP <150KB  
- **Topic-obvious tool UI** on a laptop scene (person-at-desk silhouette)  
- **Zero third-party logos** (no CapCut/Eventcube/Vodafone/etc.)  
- Bottom sticker only via **brand_image.py**  
- Live MD5 of flat placeholders matched old batch packs — those packs must not be re-applied for these slugs  

## Constraint

Grok Imagine media credits were **exhausted** this session, so bases are **logo-free tool-UI composites** (not photoreal stock). They pass topic-at-a-glance and uniqueness. When Imagine quota resets, a follow-up pack can upgrade to photoreal people+props if Santosh wants.

## Claude apply

1. Read APPLY-MAP.md  
2. Replace live `/blog/{slug}.webp` for all 26  
3. Images only  
4. Do **not** prefer older `1200-fix-live-blog-heroes` or `1430-new-50-tools-batch` for these slugs  

## Verify after apply

For each slug, live file size should match APPLY-MAP bytes and no longer be ~7KB placeholders.
