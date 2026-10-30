Sent: 2026-10-30 08:25 ET
# B-0113 Cost of Living: include housing in the headline, label all controls, add metro rent data
Priority: P2      Estimated effort: 1–2 days      Report: #95      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
The salary-needed answer should reflect the real cost of moving. Housing is the biggest difference between cities, so it can't be left out by default. The page should also be usable with a screen reader.

## Why
- testing-guidance/2026-10-30-apyhub-feedback-and-calculator-queries.md: "cost of living comparison" 0/293/pos 77 (not ranking).
- Report #95: Seattle→Austin −7.8% excludes housing; NerdWallet includes metro median rent and home price. 33 controls are unlabeled.
- Strengths to keep: state taxes (NerdWallet has none), editable budget, cited sources.

## Who uses this
People weighing a job offer in another city, remote workers relocating, HR/recruiters justifying location pay, retirees choosing where to live.

## Outcomes (ranked)
1. **Labels** on all city/category inputs and remove buttons. Low effort.
2. **Metro rent prefill** (e.g. HUD Fair Market Rent or Census ACS median rent, dated and cited) used in the headline, with "edit to your rent". Medium effort.
3. **Two headlines**: "with housing" and "excluding housing". Low effort.
4. **Take-home comparison** using the existing state income-tax engine at the entered salary. Medium effort.
5. Snippet/title around "cost of living comparison <city> vs <city>"; per-pair pages for the top metros. Medium effort.

## Constraints
No visible "free"; keep the editable budget; cite the data year.

## Test cases
| # | Check | Expected |
|---|---|---|
| 1 | accessibility tree | 0 unlabeled controls |
| 2 | Seattle→Austin, no rent typed | headline includes the prefilled metro rent and states its source/year |
| 3 | same | the "excluding housing" figure still shows −7.8% (unchanged data) |
