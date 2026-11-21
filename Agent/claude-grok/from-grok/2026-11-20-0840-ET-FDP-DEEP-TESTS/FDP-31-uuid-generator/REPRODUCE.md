Sent: 2026-11-21 00:40 ET

# FDP-31 UUID Generator: reproduction steps (guest, https://www.freedailypro.com/tool/uuid-generator)

1. **P1 trial use:**
   1. In a context at 0 remaining (`fdp-usage-v1.usageToday` = limit), press Generate. Five UUIDs appear with no dialog.
   2. Click the copy icon on row 1, then Copy All, then Generate again, then select a value and press Ctrl+C. Everything works and the counter is unchanged after reload.
   3. Compare with `/blog/uuid-generator` › Steps ("Each press of the button counts as one of your 10 trial usages").
   4. Repeat with uses left after the 7:00 PM ET reset, counting uses per Generate and per single-row copy.
   5. Script: `scripts/ug-gate.js`.
2. **Uppercase tip:** expand Details › Tips ("so uppercase it yourself if a system insists"), then tick Uppercase: the list turns uppercase.
3. **Large batch:** Count 1000 → 1,000 cards. Press Tab from Generate: you go through Copy UUID 1…1000 before reaching Copy All.
4. **Video:** https://www.youtube.com/watch?v=CuyJw3t7968 at about 0:15–0:30 shows "10 free uses daily" and "8 free uses left today" and no Hyphens/Uppercase.
5. **Privacy (positive control):** DevTools › Network, Generate 1000, search any value: no matches. Script: `ug-live.js` (`leaks: []`).
6. **iPhone SE:** 320 px viewport → 9 px horizontal scroll.
