# NOTE — hero priority list for the Grok Imagine blog agent

Sent: 2026-10-31 13:00 ET

**Intent:** The blog agent now owns hero generation and new category posts. This folder hands it a ranked list of live heroes that break HERO-IMAGE-RULE.md, so it can fix the worst ones first. Nothing here is an image; it is a list only.

**Why:** Claude's 120-slug CSV (`Agent/claude-grok/from-claude/2026-10-29-hero-list-for-blog-bot.csv`) was never relayed, so B-0025 stalled. These are the highest-impact slugs from that CSV and from a live sitemap scan (og:image + pHash near-duplicate check, 2026-10-31).

**Outcome wanted:** For each slug in `list.md` (P1 first), make a new pack `from-grok/YYYY-MM-DD-HHMM-<name>/` with `images/{slug}.webp` (photoreal person doing the task, 1200×630 WebP < 150 kB, bottom sticker via brand_image.py), plus APPLY-MAP.md, in the 2026-10-29-0300-hero-remaining-12-apply format.

**12-pack status (checked 2026-10-31 ~12:58 ET):** all 12 slugs from `2026-10-29-0300-hero-remaining-12-apply` MATCH live (same MD5 + byte size). Nothing left to apply from that pack.

**Also seen (for the blog agent's post work):** category `powerpoint-slides` has no topic page. Thin categories are 3d, animation, marketing-design and relocation (4 posts each), household and qr (5), and travel (6).

**Note on scripts:** HERO-IMAGE-RULE.md names `Agent/scripts/brand_image.py`, but that path only has `brand_hero.py`. A working copy of brand_image.py and its branding assets is in `from-grok/2026-10-28-2015-hero-image-fixes/scripts/`.

Source: owner
