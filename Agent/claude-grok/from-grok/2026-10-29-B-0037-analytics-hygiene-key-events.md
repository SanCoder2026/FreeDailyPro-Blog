# B-0037 Analytics hygiene: filter bot traffic, set up real key events, verify purchase

**Priority:** P1
**Estimated effort:** ~2 h

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

Context: read-only pull from GA4 (28d Oct 1–28), Search Console (3 months Jul 28–Oct 27; indexing updated 10/22) and AdSense (earnings since Oct 24), taken Oct 29 2026. Totals: 3,412 GA users, GSC 548 clicks / 154K impressions / 0.4% CTR / avg position 18.1, AdSense $0.39.

## Intent
Get numbers we can trust, so revenue decisions, video claims and the admin funnel reflect real humans and real conversions.

## Why
- **Singapore: 1,162 of 3,412 users (34%) with 1.29% engagement**, 15 engaged sessions and 0 key events. Realtime at ~9:05 PM EDT Oct 29 showed 10 of 10 active users from Singapore. This is almost certainly bot or datacenter traffic.
- Direct is 2,565 sessions (68%) at 7.76% engagement with 2s avg engagement. This looks bot-inflated too. A 7d engagement of 8% vs 17% over 28d suggests bot traffic is growing (Oct 23 spike: 440 users).
- Real humans look like: Organic Search 56% engaged, Organic Social 87%, Referral 73%, AI Assistant 70%, and India 62%.
- Key events: 97 over 28d, but we can't tell which events they are. tool_completed fires 275 times for 14 users. **purchase = 1 ($1.00)**, which doesn't match our known Stripe activity or prices, so it may be a test or the wrong value.
- There's no limit_hit or checkout_start event, so we can't see the funnel from tool use → trial limit → checkout → purchase.

## Outcomes
- **Events** (GA4 + our own admin funnel) with consistent params (tool_slug, tier premium/professional, plan, value, currency):
  - `tool_completed` (audit: 275/14 users looks like repeat firing; dedupe per run)
  - `limit_hit` (Premium 2/day and Professional 10/day trial limits)
  - `checkout_start` (Day Pass / monthly / API)
  - `purchase` fired from a server-confirmed Stripe success (webhook or verified session), with real value and currency and transaction_id for dedup
- **Purchase verification:** trace the single $1 purchase (test mode? hardcoded value?) and report what it was. Make sure test-mode payments don't fire production purchase events.
- **Bot / internal traffic:**
  - Our admin funnel/revenue panel excludes known bots, our own and internal traffic (admin users, box/agent browsers), and datacenter traffic. Use UA/bot heuristics, server-side signals and an internal flag, and show the "excluded" count transparently.
  - Write a short owner guide in `from-claude/` for GA4 Admin steps the owner does himself: mark the 4 events as key events; define internal traffic (traffic_type=internal) with a data filter; a "Likely bots" comparison/segment (Singapore + Direct + <1s engagement); and enable bot filtering notes. Bots don't change GA settings (owner rule: test and review only).
- After deploy: a test run shows each event in GA DebugView/Realtime and in the admin funnel. Report screenshots or logs.

## Constraints
- Privacy honesty: no new PII in events. Respect the cookie/consent behavior already shipped.
- Don't block Singapore users at the edge. Real users there must still work. Filter in reporting; only rate-limit clearly abusive automation.
- Trial limits stay at Premium 2/day and Professional 10/day.

## Not in scope / do not decide
Changing GA property settings yourself; changing trial limits.

## Owner decisions needed
The owner applies the GA4 Admin settings from the guide.

## Source
owner
