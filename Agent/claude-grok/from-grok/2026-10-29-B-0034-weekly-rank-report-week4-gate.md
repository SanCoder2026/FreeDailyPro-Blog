# B-0034 Weekly rank and usage report, plus week-4 go/no-go gate (S7, owner-approved)

**Priority:** P3
**Estimated effort:** ~45 min

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

Context: owner-approved Oct 29 (split-listings plan, items S1–S7). The evidence is in the API/MCP bot's analysis: our 7 RapidAPI / 3 API.market bundles have 0 popularity badges and rank deep or not at all (19 of 29 keywords missing; pdf merge #51, image resize #44, loan #26; absent for 'hash generator'). Single-purpose titles take the top spots on nearly every query (APIVerve 387 focused listings, API-Ninjas 101, magicapi 671 on API.market). The ranked list is `top-100-single-purpose-apis.csv` (title, category, tags, endpoints, marketplaces, wave). It is in this folder as `2026-10-29-B-0028-top-100-single-purpose-apis.csv`; rows 1–20 are wave 1. Every endpoint was checked against the live `/openapi.json`.

## Intent
Measure whether splitting actually works before we spend effort on waves 2 and 3. Expand only on evidence.

## Why
The owner approved a measured rollout. Wave 1 is a test, and we need a hard stop rule so effort isn't wasted.

## Outcomes
A script that records, per wave-1 listing: the RapidAPI rank for its keyword, 30-day calls, free and paid subscribers, badges (popularity/latency/service level), first-call 4xx rate, and free→paid conversions. Each week it writes a dated report that diffs against the week-0 baseline, filed under `from-claude/`.

## Week-4 gate (decide in writing)
Proceed to wave 2 (30 listings) if **at least 2** of these are met:
1. At least 10 of the 20 wave-1 listings are in the top 10 for their keyword
2. At least 5 have a popularity badge
3. At least 25 external free subscribers in total
4. At least 1 paid conversion

**Otherwise stop splitting** and put the effort into content and traffic.

## Acceptance criteria
- The baseline exists at week 0, and a report exists for each of weeks 1–4.
- The week-4 report states go/no-go against the 4 criteria.
- No price changes during weeks 0–4.

## Not in scope / do not decide
Starting wave 2 without the gate result.

## Owner decisions needed
None until week 4.

## Source
owner
