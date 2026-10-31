Sent: 2026-10-31 14:25 ET

# P0: B-API-13 (batch quota bypass) is still live

**Intent:** Ship and deploy the B-API-13 fix before any other work, so every MCP call in a batch is counted against quota.

**Why:** As of 2:20 PM ET, a batch of 5 MCP calls returned 5 results but used only 1 call of quota (15145 → 15144). The fix brief in commit 78af8b0 isn't deployed. Right now any trial key, or the $24 plan, is effectively unlimited through batching. That gives the product away and makes every plan limit meaningless.

**Outcome:**
1. Deploy the B-API-13 fix first, ahead of everything else.
2. Report it by ID (B-API-13) with a live test: a batch of 5 calls takes 5 calls from quota. Show the before and after counts.
3. Also still unfixed; fix these next and report each by ID:
   - **B-API-14:** 14 of 14 keyless calls went through despite the 10/hour limit.
   - **4xx errors still use up quota:** failed requests must not be charged.
4. New briefs B-API-20 to 27 are in this repo: `Agent/claude-grok/from-grok/2026-10-31-1430-ET-B-API-20-to-27.md`. They come after the items above.

Source: owner
