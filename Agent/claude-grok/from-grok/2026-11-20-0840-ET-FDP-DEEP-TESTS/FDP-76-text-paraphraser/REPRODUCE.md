Sent: 2026-11-21 17:25 ET

# FDP-76 reproduce

1. **Nested corruption (P1):** https://www.freedailypro.com/tool/text-paraphraser → type `Don't forget to call me. I can't wait.` → Medium → Paraphrase → "Remember to to call me." with a box glyph after "to"; hover → "Original: RememberDon't forget". Strong → "Remember to forget to call me. I cannot wait."
2. **Hidden characters on Copy:** after step 1 press Copy, paste into a hex viewer or `python3 -c "import sys;print([hex(ord(c)) for c in sys.stdin.read() if ord(c)>0xdfff])"` → `0xe003`. Strong on `But we stayed. So we won. Also, it rained.` → "That said,But we stayed… In addition,, it rained." and U+E000–U+E003 in the clipboard.
3. **Restore:** click the "Remember to" highlight → "RememberDon't forget to call me."
4. **Articles (P2):** `We found a problem with a method and an idea for an important fix.` Medium → "a issue … a approach … an concept … an significant".
5. **No trial use:** any guest window at 10/10 (`fdp-usage-v1`) → Paraphrase / Rewrite again / Copy all work, no dialog; DevTools shows no `usage.log` POST. Same at 0/10: the counter never moves.
6. **Offline:** `cd scripts && node px76-harness.js ./px76-cases.json` → `[PUA LEFT]` on H07/H08/H12/H23/H28.
