Sent: 2026-11-21 12:15 ET

# Live functional findings (FDP-59)

- **probe.json (Chromium, 11:57 EST, 10/10):** no strip, no Quick Buy; Generate disabled for empty and spaces; Generate → 3 drafts, no dialog; Copy ×2 → "Copied!", clipboard = draft; 10/10 after; no usage.log POST.
- **cases.json (Chromium, first context was 0/10):** 14 cases in one load, 0/10 throughout, no usage.log POST. All 14 match `px59-expected.mjs` (text and counts).
- **left-firefox.json (context 0/10 on try 18, 11:54 EST start):** L01 generate, 2 copies; L02 tone Bold; L03 LinkedIn + copy; L03b identical repeat (same drafts); reload (form cleared); L04 generate + copy. 0/10 throughout; POSTs seen were ad trackers only.
- Output issues: C08 empty drafts, C14 broken Indic hashtags, C07 filler tags, C09 stopword tags, C10 "." after Japanese.
