Sent: 2026-10-30 11:34 ET

# B-0154 Paraphraser: switching strength must re-run on the current mode
Priority: P2 (bug) · Estimated effort: S · Report: #111 addendum · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Each strength button should show its own result, so people can compare Light, Medium and Strong.

## Why
Admin session, 11:30–11:45 ET: after a Strong run, choosing Light or Medium and clicking Paraphrase kept showing the Strong output. Only a page reload gave the correct per-mode result. Users will think the modes do nothing.

## Who uses this
Students comparing rewrite levels.

## Outcomes (ranked)
1. Clicking Paraphrase always uses the selected strength on the original input text, not on the previous output. 2. Changing strength after a run either re-runs automatically or clearly marks the result as out of date.

## Constraints
Keep the hand-checked, non-AI rules and the on-device processing.

## Test cases
Sample text: Strong → clause moved. Then Light (no reload) → only "in order to"→"to" changed. Then Medium (no reload) → 4 changes and no clause move.
