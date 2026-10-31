Sent: 2026-10-31 13:16 ET
# Row 87 addendum: Book Writing Toolbox checkout (no payment made)
Method: tested in the box browser at 13:14–13:16 ET on /tool/book-writing-toolbox. The header showed "Sign In", so the admin session was not confirmed. Nothing was paid and no card was entered.

## Findings
- The "Download (0 left)" button opens a "Get download credits" dialog. There is no $3.99 unlock or 24-hour pass in that dialog.
- All three options go to checkout.stripe.com, with the merchant shown as FreeDailyPro. The price is shown in USD, no tax line is shown, and there is a promotion code option:
  - "Book Writing Toolbox - 1 Download": $6.99 (screenshot row87-stripe-checkout.png)
  - "Book Writing Toolbox - 3 Downloads": $17.99 (screenshot row87-stripe-3.png)
  - "Book Writing Toolbox - 10 Downloads": $49.99 (screenshot row87-stripe-10.png)
- Result: PASS on Stripe showing the right product and price for the 1, 3 and 10 download packs.

## Gaps for Claude
1. The $3.99 24-hour Book Toolbox pass, which appears in earlier owner pricing notes, is not offered in the credits dialog. Either add it or remove it from the pricing and copy.
2. The dialog says "the $1 day pass and the monthly plan don't include them". Check that this wording matches /pricing ($1 a day for Professional Tools).
3. The admin entitlement is still unresolved: "Download (0 left)" shows even though the profile says "Admin — unlimited". The EPUB 3 metadata and IngramSpark margin checks stay blocked until Claude's plan-status fix is in.
