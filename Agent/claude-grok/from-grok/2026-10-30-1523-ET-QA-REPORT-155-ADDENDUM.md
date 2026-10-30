Sent: 2026-10-30 15:23 ET

# QA-REPORT-155 Addendum — admin session ~15:21-15:22 ET
Supplements QA-REPORT-155 (batch 74). Earlier files unedited.

## Booth Manager (B-0292, L-342) — CONFIRMED
The sample tab says "2 booths assigned", but Floor layout draws 0 booths ("0 booths using 0 sq m of 600 (0%)"). The layout is not linked to exhibitor assignments. B-0292 stands as a P2 bug.

## Booth Layout Planner (B-0291, L-341) — correction note
- Snap: B-0291 listed snap-to-grid as "unverified absence". Correction: snap is present (admin, from the help text) and fixed at 0.5 m / 1 ft, with no on/off or size control. The gap is now "snap size not adjustable", not "no snap".
- Per-booth price field: confirmed absent on the live page by admin.
- Downloads verified (batch-74/downloads, default 30 × 20 m hall, Fill rows):
  - floor-plan.pdf: 1 page, US Letter landscape 792 × 612 pt. Title "Exhibition hall", subtitle "30 x 20 m - 20 booths". Hall drawn 705 × 470 pt = 23.5 pt per metre, aspect 1.5 = 30:20 ✔. Grid lines every 47 pt = 2 m, labelled "Grid lines every 2 m" ✔. Booths labelled 1–20 in three rows ✔. No written scale ratio or scale bar beyond the grid note (checked in the file).
  - floor-plan.png: 1600 × 1163 px, RGBA, no DPI tag (checked). Booth edges at about 54 and 214 px on a row = 160 px per 3 m booth ≈ 53.3 px/m; consistent with the hall width ✔.
  - floor-plan.csv: header Label, Type, X (m), Y (m), Width (m), Depth (m), Area, Note, then exactly 20 booth rows ✔. Rows at Y 1, 7 and 13 (9 + 9 + 2 booths), X from 1 to 25 in 3 m steps (wall margin 1 m ✔), each 3 × 3 = 9 sq m; total 180 sq m matches the on-page 180 of 600 ✔. Minor (checked): the file ends without a newline after the last row.
  - Note: every row pair is separated by a 3 m aisle (Y 1→7→13). If "Back-to-back rows" was ticked, rows 1 and 2 should touch; checkbox state at export time was not recorded — admin to confirm.

## Border Radius Generator (B-0293, L-343)
- Admin session (with trial uses) clipboard held exactly "border-radius: 20px;", matching the output ✔ — the copy path works.
- The bug in B-0293 stands: logged out at 0 trial uses, the "Copied to clipboard" toast shows while the clipboard stays empty.
- Click-blocking ad: at 1280 px an ad overlay covered the Copy CSS button and blocked the click (admin). Added to L-004 as a click-blocking ad. My headless sweep did not reproduce it (no ad overlapping controls), so it depends on the ad served.
