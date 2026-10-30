# B-0038 AdSense: raise viewability and RPM with better placements, without hurting UX

**Priority:** P2
**Estimated effort:** ~1.5 h

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

Context: read-only pull from GA4 (28d Oct 1–28), Search Console (3 months Jul 28–Oct 27; indexing updated 10/22) and AdSense (earnings since Oct 24), taken Oct 29 2026. Totals: 3,412 GA users, GSC 548 clicks / 154K impressions / 0.4% CTR / avg position 18.1, AdSense $0.39.

## Intent
Earn more from the ads we already show by putting them where real users actually look, while keeping tools fast and clean and never interfering with paying.

## Why
- Earnings started Oct 24: **$0.39 over 7d**, 1,055 page views, **page RPM $0.37**, impression RPM $2.23, 173 impressions, 5 clicks.
- **Active View viewability 18.56%.** Most ads load where nobody sees them, either far below the fold or in hidden containers.
- Only 173 ad impressions over 1,055 page views, so most page views get no ad at all.
- Ad unit report: "Tool Page Inline" $0.04 / 73 imp, In Article 1 imp. Auto ads + Auto optimize ON, 0 page exclusions.
- US page RPM is $0.68. Much of the traffic is low-value or bot (see B-0037), which drags RPM down.
- ads.txt authorized, no policy issues. Payout needs a $10 balance.

## Outcomes
- A tool-page placement shown **right after the user gets their result** (near the output/download area, the moment they're looking), with reserved space so there's no layout shift.
- One responsive unit lower on the page, beside the how-to/FAQ content from B-0036, lazy-loaded so it's in view when rendered.
- Blog articles get an in-article unit after the first sections.
- **Page exclusions for Auto ads and no manual ads** on checkout, pricing/payment dialogs, login, profile, admin and API-key pages. Paid/logged-in plan users get whatever the plan promises; check that no ad shows if ad-free is a plan benefit.
- Don't fill containers that are hidden or collapsed (that's what kills Active View).
- Report: placements changed, CLS/LCP before/after. Target in 2–3 weeks: viewability above 50%, page RPM up, no Core Web Vitals regression.

## Constraints
- Never place ads next to buttons in a way that invites accidental clicks (AdSense policy), or inside the tool's working area.
- Keep tool UX first. Output must stay visible without scrolling past an ad.
- Changes in the AdSense console (Auto ads formats, exclusions) are written up for the owner to apply. Bots don't change console settings.

## Not in scope / do not decide
New ad networks; adding ads to checkout.

## Owner decisions needed
Apply the AdSense console page exclusions/format tweaks from your note.

## Source
owner
