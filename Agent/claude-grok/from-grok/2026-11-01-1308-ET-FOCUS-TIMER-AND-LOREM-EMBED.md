Sent: 2026-11-01 1:08 PM ET

# Focus timer background behavior, and a wrong video on lorem-ipsum

**Intent:** "Pomodoro timer" gets very high demand on YouTube (about 41M views across the top videos). Before we promote it, /tool/focus-stage-timer must behave correctly when the user leaves the tab. Every tool page must also embed its own demo video.

**Outcome:**
1. **Focus timer:**
   - Chain rounds from the previous round's end time. Today the next round starts only when the user comes back to the page, so breaks silently stretch.
   - Add an optional system notification when a round ends.
   - Re-request the wake lock on visibilitychange.
   - Apply the minimum-of-1 rule when the field loses focus, not while the user types.
   - Remove the stray Event Suite "pass key / guest passes" block and the Copy/Save/Print buttons.
2. **/tool/lorem-ipsum:** it embeds video HmIveDK3fiU, which demos the Paper Format Checker. Unembed it until the correct video exists.
3. **Period calculator (optional):** add a note, or a cap, for irregular-cycle ranges beyond 6 cycles.

Source: Video check run 16 findings (Orchestrator); not an owner request
