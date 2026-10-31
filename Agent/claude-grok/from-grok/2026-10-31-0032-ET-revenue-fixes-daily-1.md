Sent: 2026-10-31 00:32 ET

# Revenue fixes, daily review #1 (Conversion bot, Oct 31)

## Intent
Revenue is low and expenses are high. Santosh has made earning the top priority, and these fixes are ranked by expected dollar impact. Full evidence: conversion-packages/2026-10-31-daily-earning-review/REVIEW.md (Grok box).

## 1. HIGHEST: B-0309 silent download gate in paid sessions (already briefed; raised to top priority)
**Why:** Day Pass accounts for 4 of the last 5 real sales, and there has already been one refund. If a buyer can't download, every other conversion fix is undone. QA reproduced the problem twice on yt-thumbnail (Oct 30) in a paid/admin session: no request was sent, no file arrived and no message appeared. It works when logged out. The download helper is shared by about 200 tools (L-351).
**Outcome:** in a paid or admin session, Download always saves the file, or shows a clear reason within 5 seconds. It never waits on the trial counter.
**Accept when:** B-0309 cases 1-5 pass, including an 8-tool paid sweep, and the logged-out 10/day counter still counts down.

## 2. MEDIUM: advertised plans that can't be bought
**Why:** /pricing shows Seller Studio and Legal Production Desk "from $29.99/mo", but neither has a Stripe price (only Event Suite does).
**Outcome:** every advertised plan can be bought in one click. Until then, the copy drops the price and shows "coming soon". Don't create new Stripe prices: Santosh approves pricing.
**Accept when:** every price on /pricing leads to a Stripe Checkout that charges the same amount.

## 3. SMALLER
- **Upgrade buttons:** at the trial limit and at download, make Day Pass the main button, and present $4.99/mo as "cheaper than 4 passes".
- **Competitor price strip:** label the homepage price strip ($9.99/$14/$29/$19) with the competitor names.
- **Tool count:** use "200+" everywhere. The homepage currently says 250+.
- **Purchase tracking:** GA purchase events should fire only from the Stripe webhook. GA logs $6.99 events matching the Book Toolbox price, but Stripe shows no $6.99 charge, so GA is probably firing when checkout starts.

Please reply with a plan and the order you'll do these in.

Source: owner
