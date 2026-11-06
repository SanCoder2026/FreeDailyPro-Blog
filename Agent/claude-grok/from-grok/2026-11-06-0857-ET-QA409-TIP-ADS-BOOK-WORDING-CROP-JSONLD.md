Sent: 2026-11-06 08:57 ET
Source: owner (standing ads rule Nov 1 2026; trial wording rule; Testing Bot QA-409 Nov 6; Web Design Crop PDF audit Nov 6 — JSON-LD bug only; sticky Crop proposals held for Santosh).

## How to work with us
Partner with FreeDailyPro. Inspect the live site and codebase first. Restate intent in your own words, challenge weak ideas, then implement the smallest change that hits the outcomes. Do not remove or turn off Google ads.

## Intent
Keep trial tools usable on phones while ads keep earning, and make Book Toolbox copy match the real metering language (trial uses, not "download credit").

## Why
1. **QA-409 tip-calculator (signed-out Guest, Nov 6 ~08:07 ET):** Osteon/anchor ad overlaps the lower action bar (Copy / Save / Print) and can cover Download CSV at some scroll positions. Standing owner rule (Nov 1): never remove or turn off ads; place them so they never cover action buttons, inputs, results, or Download; anchor must not overlap sticky bars; reserve fixed space; keep auto-ads but exclude the tool area.
2. **QA-409 Book Writing Toolbox:** SSR HTML for `/tool/book-writing-toolbox` still contains **"download credit"** twice (e.g. "uses one download credit"). Packs and $3.99/$6.99/$17.99/$49.99 download packs are retired; only $29.99/mo + 7-day trial. Wording should say trial use / download uses one trial use — never "download credit".
3. **Web Design Crop PDF mobile audit (Nov 6):** JSON-LD `SoftwareApplication` `offers.price` is still `"0"` on `/tool/crop-pdf` while the buy link correctly shows Professional $1 day pass · $4.99/month. Same class of schema bug as other PDF tools already fixed.

## Outcomes (done when)
1. On tip-calculator at 375/390, Copy / Save / Print / Download CSV stay fully tappable with the anchor ad visible; reserved bottom padding / offset clears the anchor; ads remain on the page (more slots OK in natural breaks below results / after download).
2. Live book-writing-toolbox SSR and client copy have zero "download credit" / "credit" metering phrases; trial language matches Professional vs Book Toolbox rules (Book = $29.99/mo 7-day trial only; preview watermark stays by design).
3. Live crop-pdf JSON-LD offers either omit price-0 or list the Professional day/monthly prices; title/meta/buy link unchanged unless needed for consistency.
4. No homepage mockup work. No ad removal. No DB changes outside what you already own for schema.

## Suggested direction (interpret freely)
- Tip: raise sticky/action chrome above `calc(anchor height + safe-area)`; ensure `.tool-area` / action row stay in `google-auto-ads-ignore`; keep Osteon/anchor, just stop the overlap (S4 smart placement).
- Book: grep for "download credit" / credit-meter strings on book toolbox routes and replace with trial-use wording; leave preview watermark behavior alone.
- Crop: fix JSON-LD only this brief. **Do not** implement Crop sticky Apply/Download bars yet — those are owner proposals awaiting Santosh.

## Constraints
- Free routes only for promotion elsewhere; this brief is site/copy/schema only.
- Never say "free tools" in UI.
- Public counts in multiples of 50 with +.
- Testing Bot stops at Stripe Checkout; do not ask Claude to bypass sign-in.

## Process
Inspect → restate → implement → verify live tip-calculator actions clear of ads, book page has no "download credit", crop-pdf JSON-LD price not 0 → note in next from-claude status.
