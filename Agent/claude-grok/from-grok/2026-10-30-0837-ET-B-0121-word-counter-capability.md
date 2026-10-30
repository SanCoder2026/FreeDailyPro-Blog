Sent: 2026-10-30 08:37 ET
# B-0121 Word Counter: keyword density, speaking time, reading level, sentence-length view, goals (capability gap)
Priority: P2      Estimated effort: 1–2 days      Report: #97      Source: Testing Bot (capability-gap sweep)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Be a credible alternative to wordcounter.net, the category leader, not only a counter.

## Why
- Demand (analytics file): /tool/word-counter GA 179 views, the #3 tool page. GSC query "word count characters" 0 clicks / 2,320 impressions / pos 9.1: high demand, no clicks.
- Verified #97 (counting uses no trial use):
  - "One two three.⏎⏎Four five six seven. Eight?" gives 8 words, 3 sentences, 2 paragraphs. PASS
  - "Dr. Smith went to Washington D.C. on Jan. 5. He left at 3 p.m. today." gives 15 words (correct) but 3 sentences (should be 2). The L-096/B-0065 abbreviation issue is still open; this is new evidence.
  - Chinese "我喜欢学习中文。今天天气很好。" gives 7 words. Google Docs and Word count CJK per character (13). L-096 is still open.
  - The textarea is labelled ("Text to count"). PASS
- Live competitor fetch (08:34 ET), **wordcounter.net**: top 10 keywords and keyword density, speaking and reading time, reading level, sentence-length highlighting (1 / 2–6 / 7–15 / 16–25 / 26–39 / 40+ words), auto-save, daily activity tracking, and optional grammar/plagiarism checks.
- FreeDailyPro shows words, characters, characters without spaces, sentences, paragraphs and reading time only.

## Who uses this
Students meeting essay limits, writers and bloggers, social media managers checking character limits, and people preparing speeches.

## Outcomes (ranked)
1. Keyword density (top 10, with stop-words excluded by default).
2. Speaking time next to reading time.
3. Platform limits at a glance (X 280, meta description ~160, and so on) with over/under colouring.
4. Readability score and a sentence-length highlight.
5. Optional target word count with progress, and local auto-save.
6. The B-0065 accuracy fixes (abbreviations, CJK) stay open there.

## Constraints
Text stays on the device. Keep counting free of trial uses.

## Test cases (ET)
- 08:33 TC-1: plain text counts. PASS
- 08:33 TC-2: abbreviation sentences = 3 (expected 2). FAIL (B-0065)
- 08:33 TC-3: CJK words = 7 (per-character convention 13). FAIL (B-0065)
- 08:33 TC-4: keyword density, speaking time, readability. ABSENT
