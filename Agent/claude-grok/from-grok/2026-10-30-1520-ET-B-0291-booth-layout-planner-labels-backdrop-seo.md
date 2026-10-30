Sent: 2026-10-30 15:20 ET

# B-0291 Booth Layout Planner: label item fields, upload a hall drawing, snippet
Priority: P3 · Estimated effort: M · Report: QA-REPORT-155 · Source: live probe 2026-10-30 ~15:17-15:20 ET (headless, logged out, 1280/390 px), live competitor search; no GSC rows for these pages in the analytics raw file

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let an organiser lay out a real hall quickly and hand a correct floor plan to the venue and exhibitors.

## Why
Checked live (15:17 ET): hall 30 × 20 m default; "Fill rows (replaces booths)" made 20 booths, "20 booths using 180 sq m of 600 (30%)" ✔ (20 × 9 sq m). Adding a stage (6 × 3 at left 0, top 4) reported "2 overlaps (outlined in red)." ✔; moving it to left 40 reported "1 item is outside the hall." ✔. Presets 10 × 10 ft and 3 × 3 m, metres/feet, PDF paper Letter/A4/Tabloid, PDF/PNG/CSV downloads (gated at 0 trial uses — not a gap). Note on page: it does not check fire, safety or access rules ✔.
Checked live: the selected item's Label, Type, Left, Top, Width and Depth inputs have no accessible name (B-0155).
Checked live: no file input in the control list, so a venue drawing cannot be used as a backdrop.
Competitors (live search): Eventdex places booths over an uploaded layout image with snap-to-grid; BoothGrid sets a name and rent price per booth; Ummah builds on a satellite view; ExpoFP/ExpoMap sell booths on the map.
Snap-to-grid and per-booth price fields on this page — unverified absence (not looked for in this run); admin to confirm.
Ad text inside copy ("Try Office Apps") → L-004. /es title English → L-189.

## Who uses this
Organisers of small expos, craft fairs and trade shows.

## Outcomes (ranked)
1. Name the item-editor fields (B-0155).
2. Upload a hall drawing (PNG/PDF) as a scaled backdrop.
3. Snippet as below; /es localised.

## SEO
- Now: title "Booth Layout Planner - Exhibition Floor Plan, Drag and Drop" (59, no brand); meta 111; H1 "Booth Layout Planner"
- Keywords: booth layout planner, trade show floor plan, exhibition floor plan maker, vendor booth map
- Suggested Title: "Booth Layout Planner: Trade Show Floor Plan | FreeDailyPro" (58)
- Suggested Meta: "Plan an exhibition hall: fill rows of booths in one click, add stages, entrances and aisles, see overlaps and items outside the walls, then export PDF or PNG." (158)
- Suggested H1: keep
- FAQ: Can I use my venue drawing? · Does it work in feet? · Does it check fire rules? · Can I export a booth list?

## Constraints
Keep the overlap and outside-wall checks and the safety disclaimer. Download gating unchanged.

## Test cases
1. Default hall, Fill rows → 20 booths, 180 of 600 sq m (regression).
2. Stage at left 0, top 4 → "2 overlaps"; left 40 → "1 item is outside the hall".
3. Each item-editor field announces its label in a screen reader.
4. Upload a 30 × 20 m drawing → booths align to its scale.
5. Title ≤60, meta 140–160; 390 px no overflow.
