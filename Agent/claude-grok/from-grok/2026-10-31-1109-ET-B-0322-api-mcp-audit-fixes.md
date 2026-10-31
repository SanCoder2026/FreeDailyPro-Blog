Sent: 2026-10-31 11:09 ET

# B-0322 — API/MCP audit fixes (Developer cycle-01) + site-side external audit fixes

**How we work together:** You're a partner, not someone who just follows orders. Check every finding against the live API and the codebase before acting, push back on anything that's wrong, and pick the implementation that fits our existing deploy patterns.

## Overall intent
FreeDailyPro's developer surfaces (API, MCP, llms.txt, registry, Postman, site copy) should be accurate, consistent and easy to succeed with on the first call. A developer or AI agent that audits us should find nothing that contradicts itself.

## Why
- Developer bot cycle-01 (Oct 31, about 45 live calls) found no P0 or auth bypass, and MCP and REST share the quota correctly. But it found mismatched counts, "free" wording in llms.txt, billed 4xx errors, keys that are silently ignored, and inconsistent error formats.
- The SEO bot's external audit (Oct 31) found the same count drift on public listings, a stale API root, an MCP version mismatch, and empty Postman examples.
- **Rule: never claim capabilities that are incomplete.** When in doubt, round down or leave it out.

## Items

### B-API-01 — One source of truth for counts
- **Intent:** every public number matches the live API.
- **Why:** live there are 229 OpenAPI paths (about 226 real routes) and 220 MCP tools. The site says "215+ / 211+". /developers says "225 tools". Home says "250+" and "300+". llms.txt says "about 205". A developer audit catches this first, and it undermines trust.
- **Outcome:** the site, llms.txt, server.json and marketplace copy render counts at build time from openapi.json and tools/list, rounded down (for example "225+ endpoints, 220+ MCP tools"). **Done when** the counts from curl equal the counts on the pages.

### B-API-02 — Trial wording in llms.txt
- **Intent:** AI agents quote llms.txt verbatim, so it has to follow the brand rule.
- **Why:** it currently says "Free tier" and "Get a free key".
- **Outcome:** "Trial: 20,000 calls/month" and "Get a trial key", with no "free" anywhere on API surfaces.

### B-API-03 — Auth clarity
- **Intent:** no developer should believe their key works when it doesn't.
- **Why:** `Authorization: Bearer` and `?api_key=` are silently ignored. Those requests fall back to the anonymous tier (limit 10) and get 200 on keyless routes, then 401 "Missing API key" on PDF routes. The anonymous window also isn't shown in headers.
- **Outcome:** Bearer either works (preferred, since OpenAI/Anthropic-style clients and Claude Desktop/Cursor MCP configs send it) or returns 401 with a "use X-API-Key" hint. Add `x-ratelimit-reset` and `RateLimit-Policy` headers on both anonymous and keyed calls. MCP accepts Bearer too.

### B-API-04 — Don't bill client errors
- **Intent:** trial users shouldn't burn quota while they learn, which matches best-in-class metering.
- **Why:** a 400 validation error used one call (15375 → 15374). 404s appear not to be billed.
- **Outcome:** 4xx responses aren't counted. If you decide to keep counting them, the docs must say so plainly.
- **Excluded, owner-pending:** the staging/test key with limit=5 for proving the 20k cap. Don't create it until Santosh approves.

### B-API-05 — One error envelope + per-endpoint docs_url
- **Intent:** the first call should succeed without opening Swagger.
- **Why:** errors mix the zod shape (`{"error":"Invalid input","details":{fieldErrors}}`) with plain strings, and param names are hard to guess (`annualRatePercent`, `homePrice`, `lines`, `text`).
- **Outcome:** `{error:{code,message,field,docs_url}}` everywhere, and every OpenAPI operation has an example request body.

### B-API-07 — Developer videos
- **Intent:** cut time to first call and time to MCP-in-Claude.
- **Why:** the site claims "every tool has a usage video", but /developers has no API or MCP setup video.
- **Outcome:** a 60s first-call video and a 2-min MCP setup video for Claude Desktop/Cursor, embedded on /developers. Only demo flows that work end to end today.

## Site-side fixes (SEO external audit)

### S-1 — Every count from one source
- **Intent and outcome:** the same generated counts from B-API-01 flow into every surface we control. That covers the site, llms.txt, server.json/registry text, the Postman description, and the marketplace copy we draft. Don't hand-edit numbers.

### S-2 — API root self-description
- **Why:** `GET https://api.freedailypro.com/` still says **v0.3.0** and lists only about 20 text/security/converter endpoints, which undersells the API to anyone who hits it.
- **Outcome:** the root returns the current version, generated counts, and pointers to `/openapi.json`, `/mcp` and https://www.freedailypro.com/developers.

### S-3 — MCP version matches the registry
- **Why:** MCP serverInfo reports `freedailypro-utility-tools 0.3.0`, but registry server.json is at 1.3.1.
- **Outcome:** one name and one version, sourced from package/server.json. The registry publish itself is still blocked on the DNS key (owner).

### S-4 — Postman example responses
- **Why:** the collection has `{}` example responses and an old description that leaves out PowerPoint and media.
- **Outcome:** re-import from openapi.json, save one real example response for each of the top 20 endpoints, and use a description with generated counts plus the trial line (20,000 calls/month). If Postman publishing needs owner credentials, prepare the artifact and flag it.

## Owner-pending (excluded from this brief, do not action)
- **B-API-06:** the legacy RapidAPI listing ($0 for 500k/month on 171 routes). Retire or cap it only after Santosh decides.
- **B-API-04 test key:** the staging key with limit=5 to prove cap enforcement needs Santosh's approval.

## Constraints
- Stay free-first on web tools, use trial wording on API surfaces, and be honest about privacy.
- Never claim incomplete capabilities. For example, image→PDF, OCR and HEIC aren't verified, and redact-pdf is broken (B-0098).
- Don't change pricing or plans. Don't take payment or marketplace actions.

## Process
Inspect → restate → propose → implement → verify with live curl and MCP calls. Report in `from-claude/` in your next :55 status, with commits and before/after evidence for each item.

Source: owner
