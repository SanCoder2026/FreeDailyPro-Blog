# APPLY-MAP — replace live blog heroes

**Batch:** `2026-10-28-2015-hero-image-fixes`  
**Purpose:** Fix live heroes that failed the locked FreeDailyPro hero rule (topic relevance, no floating logo in scene, unique image per post).

## How Claude should apply

For each row below:
1. Take `hero_file` from this folder.
2. Replace the live site hero at `apply_path_on_site`.
3. Keep the post body unchanged — this batch is **images only**.

| # | Blog slug | Blog title (on site) | Live URL | Hero file to apply |
|---|-----------|----------------------|----------|--------------------|
| 1 | `mail-merge-letters-and-certificates-from-csv` | Mail-Merge Letters and Certificates From a CSV | https://www.freedailypro.com/blog/mail-merge-letters-and-certificates-from-csv | `images/mail-merge-letters-and-certificates-from-csv.webp` → `/blog/mail-merge-letters-and-certificates-from-csv.webp` |
| 2 | `plan-event-one-shared-project-event-suite` | Plan Any Event in One Shared Project | https://www.freedailypro.com/blog/plan-event-one-shared-project-event-suite | `images/plan-event-one-shared-project-event-suite.webp` → `/blog/plan-event-one-shared-project-event-suite.webp` |
| 3 | `install-event-apps-iphone-android` | Install the Event Apps on iPhone and Android | https://www.freedailypro.com/blog/install-event-apps-iphone-android | `images/install-event-apps-iphone-android.webp` → `/blog/install-event-apps-iphone-android.webp` |
| 4 | `one-link-per-exhibitor-trade-show-floor` | One Link per Exhibitor: Running a Trade Show Floor | https://www.freedailypro.com/blog/one-link-per-exhibitor-trade-show-floor | `images/one-link-per-exhibitor-trade-show-floor.webp` → `/blog/one-link-per-exhibitor-trade-show-floor.webp` |
| 5 | `freedailypro-vs-tinywow-privacy-and-free-tier-compared` | FreeDailyPro vs TinyWow: Privacy and Usage Limits Compared | https://www.freedailypro.com/blog/freedailypro-vs-tinywow-privacy-and-free-tier-compared | `images/freedailypro-vs-tinywow-privacy-and-free-tier-compared.webp` → `/blog/freedailypro-vs-tinywow-privacy-and-free-tier-compared.webp` |
| 6 | `run-stage-countdown-and-focus-rounds` | Run a Stage Countdown or Focus Work Rounds | https://www.freedailypro.com/blog/run-stage-countdown-and-focus-rounds | `images/run-stage-countdown-and-focus-rounds.webp` → `/blog/run-stage-countdown-and-focus-rounds.webp` |
| 7 | `capture-event-receipts-against-budget` | Capture Event Receipts Against the Budget Line | https://www.freedailypro.com/blog/capture-event-receipts-against-budget | `images/capture-event-receipts-against-budget.webp` → `/blog/capture-event-receipts-against-budget.webp` |

**Total heroes:** 7
