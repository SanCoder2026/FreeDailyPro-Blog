Sent: 2026-11-20 08:40 ET

# Reproduce: FDP-15 Word & Character Counter

Open https://www.freedailypro.com/tool/word-counter as a guest. Counting costs no trial use.

- **R1 (paragraphs):**
  1. Type `Para one.` Enter `Para two.` Enter `Para three.` (no blank lines): Paragraphs = 1 (Word shows 3).
  2. Type `Para one.` Enter, space, Enter, `Para two.`: Paragraphs = 1.
- **R2 (platform rows):**
  1. Paste 150 × `あ`: X row "OK: 130 left". On x.com the composer shows the post over the limit.
  2. Paste `Hi 😀 ` plus 100 × `x`: "SMS (one segment) OK: 55 left". A UCS-2 SMS segment holds 70 characters.
- **R3 (copy):** open "Details: when to use it, limits, privacy" and read "When not to use it" and "Tips". Compare with the Reading ease, Top keywords and Speaking Time on the same page.
- **R4 (trial use):** in a context showing 0 remaining (`fdp-usage-v1` usageToday 10 of 10), type text and press Copy stats: "Stats copied", no dialog, count unchanged. Compare /terms ("Text utilities … take no trial use") and the blog line.
- **R5 (quotes):** `He said "Stop." Then he left.` gives Sentences 1.
- **R6 (layout):** at 1366 px the empty box is one line tall. In DevTools the textarea's computed `min-height` is 0px.
