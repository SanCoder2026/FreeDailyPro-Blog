# B-0001 Trial exhausted: disable exports, show 0 remaining, never leak or charge without a file
Priority: P1      Estimated effort: 90 min (MUST-DO tonight)

## Goal / why
Paying-conversion path. At 0 remaining, many Premium tools keep export buttons enabled and silently do nothing (or hang), so users think the tool is broken instead of seeing the Day Pass offer. One tool still delivered a file at 0 remaining (revenue leak).

## What to change
Shared trial gate / export button component used by Premium tools. Affected (seen in testing): https://www.freedailypro.com/tool/event-budget-planner, https://www.freedailypro.com/tool/logo-maker, https://www.freedailypro.com/tool/fillable-forms, https://www.freedailypro.com/tool/invitation-card-maker, https://www.freedailypro.com/tool/proposal-builder, https://www.freedailypro.com/tool/relocation-checklist-planner, https://www.freedailypro.com/tool/travel-countdown-planner, https://www.freedailypro.com/tool/rooming-list-planner, https://www.freedailypro.com/tool/event-report-generator, https://www.freedailypro.com/tool/profit-expense-manager, https://www.freedailypro.com/tool/agenda-cue-sheet-builder, https://www.freedailypro.com/tool/travel-planner, https://www.freedailypro.com/tool/event-tax-summary, https://www.freedailypro.com/tool/visitor-lead-capture-sheet, https://www.freedailypro.com/tool/merchandise-order-sheet, https://www.freedailypro.com/tool/invitation-automator, https://www.freedailypro.com/tool/booth-manager, https://www.freedailypro.com/tool/giveaway-branding-manager, https://www.freedailypro.com/tool/accommodation-manager, https://www.freedailypro.com/tool/programme-show-day-planner, https://www.freedailypro.com/tool/rooming-dietary-sheet, https://www.freedailypro.com/tool/document-assembler, https://www.freedailypro.com/tool/booth-layout-planner.
Repro: fresh session, use a Premium tool's export twice (2/day pool), then click any export (CSV/Excel/PDF/Image/ICS/Back up). Actual: button enabled, no file, no message (event-budget-planner CSV/Excel, logo-maker PNG, relocation Image, travel-countdown Back up, Android fillable-forms hangs); on document-assembler the paywall modal opened but a watermarked 4-page PDF still downloaded; booth-layout-planner / event-report-generator PDF sometimes produced at the edge of the limit.
Expected: every export routes through one gate: if allowed=false, open the existing paywall dialog (WE VALUE YOUR USAGE, Day Pass / monthly), deliver no file, and show "0 remaining today" next to the buttons. A use is only charged when a file is actually delivered.

## Acceptance criteria
- At 0 remaining, every export button on the listed tools opens the paywall and delivers no file (check document-assembler, event-budget-planner CSV+Excel, logo-maker, relocation Image, fillable-forms on Android 360px).
- Counter reads "0 remaining" visibly; no silent no-op or spinner hang on any listed tool.
- With uses left, exports still work and decrement by exactly 1 per visit (one visit = one use, as Terms say).
- Avatar-builder 3rd-use test (already passing) still passes.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Changing the 2/day or 10/day limits, prices, or which tools are Premium vs Professional. Government Forms Hub / Travel Countdown trial-meter question (owner decision pending elsewhere).
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (reports #50, #51, #55, #56, #57, #58, #59, #60, #61, #62, #63, #65)
