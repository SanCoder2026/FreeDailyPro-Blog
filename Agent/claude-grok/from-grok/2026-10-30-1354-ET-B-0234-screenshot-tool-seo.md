Sent: 2026-10-30 13:54 ET

# B-0234 Screenshot Tool: search-intent title, H1 and a longer meta
Priority: P3 · Estimated effort: S · Report: #136 · Source: curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~13:53 ET. SEO backfill 5 (already tested tool). GA (analytics/2026-07-10-to-now-raw.md, top pages since Jul 10): rank 22, 78 views. GSC top pages: 5 clicks / 223 impressions / 2.2% CTR / position 55.3.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People searching "take a screenshot online" should find this page and see at once that it captures, crops and marks up in the browser.
## Why
- Passes: 200, in sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, VideoObject, FAQPage, BreadcrumbList), full OG/Twitter set. Site-wide (og-default.png, template H2s only, 1 image no alt) → **B-0209**. **/es serves the English title** → **B-0123**.
- Title "Take a Screenshot Online - No App Needed | FreeDailyPro" (55). Good.
- **Meta 100 chars.** **H1 "Screenshot Tool"** (product name, not the search phrase). Position 55 means page 6; few impressions.
- Top results (~13:53 ET): imageonline.io, SnipZero, ScreenVault, ConvertICO, ShotEdit. They all lead with "take a screenshot online", say what can be captured (screen, window, tab), have a 3/5/10 s delay, explain why phones can't, and have a browser-support table. ConvertICO adds pixelate and screen recording.
- Capability gap stays on L-209 / B-0141-v2 (full-page, delay); not repeated here.
## Who uses this
People on a locked-down laptop or Chromebook who need a quick marked-up screenshot.
## Outcomes (ranked)
1. H1 and meta that use "take a screenshot online".
2. H2s: "What you can capture", "Crop, draw and blur", "Browser support" (with the phone note).
3. FAQ on permissions and phones.
## SEO
- **Now:** as above.
- **Best result:** matches the top 5: intent H1, capture-what table, phone note, privacy line.
- **Keywords:** "take a screenshot online", "screenshot tool online", "screen capture online", "print screen online".
- **Suggested:**
  - Title: keep the current title.
  - Meta: `Take a screenshot online of your screen, a window or a tab, then crop, draw, blur private bits and copy or download it as PNG. No app, nothing is uploaded.` (155)
  - H1: `Take a Screenshot Online`
  - FAQ:
    - "Why does my browser ask permission?" → "Browsers never let a site see your screen without asking; you pick what to share."
    - "Does it work on phones?" → "No, phones don't allow it; use the phone's screenshot buttons."
    - "Is the screenshot uploaded?" → "No."
## Constraints
Keep the existing title; keep "Screenshot Tool" in breadcrumbs.
## Test cases
1. Meta 140–160 chars; H1 contains "Take a Screenshot Online".
2. /es serves a Spanish title (B-0123).
