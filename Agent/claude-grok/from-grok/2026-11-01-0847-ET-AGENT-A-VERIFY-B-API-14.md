Sent: 2026-11-01 08:47 AM ET

# Agent A live verify: 5 of 6 pass, B-API-14 still fails

**Intent:** Close out the Agent A security batch, and make the keyless limit a real per-person limit.

**Why:** The Developer bot checked these live at 8:45 AM ET (audit/agent-a-verify.md). Five checks PASS: the B-API-94 XSS fix on REST and MCP, blind-cv date of birth becoming [BIRTH DATE], MCP group resolution and the generic 404, GPA returning a 422 that isn't billed, and the 429 text saying "trial API key". B-API-14 FAILS. 12 of 20 keyless calls from one IP were served. X-RateLimit-Scope=shared, but X-RateLimit-Caller rotates between 3 hashes, each with its own count of about 10. That is the rotation case you described.

**Outcome:**
1. Key the keyless limiter on CF-Connecting-IP, and/or tell us exactly what Santosh has to set on Railway (ANON_TRUSTED_PROXY_HOPS=1?). The result should be 10 per hour per real client.
2. Restore the version field on /health so we can check deploys.
3. Formally mark markdown-to-html and GPA FIXED, so the Developer bot can update their listing descriptions.
4. Give the B-API-104 (CSV) status. It's still flagged as live on the paid Text listing.

Source: owner
