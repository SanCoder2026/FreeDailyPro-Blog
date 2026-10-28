# FreeDailyPro Hero Image Rule — ORIGINAL STANDARD (locked)

**Source of truth (your original rules, before any Grok drift):**
- `RULES.md` §5 Image Rules (repo root / blog-agent)
- `site-blog-pack/1-NEW-BLOG-RULES.md` §10 Hero image
- `site-blog-pack/00-START-HERE-INSTRUCTIONS-FOR-GROK.md` point 8

**Gold example that matches the standard:**
`from-grok/2026-10-15-1905-new-pdf-to-jpg-and-password-generator/images/password-generator-new-accounts.webp`  
(person at a home desk, laptop + phone, password task obvious; bottom FreeDailyPro stripe only)

Claude’s first hero note (2026-10-15-1935 CHANGES) only required *shipping* a 1200×630 WebP <150 kB when a post had no image. It did **not** replace or weaken the content rules below.

---

## 1. Size & file
- Exactly **1200 × 630** WebP
- **Under 150 kB**
- Filename = post slug: `<slug>.webp`
- **One unique image per post** — never reuse across posts

## 2. People (prefer humans)
- Prefer real people in the scene
- Variety: women, men, older adults, groups as needed
- Natural, positive expression when suitable
- Attire and setting match the blog theme (office / home / outdoor / worksite / studio)

## 3. Topic relevance is MANDATORY (CRITICAL) — do not skip
- The image **MUST clearly show what the blog is about**
- **Not** a generic smiling person
- **Not** a random stock photo that could fit any post
- **Not** abstract UI / neon tech / teal-only graphics as the whole hero
- Include **visible indicators** of the tool/task:
  - Tool UI on screen (PDF pages, image editor, invoices, browser tabs, code/SQL, menu card, etc.)
  - Related props (folders labeled PDF, camera, product photos, packing slip, seating chart, audio gear, etc.)
  - Setting that matches the subject (freelancer desk, creative studio, warehouse, event floor, kitchen for catering, etc.)
- Clothing, background, and persona must fit the topic
- **If the image could fit any blog, it is wrong — regenerate until the topic is obvious at a glance**

## 4. Branding — bottom stripe only
Apply `Agent/scripts/brand_hero.py` (or identical pixel layout):
- Dark bottom bar only (~48 px)
- Logo **F.** in **#4FD8C4**
- Text **FreeDailyPro.com** — **only the first F teal**, rest white
- **No** logo floating in the scene
- **No** top-left / full-height side bar logo
- **No** third-party logos, watermarks, or copyright text
- **No** title text baked into the photo

## 5. Pipeline (every hero)
```
1. Generate or source a TOPIC-SPECIFIC photoreal scene
   (person doing THIS tool’s real task + props/UI visible)
2. python Agent/scripts/brand_hero.py SOURCE.jpg images/<slug>.webp
3. Verify: 1200x630, <150KB, bottom stripe + F. + FreeDailyPro.com
4. Confirm: topic obvious at a glance (fail if generic)
5. Write imageAlt describing what is visible (not a copy of the title)
```

## 6. Forbidden (automatic reject)
- Generic picsum / random stock that does not show the tool task
- Reusing one photo for multiple slugs
- Abstract “AI tech” panels as the full hero
- Stripe missing, wrong size, ≥150 KB
- Logo inside the scene or top-left brand mark
- Title / slogan painted on the image

## 7. Self-check before commit
- [ ] 1200×630 WebP < 150 kB  
- [ ] Bottom stripe only with teal F. + FreeDailyPro.com  
- [ ] Person (or clear hands) doing **this** task  
- [ ] Tool UI or topic props visible  
- [ ] Could **not** swap this image onto an unrelated post  
- [ ] Unique to this slug  
