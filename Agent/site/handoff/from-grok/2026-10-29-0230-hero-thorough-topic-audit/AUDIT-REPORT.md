# AUDIT-REPORT — Full live hero review (2026-10-29)

## Method (corrected)

Prior audits wrongly treated **brand bar + 1200×630** as a pass.  
This review uses the locked rule **topic-first**:

1. Read blog title / slug  
2. Ask: *Is this tool/task obvious at a glance?*  
3. Fail if: generic stock, wrong props, abstract-only, floating logo in scene, reusable on another post  
4. Brand check only after topic passes  

**Universe:** 332 sitemap blog URLs → **324** downloadable `/blog/{slug}.webp` heroes.  
**Review:** Title-labeled contact sheets (21 pages × ~16) + full-size review of tiny files, floaters, and suspects.

## Summary

| Bucket | Count |
|--------|------:|
| Live heroes reviewed | 324 |
| Size 1200×630 WebP <150KB | 324 (all) |
| Bottom FreeDailyPro brand present | 324 (all) |
| **FAIL topic relevance / uniqueness / logo-in-scene** | **27** |
| Fixed in this pack | 27 |
| PASS (no change this pack) | 297 |

## FAIL reasons (this pack)

| Failure class | Examples |
|---------------|----------|
| Floating F / logo in photo body | mail-merge, plan-event, install-event-apps, one-link-exhibitor |
| Abstract-only (no real task) | capture-event-receipts |
| Wrong props for title | bates-stamp (packing boxes), journal-submission (shipping), etsy/price (reused packing) |
| Not obvious at a glance | assign-guests seating chart (weak tablet scene) |
| Unique-image rule | freedailypro-vs-tinywow (was MD5 twin of 200-tools milestone) |
| Persona stock without tool UI | free-tools-for-*, free-toolkit-developer, how-to-stay-productive, corporate-safe, safe-alternatives |

## PASS notes (not in pack)

Full-size review confirmed many posts that look "abstract" in tiny thumbnails are actually **topic-correct** (clear tool UI), e.g.:

- `password-strength` — strength meter UI  
- `bulk-qr-codes-from-a-url-list-as-zip` — bulk QR grid + URL list  
- `cron-builder` — schedule builder fields  
- `capture-booth-leads-in-ten-seconds` — booth lead form  
- Most calculators, PDF tools, audio/video tools, book tools  

Tiny file size alone is **not** a fail (many are just heavily compressed WebP).

## Re-audit process locked for Grok

```
For every hero:
  title → required visible props/UI
  if not obvious at a glance → FAIL (do not pass on brand alone)
  generate topic-dominant scene
  brand_image.py sticker only
  verify 1200×630 <150KB
```

## Claude apply

Use `APPLY-MAP.md` in this folder. **27** replacement heroes.
