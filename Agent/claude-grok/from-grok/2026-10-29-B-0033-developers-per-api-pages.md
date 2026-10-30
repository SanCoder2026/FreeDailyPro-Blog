# B-0033 /developers per-API pages generated from listings.yaml (S6, owner-approved)

**Priority:** P2
**Estimated effort:** ~60 min

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

Context: owner-approved Oct 29 (split-listings plan, items S1–S7). The evidence is in the API/MCP bot's analysis: our 7 RapidAPI / 3 API.market bundles have 0 popularity badges and rank deep or not at all (19 of 29 keywords missing; pdf merge #51, image resize #44, loan #26; absent for 'hash generator'). Single-purpose titles take the top spots on nearly every query (APIVerve 387 focused listings, API-Ninjas 101, magicapi 671 on API.market). The ranked list is `top-100-single-purpose-apis.csv` (title, category, tags, endpoints, marketplaces, wave). The owner will attach it or place it next to this brief; rows 1–20 are wave 1. Every endpoint was checked against the live `/openapi.json`.

## Intent
Give each focused API its own page on our site at `/developers/apis/<id>`, generated from the same YAML, so the site and the marketplaces always say the same thing.

## Why
These pages give per-keyword SEO landing pages ("QR code generator API") and link out to each listing, which helps both search and marketplace ranking. Generating them from the YAML also stops /developers claims drifting away from reality, which is already a known issue there.

## Outcomes
- One page per listings.yaml entry, with title, description, endpoints, a live example, and links to that API's RapidAPI, Postman and API.market listings.
- An index on /developers.

## Acceptance criteria
- The site build fails if a YAML entry has no page.
- No claim on the page drifts from the YAML or the spec.
- The pages are in the sitemap and verified live.

## Not in scope / do not decide
Redesigning /developers. Pricing copy beyond the YAML.

## Owner decisions needed
None.

## Source
owner
