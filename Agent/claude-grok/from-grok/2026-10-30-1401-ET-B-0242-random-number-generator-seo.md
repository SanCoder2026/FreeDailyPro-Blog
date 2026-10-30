Sent: 2026-10-30 14:01 ET

# B-0242 Random Number Generator: brand the title, explain fairness, add the intent FAQ
Priority: P3 · Estimated effort: S · Report: #138 · Source: curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:00 ET. SEO backfill 6 (already tested tool). GA (analytics/2026-07-10-to-now-raw.md, top pages since Jul 10): rank 31, 66 views. GSC top pages: 4 clicks / 614 impressions / 0.7% CTR / position 11.2.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People wanting a fair number in a range (raffles, classrooms, games) should trust this page enough to click and use it.
## Why
- Passes: 200, in sitemap, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, VideoObject, FAQPage, BreadcrumbList), full OG/Twitter set. Site-wide (og-default.png, template H2s, 1 image no alt) → **B-0209**. **/es serves English** → **B-0123**.
- Title "Random Number Generator - Any Range, Free & Instant" (51; "Free", no brand).
- Meta 139 chars (one short of 140; ends with the generic "instant results in your browser").
- H1 "Random Number Generator" (fine as the exact search phrase).
- Position 11.2: just off page 1.
- Top results (~14:00 ET): W3Schools, MES and inputoutput all say they use crypto.getRandomValues and avoid modulo bias; MES and number-gen offer decimals, seeds, exclusions and dice. Function gaps (decimals; trial use per Generate) stay on L-180 / L-147.
## Who uses this
Teachers, raffle and giveaway hosts, gamers.
## Outcomes (ranked)
1. A meta and FAQ that say how numbers are chosen (secure browser randomness, every number equally likely), if true.
2. H2s "Pick numbers without repeats", "How the numbers are chosen".
3. Brand in the title.
## SEO
- **Keywords:** "random number generator", "random number 1-100", "pick a random number", "random number without repeats".
- **Suggested:**
  - Title: `Random Number Generator – Any Range | FreeDailyPro` (50)
  - Meta: `Pick random numbers in any range, one or many, with or without repeats. Every number in the range is equally likely. Works instantly in your browser.` (149)
  - H1: keep `Random Number Generator`.
  - FAQ:
    - "Is it truly random?" → "It uses your browser's secure random generator (confirm before publishing)."
    - "Can I avoid duplicates?" → "Yes, tick No repeats."
    - "Can I pick 1 to 100?" → "Set min 1 and max 100."
## Constraints
Only claim crypto-grade randomness if the code uses crypto.getRandomValues.
## Test cases
1. Title ≤ 60; meta 140–160.
2. GSC position recheck after 28 days.
