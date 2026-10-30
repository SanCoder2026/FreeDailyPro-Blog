# Homepage intro video swap: E1RC7HbYXaA → s1CA84t_PCA

**From:** Grok (for Santosh) · **Date:** 2026-10-30 08:15 ET · **Type:** homepage fix

## How to work with us
Treat this as a partner brief, not a blind order list. Inspect the real codebase, keep to how we've deployed before, push back on anything weak, and choose the best implementation.

## Intent
The homepage intro/overview video is the first "what is FreeDailyPro" pitch visitors see. Santosh replaced it with a refined overview that has a much stronger thumbnail. We want the homepage to show the new video and thumbnail, load fast, and match what's on YouTube.

## Why
- The old embed `E1RC7HbYXaA` is being retired. It stays up on YouTube **only until you confirm the swap is live**.
- New video: `s1CA84t_PCA`. It has a new custom thumbnail (round4_a, "300+ tools in your browser"), approved by Santosh. It goes live on YouTube at about **8:45pm ET on Oct 30, 2026**. Until then, YouTube's own maxres image may still show the old auto frame.
- The homepage still shows **"4,400+ users"** and **"200+ tools"**. Santosh's current figures are **5,000+ users** and **300+ tools, apps and workflows**.

## Assets
- Watch: https://www.youtube.com/watch?v=s1CA84t_PCA
- Embed: https://www.youtube-nocookie.com/embed/s1CA84t_PCA
- Poster (remote): https://i.ytimg.com/vi/s1CA84t_PCA/maxresdefault.jpg
- Poster (local, same art; use this to avoid the pre-8:45pm stale frame and a third-party fetch): `images/round4_a_final.jpg` in this folder. Convert it to WebP/AVIF in the site's usual way if that fits.

## Outcomes (done =)
1. The homepage intro shows `s1CA84t_PCA` with the new thumbnail as its poster.
2. **Fast:** use a lite/facade embed so the iframe loads only on click (or lazy-loads), and no YouTube JS runs on first paint.
3. **No layout shift:** fixed 16:9 aspect-ratio box, with the poster's width and height set.
4. Meaningful `title` on the iframe and `alt` on the poster, e.g. "FreeDailyPro overview: 300+ browser tools, apps and workflows".
5. **VideoObject JSON-LD** updated with the new embedUrl, contentUrl/url, thumbnailUrl and name/description. Keep uploadDate accurate; check it on YouTube and don't invent it.
6. **Old ID gone everywhere.** `grep -rn "E1RC7HbYXaA"` across the site (pages, schema, sitemaps, OG/meta, blog, Agent docs) returns nothing, or only an intentional historical note.
7. Stats update **suggested**: 4,400+ → 5,000+ users and 200+ → 300+ tools/apps/workflows, wherever the homepage or meta says them. If any figure is computed or sourced on the site, follow that source rather than hardcoding.
8. **Report back** in `from-claude/` (or your usual channel) once it's live on production, with the deploy URL and grep result, so Grok can take down `E1RC7HbYXaA`.

## Constraints
- Brand wording: don't push "free" as the hook ("10 trial uses per day" and "300+ professional tools, premium applications and workflow products" are fine). Make no speed claims in copy.
- Don't use a real person's photo.
- Don't touch other sections beyond the stat fix and video swap.

## Process
Inspect the current homepage and schema → restate the plan → implement → verify (Lighthouse CLS ≈ 0, embed plays, schema validates, grep is clean) → deploy → report.
