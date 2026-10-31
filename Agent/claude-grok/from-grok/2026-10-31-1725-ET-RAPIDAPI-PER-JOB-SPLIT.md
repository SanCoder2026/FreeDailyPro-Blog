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

---
**Update 5:35 PM ET (owner):** Build on the splits you've already done. Don't start over.
- Live today on RapidAPI: PDF Toolkit (13 endpoints), Image/Audio/Video (22), Finance/Tax/Health Calculator (57), Text & Developer Utilities (56), Book Publishing (10), Business Document (26). Plus the Book x3 split in the spec (1edfe28) and the ApyHub drafts.
- Already briefed, and STATUS.md lists them as not started: B-0028 to B-0034 (the listings.yaml generator, Rapid Platform API check, wave-1 launch, Postman sync, API.market copy, per-API /developers pages, weekly rank report) and B-0039/B-0040a/b (task-level split pattern plus specs for the 20 wave-1 tools).
- Order: (1) keep the 6 live listings as they are while the Developer bot rewrites their copy, tags and examples; (2) split the two oversized bundles first, Calculator (57) into Mortgage & Loan and Tax, and Text & Dev (56) into Text analyze and Dev utilities; (3) then run the B-0028/B-0039 generator and wave-1 per-job listings. The new items in this brief (PDF pipeline, image optimize) only fill gaps those don't cover.
- Report back against these existing IDs, not new ones.
