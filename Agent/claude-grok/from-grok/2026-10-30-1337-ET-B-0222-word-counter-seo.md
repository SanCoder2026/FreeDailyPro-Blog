Sent: 2026-10-30 13:37 ET

# B-0222 Word Counter SEO: win the 'word count characters' query and take 'Free' out of the title
Priority: P2 · Estimated effort: S · Report: #132 · Source: curl server HTML (seo.py) + Google top 5 (WebSearch), 2026-10-30 ~13:37–13:40 ET; GA from analytics/2026-07-10-to-now-raw.md

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People who search for a word or character count should see our result, click it, and get their numbers instantly. The page should look like the obvious answer.
## Why
- GA: /tool/word-counter has 179 views since Jul 10 (#7 page site-wide).
- GSC: "word count characters" has 0 clicks from 2,320 impressions at position 9.1. Page one, but no clicks.
- Tool quality is tracked separately: L-096 (sentence and CJK counting) and L-097 (ad inside the stats grid, B-0041).
- Top results (13:38 ET):
  - TextLimits: limit mode, platform presets (SMS 160, X 280, meta title 60), "Why is my count different from Word?"
  - WordCount: goals, a table of common word-count targets, .docx drop.
  - CharCount: pages and speaking time.
  - wordcntr: documents its counting rules.
  - Engram: bytes.
## Who uses this
Students with word limits, writers, social media and SEO people checking character limits.
## Outcomes (ranked)
1. A title and H1 that match both "word count" and "character count".
2. Add H2s that answer the questions people search: "How are words counted?" and "Why is my count different from Word or Google Docs?"
3. A short limits table (X 280, SMS 160, meta description ~160) that fills in a limit when clicked. This is also a capability gap.
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, VideoObject, FAQPage, BreadcrumbList), full OG/Twitter set. Site-wide items (og-default.png, template and footer H2s, 1 video image with no alt) → **B-0209**. **/es serves the English title** → **B-0123**.
  - Title "Word Counter - Count Words & Characters Online, Free" (52; "Free" in the title is against the rule; no brand).
  - Meta 158, good.
  - H1 "Word & Character Counter".
- **Best result:** TextLimits / WordCount: an answer in the first line, a counting-rules FAQ, presets.
- **Keywords:** "word count characters" (GSC), "word counter", "character counter", "character count with spaces".
- **Suggested:**
  - Title: `Word Counter & Character Count – Live | FreeDailyPro` (52)
  - Meta: `Free word counter and character count, with and without spaces. See sentences, paragraphs and reading time as you type. Your text never leaves your browser.` (156)
  - H1: `Word Counter & Character Count`
  - FAQ:
    - "How do I count characters with and without spaces?" → "Paste your text; both counts appear instantly."
    - "Why is my count different from Word?" → state our rule (words are separated by spaces; hyphenated words count as one).
    - "Do line breaks count as characters?" → state our rule.
    - "Is my text uploaded?" → "No."
## Constraints
"Free" goes in the meta only. Keep the meta's privacy claim.
## Test cases
1. The title is 60 chars or fewer, has no "Free" and ends with the brand.
2. The FAQ states the counting rules, and they match what the tool does (pair with L-096).
3. GSC 28-day recheck for "word count characters": CTR above 0.
