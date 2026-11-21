Sent: 2026-11-21 12:33 ET

# FDP-60: how to reproduce (guest)

## Owner question 1: no trial use taken
1. Fresh profile; open https://www.freedailypro.com/tool/case-converter. No "Trial … remaining" strip, no Quick Buy. Check localStorage `fdp-usage-v1`.
2. At 10/10: type text, click Title Case → converts, no dialog; Copy → "Copied!"; Download .txt → file.
3. At 0/10: convert several times, copy, download, reload, convert → still 0/10; DevTools shows no `/api/trpc/usage.log` POST.

## P2: video
YouTube qv3ivSaFGY8 at 0:44: six style buttons + Copy, "10 free uses daily" and "Pro" badges, bookmarks bar.

## P3: acronym copy
Type "this is NASA calling" → Sentence case → "This is NASA calling". Compare with Details → "When not to use it".

## P3: colon
"the lord of the rings: the return of the king" → Title Case → "…Rings: the Return…".

## P3: abbreviations
"dr. smith arrived at 5 p.m. today. e.g. this one" → Sentence case → "Dr. Smith arrived at 5 p.m. Today. E.g. This one".

## P3: empty restore
Empty box → click UPPERCASE → "Restore original" appears.
