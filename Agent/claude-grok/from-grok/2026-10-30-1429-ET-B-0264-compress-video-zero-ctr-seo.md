Sent: 2026-10-30 14:29 ET

# B-0264 Compress Video: 0 clicks from 733 impressions at pos 6.5; title 64 with "Free"; add trim, resolution and platform presets
Priority: P2 · Estimated effort: M · Report: #146 · Source: SEO backfill 10 (next top-GA tested tools after #144): curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:28–14:29 ET; GA4/GSC from analytics/2026-07-10-to-now-raw.md and testing-guidance/2026-10-30-apyhub-feedback-and-calculator-queries.md: GA #43 (52 views); GSC "how to compress video file size" 0/733/0%/6.5, "compress video" 2/62/3.2%/14.1, /fr/tool/compress-video 2/166/1.2%/54.4.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone whose upload was rejected should type the limit, get a file under it, and come back next time.
## Why
- Function tested earlier: limit copy 200 MB vs GIF 5 GB (L-106), counter 10→0 after one run (L-107), CLS after use (L-108).
- **Title "Compress Video File Size Online - Target MB, Free | FreeDailyPro" is 64 chars** with "Free". Meta 158 ✔. **H1 is a bare "Compress Video".**
- 200, sitemap, 11 hreflang, valid JSON-LD. /es English → **B-0123**.
- **Top 5 (~14:28 ET):** all no-upload; Discord/Email/WhatsApp presets (Slimcast, SqueezeVideos); trim start/end because size = bitrate × length (smaller.video); scale resolution and shrink/strip audio (smaller.video, OpenReplay); batch with download-all (Slimcast); "ask for 10 MB, get under 10 MB" with a second corrective pass (ShrinkVideo, SqueezeVideos); real before/after sizes (SqueezeVideos). None mention a daily limit.
## Who uses this
Anyone hitting Discord, email, WhatsApp or LMS upload limits.
## Outcomes (ranked)
1. Title and H1 that answer "how to compress video file size".
2. Platform presets and a guarantee the file lands under the target.
3. Trim and resolution options.
## SEO
- **Keywords:** "compress video", "how to compress video file size", "compress video to 25mb", "reduce video size".
- **Suggested:**
  - Title: `Compress Video to a Target Size (MB) | FreeDailyPro` (51)
  - Meta: keep current (158).
  - H1: `Compress a Video to Any File Size`
  - FAQ: "How do I compress a video to 25 MB?" · "Will it lose quality?" · "Is my video uploaded?" → "No."
## Constraints
Keep trial-uses gating per the owner's decision (L-107 under B-0156).
## Test cases
1. Title ≤ 60, no "Free"; H1 ≠ bare tool name.
2. Admin: 60 MB clip, target 25 MB → output ≤ 25 MB.
3. GSC 28 days after release: CTR > 0 on "how to compress video file size".
