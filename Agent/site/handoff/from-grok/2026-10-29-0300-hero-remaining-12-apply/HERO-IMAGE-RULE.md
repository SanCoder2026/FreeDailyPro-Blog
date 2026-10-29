# FreeDailyPro Hero Image Rule — OWNER ORIGINAL STANDARD (locked)

**Do not invent a new standard.** This file only restates what you already published before Claude/Grok drift.

## Source of truth (in order)
1. `site-blog-pack/1-NEW-BLOG-RULES.md` §10 Hero image (effective 2026-10-15)
2. `RULES.md` / `Agent/RULES.md` §5 Image Rules
3. `BLOG-RULES.md` §3 Hero image rules (do not change) — pipeline uses **bottom sticker** via `brand_image.py`
4. Gold accepted example:  
   `from-grok/2026-10-15-1905-new-pdf-to-jpg-and-password-generator/images/password-generator-new-accounts.webp`

Claude’s early ACCEPTED/CHANGES notes only asked to *ship* a missing 1200×630 WebP. They did **not** replace topic-relevance or branding rules.

---

## 1. Size & file
- Exactly **1200 × 630** WebP
- **Under 150 kB**
- Filename = post slug: `<slug>.webp`
- **One unique image per post** — never reuse across posts
- `imageAlt` describes what is **visible**, not a copy of the title

## 2. People (prefer humans)
- Prefer people in a real workflow
- Variety: women, men, older adults, groups as needed
- Natural, positive expression when suitable
- Attire and setting match the theme (office / home / studio / outdoor / worksite)

## 3. Topic relevance is MANDATORY (CRITICAL)
From your RULES.md §5 — do not weaken:

- The image **MUST clearly show what the blog is about**
- **Not** a generic smiling person
- **Not** random stock that could fit any post
- **Not** abstract UI / neon “AI tech” as the whole hero
- Include **visible indicators**:
  - Tool UI on screen (PDF pages, editor panels, invoices, browser tabs, SQL, menu card, etc.), **and/or**
  - Related props (PDF folder, camera, product photos, packing slip, seating chart, audio gear, etc.), **and/or**
  - Setting that matches the subject
- Clothing, background, persona fit the topic
- **If the image could fit any blog, it is wrong — regenerate until the topic is obvious at a glance**

## 4. Branding — bottom sticker only
**Canonical sticker script (owner original):**  
`Agent/scripts/brand_image.py`  
Assets: `Agent/scripts/branding/logo_f_icon.png` (+ fonts when valid)

What the sticker does (original Aug 2026 design):
- Cover-crop to 1200×630
- Bottom **gradient** dark strip (~78 px)
- Real **F. icon** + text **FreeDailyPro.com** (first **F** `#4FD8C4`, rest white)
- Thin **teal hairline** at the very bottom edge
- **No** logo inside the photo scene
- **No** top-left / full-height side bar
- **No** third-party logos or watermarks
- **No** title/slogan painted into the photo

`Agent/scripts/brand_hero.py` is a **later simplified** lockup (flat 48 px bar + drawn circle F).  
**Prefer `brand_image.py`.** Do not treat the simplified script as a reason to skip topic-relevance.

## 5. Pipeline (every hero — do not deviate)
```
1. Create a TOPIC-SPECIFIC photoreal scene
   person doing THIS tool’s real task + props/UI visible
   (prompt must NOT put FreeDailyPro logo in the scene)

2. Apply the owner sticker:
   python3 Agent/scripts/brand_image.py SOURCE.jpg images/<slug>.webp

3. Verify all of:
   - 1200×630 WebP < 150 kB
   - bottom sticker only (F. icon + FreeDailyPro.com)
   - topic obvious at a glance (fail if generic / reusable on another post)
   - unique to this slug
```

## 6. Forbidden (automatic reject)
- Generic picsum / stock with no tool task
- Reusing one photo for multiple slugs
- Abstract-only “tech panel” heroes
- Missing sticker, wrong size, ≥150 kB
- Logo baked into the scene **and** sticker
- Top-left brand mark or full-height teal side bar
- “Fixed” by only adding a dark bar to a still-generic photo

## 7. Self-check before commit
- [ ] 1200×630 WebP < 150 kB  
- [ ] Bottom sticker via `brand_image.py` (icon + FreeDailyPro.com + teal hairline)  
- [ ] Person (or clear hands) doing **this** task  
- [ ] Tool UI or topic props visible  
- [ ] Could **not** swap this image onto an unrelated post  
- [ ] Unique to this slug  

## 8. Live-site hero fixes
If replacing live `/blog/{slug}.webp` files:
- New folder: `from-grok/YYYY-MM-DD-HHMM-hero-image-fixes/`
- `images/{slug}.webp` named exactly as live slug
- `APPLY-MAP.md` with slug + **blog title** + live URL
- Regenerate **scene first** when the live hero is abstract/generic; do not only re-stripe

---

*Keep this file aligned with RULES.md / 1-NEW-BLOG-RULES.md. Change only when the owner asks.*
