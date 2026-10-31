Sent: 2026-10-31 1:35 PM ET

# OWNER NOTE: Workflow products have their own pricing

Santosh's words: "$1 pass and $4.99 monthly are not applicable to any product in workflow product category. those product have there own pricing model."

**Intent:** Workflow-category products, such as the Book Writing Toolbox, use their own pricing. The $1 day pass and the $4.99/month plan do not cover them. The credits dialog that says the day pass and monthly plan don't include these products is correct; keep it.

**Why:** When the site suggests the $1 or $4.99 plans unlock a workflow product, buyers feel misled at checkout, which costs refunds and trust. The Book Toolbox packs work correctly in Stripe today: 1 download for $6.99, 3 for $17.99 and 10 for $49.99 (Testing Bot, ADDENDUM-ROW-87-STRIPE with screenshots).

**Outcome:**
1. Check /pricing, the blog posts and the tool pages, and make sure none says or implies the $1 day pass or the $4.99 monthly plan covers workflow products. Fix the copy once, at the source (template or one site-wide replace), then grep to confirm zero mismatches.
2. The EPUB tab shows a "$3.99 unlock" that doesn't exist at checkout. Either remove it, or make it match the packs. Report which you chose and why.
3. The earlier P1 (2026-10-31-1311-ET-P1-BRIEF-book-toolbox-plan-status.md) **still stands for admin entitlement**: the admin account must not see "(0 left)". Its earlier assumption that subscribers get clean downloads is replaced by this note: subscribers to the $1 or $4.99 plans do not get workflow products. They buy the packs.

Source: owner
