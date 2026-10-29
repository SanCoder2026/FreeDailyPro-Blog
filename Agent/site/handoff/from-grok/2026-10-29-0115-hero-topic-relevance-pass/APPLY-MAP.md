# APPLY-MAP — replace live blog heroes

**Batch:** `2026-10-29-0115-hero-topic-relevance-pass`
**Purpose:** Topic-relevance pass — fix heroes that fail locked rule §3 (topic must be obvious at a glance).

## How Claude should apply

For each row: replace live `/blog/{slug}.webp` with `images/{slug}.webp`. Images only.

| # | Blog slug | Blog title | Why fixed | Hero file |
|---|-----------|------------|-----------|-----------|
| 1 | `assign-guests-to-tables-seating-chart` | Assign Guests to Tables With a Seating Chart | Large seating chart board + digital chart — topic obvious at a glance (was weak/generic-looking) | `images/assign-guests-to-tables-seating-chart.webp` → `/blog/assign-guests-to-tables-seating-chart.webp` |
| 2 | `bates-stamp-production-zip-legal-desk` | Build a Bates-Stamped Production ZIP | Was packing boxes — now Bates stamps + production ZIP UI | `images/bates-stamp-production-zip-legal-desk.webp` → `/blog/bates-stamp-production-zip-legal-desk.webp` |
| 3 | `journal-submission-pack-paper-desk` | Prep a Journal Submission Pack in One Pass | Was shipping boxes — now manuscript/cover letter submission pack | `images/journal-submission-pack-paper-desk.webp` → `/blog/journal-submission-pack-paper-desk.webp` |
| 4 | `mail-merge-letters-and-certificates-from-csv` | Mail-Merge Letters and Certificates From a CSV | Was abstract teal + floating F | `images/mail-merge-letters-and-certificates-from-csv.webp` → `/blog/mail-merge-letters-and-certificates-from-csv.webp` |
| 5 | `plan-event-one-shared-project-event-suite` | Plan Any Event in One Shared Project | Was abstract UI + floating F | `images/plan-event-one-shared-project-event-suite.webp` → `/blog/plan-event-one-shared-project-event-suite.webp` |
| 6 | `install-event-apps-iphone-android` | Install the Event Apps on iPhone and Android | Was floating F on phones | `images/install-event-apps-iphone-android.webp` → `/blog/install-event-apps-iphone-android.webp` |
| 7 | `one-link-per-exhibitor-trade-show-floor` | One Link per Exhibitor: Running a Trade Show Floor | Was huge floating F | `images/one-link-per-exhibitor-trade-show-floor.webp` → `/blog/one-link-per-exhibitor-trade-show-floor.webp` |
| 8 | `capture-event-receipts-against-budget` | Capture Event Receipts Against the Budget Line | Was abstract colorful boxes | `images/capture-event-receipts-against-budget.webp` → `/blog/capture-event-receipts-against-budget.webp` |
| 9 | `freedailypro-vs-tinywow-privacy-and-free-tier-compared` | FreeDailyPro vs TinyWow: Privacy and Usage Limits Compared | Exact duplicate of 200-tools milestone image | `images/freedailypro-vs-tinywow-privacy-and-free-tier-compared.webp` → `/blog/freedailypro-vs-tinywow-privacy-and-free-tier-compared.webp` |
| 10 | `run-stage-countdown-and-focus-rounds` | Run a Stage Countdown or Focus Work Rounds | Near-reuse of manuscript hero pose | `images/run-stage-countdown-and-focus-rounds.webp` → `/blog/run-stage-countdown-and-focus-rounds.webp` |
| 11 | `launch-etsy-batch-with-seller-studio` | Launch a Product Batch With Seller Studio | Wrong/reused packing scene — now product batch listings | `images/launch-etsy-batch-with-seller-studio.webp` → `/blog/launch-etsy-batch-with-seller-studio.webp` |
| 12 | `price-after-marketplace-fees-seller-pricing-desk` | Price Products After Marketplace Fees | Wrong/reused scene — now fee pricing sheet | `images/price-after-marketplace-fees-seller-pricing-desk.webp` → `/blog/price-after-marketplace-fees-seller-pricing-desk.webp` |
| 13 | `free-tools-for-marketers` | The Toolkit Every Marketer Actually Uses | Generic marketer stock — now UTM/campaign toolkit UI | `images/free-tools-for-marketers.webp` → `/blog/free-tools-for-marketers.webp` |
| 14 | `free-toolkit-every-developer-actually-uses` | The Toolkit Every Developer Actually Uses | Generic developer stock — now JSON/regex/Base64 tools | `images/free-toolkit-every-developer-actually-uses.webp` → `/blog/free-toolkit-every-developer-actually-uses.webp` |
| 15 | `how-to-stay-productive-when-company-blocks-ai-tools` | Staying Productive When Your Company Blocks Chat Assistants | Generic office — now local PDF tools + AI blocked policy | `images/how-to-stay-productive-when-company-blocks-ai-tools.webp` → `/blog/how-to-stay-productive-when-company-blocks-ai-tools.webp` |

**Total heroes:** 15
