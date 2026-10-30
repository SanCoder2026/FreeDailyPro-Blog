Sent: 2026-10-30 11:27 ET

# B-0150 Paraphraser: visible result state, labelled controls, named modes
Priority: P2 · Estimated effort: S–M · Report: #111 · Source: QA sweep + live competitor fetch 2026-10-30 11:25 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Make it obvious what happened when you click Paraphrase, and make the tool competitive for searchers.

## Why
At 0 trial uses, clicking gives no output and no visible message. The textarea and strength buttons are unlabelled. The page ranks at position 9.8 with 1,710 impressions but gets only 2 clicks. Paraphraser.io advertises formal, creative and fluency modes.

## Who uses this
Students and writers rewording a paragraph.

## Outcomes (ranked)
1. A clear gated or empty state message on click. 2. aria-labels on the textarea and the strength group. 3. Rename the strengths into user-facing modes (e.g. Simple, Formal, Restructure) built on the existing hand-checked rules.

## Constraints
Stay non-AI and on-device as the page promises; never break grammar.

## Test cases
The sample "…because they showed a big change…" on Strong → the because-clause moves to the front and the result stays grammatical. At 0 trial uses, the click shows a message. get_by_label finds the textarea.
