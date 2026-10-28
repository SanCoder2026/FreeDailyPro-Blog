# NOTE — 2026-10-28-2015-hero-image-fixes

**Type:** HERO IMAGE FIX (no new posts)  
**Date:** 2026-10-28 20:15 UTC  
**Count:** 7 replacement heroes  

## Full live audit (324 downloadable heroes)

| Check | Result |
|-------|--------|
| 1200×630 WebP <150KB | All pass |
| Bottom FreeDailyPro sticker present | All pass |
| Unique image per post | **2 exact MD5 duplicates found** |
| Topic relevance / no floating logo in scene | **Several failures** |

### Failures fixed in this pack

| Slug | Why it failed |
|------|----------------|
| `mail-merge-letters-and-certificates-from-csv` | Abstract teal tech + huge floating F logo on photo body |
| `plan-event-one-shared-project-event-suite` | Abstract UI + floating F logo |
| `install-event-apps-iphone-android` | Floating F logo over phone scene |
| `one-link-per-exhibitor-trade-show-floor` | Huge floating F over trade-show booth |
| `freedailypro-vs-tinywow-privacy-and-free-tier-compared` | **Exact same image** as `freedailypro-200-free-tools-milestone` (reuse forbidden) |
| `run-stage-countdown-and-focus-rounds` | Near-identical reuse of the manuscript-format hero pose (unrelated topics) |
| `capture-event-receipts-against-budget` | Abstract colorful boxes only — no person, no receipts/budget UI |

### Method (locked rule)

1. Topic-specific photoreal scene (person + tool UI/props)  
2. `scripts/brand_image.py` bottom sticker only  
3. Verify 1200×630 WebP <150KB  

### Claude apply

1. Read `APPLY-MAP.md`  
2. Replace live `/blog/{slug}.webp` with `images/{slug}.webp`  
3. Images only — do not change post Markdown  

### Not in this pack

- Prior pack `2026-10-28-1300-hero-image-fixes-topic-relevant` (36) already applied on live  
- Remaining ~317 heroes passed technical + sampling review for this pass  

