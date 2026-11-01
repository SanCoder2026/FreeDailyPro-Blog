# Agent A done: API security and limits (pushed, NOT yet live-verified)

Commits on main: c160be91 (markdown XSS), 9c8056ee (keyless limiter), 0e0a1247 (blind-CV), 69090d59 (routes), b6fb67be (wording), 6162db1b (GPA).

## Needs Santosh
- If Testing Bot shows the keyless caller key rotating, set ANON_TRUSTED_PROXY_HOPS=1 on Railway (utility-api).

## B-API-14 (keyless limit)
No code defect found: 20 sequential calls, 1 and 3 replicas, call 11+ gets 429; spoofed XFF/CF-Connecting-IP cannot reset. Likely your probes hit a rotating caller key. Hardened: IPv6 keyed by /64, Cloudflare-egress callers share a bucket, ANON_TRUSTED_PROXY_HOPS env, no count rollback on DB blip. New headers: X-RateLimit-Caller (8-hex hash), X-RateLimit-Scope (shared|process).
Testing Bot: send 20 keyless calls, capture ALL headers + timestamps. If X-RateLimit-Caller changes, record CF-Connecting-IP and X-Forwarded-For. If stable and no 429, check Scope (process = DB fallback, /health shows memory-fallback).

## Live checks (after utility-api deploy)
- markdown-to-html: `[click](javascript:alert(1))` and `[a](jav&#x09;ascript:alert(1))` -> no <a, no href. GFM table/task list/footnote render. Output shape changed: soft breaks are \n not <br/>.
- blind-cv: "Date of birth: 1990-03-14" -> exactly [BIRTH DATE].
- /mcp/mortgage-loans and /mcp/unit-converter resolve (same tools as loans-mortgage / units). /mcp/nope -> generic 404, no internal path.
- GPA grade 5 or -1 on 4.0 -> unbilled 422.
- 429 body says "trial API key"; llms.txt says 200+ paths; "Trial and Basic keys" gone from specs.
- Known: cover-letter `date` and offer-letter `candidate` bad dates still return billed 200 (Agent B area). calcBriefs3 calorie-cycling test fails on main (pre-existing).
