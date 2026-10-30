# B-0073 BMI Calculator: search snippet earns no clicks
Priority: P2      Estimated effort: 15 min      Report: #78      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
People searching "bmi calculator online" should see, in the result, why this one is worth the click.

## Why
- GSC (analytics/2026-07-10-to-now-raw.md): "bmi calculator online" 0 clicks / 504 impressions, position 6.8. Page views: 54.
- Current title: "BMI Calculator Online - Metric & Imperial, Free | FreeDailyPro". The meta says only "metric or imperial, instant result, nothing is saved".
- The tool does more than the snippet says (verified #78): healthy weight range in kg/lb, Asian cut-offs, "kg to lose/gain".
- Competitors in the top results: calculator.net (WHO/CDC, adults and children), NHS ("find out if you're a healthy weight… advice on what to do next").

## Outcomes
The title/meta state the differentiators (healthy weight range, Asian cut-offs, kg/lb to reach the range). Track CTR in GSC over 4 weeks.

## Constraints
"Free" in SEO tags is by design. Keep the meta ≤ 160 chars. No content change in the tool.

## Test cases
View source: the new title and meta are present; length ≤ 60 / ≤ 160; the self-canonical is unchanged.
