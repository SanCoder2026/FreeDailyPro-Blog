Sent: 2026-10-31 5:25 PM ET

# RapidAPI: split the API into per-job products (P1, revenue)

**Intent:** Earn real revenue from RapidAPI, the largest API marketplace. Today we have 6 paid listings with 1 subscriber each.

**Why:** Buyers on RapidAPI search for a single job ("PDF API", "image compression API", "mortgage calculator API") and subscribe to focused products that have a clear free tier. Big catch-all bundles don't show up in those searches and are harder to trust. The Developer bot is already rewriting listing copy and examples (step 1). Your part is the product structure underneath.

**Outcome wanted:**
- Package the API into focused per-job products, each with its own base URL or path group, docs and OpenAPI: PDF pipeline (merge, compress, watermark, split; a pipeline call billed per step), Image optimize (resize, compress, convert to WebP), Text analyze (grammar, readability, case, counts, as one combined call), Mortgage & Loan calculators, Tax calculators, and Dev utilities (JWT, regex, UA, hash and similar).
- Each product must be complete and benchmark-competitive before it's listed (Rule 1). Don't package QR, OCR, TTS or speech until they're complete (B-API-38).
- Propose a free tier and paid tiers for each product, for Santosh to approve. Don't publish any pricing without his OK.
- The keys and the shared quota keep working across the direct API, MCP and RapidAPI.
- Fix the trust blockers first, because they affect conversion: B-API-14 (anon limit), B-API-36 (headers), B-API-45 (one response shape), B-API-41 (compress 422).

**Done when:** each product has its own OpenAPI file in the repo, ready to import to RapidAPI, plus a pricing proposal table for Santosh, reported back by ID.

Source: owner
