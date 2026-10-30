# B-0030 Launch the 20 wave-1 focused listings on RapidAPI (S3, owner-approved)

**Priority:** P1
**Estimated effort:** ~90 after S1/S2 min

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

Context: owner-approved Oct 29 (split-listings plan, items S1–S7). The evidence is in the API/MCP bot's analysis: our 7 RapidAPI / 3 API.market bundles have 0 popularity badges and rank deep or not at all (19 of 29 keywords missing; pdf merge #51, image resize #44, loan #26; absent for 'hash generator'). Single-purpose titles take the top spots on nearly every query (APIVerve 387 focused listings, API-Ninjas 101, magicapi 671 on API.market). The ranked list is `top-100-single-purpose-apis.csv` (title, category, tags, endpoints, marketplaces, wave). It is in this folder as `2026-10-29-B-0028-top-100-single-purpose-apis.csv`; rows 1–20 are wave 1. Every endpoint was checked against the live `/openapi.json`.

## Intent
Put 20 focused, keyword-first listings on RapidAPI so we start ranking for the queries where buyers actually search.

## Why
This is the core bet of the plan, and RapidAPI is the top-priority marketplace. Low-competition queries (pdf redact 11 results, hash generator 18, jwt 23, markdown to pptx 6) can reach the top 5 with a focused title.

## Outcomes
- All 20 wave-1 listings (from S1 output) are public.
- **Keep the existing 6 bundle listings** as they are. The focused listings are added alongside them and link back to them.
- **Default pricing:** use the existing per-product plan templates. The image/media free tier is at least 500 calls. No price increases until there's traction.

## Acceptance criteria
- Gate: the RapidAPI first call works (sample code and spec fix, "Traction F1"). Don't launch onto a broken first call.
- All 20 are public. A test-subscription call on each returns 200, with status per listing in your report.
- Titles, tags and categories match listings.yaml.

## Suggested direction
Use PAPI or the GitHub Action if S2 says yes. Otherwise the owner does the clicks from `copy.md`, so list those steps under Owner actions.

## Not in scope / do not decide
Deleting or privatizing the legacy listing (owner decision pending). Price changes.

## Owner decisions needed
None for the launch itself. Any Studio-only steps go under Owner actions.

## Source
owner
