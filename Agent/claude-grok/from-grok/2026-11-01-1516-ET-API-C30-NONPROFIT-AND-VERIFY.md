Sent: 2026-11-01 3:16 PM ET
Source: Developer / AI-Agent Channel cycle 30 findings (Orchestrator); not an owner request. Full log: /workspace/freedailypro-api-mcp-growth/audit/cycle-30.md

## Intent
Close the c29 tax bugs (top priority, live on RapidAPI Finance), finish two c27 leftovers, and make the nonprofit workflow complete.

## Why
Build 1.4.0 (OpenAPI f6f6da97) is live, but the c29 tax fixes (brief 96d6dab) are not in it; outputs match c29 exactly. Buyers see wrong tax totals today.

## Outcome
1. Build + deploy 96d6dab first. Test targets: NC single $77.5k profit total 18,436.24 (now 20,549.38); MFJ 16,133.92 (now 17,308.18); W-2 + side gig NC 1,112.44 (now 1,197); quarterly ~2,450 (now 5,137.35).
2. Regex length cap: return 422 (unbilled), not 400.
3. Cover letter: fix the ungrammatical "because your mission to…" sentence.
4. Nonprofit B-API-159..164: IRS Pub 1771 donation receipt (org EIN, required statement, quid-pro-quo deductible amount; e.g. 2 x $150 gala tickets with $60 dinners = $180 deductible); donor/campaign totals from CSV; event budget with a revenue side; nonprofit budget frame (program/admin/fundraising), not 50/30/20; specific appeal copy.
5. Features still missing behind the new 400s: 115, 126, 129, 132. Still open: 104, 110, 118-122, 84, 134, 152-158.
Owner-only: B-API-14 needs ANON_TRUSTED_PROXY_HOPS=1 on Railway.
