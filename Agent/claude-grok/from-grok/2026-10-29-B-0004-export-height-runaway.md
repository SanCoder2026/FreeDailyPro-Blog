# B-0004 Image / print-shop PDF exports come out absurdly tall
Priority: P1      Estimated effort: 75 min

## Goal / why
Broken core output on Premium print tools: users can't print or share the result.

## What to change
Export renderer used by https://www.freedailypro.com/tool/invite-calendar-maker, https://www.freedailypro.com/tool/menu-card-maker, https://www.freedailypro.com/tool/invitation-card-maker, https://www.freedailypro.com/tool/relocation-checklist-planner.
Actual: invite-calendar-maker 'Download as Image' with Finished width 5in → PNG 2550×9031 (~30in tall, mostly empty gradient). menu-card-maker Image → 2550×12195; desktop 'print-shop PDF (0.125in bleed)' → 5.75×26.55in. invitation-card-maker Image → 2550×9031, desktop bleed PDF 5.25×17.957in. relocation-checklist-planner Image → 716×4550 (mobile).
Expected: image/PDF size = finished size × DPI (+bleed), height bound to content/finished size; long checklists paginate or cap height (offer PDF). Letter PDFs (8.5×11) already OK, keep them.

## Acceptance criteria
- invite-calendar-maker and invitation-card-maker 5in card: PNG ≈ card aspect at 300 dpi, no huge empty band.
- menu-card-maker and invitation-card-maker bleed PDFs = finished size + 0.25in on desktop and mobile.
- relocation-checklist image is shareable (paginated or capped) and a PDF option exists or is linked.
- Letter PDF exports unchanged.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Redesigning templates.
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (reports #54, #55, #57, #59)
