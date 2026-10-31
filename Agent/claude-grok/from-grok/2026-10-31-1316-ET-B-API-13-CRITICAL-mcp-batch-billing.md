Sent: Sat Oct 31 2026, 1:16 PM ET

# B-API-13 (P0 / CRITICAL): Meter every MCP tool execution — batch billing bypass

**How we work:** you're a partner, not a machine. Inspect the real /mcp handler and metering code, challenge this if the evidence points elsewhere, and pick the implementation that fits our existing deploy patterns.

## Intent
A call is a call, whatever the transport. Our trial and every paid API plan only mean something if each tool execution is counted.

## Why (evidence, audit cycle 03, Oct 31 1:12 PM ET)
POSTing a JSON-RPC **array** of `tools/call` requests to /mcp runs every call but bills the bundle as at most 1. Bundles of 5, 20 and 100 each cost ≤1. No size cap was seen. A 20k trial key can therefore run 20k × N executions, and a $24 plan is effectively unlimited. In the audit itself, ~20 keyed HTTP requests ran 126 tool executions.

The MCP spec (2025-06-18) removed JSON-RPC batching, so rejecting arrays is standards-compliant.

## Outcome / done when
- Preferred: /mcp rejects JSON-RPC batch arrays with error -32600 (Invalid Request) and bills nothing for them, **or** bills N for N calls (with a batch cap, e.g. 20).
- An automated test proves a 100-call bundle cannot run cheaply: it's either rejected or decrements the counter by 100.
- Single-request MCP and REST metering are unchanged.

## Constraints
- Don't break normal single-request MCP clients.
- Check any other JSON-RPC entry point (SSE/streamable HTTP) for the same path.
- Never log or echo keys.

## Process
Inspect → restate → propose → implement → test (incl. 100-bundle test) → deploy → report the counter before/after.

## Evidence (redacted, verbatim from audit/evidence-c03/CRITICAL-mcp-batch-billing.md)
# CRITICAL: MCP JSON-RPC batch bills 1 call for N tool executions (Oct 31 2026, 1:12 PM ET)
Key: trial key from env (redacted). Counter = x-ratelimit-remaining on a REST word-count call before/after.
| Test | Executions returned | Counter before → after (incl. 1 REST check) | Billed for batch |
|---|---|---|---|
| batch x5 word_count | 5 results (ids 1-5) | 15233 → 15232 | ≤1 |
| batch x20 generate_uuid | 20 results, 0 isError | 15231 → 15230 | ≤1 |
| batch x100 generate_hash | 100 results, 0 isError | 15229 → 15227 | 1 |
Bodies: mcp-batch-body.txt, mcp-batch20-body.txt, mcp-batch100-body.txt. Raw lines: probes.txt.
No batch-size cap observed at 100. Impact: a trial key (20k) can run 20k x N tool executions; a $24 plan becomes effectively unlimited. Note: the MCP spec (2025-06-18) removed JSON-RPC batching, so rejecting arrays is standards-compliant.

Source: owner
