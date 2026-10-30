Sent: 2026-10-30 14:53 ET

# B-0276 Grammar Checker: lift CTR on high-impression grammar queries
Priority: P2 · Estimated effort: S · Report: QA-REPORT-150 · Source: GSC Top-50 pages (analytics/2026-07-10-to-now-raw.md), live probe 2026-10-30 ~14:50 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Turn the grammar checker's large search impression count into clicks by making the snippet match what searchers type ("grammar check", "online grammar check"), and keep checks trustworthy.

## Why
GSC page: 8 clicks / 8,397 impressions / 0.1% CTR / avg position 21.3. "grammar check" 1/123/0.8%/pos 74.6; "online grammar check" 1/68/1.5%/36.4; "grammar checker -ai" 1/5/20%/4.8 — a non-AI, rule-based checker converts when it ranks.

## Who uses this
Students, job seekers and non-native writers proofreading short text before sending.

## Outcomes (ranked)
1. Title/meta/H1 aligned to "grammar check" and "online grammar check"; /es page serves a Spanish title (L-189).
2. Content states plainly that it is rule-based (no AI rewriting) — matches the "-ai" query that converts.
3. Gaps seen in live competitor research (TextCheck, EyeSift, Scribbr, Grammarly, Microsoft Editor): readability score (Flesch), punctuation checks (comma splices, unmatched quotes), file upload (.docx/PDF), and Canadian/Australian spelling options. TextCheck and EyeSift both pitch "runs in your browser" — FreeDailyPro already does this; say it in the meta.
4. Open items still apply: L-086 ("Me and him goes", "I seen"), L-087 (UK spelling changed to US).

## SEO
- Now: title "Grammar & Spell Checker Online | FreeDailyPro" (45); meta 157 chars and contains "Free"; H1 "Grammar Checker"; /es title in English.
- Keywords: grammar check, online grammar check, spelling and grammar check, grammar checker without AI.
- Suggested Title: "Grammar Checker – Spelling & Grammar Check | FreeDailyPro" (57)
- Suggested Meta: "Check English grammar and spelling online with US or UK spelling. Fixes clear errors, lists unsure ones as suggestions, and keeps your text in your browser." (156)
- Suggested H1: "Grammar Check Online – Spelling & Grammar (US/UK)"
- FAQ: Does it use AI? · Is my text uploaded? · US vs UK spelling? · What does it not catch?

## Constraints
Trial-use gating unchanged. No AI rewrite claims. Do not change URLs.

## Test cases
1. View source: title/meta as above, ≤60 / 140–160 chars.
2. /es/tool/grammar-checker: Spanish title and H1.
3. Paste "Their going to the park tomorow. She dont like it. He has went home. I seen a apple." → their→They're, tomorow, dont, has went fixed; "I seen" flagged.
4. UK mode: "centre's colour" unchanged.
5. URLs, emails, file names, "v2.0" untouched.
6. 390 px: no horizontal overflow.
