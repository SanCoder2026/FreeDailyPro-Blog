# B-0025 Replace off-topic blog hero images

**Priority:** P1
**Estimated effort:** ~2h (rolls over as images arrive)

## Goal / why
Owner reports many blog heroes are generic and off-topic (e.g. `automate-event-invite-card-calendar-and-page` shows a night city skyline). Only 19 were replaced; the 120-post list (`from-claude/2026-10-29-hero-list-for-blog-bot.csv`) was never actioned.

## What to change
- Image list: `Agent/claude-grok/from-grok/2026-10-29-B-0025-hero-image-requests.csv` (120 rows: slug, title, current hero, problem, output filename, prompt). Start with the invite post.
- The Grok blog image agent drops new heroes in its usual handoff folder for Claude; apply them as they arrive.
- Check each current hero first; if it already passes, mark "already OK".
- Reject images breaking the hero rule: topic-relevant, person plus visible tool UI, brand stripe at bottom only, no floating logo, unique, 1200x630 WebP under 150 kB, no other companies' logos.
- Update on-page hero, og:image and twitter:image together.

## Acceptance criteria
Each slug reported as replaced (live and checked) / already OK / waiting for image / rejected (reason); no duplicate heroes site-wide.

## Not in scope / do not decide
Blog text, slug changes, Claude generating images, writing to the image agent's handoff folders.

## Owner decisions needed
None.

## Source
owner
