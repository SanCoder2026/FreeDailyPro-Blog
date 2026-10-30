# B-0027 Checkout flow improvements (owner-approved)

**Priority:** P1
**Estimated effort:** ~90 min

## Goal / why
Testing Bot's Stripe audit (Oct 29) found every paid path works up to a gate, but extra steps and confusing labels before Stripe lose buyers. Owner approved these changes to shorten the path to payment without losing the account/email link we need.

## What to change
1. **Monthly plans (Professional $4.99, Premium $9.99):** remove the pre-checkout email/sign-in step for signed-out users. Send them straight to Stripe Checkout, which collects the email. On successful payment (Stripe webhook), create or link the account by that email, attach the subscription, and email a magic sign-in link. Signed-in users keep the current flow, with their email prefilled.
2. **Day Pass ($1 / $3):** keep guest checkout. Change the card label "Sign in to buy" to "Buy Day Pass" so it matches the actual flow.
3. **API plans:** keep sign-in (the key must belong to a known email). Add a clear line on or under the Upgrade button, e.g. "Sign in with Google to create your API key", so the jump to Google isn't a surprise.
4. **Mobile overlap:** while a payment or checkout dialog is open, suppress the privacy pop-up and the EEA/UK cookie banner. Show them again after the dialog closes. The cookie banner must still be shown before any non-essential cookies load.
5. `/account` and `/workflows` return 404. Redirect `/account` to `/profile` and `/workflows` to the workflow products page (or the right existing page).

## Acceptance criteria
- A signed-out user reaches checkout.stripe.com from a monthly plan in one click. After test-mode payment, the account exists with an active subscription and the magic link is sent.
- Day Pass cards read "Buy Day Pass".
- The API Upgrade button explains the Google sign-in.
- On 390px width, no banner or pop-up overlaps the payment dialog.
- `/account` and `/workflows` no longer 404.
- Verified live, with status per item in the from-claude report.

## Not in scope / do not decide
Prices, plans, trial limits, Stripe account settings, real charges.

## Owner decisions needed
None. All approved Oct 29 evening.

## Source
owner
