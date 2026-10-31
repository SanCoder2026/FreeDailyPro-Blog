Sent: 2026-10-31 12:57 PM ET

# B-0326: Fix the trial-limit wording across the whole site in one pass

**Intent:** Every visitor should see one correct trial rule that reads the same everywhere. When blog posts disagree with each other or with the pricing page, people stop trusting our pricing, and they churn before they ever try a paid tier.

**Outcome:** Every post and the blog template state the canonical rule below word for word, and a grep finds zero mismatches.

**Canonical text (use it verbatim):**
> Professional Tools: 10 trial uses a day, then a $1 day pass or $4.99/month. Premium Applications (Universal File Converter, Document Scanner, Catalog Maker, Resume/CV Builder, Magazine Maker): 2 trial uses a day.

Trial uses count **per tool**; they are not shared across tools. Say this wherever the limit is explained.

**What's wrong now (lists are in QA reports 293–336):**
- 22 posts say 2 uses a day for non-Premium (Professional) tools. The correct limit is 10.
- 5 posts suggest Premium Applications get 10 uses a day. The correct limit is 2.

**How to fix it:** make the change **once, at the source**. Put the rule in a shared blog template or partial, or run one find-and-replace across all posts. Don't edit posts one by one, because the wording drifts again. If the rule lives in the template, remove the hard-coded copies from the posts.

**Check before closing:** grep all posts, the template and the pricing copy for trial and daily-limit phrasing. Look for "2 uses", "10 uses", "trial uses", "per day", "a day" and "free uses". Report back the grep command and its result, which should be **zero remaining mismatches**, plus the list of files changed.

Source: owner
