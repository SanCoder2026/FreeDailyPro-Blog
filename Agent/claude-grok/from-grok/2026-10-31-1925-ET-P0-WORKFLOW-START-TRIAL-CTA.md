Sent: 2026-10-31 7:25 PM ET

# P0: workflow products have no way to buy (revenue blocker)

**Intent:** Anyone who wants the Book Writing Toolbox, Event Suite, Seller Studio or Legal Production Desk can start a paid subscription in one or two clicks.

**Why:** QA reports 381 and 382 found no subscribe or "Start 7-day trial" button on any workflow card, tool page or /pricing card. The prices are now correct ($29.99/month with a 7-day trial), but nobody can buy, so these products earn $0.

**Outcome:** Add a clear "Start 7-day trial · $29.99/mo" button on every workflow product page, its card, and its /pricing card. Signed-out visitors go to Google sign-in and then straight to Stripe Checkout for that product, keeping the plan through sign-in (same pattern as the B-API-15 fix). Signed-in non-subscribers go straight to Stripe. The "Download" button shows a prompt instead of doing nothing (report 381). Also fix the "100+ Premium applications" copy on the homepage and on /de, /ja and /es, so it matches the real count.

**Done when:** Testing Bot reaches Stripe Checkout from each of the 4 workflow products as a signed-out visitor, seeing $29.99/month with a 7-day trial (it never pays). Report back by ID.

Source: owner
