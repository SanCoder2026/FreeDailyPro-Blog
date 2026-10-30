# B-0029 Check whether RapidAPI Platform API can automate listings (read-only) (S2, owner-approved)

**Priority:** P1
**Estimated effort:** ~30 min

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

Context: owner-approved Oct 29 (split-listings plan, items S1–S7). The evidence is in the API/MCP bot's analysis: our 7 RapidAPI / 3 API.market bundles have 0 popularity badges and rank deep or not at all (19 of 29 keywords missing; pdf merge #51, image resize #44, loan #26; absent for 'hash generator'). Single-purpose titles take the top spots on nearly every query (APIVerve 387 focused listings, API-Ninjas 101, magicapi 671 on API.market). The ranked list is `top-100-single-purpose-apis.csv` (title, category, tags, endpoints, marketplaces, wave). The owner will attach it or place it next to this brief; rows 1–20 are wave 1. Every endpoint was checked against the live `/openapi.json`.

## Intent
Find out whether we can create and update RapidAPI listings by API or GitHub Action, rather than through owner clicks in Studio.

## Why
RapidAPI is the owner's top priority ("we have to make it work on RapidAPI"). The Platform API (GraphQL) docs mostly target Enterprise Hub, and we don't know whether our public-Hub account can use it. The answer decides how S3 gets done.

## Outcomes
A short note in your report with:
- PAPI usable: yes/no
- Create API via PAPI: yes/no
- Billing plans settable: yes/no
- Whether the official GitHub Action (spec upload) works for us

## Acceptance criteria
- One read-only PAPI query that lists our own APIs succeeds using the owner's key (referenced by name only), or there's a documented "no" with the error.
- Nothing is created, updated or deleted. Any write needs a separate owner approval.

## Not in scope / do not decide
Changing existing listings, plans or the legacy listing.

## Owner decisions needed
Only if it's usable: approve write access for S3.

## Source
owner
