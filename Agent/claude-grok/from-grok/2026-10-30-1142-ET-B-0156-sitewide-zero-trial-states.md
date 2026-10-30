Sent: 2026-10-30 11:42 ET

# B-0156 Site-wide: no broken states at 0 trial uses
Priority: P2 · Estimated effort: M · Report: #66–#113 ledger · Source: QA ledger + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
At 0 trial uses, every tool tells the truth: it never claims something happened that didn't, never shows a silent blank, and every paywall names the action that was actually blocked.

## Why
Across 14 ledger entries, the 0-trial-uses state behaves differently from tool to tool. Some are outright broken: a false "Copied" toast, a blank result, files silently dropped. Visitors who hit these think the tool is broken, not limited, and leave without trusting the paywall.

## Who uses this
Every logged-out visitor after their daily trial uses, which is the state the paywall exists to convert.

## Outcomes (ranked)
**OWNER DECISION (pending Santosh): should results and copy always stay free, with only downloads counting against trial uses?** Do not change gating policy until he decides. Until then, fix only these broken states:
1. False success: no "Copied" or other success toast when the action was blocked (L-216).
2. Blank output: when a result is withheld, show "Your result is ready. Today's trial uses are used up" plus the paywall, never an empty panel (L-218).
3. Wording: the paywall/inline text names the blocked action ("copy", "generate", "check", "add files"), not "download" for a copy (audit L-210, L-216, L-221, L-224).
4. One counter: the header and the panel show the same remaining count from the same source, and a reload doesn't change it (L-053, L-204, L-023).
5. No silent drops: an upload that is blocked by the trial says so and keeps the file list (L-224).

Affected:
| Ledger / brief | Tool | Behaviour at 0 trial uses | Broken state? |
|---|---|---|---|
| L-023 / B-0051 | audio-comparer | use counted on file select, 9 vs 8 | counter inconsistency |
| L-053 / B-0055 | site-wide | counter differs between server instances | header ≠ panel / reload changes count |
| L-150 | image-to-pdf / password / case-converter | outputs blocked | policy |
| L-180 / B-0115 | random-number-generator | Generate consumes / is blocked | policy |
| L-183 / B-0118 | password-generator | Generate blocked | policy |
| L-204 / B-0136 | monthly-budget-planner | counter 2→0 after one Export CSV | header ≠ panel (unconfirmed) |
| L-210 / B-0142 | emoji-picker | single-emoji copy → paywall | policy; check wording |
| L-216 / B-0148 | ascii-art-generator | "Copied to clipboard" toast while paywall up, clipboard empty | **false Copied toast** |
| L-217 / B-0149 | paper-format-checker | check result fully gated | policy |
| L-218 / B-0150 | text-paraphraser | no output and no message | **blank output, no message** |
| L-221 / B-0153 | invisible-text-generator | copy (the only job) → paywall | policy; check wording |
| L-222 | audio-trimmer | trim runs; "0 remaining today Get a Day Pass to download" | OK (download-gated) |
| L-223 | silence-remover | processes (0:04→0:02), download gated | OK (download-gated) |
| L-224 | audio-merger | **adding files opens the paywall; files silently dropped, nothing listed** | inconsistent with trimmer/silence |

## Constraints
TEST-AND-REVIEW findings only; no pricing changes. Keep the existing trial counts.

## Test cases
At 0 trial uses (fresh logged-out session after 10 uses):
- ascii-art: Copy → no "Copied" toast; clipboard unchanged; the paywall says "copy".
- text-paraphraser: Paraphrase → a visible message or paywall, never an empty output with no explanation.
- emoji-picker / invisible-text: Copy → the paywall text contains "copy", not "download".
- audio-merger: add 2 files → the files are listed, or a message says adding files needs a trial use; never a silent drop.
- Header and panel counters are equal on 5 tools and stay equal after a reload; after one counted action both drop by exactly 1.
