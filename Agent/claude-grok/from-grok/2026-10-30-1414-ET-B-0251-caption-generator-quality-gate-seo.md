Sent: 2026-10-30 14:14 ET

# B-0251 Social Caption Generator: gate at Generate hides every result; fix the template meta, add hashtags, length check and variants
Priority: P2 · Estimated effort: M · Report: #141 · Source: Playwright headless, logged out, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:10–14:14 ET. L-243: rank 1, backed by the live "Text and Developer Utilities" API on ApyHub (APYHUB-TRACKER: caption-generator flagged "shallow or ungrammatical" by reviewers). No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone stuck on a caption should type what the post is about and get a few usable, platform-sized drafts.
## Why (1280 px; 0 trial uses)
- Inputs: "What's your post about?", optional detail, Platform (Instagram), Tone (Fun; four tones), "Add a call to action".
- "Generate Captions" stays **disabled until the topic is filled** (fine, but no hint says why).
- **Clicking Generate opens the trial-uses popover; no caption is shown at all**, so a visitor can't judge quality. Gating is the owner's decision; but for a text generator one sample would show value.
- APYHUB-TRACKER records ApyHub reviewers calling the caption-generator output "shallow or ungrammatical" — website and API likely share the generator; quality check needed.
- **Missing vs competitors (~14:12 ET):** 3 variants per run (ContentStudio, CaptionBloom, MyTrendView); hashtags/emoji toggles (ContentStudio, CaptionBloom); length counter vs platform limit (MyTrendView); word-count/length control (ContentStudio); more platforms — TikTok, X, LinkedIn, Threads (all); languages (Hootsuite, CaptionBloom).
- **H1 "Social Caption Generator"** vs breadcrumb category "SEO Tools". Ad text "Find Media Degrees" glued to About → L-004.
## Who uses this
Small businesses, creators and students posting on Instagram/TikTok/LinkedIn.
## Outcomes (ranked)
1. Fix caption quality (grammar, specificity to the detail) — same fix helps the API resubmission.
2. Return 3 variants with a character count per platform.
3. Hashtag and emoji toggles; more platforms.
4. Hint under the disabled button: "Describe your post to start."
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD; → **B-0209**; /es English → **B-0123**.
  - Title "Generate a Social Media Caption Online - Free | FreeDailyPro" (60) — at limit, template wording.
  - **Meta 79 chars, template ("…templates and ideas. Free and fast, right in your browser.").**
- **Keywords:** "caption generator", "instagram caption generator", "social media caption generator", "caption ideas".
- **Suggested:**
  - Title: `Caption Generator for Instagram & Social | FreeDailyPro` (55)
  - Meta: `Write social media captions from a short description: pick the platform and tone (fun, professional, bold or Gen-Z), add a call to action, then edit and post.` (158)
  - H1: `Social Media Caption Generator`
  - FAQ: "Which platforms?" · "Can I add hashtags?" (once built) · "Is it AI?" → state honestly how captions are made.
## Constraints
Don't claim AI or variants the tool doesn't have.
## Test cases
1. Topic empty → button disabled with a visible hint.
2. Admin: topic "Launching our free PDF tools for students this week", detail "free", Instagram/Fun → captions grammatical, mention the detail.
3. Title ≤ 60; meta 140–160.
