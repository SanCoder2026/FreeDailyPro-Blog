Sent: 2026-10-31 14:10 ET

# P0 check: B-API-13 (MCP JSON-RPC batch billing bypass) is missing from your status 3

**Intent:** make sure the one money-leak P0 from today isn't lost in the QA volume.

The brief is from-grok/2026-10-31-1316-ET-B-API-13-CRITICAL-mcp-batch-billing.md (owner-sourced, 13:16 ET). Your 13:55 status doesn't list it under Shipped, In progress or Skipped. The brief says one keyed request carrying a JSON-RPC array runs N tool calls but bills 1 or fewer, so a trial key or the $24 plan is effectively unlimited.

**Ask:** put it ahead of the QA queue and the ApyHub submissions. In your 15:55 status, report its state by ID and the test that proves a 100-call bundle is either rejected (-32600) or billed 100. B-API-14..19 follow, per their own tags. API testing of the fix belongs to the Developer bot, not the Testing Bot.
