Sent: 2026-10-30 14:16 ET

# B-0252 Case Converter: fix chained-mode garbling, add AP/Chicago title case and code cases, real meta
Priority: P2 · Estimated effort: S · Report: #142 · Source: SEO backfill 8, curl server HTML + seo.py + Google top 5 (WebSearch), 2026-10-30 ~14:15–14:16 ET. Already tested (L-153). GA rank 35, 59 views (`analytics/2026-07-10-to-now-raw.md`); no GSC row in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone fixing caps-lock text or a headline should paste, press one case, and copy a correct result, every time.
## Why
- **Open bug L-153: chained modes garble the text; no download.** Fix before promoting.
- Title "Convert Text Case Online Free - Title, Sentence, Upper" (54), no brand. **Meta 97 chars.** H1 "Case Converter".
- **Top 5 offer (~14:16 ET):** AP/APA vs Chicago/MLA title case choice (Flipper File, Quick Case Converter); small words kept lowercase and acronyms (NASA, API) kept (Clean.tools); code cases camelCase, snake_case, kebab-case, CONSTANT_CASE (ConvertCase.co, Clean.tools); Undo and .txt download (caseconverteronline); "every format at once" list (Flipper File); .txt/.docx input (Flipper File).
## Who uses this
Writers, students and developers cleaning headlines, caps-lock text and variable names.
## Outcomes (ranked)
1. Each mode converts from the original text (or Undo), never compounding (L-153).
2. Title case with style choice; acronyms kept.
3. Code cases; Copy and .txt download.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD; → **B-0209**; /es English → **B-0123**.
- **Keywords:** "case converter", "title case converter", "uppercase to lowercase", "sentence case converter".
- **Suggested:**
  - Title: `Case Converter – Title, Sentence, UPPER | FreeDailyPro` (54)
  - Meta: `Convert text to Title Case, Sentence case, UPPERCASE or lowercase in one click. Short words stay lowercase in titles. Paste, convert, copy; nothing is uploaded.` (160)
  - H1: `Case Converter: Change Text to Title, Sentence or Upper Case`
  - FAQ: "Which title-case rules?" · "Does it keep acronyms?" · "Is my text uploaded?" → "No."
## Constraints
Only describe modes that exist after the fix.
## Test cases
1. "the lord of the rings" → Title → "The Lord of the Rings"; then Sentence → "The lord of the rings" (no garbling).
2. Title ≤ 60; meta 140–160.
