# B-0065 Word Counter: sentence count trips on abbreviations; CJK words; add speaking time and keyword density
Priority: P3      Estimated effort: 45–60 min      Report: #73      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Students and writers trust a counter only if its numbers match Word/Docs. Word Counter is close to mature, so this closes the last accuracy gaps and the two features competitors list as standard.

## Why
- 16 cases (Oct 29, 22:47 ET, desktop + mobile). Words, characters (grapheme-aware: emoji counted right), paragraphs and 200k-word input in ~1 s all pass.
- "Dr. Smith met Mr. J. R. R. Tolkien at 9 a.m. in the U.S. It was fun." gives **4 sentences** (expected 2).
- "你好世界。日本語のテキスト。" gives 5 words; Word/Docs count CJK per character (13).
- wordcounter.net, wordcharactercount.com and others list speaking time and keyword density (seo-wire.com 2026 comparison); FDP has neither.
- Page has 179 GA views, and "word count characters" gets 2,320 impressions (CTR is handled by B-0036/B-0043, not here).

## Outcomes
- Sentence splitter ignores common abbreviations and initials.
- CJK/Thai characters are counted per character (or the policy is stated).
- Add Speaking Time (~130 wpm) and a top-10 keyword list. Optional: /tool/character-counter (404 today) redirects here if you agree it helps.

## Constraints
Copying stats stays the counted action; typing stays uncounted.

## Test cases
The two strings above → 2 sentences and 13 words. Regression set WC-01…WC-12 in report #73 still passes.
