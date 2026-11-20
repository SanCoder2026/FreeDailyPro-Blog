Sent: 2026-11-20 08:40 ET

# Priorities: FDP-15 Word & Character Counter

- **Written:** 2026-11-19 14:59 EST (box `date`, ET). Repro steps are in REPRODUCE.md (R-numbers).

## P1
1. **Paragraph count (R1).** Text with single line breaks (as pasted from Word) shows Paragraphs 1. A blank line that contains a space doesn't split either. The page claims word-processor parity.
2. **Platform-limit verdicts (R2).**
   - X row: 150 Japanese characters gives "OK: 130 left", but X weights CJK as 2, so the post is over.
   - SMS row: any emoji or non-GSM text still uses 160, but one segment is 70.
   - Users are told "OK" for posts that fail or split.
3. **Page copy contradicts features (R3).**
   - "When not to use it": "readability scoring, keyword density … this tool only counts", but both features are on the page.
   - "Tips": only a 200 wpm estimate, yet there is a Speaking Time card.
   - The paragraph claim (see 1) is also false.
4. **Trial-use POLICY QUESTION for Santosh (R4).**
   - Copy stats works at 0 remaining with no charge.
   - /terms says text utilities take no trial use.
   - The Oct 30 owner policy says copy and results count in all tools.
   - The blog says "10 trial usages a day".
   - Not a PASS.

## P2
5. A period inside closing quotes isn't a sentence end (`He said "Stop." Then he left.` gives 1).
6. The idle text box is 38 px tall: computed min-height is 0 despite `min-h-[200px]`.
7. iPhone SE: counts below the fold while typing. No aria-live for counts. Focus is lost after Clear.
8. axe: 12 serious color-contrast nodes on the green "OK: N left" texts.
9. FAQPage has 1 question. The es title says "gratis". 8 English locale copies under a foreign `lang`.
10. Video: old 6-card UI, personal bookmarks bar, PUMA trademark sample, 32 s outro, "Free" wording.
11. Blog: reading-time decimals (1.5 → 1.2 min) the tool doesn't display.
12. No autosave; no unique-words or pages estimate (competitor features).
