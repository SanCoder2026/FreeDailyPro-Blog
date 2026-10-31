Sent: 2026-10-31 09:06 ET

# B-0317: Tag FreeDailyPro Stripe checkouts by app, separate WriterCaddy revenue, and fix the Oct 18 refund attribution

**How we work with you:** you're a partner here, not just executing orders. Look at the real codebase, push back on anything weak in this brief, and pick the implementation that fits how we've deployed before. The intent and outcomes below matter more than the suggested steps.

## Intent
Stripe is our source of truth for revenue. Right now it can't tell FreeDailyPro sales apart from WriterCaddy sales, because both apps share one Stripe account (acct_1TojtpBiVs2UEbbd). We want every FreeDailyPro report, webhook-driven event (including GA purchase events) and daily earning review to count only FreeDailyPro money. We also want every buyer to see the brand of the site they came from at checkout.

## Why (evidence, live Stripe read on 2026-10-31 at 09:04 ET)
- **Wrong attribution.** The refunded $2.99 charge ch_3US1r7BiVs2UEbbd1gvVbLh8 (Oct 18) came from session cs_live_a1H1rlL8SSbyG2jFbLFZT6svPRAkaXWbID97RC3rCTcMoam0AYwViBBsKp. Its metadata is app=writercaddy and sku=vault-100, and it was a WriterCaddy self-test by the owner. It was **not** a FreeDailyPro Book Toolbox "Save File" refund. Please correct any notes, QA reports or docs in the repo that say otherwise.
- **Untagged FreeDailyPro sessions.** FreeDailyPro Checkout sessions carry only `plan` and `guest` metadata and no `app` key, so nothing can filter on them.
- **Brand mismatch.** Five WriterCaddy sessions (ai-1, ai-3, ai-10 and dl-10, at $9.99, $24.99, $64.99 and $49.99) show the display name "FreeDailyPro" but return buyers to writercaddy.com. That confuses buyers and can cause them to abandon checkout.
- **This ties into B-0309/revenue-fixes-daily-1 item 3.** GA purchase events should come only from the Stripe webhook. That webhook now also has to ignore events from other apps.

## Outcomes (what done looks like)
1. Every new FreeDailyPro Checkout session (subscriptions, Day/Week passes, Book Toolbox, seats and API plans) carries `metadata.app=freedailypro`. Where subscriptions are created, `subscription_data.metadata` carries it too, so invoices and renewals stay attributable.
2. The FreeDailyPro webhook handler, including entitlement grants and GA purchase events, acts only on events whose session, subscription or payment metadata has app=freedailypro. Events from other apps are skipped and logged, not errored.
3. Any internal revenue or earning reporting code filters on, or splits by, `app`. Sessions with no `app` value from before the change are handled explicitly, for example reported as "untagged/legacy" rather than silently counted.
4. WriterCaddy checkouts show WriterCaddy branding. If WriterCaddy's checkout code lives in a repo you control, it should send its own branding settings per session and keep its own `app=writercaddy`. If it doesn't, tell us what's needed, and don't change the shared account's branding.
5. Repo docs, QA notes and reports that blamed the Oct 18 $2.99 refund on Book Toolbox are corrected.

## Suggested direction (interpret freely)
- Centralize session creation, or a metadata helper, so no checkout path can skip the tag.
- Prefer per-session parameters in code. **Do not change Stripe dashboard or account settings**, including account branding, recovery, emails or the payment-method config. Those belong to the owner.
- Add a test or assertion that fails when a checkout is created without `app`.

## Constraints
- Don't create new Stripe prices or products. That needs the owner.
- Keep free-first, privacy-honest behavior. Don't add new data collection.
- Don't change prices or metering.
- **Out of scope:** abandoned-cart recovery for checkout (NEW #1 in today's review) is waiting on the owner's decision. Don't implement it here.

## Process
Inspect the code, then restate what you found (every checkout creation path, the webhook and the reporting code). Then propose, implement, and verify in test mode. A new session should show app=freedailypro, and a webhook event without it should be ignored.

## Acceptance
- Every new live FreeDailyPro session has app=freedailypro.
- The webhook and GA purchase events fire only for FreeDailyPro.
- Revenue reporting splits by app.
- The refund attribution is corrected in the repo.

Source: owner
