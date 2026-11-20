Sent: 2026-11-20 08:40 ET

# Test cases: FDP-13 Grammar Checker (rerun after any fix)

Expected = what a correct tool should do. "Today" = observed 2026-11-19 14:13–14:17 EST. Full sentence lists: `scripts/gc-cases.json` (FP01–FP28 correct sentences, FX01–FX15 errors).

| ID | Input / action | Expected | Today |
|---|---|---|---|
| GC-01 | FP01–FP28 (28 correct sentences), one at a time | 0 fixes applied; output = input | FAIL: 23 changed |
| GC-02 | "Does she have time…?" / "Did it work…?" / "Can he go…?" / "Should she have called first?" | unchanged | FAIL: has/works/goes/has |
| GC-03 | "I watched it fly over the hill." | unchanged | FAIL: "it flies" |
| GC-04 | "your right to vote", "Your welcome email", "their late father's", "their doing", "Their being late", "gave their all" | unchanged | FAIL: you're/they're |
| GC-05 | "its very best engineer", "Its hard shell" | unchanged | FAIL: it's |
| GC-06 | "a URL", "a USB", "a UI kit", "plan a or plan b" | unchanged | FAIL: an |
| GC-07 | "Santosh reviewed it.", "Priya and Rahul…", "kubectl applies… webhook" | names/terms unchanged (suggestion at most) | FAIL: Santos, Oriya, webfoot |
| GC-08 | "We flew to Bora Bora" | unchanged | FAIL: "Bora" |
| GC-09 | "(i) first item; (ii) second item." | unchanged | FAIL: "(I)" |
| GC-10 | FX01 "i dont know if their going to the party." | I don't know if they're going… | PASS |
| GC-11 | FX02–FX07, FX09, FX14, FX15 | fixed as in gc-cases.json | PASS |
| GC-12 | FX08 "taller then me", FX11 "less people" | suggestion (as page states) | PASS (suggestion) |
| GC-13 | FX10 "Me and him was late." | suggest "He and I were" | FAIL: "him and I were" |
| GC-14 | FX12 "Who's book is this?" | fix or suggest "Whose" | FAIL: missed |
| GC-15 | FX13 "I could care less" | suggestion | FAIL: missed (P2) |
| GC-16 | URL/e-mail/file name: "Puma.com … no-reply@email-in.puma.com … index.html" | untouched | PASS |
| GC-17 | English (UK) with "color/center/gray/organized" | left as written (stated) | PASS |
| GC-18 | 10,801-word paste | completes < 5 s, no false fixes | PARTIAL: 2.5 s, 600 false "she has" |
| GC-19 | Check Grammar and Copy at 0 remaining | per Santosh's policy decision | POLICY QUESTION: ungated |
| GC-20 | Page/FAQ/meta/blog claims vs behaviour | consistent | FAIL |
| GC-21 | axe on main after Check | 0 critical | FAIL: `label` on output textarea |
| GC-22 | Result announced to screen readers | aria-live/status | FAIL: none |
| GC-23 | iPhone SE 320×568 after Check | corrected text visible or scrolled into view | PARTIAL: starts at y≈577 |
| GC-24 | Keyboard: textarea → Tab → Enter | runs Check, visible focus | PASS |
