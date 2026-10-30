# B-0037 Owner guide: GA4 Admin steps (you do these, bots do not touch GA settings)

Use the GA4 property that belongs to your second Google login. The site's tag ID in the code is G-Q1H24JEZX6: open Admin > Data streams > the web stream and confirm the Measurement ID shown there is the same one. If it is different, tell us before anything else (events would be going to another property).

## What the site now sends (after the B-0037 deploy)
All events keep the existing parameter names (`tool_id`, not `tool_slug`, so the dimensions already registered keep working).

| Event | When | Parameters |
|---|---|---|
| `tool_completed` | A tool finishes a run (repeat callbacks within 2.5 s of the same tool are dropped) | tool_id, tool_category, tier |
| `limit_hit` | The trial-limit dialog opens (already shipped) | tool_id, tier, uses_today, placement |
| `checkout_start` | A Stripe Checkout link was created and the visitor is being sent to it | tier (professional / premium / api), plan (day_pass / monthly / api), value, currency, tool_id when started from a tool |
| `purchase` | Only after the server has read the paid, live-mode Stripe session | transaction_id (Stripe session id), value (Stripe's amount), currency, tier, plan, items |
| every event | Our own devices, admin sessions, automated browsers | traffic_type = internal |

No file names, contents or emails are ever sent. Do-not-track, Global Privacy Control and cookie consent still stop every event.

## 1. Mark the 4 key events
Admin > Data display > Events (events appear after they fire once; use the test run below). Switch "Mark as key event" on for: `tool_completed`, `limit_hit`, `checkout_start`, `purchase`. Then in Admin > Data display > Key events, un-mark any others you do not want (for example scroll or page_view) so the "97 key events" number stops being a mystery.

## 2. Register the parameters as custom dimensions (needed to break reports down)
Admin > Data display > Custom definitions > Create custom dimension, scope Event, one for each: `tool_id`, `tier`, `plan`, `placement`, `traffic_type` (skip any that already exist). `value` and `currency` need no setup.

## 3. Internal traffic filter
1. Admin > Data collection and modification > Data streams > your web stream > Configure tag settings > Show all > Define internal traffic: you can leave IP rules empty; the site labels internal traffic itself with traffic_type=internal.
2. Admin > Data collection and modification > Data filters > Internal Traffic: set the filter's parameter value to `internal` if you can edit it, and leave it in **Testing** state first.
3. After a day, open a report with the "Test data filter name" dimension, confirm only your own sessions are tagged, then set the filter to **Active**. Active filters cannot be undone for past data, so test first.
To flag a device as yours: open any page once with `?fdp_internal=1` at the end of the address (for example https://www.freedailypro.com/?fdp_internal=1). Admin sign-ins flag the device automatically. `?fdp_internal=0` removes the flag. Browsers driven by automation (box/agent browsers) are flagged on their own.

## 4. "Likely bots" comparison (view only)
Explore or Reports > Add comparison: Country = Singapore, OR Session default channel group = Direct with Average engagement time per session under 1 second. Save it as "Likely bots". Use it as a comparison, not a filter, so nothing is deleted. Real-human reference points from the pull: Organic Search 56% engaged, Referral 73%, AI assistant 70%, India 62%.

## 5. Bot filtering notes
GA4 already removes known bots and spiders (IAB list) automatically and it cannot be switched off. Datacenter traffic that looks like a browser (the Singapore pattern) is not caught by that list, which is why steps 3 and 4 exist. Do not block Singapore: real visitors there must still work.

## 6. After the deploy: prove it
1. Admin > Data display > DebugView. Open the site in Chrome with the GA Debugger extension (or add `?debug_mode=1`), and make sure the device is NOT flagged internal (`?fdp_internal=0`), otherwise events are labelled internal.
2. Run a Professional tool once: expect `tool_completed` once. Run it 3 times: expect 3, not 6.
3. Use up the trial and open the paywall: expect `limit_hit`. Click Day Pass: expect `checkout_start` with value 1 (Professional) or 3 (Premium).
4. Real purchase check: the next genuine live payment should produce one `purchase` with Stripe's amount and a transaction_id starting with `cs_live_`. Test-mode payments fire nothing by design.
5. Our admin page /admin/funnel shows the Funnel and a new line "Not counted in these numbers" with the excluded visits by reason.

## About the single $1 purchase
The old code fired `purchase` from the browser using a hard-coded price table (`day_pass` = 1.0, `monthly` = 4.99), as soon as the account showed Pro access on a URL containing `?checkout=success&plan=...`, with a made-up transaction_id (`day_pass_<timestamp>`). A $1 Professional Day Pass is a real price, so it may well have been a genuine $1 purchase or your own test; the old event cannot tell test mode from live, ignored coupons, and never fired for Premium Applications. Check Stripe (Payments, filter live and test mode) for a $1.00 charge around that date to settle which it was.
