# Agent B done: API documents and calculators (pushed, NOT yet live-verified)

Commits on main: d856730e (job-experience), f3d41320 (cover letter), offer letter/resume outline (c28aa5db regenerates openapi), ed063598 (citations/paper-format), 087f758c (sales tax, marketplace fee).

## Needs Santosh
- Nothing new.

## What changed
- job-experience: with otherJobs, top-level years/months/days/totalMonths/label = merged total (overlap counted once); adds scope, rule, firstJob, history.
- cover letter: grammar, strict schema, bad date -> 422, optional .docx via includeDocx. Offer letter: shared builder, bad salary/date/period -> 422, past dates = warnings, optional .docx.
- citation: website/book/journal/chapter in APA7, MLA9, Chicago (default 17; send chicagoEdition "18" for 18). paper-format returns structured guidance per style or all. Both responses: `result` is now an object (shape change).
- sales-tax with items: top-level taxAmount/total/net/steps come from the cart.
- marketplace-fee with compare and no feePct: no top-level fee/net/steps, a note instead; new `assumptions` object.
- Page vs API $28.91: math identical; page pre-fills shipping cost 4.50, return rate 5%, return postage 4.50, API treats omitted as 0 (documented). tests/marketplaceParity.test.ts confirms 28.91 with page defaults.

## Not reproduced
Etsy margin 49.21 vs 49.23: likely profit.marginPct (your feePct) vs comparison[].marginPct (Etsy preset rates). Please send the exact request that gave 49.21.

## Live checks
- sales-tax: omit amount, send items (1 taxable, 1 exempt) + discount + shipping; top-level taxAmount/total == cart.tax/cart.total.
- marketplace-fee: price 48, cost 12, shippingCharged 5, shippingCost 4.5, returnPct 5, returnPostage 4.5, compare Etsy+eBay -> Etsy expectedProfit 28.91. compare only -> no top-level fee/net.
- citation 4 source types x 3 styles; paper-format style apa.
- cover-letter / offer-letter-draft includeDocx true; bad salary/date -> 422.
- job-experience with overlapping otherJobs: top-level == merged total.
- Known: documents.test.ts fails on 4 live-data routes (pre-existing); units audit item was Agent A's (fixed).
