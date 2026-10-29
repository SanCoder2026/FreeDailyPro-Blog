# B-0016 Small touch targets on mobile (13–16px checkboxes, icons)
Priority: P3      Estimated effort: 45 min

## Goal / why
Mobile usability/a11y across tools.

## What to change
Recurring: 13×13 checkboxes, 16×16 share/icons, sub-16px range sliders and inputs on https://www.freedailypro.com/tool/volume-booster, https://www.freedailypro.com/tool/video-speed-changer, https://www.freedailypro.com/tool/ringtone-maker, https://www.freedailypro.com/tool/book-interior-maker, https://www.freedailypro.com/tool/relocation-checklist-planner, https://www.freedailypro.com/tool/catering-quantity-calculator, https://www.freedailypro.com/tool/seating-chart-planner, https://www.freedailypro.com/tool/name-badge-maker, https://www.freedailypro.com/tool/digital-download-packager, https://www.freedailypro.com/tool/manuscript-formatter, https://www.freedailypro.com/tool/invite-calendar-maker and more. Fix in shared components: min 24×24 (ideally 44×44) hit area for checkbox/range/icon buttons and ≥16px input font on mobile (also avoids iOS zoom).

## Acceptance criteria
- Shared checkbox/range/icon components meet ≥24px hit area at 390px; inputs ≥16px font. No layout overflow introduced.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Visual redesign.
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (reports #46, #53–#65)
