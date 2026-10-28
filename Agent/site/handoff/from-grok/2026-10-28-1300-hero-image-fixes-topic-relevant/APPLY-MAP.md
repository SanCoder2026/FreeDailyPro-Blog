# APPLY-MAP — replace live blog heroes

**Batch:** `2026-10-28-1300-hero-image-fixes-topic-relevant`
**Purpose:** Replace 36 non-standard live heroes (abstract/generic or floating-logo) with topic-relevant people-in-context scenes + owner brand sticker (`brand_image.py`).

## How Claude should apply

For each row below:
1. Take `hero_file` from this folder.
2. Replace the live site hero at `apply_path_on_site` (same basename as the blog slug).
3. Keep the post body unchanged — this batch is **images only**.

| # | Blog slug | Blog title (on site) | Live URL | Hero file to apply |
|---|-----------|----------------------|----------|--------------------|
| 1 | `api-video-audio-image-expansion` | FreeDailyPro API Adds Video, Audio and Image Processing | https://www.freedailypro.com/blog/api-video-audio-image-expansion | `images/api-video-audio-image-expansion.webp` → `/blog/api-video-audio-image-expansion.webp` |
| 2 | `book-writing-toolbox` | Chapters to a KDP-Ready Book, One Pre-flight at a Time | https://www.freedailypro.com/blog/book-writing-toolbox | `images/book-writing-toolbox.webp` → `/blog/book-writing-toolbox.webp` |
| 3 | `bulk-image-batch-processing` | Process Dozens of Images at Once: Bulk Image Tools for Real Work | https://www.freedailypro.com/blog/bulk-image-batch-processing | `images/bulk-image-batch-processing.webp` → `/blog/bulk-image-batch-processing.webp` |
| 4 | `compare-pdf-document-differences` | Compare Two PDFs Side by Side and Spot Contract Changes Fast | https://www.freedailypro.com/blog/compare-pdf-document-differences | `images/compare-pdf-document-differences.webp` → `/blog/compare-pdf-document-differences.webp` |
| 5 | `compound-interest-sip-calculators` | See Compound Growth Clearly: Compound Interest and SIP Tools | https://www.freedailypro.com/blog/compound-interest-sip-calculators | `images/compound-interest-sip-calculators.webp` → `/blog/compound-interest-sip-calculators.webp` |
| 6 | `contract-templates-free-drafts` | Start Contracts Faster With Templates: NDA, Lease and More | https://www.freedailypro.com/blog/contract-templates-free-drafts | `images/contract-templates-free-drafts.webp` → `/blog/contract-templates-free-drafts.webp` |
| 7 | `corporate-safe-tools` | Getting Document Work Done When Chat Assistants Are Blocked | https://www.freedailypro.com/blog/corporate-safe-tools | `images/corporate-safe-tools.webp` → `/blog/corporate-safe-tools.webp` |
| 8 | `favorites-your-own-tools-page` | Build Your Own FreeDailyPro Page With Just the Tools You Love | https://www.freedailypro.com/blog/favorites-your-own-tools-page | `images/favorites-your-own-tools-page.webp` → `/blog/favorites-your-own-tools-page.webp` |
| 9 | `free-audio-tools-voice-memos-podcast-cleanup` | Audio Tools: From Voice Memos to Podcast Cleanup | https://www.freedailypro.com/blog/free-audio-tools-voice-memos-podcast-cleanup | `images/free-audio-tools-voice-memos-podcast-cleanup.webp` → `/blog/free-audio-tools-voice-memos-podcast-cleanup.webp` |
| 10 | `free-browser-tools-no-install-needed` | 10 Browser Tools That Save You From Installing Software | https://www.freedailypro.com/blog/free-browser-tools-no-install-needed | `images/free-browser-tools-no-install-needed.webp` → `/blog/free-browser-tools-no-install-needed.webp` |
| 11 | `free-household-budgeting-and-grocery-tools` | Household Budgeting, Grocery and Family Planning Tools | https://www.freedailypro.com/blog/free-household-budgeting-and-grocery-tools | `images/free-household-budgeting-and-grocery-tools.webp` → `/blog/free-household-budgeting-and-grocery-tools.webp` |
| 12 | `free-legal-document-templates-guide` | How to Create an NDA, Lease or Power of Attorney Online | https://www.freedailypro.com/blog/free-legal-document-templates-guide | `images/free-legal-document-templates-guide.webp` → `/blog/free-legal-document-templates-guide.webp` |
| 13 | `free-menu-invitation-and-print-design-tools` | Menu, Invitation and Print Design Tools | https://www.freedailypro.com/blog/free-menu-invitation-and-print-design-tools | `images/free-menu-invitation-and-print-design-tools.webp` → `/blog/free-menu-invitation-and-print-design-tools.webp` |
| 14 | `free-pdf-toolkit-everyday-workflow` | The PDF Toolkit for Your Everyday Work | https://www.freedailypro.com/blog/free-pdf-toolkit-everyday-workflow | `images/free-pdf-toolkit-everyday-workflow.webp` → `/blog/free-pdf-toolkit-everyday-workflow.webp` |
| 15 | `free-relocation-and-moving-tools` | Tools for Relocating or Moving to a New City | https://www.freedailypro.com/blog/free-relocation-and-moving-tools | `images/free-relocation-and-moving-tools.webp` → `/blog/free-relocation-and-moving-tools.webp` |
| 16 | `free-tools-for-college-students` | Tools for College Students (and the Parents Paying for It) | https://www.freedailypro.com/blog/free-tools-for-college-students | `images/free-tools-for-college-students.webp` → `/blog/free-tools-for-college-students.webp` |
| 17 | `free-tools-for-freelancers-and-solopreneurs` | Freelancers: Stop Paying for Tools You Rarely Use | https://www.freedailypro.com/blog/free-tools-for-freelancers-and-solopreneurs | `images/free-tools-for-freelancers-and-solopreneurs.webp` → `/blog/free-tools-for-freelancers-and-solopreneurs.webp` |
| 18 | `free-tools-for-personal-finance-planning` | Tools for Planning Your Own Finances | https://www.freedailypro.com/blog/free-tools-for-personal-finance-planning | `images/free-tools-for-personal-finance-planning.webp` → `/blog/free-tools-for-personal-finance-planning.webp` |
| 19 | `free-tools-for-small-business-owners` | Tools for Running a Small Business | https://www.freedailypro.com/blog/free-tools-for-small-business-owners | `images/free-tools-for-small-business-owners.webp` → `/blog/free-tools-for-small-business-owners.webp` |
| 20 | `free-tools-for-writers` | A Writer's Toolkit: Tools for Long-Form Work | https://www.freedailypro.com/blog/free-tools-for-writers | `images/free-tools-for-writers.webp` → `/blog/free-tools-for-writers.webp` |
| 21 | `free-travel-and-event-planning-tools` | Tools for Planning a Trip or an Event | https://www.freedailypro.com/blog/free-travel-and-event-planning-tools | `images/free-travel-and-event-planning-tools.webp` → `/blog/free-travel-and-event-planning-tools.webp` |
| 22 | `guide-to-free-health-calculators` | A Practical Guide to Health Calculators: BMI, Calories and More | https://www.freedailypro.com/blog/guide-to-free-health-calculators | `images/guide-to-free-health-calculators.webp` → `/blog/guide-to-free-health-calculators.webp` |
| 23 | `jwt-decoder-debug-tokens` | Decode JWTs Instantly in Your Browser for Auth Debugging | https://www.freedailypro.com/blog/jwt-decoder-debug-tokens | `images/jwt-decoder-debug-tokens.webp` → `/blog/jwt-decoder-debug-tokens.webp` |
| 24 | `language-support-multiple-languages` | FreeDailyPro Now Speaks Your Language | https://www.freedailypro.com/blog/language-support-multiple-languages | `images/language-support-multiple-languages.webp` → `/blog/language-support-multiple-languages.webp` |
| 25 | `magazine-maker-launch` | Your Newsletter Doesn't Have to Look Like a Newsletter | https://www.freedailypro.com/blog/magazine-maker-launch | `images/magazine-maker-launch.webp` → `/blog/magazine-maker-launch.webp` |
| 26 | `mesh-3d-converter` | Converting 3D Print Files Between STL, OBJ, and PLY | https://www.freedailypro.com/blog/mesh-3d-converter | `images/mesh-3d-converter.webp` → `/blog/mesh-3d-converter.webp` |
| 27 | `moving-cost-estimator` | What a Local or Long-Distance Move Might Cost | https://www.freedailypro.com/blog/moving-cost-estimator | `images/moving-cost-estimator.webp` → `/blog/moving-cost-estimator.webp` |
| 28 | `online-timer` | Online Timer With 10 Minute and Pomodoro Presets, No Signup | https://www.freedailypro.com/blog/online-timer | `images/online-timer.webp` → `/blog/online-timer.webp` |
| 29 | `pay-stub-generator` | Make a Pay Stub From the Rates You Actually Withhold | https://www.freedailypro.com/blog/pay-stub-generator | `images/pay-stub-generator.webp` → `/blog/pay-stub-generator.webp` |
| 30 | `publishing-platform-picker-kdp-ingramspark-bn-lulu` | Why Your Book’s Trim Size and ISBN Depend on the Platform You Pick | https://www.freedailypro.com/blog/publishing-platform-picker-kdp-ingramspark-bn-lulu | `images/publishing-platform-picker-kdp-ingramspark-bn-lulu.webp` → `/blog/publishing-platform-picker-kdp-ingramspark-bn-lulu.webp` |
| 31 | `removed-login-requirement-file-tools` | You No Longer Need to Sign In for Any Tool, Including File-Based Ones | https://www.freedailypro.com/blog/removed-login-requirement-file-tools | `images/removed-login-requirement-file-tools.webp` → `/blog/removed-login-requirement-file-tools.webp` |
| 32 | `retirement-calculators-explained` | What Social Security, 401(k) and FIRE Calculators Tell You | https://www.freedailypro.com/blog/retirement-calculators-explained | `images/retirement-calculators-explained.webp` → `/blog/retirement-calculators-explained.webp` |
| 33 | `safe-alternatives-to-chatgpt-for-document-work` | Safe Alternatives to ChatGPT for Document Work | https://www.freedailypro.com/blog/safe-alternatives-to-chatgpt-for-document-work | `images/safe-alternatives-to-chatgpt-for-document-work.webp` → `/blog/safe-alternatives-to-chatgpt-for-document-work.webp` |
| 34 | `shunn-manuscript-onix-preflight-check` | Shunn Format, ONIX and Pre-flight: The Step Writers Skip | https://www.freedailypro.com/blog/shunn-manuscript-onix-preflight-check | `images/shunn-manuscript-onix-preflight-check.webp` → `/blog/shunn-manuscript-onix-preflight-check.webp` |
| 35 | `vendor-quote-comparison` | Compare Vendor Quotes Without Picking Only the Cheapest | https://www.freedailypro.com/blog/vendor-quote-comparison | `images/vendor-quote-comparison.webp` → `/blog/vendor-quote-comparison.webp` |
| 36 | `where-to-get-official-tax-employment-forms` | Where to Find Official W-4, W-9 and I-9 Forms | https://www.freedailypro.com/blog/where-to-get-official-tax-employment-forms | `images/where-to-get-official-tax-employment-forms.webp` → `/blog/where-to-get-official-tax-employment-forms.webp` |

**Total heroes:** 36
