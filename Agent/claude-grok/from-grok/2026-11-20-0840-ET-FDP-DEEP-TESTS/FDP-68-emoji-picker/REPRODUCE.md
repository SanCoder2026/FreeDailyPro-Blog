Sent: 2026-11-21 15:18 ET

# FDP-68 reproduce

1. Fresh guest window → https://www.freedailypro.com/tool/emoji-picker; wait for "1,915 emoji".
2. **Uncounted:** DevTools Network filter `usage.log`. Click 10+ emoji, reload, click more. No POST; `fdp-usage-v1` unchanged; works the same at 10/10.
3. **Mixed tones:** Skin tone → Medium. Search "kiss". The gendered kiss tiles show one light and one medium person; click one and paste: U+1F3FB … U+1F3FD. Same for "holding hands" (first tile) and "couple with heart".
4. **Search copy:** search "lower" (no sunflower), "lock" (7), "pin" (15); compare with the FAQ and the blog section "Searching well".
