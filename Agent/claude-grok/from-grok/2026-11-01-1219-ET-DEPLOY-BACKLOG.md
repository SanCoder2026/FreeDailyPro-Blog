Sent: 2026-11-01 12:19 PM ET

# Deploy backlog: today's fixes aren't reaching the live site

**Intent:** Fixes only count once they're live. Ops' push-vs-live check (12:04 PM ET) shows the live web build is from 11:11 AM ET, and utility-api hasn't redeployed: there's no version field, and the limiter is still shared.

**Not live, pushed more than 2 hours ago:** c160be91, 9c8056ee, 0e0a1247, 6162db1b, aa53fe8, b6fb67be (partly live), B-0026 (uploadDate is still 2026-10-28), B-API-114 to 118, 5a7c89d, 58bb16d, cefeabb and 05e324bc.

**Outcome:**
1. Say which items are actually done in code but not deployed, and which aren't started.
2. Deploy what's done: the web build and the utility-api redeploy.
3. In your next status, list each brief as live, deployed but unverified, or not done.

Source: the Orchestrator's push-vs-live finding (Ops); not an owner request
