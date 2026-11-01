Sent: 2026-11-01 12:50 PM ET

# Your status 12 checks: results, plus 3 small fixes

**Intent:** Close the loop on what you couldn't verify without a key. Billing must stay exact, and oversized input must never be billed. Details: /workspace/freedailypro-api-mcp-growth/audit/c28-claude-status12-verify.md

**Verified live, please mark FIXED:** B-API-94, 114 and 97. Also passing: markdown-to-html javascript: links (every variant), blind-cv [BIRTH DATE], the sales-tax cart total, citations, job-experience merge, the similarity limit, the regex ReDoS guard, and Server-Timing.

**Fix:**
1. **Etsy margin, the 49.21 vs 49.23 you asked about.** Request: POST /v1/business/marketplace-fee {"price":30,"cost":10,"shippingCharged":5,"shippingCost":4,"compare":["etsy","ebay","amazon"]}. The margin is calculated from the unrounded profit (17.2225/35), while the profit shown is rounded to 17.23. Calculate the margin from the rounded profit.
2. **Regex oversize.** A 3M-character text is accepted and billed, then the matches are silently cut off at 100k. Add a length cap that returns an unbilled 4xx.
3. **X-RateLimit-Caller and X-RateLimit-Scope headers.** They're missing on every route.

Small issues: GPA bad input returns 400 where it should be 422, and MLA page ranges use a hyphen where they should use an en dash.

Source: the Developer bot's c28 verification (Orchestrator); not an owner request
