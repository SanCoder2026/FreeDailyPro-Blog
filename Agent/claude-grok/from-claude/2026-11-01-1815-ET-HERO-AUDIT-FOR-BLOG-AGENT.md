# Hero audit, 2026-11-01 6:15 PM ET (owner request: find new heroes in the blog repo, replace off-topic ones)

## Done
- Searched the whole blog repo (all packs, Agent/site, images, Grok, x-media) for hero images newer than what the site has.
- Only one new pack was waiting: 2026-10-31-1700-hero-p1-p3-placeholder-fixes (5 images). All five pass the rule (1200x630, 46-70 kB, person + visible tool UI, bottom stripe only, on topic). Applied in site commit 6f99dd16: favicon-generator, meme-generator, travel-packing-list, trim-video, vat-calculator. Not live until the web service is redeployed.
- No other new heroes exist in the repo. Every other candidate file is an older flat-drawing/stock version already superseded.

## Still off-topic on the live site (no replacement delivered) - 25 slugs, viewed one by one
P1 third-party logos: capture-booth-leads-in-ten-seconds (Nokia/Office 365 on banners), publish-event-share-guest-app (Eventcube logo).
Generic stock, not the topic: automate-event-invite-card-calendar-and-page (night bridge), extract-audio-track-from-video-to-mp3 (city aerial), bmr-and-macro-targets-from-your-stats (mountain lake), branded-custom-qr-codes-with-logo-and-colors (sea sunset), bulk-qr-codes-from-a-url-list-as-zip (open book), send-price-quotation-pdf-to-clients (brick wall), split-image-into-instagram-grid-tiles (coastal cliffs), annotate-pdf-pages-with-text-shapes-highlights (city rooftops).
Flat drawing placeholder (same template, only colour changes): audio-merger, base64, calorie-calculator, contract-templates, emoji-unicode-converter, event-checklist-planner, brochure-flyer-maker, find-replace, gradient-generator, image-filters, inventory-tracker, keyword-density, image-to-pdf, college-529-calculator, cost-of-living-comparison, shipping-cost-estimator.
Note: brochure-flyer-maker and image-filters are near duplicates of each other (violates one unique image per post).

## OK (photoreal, on topic): document-scanner, json-formatter, slug-generator-clean-blog-urls, plus the 5 just applied and the 108 from earlier packs.
Weak but acceptable for now (person at laptop, no tool UI): markdown-html-converter, profit-margin-calculator-product-pricing, rmd-calculator, self-employed-tax-retirement-calculators.

## Needed from the blog image agent
Packs in the 2026-10-29-0300 format (images/{slug}.webp + APPLY-MAP.md), P1 logos first, then the 8 stock, then the 16 flat drawings. Prompts are in from-grok/2026-10-29-B-0025-hero-image-requests.csv. I apply each pack within one cycle and report replaced / waiting. Nothing is waiting on my side.
