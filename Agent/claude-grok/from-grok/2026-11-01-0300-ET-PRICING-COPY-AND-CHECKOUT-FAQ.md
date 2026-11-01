Sent: 2026-11-01 03:00 EST (Grok Orchestrator)

# /pricing copy and checkout FAQ fixes (no price changes)

## Intent
Make /pricing clear and consistent for every workflow product, so buyers know exactly what they pay and how they sign in.

## Why
The intro line and meta description leave out Book, the Book card is formatted differently, the team-plan note is incomplete, and checkout wording confuses guest buyers. Prices stay the same.

## Outcome
Apply the brief below and meet its 7 acceptance checks.

---

# Claude brief: /pricing Book card parity + checkout-copy clarity

Evidence gathered Nov 1, 2026, about 3:10 AM ET. Read-only: I used curl on the live https://www.freedailypro.com/pricing (prerendered HTML) and its chunks (PricingPage-CevcrSOb.js, WorkflowTrialButton-eLFIsXP-.js, workflowCta-BymOs9RW.js, suitePlans-CeYoN8tm.js, index-CNezZ27X.js). Nothing on the site was changed. Sources: QA-389 (cycles/next-morning-report.md, line 60) and FRICTION.md in this folder.

## How to work with us
You're a partner, not an order-taker. Read the real code first, then tell us what you think the problem is. Push back where our evidence is stale or the idea is weak. Pick the implementation that fits how /pricing, WorkflowTrialButton and the FAQ/JSON-LD already work. The checks at the end describe what "done" means. They are not a recipe.

## Intent
A buyer on /pricing should see the Book Writing Toolbox as a first-class Workflow Product, just like Seller Studio and Legal Production Desk: the same card, the same price line, and the same "Start 7-day trial · $29.99/mo" path to a Stripe session named for Book. Every buyer, whether they use guest checkout or sign in first, should also know before paying how they'll get back into what they bought.

## Why (evidence)
1. **The intro line leaves out Book (CONFIRMED live).** The `<p>` under the `<h1>Simple pricing</h1>` and the `<meta name="description">` both say:
   > "…Event Suite, Seller Studio and Legal Production Desk from $29.99 a month…"

   Book is also $29.99/mo with a 7-day trial, so this hides one of our four workflow products on the page that sells them. Related: the org-plans note (premium tier) says "Workflow Products (Event Suite, Book Writing Toolbox) are not included." That one leaves out Seller and Legal. It's the same kind of drift in the other direction.
2. **The Book card's formatting differs (CONFIRMED in code).** The three cards share one map inside `[data-testid="pricing-workflow-desks"]` (`pricing-${slug}` cards). The body text branches on `t==="book-writing-toolbox"`:
   - Book: `` `Book Writing Toolbox: $${monthlyUsd}/month. ${I}-day trial. Everything to write, format and export your book. Previews are watermarked, and clean files download on your plan. Cancel anytime.` ``
   - Seller/Legal: `` `${tagline} $${monthlyUsd} per month, billed monthly, with a ${I}-day trial. Cancel any time; your plan continues to the end of the paid month.` ``

   Book repeats its own name (the h2 already says "Workflow Products: Book Writing Toolbox"), ignores its tagline ("Write your book and get it ready to publish." in suitePlans), uses "/month" instead of "per month, billed monthly", says "anytime" instead of "any time", and leaves out the end-of-paid-month line. That reads like a different product tier.
3. **Book card has no trial button: NOT reproduced now.** QA-389 reported it, but the live prerendered HTML has
   `data-testid="pricing-book-writing-toolbox-subscribe" data-cta="trial"` → "Start 7-day trial · $29.99/mo", rendered by the same `WorkflowTrialButton` as Seller and Legal. It was probably fixed by f7f3943c (per-product checkout) after QA-389 ran. Please confirm it shows in a real signed-out and signed-in browser, including when `workflowProduct.status` loads slowly or errors. If the button disappears in any state (for example `data-cta="open"` for an entitled user is expected, but a blank space isn't), fix that state. If you can't reproduce it, say so and don't change it.
4. **Checkout copy friction (FRICTION.md).**
   - The day-pass/monthly line (`b2`): "Pay securely with Stripe. No sign-in needed, just your email." It never says how a guest gets back in. Sign-in on the site is Google-only, so guests may think their purchase is lost.
   - The "How does checkout work?" FAQ (`L0`/`F0`, on /pricing and /developers, plus the FAQPage JSON-LD) doesn't say "Google" and calls the renewing $4.99/mo plan a "monthly pass".

## Outcomes (what done looks like)
- The Book card can't be told apart from the Seller and Legal cards in structure, tone and price line. Only the name, tagline and link differ.
- The intro, the meta description and the org note list all four workflow products correctly. The intro lists the three $29.99 desks plus Event Suite.
- The Book button sends signed-out users through sign-in with `autoBuy=workflow:book-writing-toolbox` (the same `S2`/`yk` path as the others), then to a Stripe Checkout session named for Book at $29.99/mo with a 7-day trial.
- Guests know their access comes through an emailed sign-in link. Sign-in-first buyers know it's Google. Monthly buyers know it renews.

## Suggested direction (use your judgment)
- Drop the Book special case and let all three cards use the `${tagline} $${monthlyUsd} per month, billed monthly, with a ${I}-day trial. Cancel any time; your plan continues to the end of the paid month.` template. If the watermark/clean-download point matters, add it as one feature line for every product or in the tagline, not as a one-off branch.
- Intro copy, keeping existing tone (paste-ready):
  > "Professional Tools from $1 a day or $4.99 a month. Premium Applications from $3 a day or $9.99 a month. Workflow Products (Book Writing Toolbox, Event Suite, Seller Studio and Legal Production Desk) from $29.99 a month, each with a 7-day trial. Teams, APIs and custom software are below."

  Mirror it in the meta description. Better still, build both from the `Ss` list so they can't drift again.
- Org note (premium tier): "Workflow Products (Book Writing Toolbox, Event Suite, Seller Studio and Legal Production Desk) are not included." Consider reusing the existing `Aa` constant.
- Day-pass line `b2` (paste-ready):
  > "Pay securely with Stripe using just your email, with no account needed. We email you a sign-in link for your access."
- "How does checkout work?" `F0` (paste-ready; update the FAQPage JSON-LD on /pricing and /developers from the same source string):
  > "Workflow Products, API plans and organization seats: sign in with Google first so the plan is attached to your account, then pay on Stripe's secure checkout page. Day Pass and Monthly for Professional Tools and Premium Applications: no account needed. Pay on Stripe with your email and we email you a sign-in link for your access. Monthly renews each month, and you can cancel any time from your account page."

## Constraints
- **Book's only price is $29.99/mo with a 7-day trial.** Don't bring back the pack, single-book or $3.99/$6.99/$17.99/$49.99 text for Book. Event Suite Premium at $49.99 is a separate open question for Santosh, so leave it as is.
- Use "Trial", never "free tier". Don't over-emphasize "free".
- Don't add or repeat any claim that the keyless API limit is enforced. It's currently NOT enforced: cycle 17 served 20 of 20 keyless calls with no 429.
- Counts use multiples of 50 with a plus sign (for example "200+" or "300+"). Don't add new exact counts.
- No Stripe dashboard or price changes, and no new checkout endpoints. Reuse WorkflowTrialButton and the existing autoBuy flow.
- The "sign-in link" promise must stay true. If guest access isn't actually delivered by emailed link, tell us, and don't ship that wording.

## Process
Inspect → restate the problem in your own words (including whether #3 still reproduces) → propose → implement → verify against the checks below → report the commit and anything you disagreed with.

## Acceptance checks
1. On /pricing, signed out: `[data-testid="pricing-book-writing-toolbox"]`, `pricing-seller-studio` and `pricing-legal-production-desk` have the same DOM structure (h2 → body p → button row → `checkout-note`) and the same body template, and they look the same at 375px and 1280px widths.
2. `[data-testid="pricing-book-writing-toolbox-subscribe"]` exists with `data-cta="trial"` and the text "Start 7-day trial · $29.99/mo". Signed out, clicking it goes to sign-in with a return URL containing `autoBuy=workflow:book-writing-toolbox`.
3. After sign-in, checkout resumes on its own and opens a Stripe Checkout session whose line item is named for **Book Writing Toolbox** (not "Event Suite (monthly)") at **$29.99/month** with a **7-day trial**. The same goes for Seller Studio and Legal Production Desk, each under its own name. (Testing Bot can't complete this because it never pays and needs a non-admin login. Santosh or a non-admin box session must click through.)
4. The intro `<p>` and the `<meta name="description">` name all four workflow products. The org premium note names all four.
5. Grep of the built /pricing chunk finds no "Cancel anytime." Book-only branch, no "free tier", no keyless-limit-enforced claim, and no Book price other than 29.99.
6. The `b2` and `F0` text renders as above, and the FAQPage JSON-LD on /pricing and /developers matches the visible FAQ answer word for word.
7. A signed-in, entitled Book user sees "Open"/"Manage subscription" in place of the trial button, never an empty space.

## Test note: unverified, needs a real buyer
Can a **guest Monthly** buyer (paid with just an email, no Google account) actually cancel "from your account page" after signing in through the emailed link? The new FAQ copy promises this. Testing Bot can't check it because it never pays. Santosh or a real subscriber needs to: buy Monthly as a guest, then open the emailed link in a fresh browser. Check that /account shows the subscription and that "Manage subscription" opens the Stripe portal with Cancel. If any step fails, change the FAQ to say how to cancel (for example "use the link in your Stripe receipt email") or fix the account page before shipping the copy.


Source: owner
