Sent: 2026-11-21 17:04 ET

# FDP-74 reproduce

1. **No trial use:** any guest window (also one whose `fdp-usage-v1` shows 10/10) → https://www.freedailypro.com/tool/ascii-art-generator → type "Deploy" → Copy ASCII Art → paste: the art is copied, the toast says "Copied to clipboard", no dialog, and DevTools shows no `usage.log` POST. Repeat with new text, a new font, Ctrl+C on the art, and after a reload.
2. **Accents:** type "Café Zürich" → the art reads "Cafe Zurich" with the status note. Compare with FAQ "Why can't I type accents…" and Limitations.
3. **Centre trailing spaces:** type "Hi" (Enter) "There friend" → Centre → Copy → the blank line between banners holds 29 spaces.
4. **Video:** https://www.youtube.com/watch?v=knX3VOJhhuo at 0:40 → the browser tab strip shows the Gmail inbox tab.
