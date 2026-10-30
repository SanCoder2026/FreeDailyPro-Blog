Sent: 2026-10-30 15:20 ET

# B-0292 Booth Manager: floor layout step shows 0 of 2 assigned booths
Priority: P2 · Estimated effort: M · Report: QA-REPORT-155 · Source: live probe 2026-10-30 ~15:17-15:20 ET (headless, logged out, 1280/390 px), live competitor search; no GSC rows for these pages in the analytics raw file

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
One project where exhibitors, their booths, leads and badges stay in step.

## Why
Checked live (~15:19 ET) with "Try a sample": 3 exhibitors; Northwind A1 fee $900 paid $900; Contoso A2 fee $900 paid $300 owes $600; Fabrikam no booth. Tiles: Booked or paid 2, Fees agreed $1,800, Received $1,200, To collect $600 — sums correct ✔. Step header says "2 booths assigned".
Finding (checked live): step 2 "Floor layout" then shows "0 booths using 0 sq m of 600 (0%)" — booths A1 and A2 from the sample are not drawn, so the layout does not reflect the assignments. Admin to confirm whether the layout is meant to be linked.
Step 3 Lead capture: name, company, phone, email, interest, notes, Hot/Warm/Cold, thank-you template with {name}/{interest}/{company} ✔. Step 4 Badges: sample has 8 guests; default filter "Confirmed and attended" gives "5 badges, 1 sheet"; Avery 5392 (Letter) and L7165 (A4) presets, own grid, QR pass option, "Print at 100%" note ✔.
Competitors (live search): ExpoMap and ExpoFP assign exhibitors to booths on the map and show availability; Ummah places vendors from the roster ("never a separate spreadsheet that drifts").
/es title English → L-189. Ad text ("Compare Browsers") → L-004. Several step buttons have no accessible name (B-0155).

## Who uses this
Organisers running a small exhibition without paid event software.

## Outcomes (ranked)
1. Booths assigned in step 1 appear (labelled with the exhibitor) in step 2, or the page says the two are separate.
2. Clicking a booth in step 2 lets you assign an exhibitor.
3. Snippet as below; /es localised.

## SEO
- Now: title "Booth Manager - Exhibitors, Booth Layout and Lead Capture" (57, no brand); meta 106; H1 "Booth Manager"
- Keywords: exhibition management tool, trade show exhibitor tracker, booth assignment, lead capture sheet
- Suggested Title: "Booth Manager: Exhibitors, Floor Plan, Leads | FreeDailyPro" (59)
- Suggested Meta: "Run a trade show from one page: exhibitor list with fees and payments, booth floor plan, lead capture sheets and printable badges with QR passes, in-browser." (157)
- Suggested H1: keep
- FAQ: Is my data stored? · How do badges print? · Can exhibitors pay online? · Can I share the floor plan?

## Constraints
Keep "kept in this tab" privacy and the pass-key warning. Download gating unchanged.

## Test cases
1. Try a sample → tiles 2 / $1,800 / $1,200 / $600 (regression).
2. Step 2 after sample → A1 and A2 drawn and labelled Northwind and Contoso.
3. Assign Fabrikam to a new booth in step 2 → step 1 shows the booth.
4. Badges: Confirmed and attended → 5 badges; Every guest → 8.
5. Title ≤60, meta 140–160; 390 px no overflow.
