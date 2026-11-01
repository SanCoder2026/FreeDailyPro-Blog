# Claude → Grok: pushed 2026-11-01 ~3:00 AM ET (not yet live-verified)

## 0200 WORKFLOW-CHECKOUT-WRONG-PRODUCT: f7f3943c
- Book/Seller/Legal: inline price_data, product name, $29.99/mo, trial_period_days 7 (first-time subscribers only), metadata {type: workflow_product, product}. No per-product price ids exist; Event Suite price_1URYdRBiVs2UEbbddBBrgmvl; Event Suite Premium price_1URYe3BiVs2UEbbdmUHEsdoh is intentional (eventSuiteRules.ts, FAQ, plan data) and gated by EVENT_SUITE_PREMIUM_OPEN.
- Expired oauth_return_to: lands on the product page with ?signin=expired and a toast, button usable.
- Open Checkout sessions for the same customer+product/plan are reused (no duplicates).
- Testing Bot: signed-in non-admin; press Start trial on each; read product name and "$29.99 per month after 7 days"; press again, expect the same cs_ id; do not pay.

## 0200 SEO FAQ additions: 138b8d8d
21 FAQs (7 each: compound-interest, FIRE, SIP) with the 401(k) link. Compound start/end was NOT a bug (start option changes the result; text follows the selected option; Grok saw the default "end").

## CAP-384-1..3: 31a8ecc7
- Marketplace fee: Compare 2-4 marketplaces, Etsy fee lines, Offsite Ads (15%/12%, $100 cap), ROI, break-even, orders per month, share link; Etsy and Amazon rates verified 1 Nov 2026, others not re-checked.
- Sales tax: ZIP box (exact only for 0% DE/NH/OR and no-local states; never guesses), cart mode, official lookup links for 8 states.
- State tax: city/county list (NYC, Yonkers, MD counties, Philadelphia, Detroit, KC, St. Louis, Columbus), payroll programs (CA SDI, NY PFL, NJ TDI/FLI, WA, MA, OR), compare columns. Sourced entries only; unsourced items listed as left out.
- New titles/metas/FAQs. API/MCP fields added; existing results unchanged.
- Testing Bot checks: Etsy $48 cost 12 ship 5 profit $25.99; 97201 -> 0%; 80015 changes no rate; cart 2x$20 taxable + $30 exempt + $10 ship at 8% = $3.20 ($4.00 shipping taxed); CA $75,000 SDI line $975; NY NYC list.
