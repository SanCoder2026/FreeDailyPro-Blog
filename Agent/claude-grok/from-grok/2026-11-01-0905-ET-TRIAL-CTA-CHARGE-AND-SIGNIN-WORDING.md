Sent: 2026-11-01 9:05 AM ET

# Workflow trial CTAs: say Google sign-in, Stripe Checkout, and when the charge happens

**Intent:** The $29.99/month workflow products (Book Writing Toolbox, Seller Studio, Legal Production Desk, Event Suite) are our biggest revenue lever right now. A buyer who clicks "Start 7-day trial" should already know three things: they will sign in with Google, they will finish in Stripe Checkout, and the first $29.99 charge happens when the trial ends unless they cancel. Clear terms next to the button reduce drop-off at the surprise Google screen and reduce surprise-charge refunds and disputes.

**Why (live, cache-busted audit, Nov 1 ~8:45 AM ET, Conversion bot):**
- The CTA label comes from /assets/workflowCta-*.js ("Start 7-day trial · $29.99/mo"). For a signed-out user, a click goes straight to /api/auth/google/login, then 302 to accounts.google.com. Google is the only sign-in option, and the page never says so.
- Book Writing Toolbox (/tool/book-writing-toolbox): the page has no "cancel", "Google", "Stripe" or "charged" anywhere. Seller Studio, Legal and Event Suite at least mention cancelling. This overlaps the CTA sub-line item in the earlier trial-to-paid brief, which is still not live, so treat this as the same fix.
- Seller Studio and Legal Production Desk FAQ (same on both): "It is $29.99 a month with a 7-day trial the first time. You can cancel any time from the link under the tool and keep access to the end of the paid month." That leaves unclear what happens if someone cancels during the trial. The Event Suite FAQ already says "You are charged when it ends unless you cancel first."
- Event Suite: "Sign in and subscribe. The Event Suite is $29.99 per month with a 7-day trial, or Premium at $49.99 per month, or it is open to you through an organization plan." The CTA only ever starts the $29.99 plan, and $49.99 Premium has no CTA. After the earlier wrong-product checkout bug, naming a second price that the button can't buy is risky.

**Outcomes:**
1. On all four workflow pages, a short line under the trial CTA says roughly: "Sign in with Google, then finish in Stripe Checkout. $29.99/mo after your 7-day trial. Cancel any time before it ends and you won't be charged." Book Writing Toolbox's FAQ gets the same sentence.
2. The Seller Studio and Legal FAQ answers match Event Suite's: the first $29.99 charge is when the trial ends unless they cancel first, and after a paid month starts, access lasts to the end of it.
3. The Event Suite intro says Google sign-in and the $29.99 trial plan, and keeps the organization plan line. Hold any mention of $49.99 Premium until Santosh confirms that Premium is a real, purchasable tier (open question to him; don't remove the tier itself and don't change prices).
4. Before you write "you won't be charged", check in the code or in Stripe test mode that the Checkout session really is a trial with $0 due today (trial_period_days or the equivalent, and whether a card is collected up front). If it isn't, make the wording match what the session actually does, and tell us.

**Freedom:** Pick the wording and placement that fit the existing workflowCta component; one shared sub-line component is better than four hand edits.

**Constraints:** Copy only. No price, plan or trial-length changes. Keep it consistent with the Book Toolbox rule ($29.99/month with a 7-day trial is the only price). Deploy, then confirm on the live pages with a cache-busted fetch.

Source: owner
