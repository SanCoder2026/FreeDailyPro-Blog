Sent: 2026-11-01 08:00 AM ET (Grok Orchestrator, hourly check)
Source: owner (Santosh's standing order: best-in-world, easy to use; never promote incomplete capabilities)

# API cycle 22: e-commerce seller workflow (B-API-114..118)
Full evidence: Developer / AI-Agent Channel audit cycle 22 (no deploy since c21; 1.4.0, 225 tools, 234 paths; metering exact, B-API-13 holds).

## Why this matters
Sellers are a strong demand segment ("shipping cost calculator API", "dimensional weight API", "Etsy SEO API", "product description generator API", "product schema JSON-LD"). Our Etsy rule checker and margin math are genuinely strong, but the rest of the seller job is thin, and in several places our own site tools are already ahead of the API. Some of these are live on paid RapidAPI listings, so wrong answers cost buyer trust.

## Priority order (please work top-down)
B-API-94 (markdown XSS, HIGH, still live) -> B-API-104 (silent CSV data loss) -> B-API-114 -> B-API-118 / B-API-110 -> B-API-115 -> B-API-117 -> B-API-116. Also: please mark "Mortgage & Home Finance" READY if B-API-103 is satisfied.

## B-API-114 Sales tax top-level fields must match the cart (P2, paid RapidAPI Finance)
- Intent: a checkout reading `result.taxAmount` charges the right tax.
- Why: with `items`, top-level taxAmount/total/net tax the whole subtotal (exempt lines included) and skip shipping. Input 2x$20 taxable + $30 exempt + $10 shipping @8% gives top-level 5.60 / 75.60 while `cart.tax` 3.20 / `cart.total` 83.20 is correct.
- Outcome: when `items` is present, top-level fields equal the cart values (or are omitted with a note); top-level steps describe the cart; REST = MCP.
- Done when: that input returns taxAmount 3.2, total 83.2; with shippingTaxable:true 4.0 / 84.0; non-cart calls unchanged.

## B-API-115 Shipping estimate at parity with our own Shipping Cost Estimator
- Intent: a seller sends box + weight and gets what the carrier will actually bill.
- Why: `/v1/business/shipping-estimate` silently drops lengthCm/widthCm/heightCm/carrier/toZip (200 billed, despite OpenAPI additionalProperties:false) and returns 10.10 when a 30x20x15 cm, 0.9 kg box bills at 1.8 kg dim weight. The site tool already does dim weight, divisors (139 in / 5000 cm), rounding, lb/in, packaging and markup. Competitors (Warp Dim Weight API, Leumas, SMKlog) lead with billable weight.
- Outcome: accept weight + weightUnit, length/width/height + dimUnit, dimDivisor or carrier presets, roundUp, ratePerUnit, base, optional rate table, packagingCost, markupPct, quantity; return actualWeight, dimWeight, billableWeight, billedBy, carrierCost, customerCharge, steps. Unknown keys -> free 400 naming the key. Old weightKg/ratePerKg/base keep working.
- Done when: the 30x20x15 / 0.9 kg / 6.5 per kg + 4.25 case returns dimWeight 1.8, billedBy "dim", and the site tool's default inputs give the same result as the site.

## B-API-116 Product description reads naturally and fits each marketplace (paid RapidAPI Text)
- Why: output included "Standout qualities include feels good in the hand." No platform targets, keywords, or title.
- Outcome: fix verb-led benefit phrasing; optional platform etsy|amazon|shopify|ebay with length targets; optional keywords[] woven in (reported as keywordsUsed); optional title. Still rule-based, no invented facts.
- Done when: our own grammar-check route finds 0 issues on that output; platform:"amazon" gives exactly 5 bullets each <= 500 chars.

## B-API-117 Etsy check returns a listing that actually passes
- Why: `cleaned` still contains "-pottery" and a 32-char tag, so pasting it yields an invalid listing. Competitors (Seerxo, Apify Listing SEO Auditor) return a fixed title + 13 valid tags.
- Outcome: `fixed.title` (banned chars removed, <= 140 at a word boundary) and `fixed.tags` (max 13, <= 20 chars, no leading -/', deduped, reported kept/changed/dropped); document `cleaned` as de-dup only; optional amazon/ebay rule sets; MCP mirrors.
- Done when: re-checking `fixed` through the same route returns 0 errors.

## B-API-118 Seller calculator validation + target price (paid RapidAPI Business)
- Why: product-margin with price 0 returns 200 billed with marginPct 0 (undefined); unknown fields are billed across business/* routes.
- Outcome: impossible inputs and unknown keys -> free 400 naming the field; add targetMarginPct / targetMarkupPct -> price; optional fees for after-fee margin.
- Done when: price 0 -> 400 at 0 cost; cost 12 + targetMarginPct 60 -> price 30.00.

## Updates to existing items
- B-API-58 (Product schema): `seo/schema` rejects type "product"; our site Schema Markup Generator already offers Product/LocalBusiness/Recipe. Include Offer + shippingDetails + hasMerchantReturnPolicy (Google merchant listing).
- B-API-59 (meta tags): `og:image`/`twitter:image` accept `javascript:alert(1)`; reject non-http(s) URLs; add product:price:amount/currency for type product.
- B-API-87 (hashtags): max 10 returned only the 3 input keywords.

## Not promoted until done
Shipping/dim-weight claims (115), product schema (58), sales-tax top-level with items (114), Etsy "fixer" (117), hashtag research (87). An "E-commerce Seller API" job-named listing is on hold until 114, 115, 117 and 58 land; please tell us when an `ecommerce` group is READY.
