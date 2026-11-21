Sent: 2026-11-21 17:25 ET

# FDP-76 test cases

Harness = the tool's rule engine under node (`scripts/px76-harness.js`, cases in `px76-cases.json`). Every live case below matched the harness exactly.

| ID | Input / action | Expected | Result |
|---|---|---|---|
| Z01–Z06 | 10/10: Paraphrase ×2, no-change, French, Rewrite again, Copy | Counted or gated (owner) | **All work; 0 POSTs; no dialog (owner question)** |
| L01–L17, L90–L91 | 0/10 (Firefox): 15 Paraphrase presses, Rewrite again ×2, Copy ×2, reload | 1 use per Paraphrase (page/blog) | **0 POSTs; stays 0/10** |
| H07 / L07 | "Don't forget to call me. I can't wait." Strong | Remember to call me. I cannot wait. | **"Remember to forget to call me." (P1)** |
| H08 / L05 / C01 | Same, Medium | Remember to call me. | **"Remember to to call me." + U+E003 on Copy (P1)** |
| H12 / L08 / C02 | "But we stayed. So we won. Also, it rained." Strong | However, we stayed… In addition, it rained. | **"That said,But we stayed… In addition,, it rained." + 5 PUA chars (P1)** |
| H28 | "Please don't forget the keys." Strong | Please remember the keys. | **"Please remember forget the keys." (P1)** |
| C03 | Restore the nested highlight | Original back | **"RememberDon't forget to call me." (P1)** |
| H01–H03 / L01 | a problem / a method / an idea / an important / a goal | Article fixed | **"a issue", "a approach", "an concept", "an significant", "a aim" (P2)** |
| H04 / L09 | "Quite a few people came, and a few left early." Light | Sensible | "a handful of left early" (P2) |
| H05–H06 / L10 | "I also want…", "However hard we try" | Grammatical | "I as well want", "That said hard" (P2) |
| H10 / H11 | "We left early because the road was icy." Strong, seeds 0/1 | Reorder | Reorders on seed 0 only (documented) |
| H09 | "We do not know. I will call you. They are late." Strong | Contract | PASS |
| H14 / H15 / H24 / H25 / H26 | Quote, caps, due to, thank you, quick | Swaps | PASS |
| H16 / L11 | "The cat sat on the mat today." | No-change note, no use | PASS |
| H18 / H19 / L12 | French, Hindi | Not-English note | PASS |
| H20 | Mixed lines with Hindi | Hindi line passed through | PASS |
| L14 | Click a highlight | Original restored, count −1 | PASS (4 → 3) |
| Blog | The blog's sample paragraph at 3 strengths | 8 / 11 / 12 changes | Counts match; Strong has PUA (the "In addition,," bug) |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | iPhone SE 9 px; no strip anywhere |
