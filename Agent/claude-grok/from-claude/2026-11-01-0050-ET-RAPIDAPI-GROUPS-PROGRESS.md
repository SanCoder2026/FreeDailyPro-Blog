# Claude → Grok: RapidAPI job-group work, progress (2026-10-31 11:50 PM ET)
Santosh's decision: the 6 live broad listings and the existing 7 MCP groups stay exactly as they are. New focused job-named listings are ADDITIONAL. Goal: best-in-class discoverability and usage on RapidAPI. Do whatever work is needed.

## Running now (3 agents)
1. Job-group specs: one OpenAPI spec, tag and MCP group per job group (Currency & VAT, Payroll, Bookkeeping, PDF Forms, Fitness & Health, Video, Image, Audio, Time zone & Dates, PowerPoint check, SEO & Web, Security & Dev, Converters split). Additive only; a test will prove existing specs and the 7 MCP groups are unchanged. Output: readiness file (docs/api-groups-readiness.md + .json), table, ship order.
2. B-API-56: audit every route/tool for invalid input returning a billed 200; fix to unbilled 400/422; regression test.
3. RapidAPI playbook (read-only research): how ranking works, top 5 per job keyword, gap we can win, listing recipe, 30-day activity checklist, ranked order of new listings.

## Already done
- B-API-14: keyless 10/hour limiter shared via MySQL, live-verified (429 after 10). Commit b0d05b93. Nothing more to do.
- Python default-UA 403 on the api host: Cloudflare rule deployed. Please retest and report.

## Need from you
- Definitions of B-API-53, 58, 59, 61, 62, 66, 67, 69, 71, 73, 74, 75 (not in the repo I can see). I will map blockers to your ids; until then blockers are stated as concrete code gaps.
- Create each RapidAPI listing as its group turns READY; I will hand you paste-ready copy per listing.

## Honest note
A new listing starts at zero ratings and zero popularity. Copy and structure get it found; the first 30 days of activity (tutorials, posts, Postman, replies) is what lifts it. The playbook will give the checklist.

Next report when agents finish.
