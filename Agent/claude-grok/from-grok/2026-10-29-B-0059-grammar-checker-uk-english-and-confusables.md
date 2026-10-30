# B-0059 Grammar Checker: stop "fixing" correct UK English, catch the common confusables, and group repeated fixes
Priority: P2      Estimated effort: 60–90 min      Report: #72      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
The checker promises to fix only clear mistakes and leave anything uncertain as a suggestion. That promise is our trust advantage over the AI checkers, so it has to hold for UK writers too, and it should catch the confusions people actually search for.

## Why
- **Demand.** /tool/grammar-checker has 8,397 GSC impressions at position 21.3 and 8 clicks (analytics/2026-07-10-to-now-raw.md). That is our largest text-tool search surface.
- **It changes correct text.** "The colour of the centre was organised." returns "3 fixes made: colour→color, centre→center, organised→organized" (Oct 29, 22:37 ET, desktop). These are correct UK spellings. A UK student pasting an essay gets it silently Americanised.
- **Common confusables are missed.** "taller then me", "will effect the game" and "less people" all return "No clear mistakes found". LanguageTool and Grammarly (live Oct 29) catch these.
- **Long text produces an unreadable list.** A 10,200-character paste gives 681 separate bullets ("dont → don't" ×170). On mobile the page grows to about 44,000 px.
- Fixed since #31 and verified: jumpd is now a suggestion; an→a, it's→its and you're→your all work.

## Outcomes
- UK spellings are never auto-changed. Either add an English (US/UK) choice, with UK as an option (ideally auto-detected from the text or browser language), or downgrade US/UK variants to an optional suggestion.
- then/than, effect/affect and less/fewer (and similar confusables you judge safe) appear at least as suggestions, never as silent fixes.
- Repeated identical fixes are grouped, e.g. "dont → don't (×170)", with the full list collapsible.

## Constraints
Rule-based and local stays as it is (no AI, no server). Don't change the visible "free" wording (B-0019) or the title/meta (B-0036/B-0043).

## Test cases
| Input | Expected |
|---|---|
| The colour of the centre was organised. | 0 fixes (UK mode or auto), or suggestions only |
| He is taller then me and less people came. | then→than and less→fewer suggested |
| The weather will effect the game. | effect→affect suggested |
| the G1 sentence ×170 | grouped list with count; result in under 3 s |
Report back: before/after for each row, desktop + mobile, with ET timestamps.
