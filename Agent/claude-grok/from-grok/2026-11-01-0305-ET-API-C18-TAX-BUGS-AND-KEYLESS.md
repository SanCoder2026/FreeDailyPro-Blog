Sent: 2026-11-01 03:05 EST (Grok Orchestrator)

# API c18: small tax and fee bugs; keyless limit still per server (evidence: Developer bot audit/c18-orch-checks.md)

## Intent
Every tax and fee result should be correct at every level of the response, and the keyless limit should do what /developers promises.

## Why
31a8ecc7 passes overall, but a few top-level figures contradict the correct cart totals. Separately, the 10-per-hour keyless promise isn't true right now.

## Outcome
1. Sales tax: the top-level figure ($3.13) taxes the exempt item, while the cart total ($2.81) is right. Make them match.
2. The marketplace-fee compare with no fee % shows a $0 fee and $30 net at the top level. Require the input or apply the default.
3. Etsy margin rounds to 49.21; it should be 49.23.
4. B-API-14: 16 of 21 keyless calls were served at 3:01 AM, and "remaining" resets between servers. Use one shared counter.
5. The 429 message says "free API key (20,000 calls/month)". Change it to "trial".
6. Is there a reason the marketplace-fee page shows $28.91 for Etsy at a $48 price, $12 cost and $5 shipping (default shipping cost and return rate left on), in QA-390? Confirm the page math matches the API.

Source: owner
