Sent: 2026-10-31 09:37 ET

# B-0318: Supersedes B-0317. Cancel the Stripe app-tagging work and only exclude WriterCaddy's past charges

## Intent
Keep the FreeDailyPro revenue numbers accurate with as little change as possible. The owner has confirmed that WriterCaddy used FreeDailyPro's Stripe account for only about a week and now has its own Stripe account. The shared-account problem B-0317 was solving no longer exists going forward.

## Cancelled from B-0317 (please don't build these)
- Adding `app=freedailypro` metadata to checkout and subscription sessions
- Filtering the webhook or GA purchase events by app
- Per-session WriterCaddy branding
- The tag-guard test

If any of this has already been started, drop it unless it's already merged and harmless. If so, tell us.

## Keep (the only work left)
1. **Exclude WriterCaddy's historical charges** from FreeDailyPro revenue reporting, the earning review and any metrics code, using a simple exclusion:
   - Key it on SKU or metadata, for example `sku` in WriterCaddy SKUs such as vault-100, ai-1, ai-3, ai-10 and dl-10, or the existing `app=writercaddy`.
   - Or key it on WriterCaddy's date window on the shared account, if that's simpler.
   - Pick whichever is cleanest in the code.
   - Known example: the refunded $2.99 charge ch_3US1r7BiVs2UEbbd1gvVbLh8 (Oct 18, sku vault-100), which was a WriterCaddy self-test.
2. **Correct the repo docs and QA notes** that blamed that Oct 18 $2.99 refund on the FreeDailyPro Book Toolbox "Save File".

## Constraints
Do not change Stripe dashboard settings, prices or products. Abandoned-cart recovery is still waiting on the owner's decision and is out of scope.

## Done when
FreeDailyPro revenue totals no longer include any WriterCaddy charge, and the refund attribution is correct in the repo.

Source: owner
