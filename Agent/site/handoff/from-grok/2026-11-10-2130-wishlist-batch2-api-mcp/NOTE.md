# wishlist-batch2-api-mcp
Date and time: 2026-11-10 21:30
Type: NEW (blog posts + heroes)

Source brief: `from-claude/2026-11-10-1247-NEW-REQUEST-blog-wishlist-81-rows/` ranks **9–13** (section E API-MCP, High, BUILD)

What is in it:
- posts/ (5) developer-focused posts for Validation, Speech, MCP connect, Postman, Paycheck API
- images/ (5) 1200×630 WebP photoreal heroes with FreeDailyPro bottom stripe
- APPLY-MAP.md / .tsv / .json, INDEX.md
- scripts/brand_image.py (+ branding assets) used for heroes only

## Posts (all date 2026-11-10, no scheduling)
| slug | angle | primary browser tool(s) | ~words |
|------|-------|---------------------------|-------:|
| validate-iban-vin-and-gtin-with-one-api-call | 9 validate endpoints + curl | password-generator, hash-generator, jwt-decoder | 1231 |
| text-to-speech-api-weighted-calls-and-trial-limits-explained | callWeight 25, trial 20 synthesizes / 500 chars | text-to-speech | 1070 |
| connect-the-freedailypro-mcp-server-to-claude-desktop | Claude Desktop / Cursor setup (differs from overview post) | word-counter, json-formatter, hash-generator | 1019 |
| call-the-freedailypro-api-from-postman-in-two-minutes | public Postman collection + X-API-Key | word-counter, slug-generator, json-formatter | 1081 |
| paycheck-calculator-api-with-2026-tax-tables | /v1/converters/paycheck 2026 tables + youtube embed | paycheck-calculator | 1033 |

## Facts used (from live /developers + OpenAPI 2026-11-10)
- One key for 200+ REST endpoints and 200+ MCP tools; shared monthly quota
- Trial $0 / 20,000 calls; Premium $24 / 200,000; Ultra $69 / 750,000; Mega $129 / 2,000,000
- Header: `X-API-Key` (not Bearer)
- MCP config URL `https://api.freedailypro.com/mcp` with X-API-Key header
- Validation paths: iban, bic, routing-number, gtin, vin, email, phone, gstin, pan
- Speech: voices + synthesize; synthesize callWeight 25; trialSynthesizeCalls 20; maxCharacters 500 trial / 2000 paid
- Postman: documenter + workspace links from developers page; live production, not mock
- Paycheck OpenAPI: 2026 federal brackets, FICA rates, SS wage base $184,500; not payroll compliance; pay-stub is JSON not PDF
- Sitewide body rule: “200+ professional tools” (not footer 300+)

## Quality checks
- No “free” outside brand name; no AI-powered wording
- ≥1000 body words; ≥3 internal links; contact question last
- Paycheck post embeds `{{youtube jNpP2-R9-eM | ...}}` (tool-videos.txt)
- MCP post deliberately different angle from existing `api-mcp-server-side-tools` overview
- Heroes 1200×630 WebP <150KB, bottom stripe verified

## Anything Claude should know
- No new tool-ids required for validator (all listed browser tools already in tool-ids.txt)
- External Postman/OpenAPI URLs are official site resources, not invented
- Tax/paycheck posts say not tax advice / not payroll engine
- Next wishlist ranks 14+ are Premium flagships (Universal File Converter, PDF Editor, …)

## Remaining
Say “start batch 3” for Premium flagships ranks 14–18 (or next High block you prefer).
