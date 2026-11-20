Sent: 2026-11-20 08:40 ET

# Desk findings: Word & Character Counter (FDP-15)

- **Sources (2026-11-19):**
  - curl: the tool page and headers, 9 locales and /ar, the blog, /terms.
  - JS: the WordCounter and WordCounterExtras chunks (raw and prettified).
  - WebSearch.
- **Test plan (quoted from TEST-ORDER.md, not re-verified):** row 15, Pro, Text & Writing, "test-plan rank 14: 179 views; 'word count characters' 2,320 impr 0 clicks". **GSC data is not available.**

## Page and SEO
- Title "Word Counter - Count Words & Characters Online | FreeDailyPro". H1 "Word & Character Counter". Meta: "Word count and character count (with and without spaces), plus sentences, paragraphs and reading time as you type…". Self-canonical, 200, in the sitemap (plus the blog, a word-count API use-case page and an "estimate book pages" blog).
- The title matches the "word count characters" query, so 0 clicks on 2,320 impressions (test plan) is more likely a ranking/SERP-feature problem than a title mismatch.
- **FAQPage has one question** ("Do character counts include spaces?"; yes). The visible "Common questions" section also has only that one. The rich features (platform limits, readability, keywords, goal, speaking time, CJK counting) are good FAQ and long-tail material ("character counter for X", "SMS character counter", "reading time calculator").
- **Copy contradictions on the page:**
  - "When not to use it": "readability scoring, keyword density … this tool only counts". But the tool shows Reading ease / Flesch-Kincaid and Top keywords.
  - "Tips": only a 200 wpm estimate, "mentally adjust" for speech. But there is a Speaking Time card at 130 wpm.
  - Details: paragraphs counted "the same way most word processors treat a paragraph break". But blank lines are required (see live §2).
  - The intro says "the words you use most" (true).
- **Locales:**
  - es has a translated title, meta and H1: "Contador de palabras y caracteres **gratis**, en línea". That is "free" wording in site copy (P2 wording). The body is English.
  - pt, fr, de, ja, hi, zh, ko, id: English under the locale `lang`.
  - /ar: 404 (not in hreflang).
  - Since the counter handles CJK, Thai and Arabic well, translated locale pages would be unusually credible for this tool.

## Blog (/blog/word-counter, Oct 17, 2026)
- "Hit a Hard Word Cap Without Guessing in the Dark": solid abstract-cutting workflow.
- "stay aware of 10 trial usages a day—prepare the paste first so each run is intentional". The tool is ungated, so this follows the policy question.
- "Reading time drops from about 1.5 minutes to under 1.2 minutes". The tool shows whole minutes (312 words → "2 min", 248 → "1 min"), so the blog's figures can't be reproduced in the tool (P2).
- "Where counters disagree" is honest about hyphens, em dashes and URLs.

## Engine (code review)
- Words: whitespace split; a token counts if it has a letter or number. CJK, kana and Thai/Korean go through `Intl.Segmenter` with per-character CJK counting. Characters are graphemes via `Intl.Segmenter`.
- Sentences: a careful abbreviation-aware splitter. Its gap is a closing quote or bracket after the terminator.
- Paragraphs: `/\n\n+/` (see live §2).
- Readability: Flesch / FK, English-like scripts only, links removed, "How this was calculated" steps.
- Keywords: stop-word list, ≥2 letters, numbers and CJK excluded.
- Platform rows: plain grapheme counts (see live §4).
- Text above 200,000 characters goes to a Web Worker.

## Competitors (WebSearch, 2026-11-19)
- **WordCounter.net:** unique words, longest/shortest/average sentence, pages, syllables, lines, reading level, reading/speaking/handwriting time, 1–3-word keyword density, **autosave**. Its privacy policy says text goes to its servers.
- **TypeCount:** platform limits as its key feature.
- **Here:** platform limits, readability with shown steps, keywords, goal, sentence-length view, CJK-correct counting, and fully local processing (a privacy differentiator worth stating).
- **Gaps:** autosave/restore, unique words, multi-word phrases, pages estimate (a blog exists for it), X-weighted and SMS-segment counting.

## Clusters
- Not listed in DUPLICATES.md.
- Related: reading-level (C47) overlaps with the readability card here. Keep both; cross-link "Reading level" for the deeper analysis.
