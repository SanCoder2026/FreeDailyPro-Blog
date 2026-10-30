# B-0032 API.market: paste copy for 5 focused products (S5, owner-approved)

**Priority:** P2
**Estimated effort:** ~30 min

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

Context: owner-approved Oct 29 (split-listings plan, items S1–S7). The evidence is in the API/MCP bot's analysis: our 7 RapidAPI / 3 API.market bundles have 0 popularity badges and rank deep or not at all (19 of 29 keywords missing; pdf merge #51, image resize #44, loan #26; absent for 'hash generator'). Single-purpose titles take the top spots on nearly every query (APIVerve 387 focused listings, API-Ninjas 101, magicapi 671 on API.market). The ranked list is `top-100-single-purpose-apis.csv` (title, category, tags, endpoints, marketplaces, wave). The owner will attach it or place it next to this brief; rows 1–20 are wave 1. Every endpoint was checked against the live `/openapi.json`.

## Intent
Test focused products on API.market, where our search evidence shows demand. magicapi's QR product has 23,676 calls and 47 subscribers.

## Why
API.market search rewards single-function products (magicapi 671 products, tidydata 63). We have 3 bundles there today.

## Outcomes
Paste-ready `copy.md` (from S1) for exactly 5 products: QR Code Generator, PDF Merge, PDF Compress, PDF Redact, Image Resize. Each has the title, description, tags, endpoint subset, examples and default pricing. Claude publishes them in the API.market seller console from this copy.

## Acceptance criteria
- 5 copy files are present, and each passes against the live API (examples real).
- Submitted. Report each as submitted / approved / appears in API.market search for its keyword.
- Reviews are slow, so be patient: "submitted, pending review" counts as done for tonight.

## Not in scope / do not decide
Pricing changes. Payout, Purpose code or Tax ID settings (owner decision pending). More than 5 products.

## Owner decisions needed
None. If the console can't back several products from one API Source, report it and stop.

## Source
owner
