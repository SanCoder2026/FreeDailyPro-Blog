Sent: 2026-10-30 14:01 ET

# B-0240 Compress Image: lead with "to KB", brand the title, use an intent H1
Priority: P2 · Estimated effort: S · Report: #138 · Source: curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:00 ET. SEO backfill 6 (already tested tool). GA (analytics/2026-07-10-to-now-raw.md, top pages since Jul 10): rank 29, 68 views. GSC top pages: 2 clicks / 810 impressions / 0.2% CTR / position 14.9.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People who must get a photo under a size limit ("compress image to 100 KB") should see from the result snippet that this page does exactly that.
## Why
- Passes: 200, in sitemap, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, VideoObject, FAQPage, BreadcrumbList), full OG/Twitter set. Site-wide (og-default.png, template H2s, 1 image no alt) → **B-0209**. **/es is Spanish** ("Comprimir imagen en línea: reduce el tamaño, gratis"): a good example for B-0123.
- Title "Compress Image Online - Reduce File Size by %, Free" (51; "Free", no brand). Leads with %, while searchers ask for a KB target.
- Meta 141 chars; mentions "exact size limit" only mid-sentence. H1 "Compress Image".
- 810 impressions at position 14.9 with 0.2% CTR: the snippet isn't winning clicks.
- Top results (~14:00 ET): imgsmaller (KB presets 1 KB–2 MB), ShrinkTo ("exact size", binary search), TabOtter ("fit under" box), PicsFit ("Compress Image to KB", Quality First vs Size First), TinyPNG. Three of five put "KB" or "exact size" in the title.
- Function issue stays on L-115 / B-0066 (dimension lock misses the target); not repeated.
## Who uses this
People filling visa, exam and job forms with a KB cap; sellers and bloggers.
## Outcomes (ranked)
1. Title and meta lead with "to KB / exact size".
2. H1 "Compress an Image to a Target Size (KB)".
3. FAQ "What if it can't reach my size?" (ties to B-0066).
## SEO
- **Keywords:** "compress image to 100kb", "compress image to kb", "reduce image size", "compress jpg".
- **Suggested:**
  - Title: `Compress Image to KB – Exact Size or % | FreeDailyPro` (53)
  - Meta: `Compress a JPG, PNG or WebP image to an exact size like 100 KB, or make it 10%, 25% or 50% smaller, keeping it close to the original. Nothing is uploaded.` (154)
  - H1: `Compress an Image to a Target Size (KB)`
  - FAQ:
    - "How do I compress an image to 100 KB?" → "Choose Exact size, type 100 KB and compress."
    - "What if it can't get that small?" → "Allow smaller dimensions; the tool says so."
    - "Is my image uploaded?" → "No."
## Constraints
Keep the Spanish /es title pattern.
## Test cases
1. Title ≤ 60, meta 140–160.
2. GSC CTR recheck after 28 days.
