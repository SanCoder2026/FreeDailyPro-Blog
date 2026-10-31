# Request to Grok: test pricing/checkout updates — 2026-10-31 12:40 ET (P0)

Live on freedailypro.com as of 12:37 ET. Railway has STRIPE_PRICE_EVENT_SUITE = the existing $29.99 price (…gmvl). Please test as a signed-OUT visitor and as a signed-in non-admin user (the owner's browser is admin so it shows "Open"). Do NOT enter a real card; stop at the Stripe Checkout page and record what it shows.

1. /pricing: Seller Studio and Legal Production Desk cards exist (commit 12cd7716). Subscribe on each: sign-in prompt, then Stripe Checkout. Expect $29.99/month, 7-day trial on first purchase, terms text. Report any error such as "not open for sign-up yet".
2. /pricing and desk pages at 375px and desktop: layout, buttons, no overlap.
3. Trial-limit and download paywall dialog (3eef94eb): Day Pass is the main (filled) button, "Save big on day pass with our monthly pass at just $4.99" line, monthly outline button; check Professional and Premium prices ($1/$4.99 and $3/$9.99).
4. Counts: 300+ for the whole site, 250+ only for professional tools, on home, /pricing, /about, and /de /ja /es pages (d075684d).
5. Expense Tracker opt-in (84985a5e): "Keep my entries in this browser" off by default; tick, add 3 entries, reload, entries return; "Delete everything saved here" clears; private window message; reminder after 20 entries.
6. College cost calculator default loan rate now 6.52% (2026-27) (067f8db6).
7. After one real owner purchase later, GA DebugView should show exactly one purchase event with the Stripe session id; reload fires nothing (0460cd68). Separately investigate where GA's $6.99 purchase events come from (code never emits 6.99).
Report each as pass/fail with URL and screenshot notes in from-grok.
