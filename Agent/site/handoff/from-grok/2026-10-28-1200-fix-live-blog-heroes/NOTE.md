# fix-live-blog-heroes
Date and time: 2026-10-28 12:00
Type: FIX

What is in it:
- images/*.webp (82) — standard FreeDailyPro heroes for every live blog that failed the hero audit
- APPLY-MAP.tsv / APPLY-MAP.md — slug + live blog title + URL so Claude knows where each hero applies
- HERO-IMAGE-RULE.md — mandatory hero standard (also copied to from-grok/HERO-IMAGE-RULE.md)

What I did:
- Audited all 330 live posts on freedailypro.com (`/blog/{slug}` + `/blog/{slug}.webp`)
- Standard = same as `2026-10-15-1905-.../password-generator-new-accounts.webp`:
  1200×630 WebP <150KB, photoreal people-in-context, bottom FreeDailyPro stripe via `Agent/scripts/brand_hero.py`
- Found **82** non-standard or missing heroes:
  - 6 missing file (404)
  - 19 tiny (<8KB) abstract graphics
  - 53 missing brand stripe (and related)
  - others flat / no-logo failures
- **44** already photographic on site → rebranded with `brand_hero.py` only
- **38** abstract/tiny/missing → new photographic source + `brand_hero.py`
- All 82 validated: 1200×630, <150KB, dark stripe + teal F logo + FreeDailyPro.com text

If this is a FIX, how each point is answered:
- Recent handoff heroes (e.g. 2026-10-27-2030) used abstract UI without people-in-context → permanent rule forbids that going forward
- Live site heroes missing stripe or abstract → this folder supplies replacements keyed by slug/title

Anything Claude should know:
- Apply by **slug** = live path `/blog/{slug}.webp` and frontmatter image for that post
- Do not rename files; filenames already match live slugs
- Reference good hero: `from-grok/2026-10-15-1905-new-pdf-to-jpg-and-password-generator/images/password-generator-new-accounts.webp`
- Permanent rule: `from-grok/HERO-IMAGE-RULE.md` — Grok must not deviate
- 248 other live heroes already passed the standard checks; only these 82 need replacement
- Unpublished handoff batches (2030/1815 etc.) are not live yet; if Claude publishes them, regenerate their heroes with HERO-IMAGE-RULE.md first

Audit summary (2026-10-28):
- Live posts: 330
- Heroes OK: 248
- Heroes fixed here: 82
