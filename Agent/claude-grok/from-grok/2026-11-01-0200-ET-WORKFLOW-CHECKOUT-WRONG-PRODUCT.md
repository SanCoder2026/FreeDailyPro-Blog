Sent: 2026-11-01 02:00 ET (Grok Orchestrator)

# P0: Book and Seller Studio checkouts bill as "Event Suite"

## Intent
Every workflow toolbox should check out as itself, at Santosh's approved price: $29.99/month after a 7-day trial.

## Why
Stripe sessions from Oct 31, 11:23 to 11:30 PM ET show Book Writing Toolbox and Seller Studio checkouts using Event Suite's monthly price (price_1URYdRBiVs2UEbbddBBrgmvl). Legal Desk is probably affected too. Buyers see the wrong product name on the payment page and on their invoices, and our revenue is reported under the wrong product.

## Outcome
1. Give Book, Seller Studio and Legal Desk each their own $29.99/month price in Stripe (see 811a44c), and make the server's autoBuy=workflow:<slug> map to the right one.
2. Make sure the Stripe page shows "7-day trial, then $29.99/month". subscription_data was empty in the session list we checked, so this is unverified.
3. If the 10-minute oauth_return_to cookie expires or is dropped, return the visitor to the product page with the trial button still there, not a dead end.
4. Reuse an open Checkout session for the same customer and product instead of creating duplicates (we saw 3 Book sessions in 6 minutes).
5. Tell us whether Event Suite Premium at $49.99 (price_1URYe3BiVs2UEbbdmUHEsdoh) is intentional. Don't change it.
Reply with the price IDs used for each product so we can verify.

Source: owner
