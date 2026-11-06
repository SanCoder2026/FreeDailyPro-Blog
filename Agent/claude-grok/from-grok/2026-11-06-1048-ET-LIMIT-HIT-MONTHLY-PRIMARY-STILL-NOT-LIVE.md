Sent: 2026-11-06 10:48 AM ET

# B — Limit-hit paywall: Monthly still not primary (re-ship)

**Intent:** Convert more trial-limit visitors into Monthly subscribers ($4.99 Pro / $9.99 Premium) instead of one-off Day Passes, without changing any prices.

**Why:** Owner already said go ahead on 2026-11-01 (`from-grok/2026-11-01-0922-ET-LIMIT-POPUP-MONTHLY-AND-BOOK-PREVIEW-CTA.md`, Source: owner). Fresh Nov 6 ~9:58 AM ET curl of live `/tool/crop-pdf` + served `index-Cl41DAR6.js` still shows Day Pass as the filled primary (`onClick:()=>D("day_pass")` with no `variant:"outline"`) and Monthly as the outline secondary. Body copy still leads with Day Pass; saverLine is still “Save big on day pass…”. Conversion evidence: `conversion-packages/2026-11-06-revenue-review/MONTHLY-PRIMARY-IMPLEMENTATION-DELTA.md`. Only recurring Stripe sub is past_due $4.99; Day Pass one-offs exist but Monthly is the recurring path.

**Outcomes / done when:**
1. Professional limit-hit: Monthly ($4.99/mo) is the filled primary button; Day Pass ($1 / 24h) is secondary outline.
2. Premium limit-hit: Monthly ($9.99/mo) filled primary; Day Pass ($3) secondary.
3. Body names Monthly first, then Day Pass; either pass still removes the “Created with FreeDailyPro.com” mark.
4. Saver line: “Using it more than 4 days a month? Monthly costs less.” (Premium: “more than 3 days”).
5. Prices unchanged. Wording stays “trial uses” / Professional Tools — never “free tools”.
6. Live JS on a Professional tool (e.g. crop-pdf) and a Premium tool confirms the swap after deploy.

**Suggested direction:** Re-open the shared paywall component that builds `M0` / Day Pass first button; flip order + variants + body/saver strings. Inspect real code; challenge weak copy; match prior deploy patterns. Book preview CTA from the Nov 1 brief is still welcome if not already shipped — verify live before redoing.

**Constraints:** No price changes. Do not remove Google ads. Do not invent funnel % lifts. Owner approval already on file for Monthly-as-primary.

**Process:** Inspect live bundle + source → restate the gap → implement → verify on Professional and Premium tools → note DONE in from-claude.

Source: owner
