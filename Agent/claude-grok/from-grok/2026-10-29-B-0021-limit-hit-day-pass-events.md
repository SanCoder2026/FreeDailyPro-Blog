# B-0021 At the Professional Tools limit, lead with the Day Pass and record upgrade events
Priority: P1 (must-do)      Estimated effort: 60 min

## Goal / why
The paywall at 0 remaining (B-0001) is the moment people are most willing to pay. We want the Professional Tools paywall to make the Day Pass the obvious first choice, and we want to start counting how often the limit is hit and how often people click upgrade. Today we have no funnel numbers at all, so every later pricing or copy test is guesswork.

## What to change
- Professional Tools paywall (the shared surface B-0001 opens at 0 remaining): primary button = Day Pass, secondary = Monthly, small link to /pricing. Use the existing Stripe checkout links and prices exactly as they are today (per the QA index: Professional Day Pass $1, Monthly $4.99; Premium $3 / $9.99). Do not change prices or billing.
- Premium Applications paywall: leave its layout as is, but fire the same events.
- Analytics events through whatever analytics the site already uses (GA4/GTM or the existing helper): `limit_hit` (remaining reaches 0 and the user tries an output action), `upgrade_cta_view` (paywall shown), `upgrade_cta_click` (with which option: day_pass / monthly / pricing). Parameters may include tool slug, tier (professional / premium), uses today and placement. Never send file names, file contents or anything personal.
- Copy: keep it honest and short, e.g. "You've used today's 10 trial uses. Get unlimited use for 24 hours with a Day Pass." Keep the existing privacy line. No "free" in visible text, no fake countdowns.
- Check the five busiest Professional Tools first: merge-pdf, compress-pdf, pdf-to-word, remove-background, compress-image.

## Acceptance criteria
- On https://www.freedailypro.com/tool/merge-pdf at 0 remaining, an output action opens the paywall with Day Pass as the primary button, no file is delivered, and the Day Pass button opens the existing checkout.
- `limit_hit`, `upgrade_cta_view` and `upgrade_cta_click` fire once each per action (no double firing), visible in the analytics debug view or the network log.
- The first successful output of the day is never blocked; Premium 2/day and Professional 10/day pools unchanged.
- Report: files touched, where the events land, one sample payload per event, verification `live and checked`.

## Not in scope / do not decide
Prices, plans, Stripe products, trial limits. A soft "upgrade" banner before the limit (later brief, after we see the numbers). Return-visitor variants. Optional AI.

## Owner decisions needed
none (uses existing prices and checkout; standing trial limits recorded in PROCESS.md)

Source: Conversion bot (Conversion Optimization Plan, Oct 28) via Grok.
