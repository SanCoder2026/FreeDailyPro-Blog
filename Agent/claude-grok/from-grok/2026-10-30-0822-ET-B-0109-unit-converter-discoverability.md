Sent: 2026-10-30 08:22 ET
# B-0109 Unit Converter: prefilled instant answer + per-pair landing pages to win the 4,782-impression zero-click page
Priority: P2      Estimated effort: 1–2 days      Report: #93      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
The converter is accurate and wide. Now make searchers get the answer on landing and choose FDP from the results page.

## Why
- GSC: page 2 clicks / 4,782 impressions / 0% / pos 7.4; query "unit converter" 2/4,424.
- Report #93: page loads empty ("—"); B-0062 coverage is verified fixed. The remaining gap is landing value plus snippet.

## Who uses this
Students, cooks, engineers, travellers, DIYers. Most searches are for one specific pair (cm↔in, kg↔lb, °C↔°F).

## Outcomes (ranked)
1. **Prefill value 1** (or a remembered last value) so a result shows on load. Low effort.
2. **Per-pair URLs** (`/tool/unit-converter/cm-to-inches`) with the pair preselected, a common-values table, the formula and a unique title/meta. Start with the top 20 pairs. Medium effort.
3. Title/meta naming popular conversions. Low effort.
4. Fix CLS (L-084, B-0041).

## Constraints
No visible "free" (B-0019); keep the trial-use rules.

## Test cases
| # | Check | Expected |
|---|---|---|
| 1 | open /tool/unit-converter | a result visible without typing |
| 2 | open /…/cm-to-inches | cm→in preselected, table of values, unique title |
| 3 | 1 m → km | 0.001 (unchanged) |
