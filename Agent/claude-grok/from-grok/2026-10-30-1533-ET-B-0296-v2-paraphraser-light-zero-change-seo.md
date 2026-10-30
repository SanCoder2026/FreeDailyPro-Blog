Sent: 2026-10-30 15:33 ET


Supersedes: B-0296 (2026-10-30 15:27 ET) — removes the trial-use question; owner policy: results count against the trial.
# B-0296-v2 Paraphraser: Light changes nothing on common sentences, snippet without "Free"
Priority: P2 · Estimated effort: S · Report: QA-REPORT-156 · Source: live probe 2026-10-30 ~15:23-15:26 ET (headless, logged out, 1280/390 px), GSC Top 50 pages (analytics raw file), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Every mode should visibly rewrite, so the result is worth the trial use.

## Why
GSC: 2 clicks / 1,710 impressions / 0.1% CTR / position 9.8.
Checked live (15:25 ET), input "We need to finish the report because the deadline is tomorrow. It is very important to help the team.":
- Light → identical text, "0 changes highlighted", counter 9.
- Strong → "Because the deadline is tomorrow, we need to finish the report. It is very significant to assist the team." (3 changes) ✔ grammatical; counter 8; the repeat Light run did not tick.
- Back to Light → the Light result again (0 changes), not stale Strong output: the L-218 stale-mode bug did not reproduce this run.
Medium: not run this batch.
Competitors (live search): Wow1 and Free.ai offer 8 modes with a synonym-strength control and several variations; TotBot offers word locking and click-a-word synonyms; theStacc shows side-by-side highlights. FreeDailyPro positions itself as a non-AI rewriter ("it is not an AI rewriter, so review the result"), which is a fair difference to keep.
FreeDailyPro: word locking and click-a-word synonyms — unverified absence (no such control in the control list, but output interactions were not tried); admin to confirm.
Title 63 (over 60, has "Free"); meta 160 includes "Free". /es title English → L-189. Ad text ("Find Song Lyrics") → L-004.

## Who uses this
Students and writers polishing short passages.

## Outcomes (ranked)
1. When Light makes 0 changes, say so and suggest Medium or Strong.
2. Snippet as below; /es localised.
3. Click a highlighted word to pick another synonym.

## SEO
- Now: title "Rewrite Sentences Online - Paraphrase Text, Free | FreeDailyPro" (63, has Free); meta 160 (has Free); H1 "Paraphraser / Rewriter"
- Keywords: paraphrasing tool, rewrite sentences, paraphrase text, sentence rewriter
- Suggested Title: "Paraphrasing Tool: Rewrite Sentences | FreeDailyPro" (51)
- Suggested Meta: "Rewrite English sentences with hand-checked word, phrase and clause changes. Pick Light, Medium or Strong, see every change highlighted, text stays local." (154)
- Suggested H1: "Paraphrasing Tool – Rewrite Sentences"
- FAQ: Is this AI? · What does each strength change? · Is my text sent anywhere? · Will it keep my meaning?

## Constraints
Copy counting against the trial stays as is. Keep the non-AI, local-only promise.

## Test cases
1. Sample sentence, Light → at least one change, or a "no changes" note suggesting Strong.
2. Strong → clause moved, grammatical (regression).
3. Strong then Light without reload → Light output (L-218 regression).
4. Medium → between Light and Strong in change count.
5. Title ≤60, meta 140–160; 390 px no overflow.
