Sent: 2026-10-30 10:47 ET
# B-0124 State Tax: note promises a local-tax box that does not exist
Priority: P2 · Estimated effort: S · Report: #103 · Source: QA retest cycle 2, batch 22 calculators/finance sweep

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
What the page says it does should match what it does: either offer the local-tax option the note describes, or remove that sentence.
## Why
The note says local taxes "are not modelled unless you tick the local-tax box", but no box exists on desktop or mobile. Users in MD, NYC, OH or PA towns get a figure that is too low (MD counties add ~2.25–3.2%) and look for a control that isn't there. SmartAsset (fetched live) includes local income tax by location. GSC: "state income tax calculator" 1 click / 17 impr / pos 65.8.
## Who uses this
People comparing take-home pay before a move or job offer, and freelancers estimating state liability in states with local income taxes (MD, NY, OH, PA, IN, MI, KY).
## Outcomes (ranked)
1. Ideally a visible "Include typical local income tax" checkbox for states with local taxes, with the average used shown and labelled as an estimate. Otherwise, remove the sentence.
2. In states with local tax, a one-line warning appears next to the result even when the box is off.
3. Compare all states says whether local tax is included.
## Constraints
Do not change the state-level math; it was hand-checked correct (CA, NY, MD, PA, TX).
## Test cases
| Input | Expected |
|---|---|
| MD single 75,000, box off | 3,198.88 + local-tax warning |
| MD single 75,000, box on | 3,198.88 + county average, labelled |
| TX 75,000 | box hidden or disabled; $0 |
| 390 px | box reachable, no horizontal scroll |
