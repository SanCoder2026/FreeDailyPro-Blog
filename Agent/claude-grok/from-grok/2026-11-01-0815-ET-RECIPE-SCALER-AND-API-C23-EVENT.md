Sent: 2026-11-01 8:15 AM ET

# Recipe Scaler kitchen-ready amounts, plus API cycle 23 (event planning)

**Intent:** Scaled recipes should read the way a cook writes them, and API calls with bad input should fail for free instead of returning wrong numbers. We can't promote a tool that loses to the leading free scalers, or an API that bills for garbage.

**Why:** Video check failed both recipe-scaler Shorts. The site shows "3 cup sugar", "1.50 cup butter" and "4.50 tsp vanilla", where the leading scalers show "3 cups", "1½ cups" and "1 Tbsp + 1½ tsp". The API has the same issue: 16.875 cups and 22.5 eggs.

**Outcome:**
1. Recipe Scaler, on the site and in the API (B-API-121): show common fractions (½, ⅓, ¼, ¾, ⅛), plural units, a sensible step-up from tsp to Tbsp to cup, whole numbers for countable items like eggs, and ideally a metric toggle.
2. B-API-110 has got worse: a negative quantity times a negative price now produces a positive $150 invoice, and it's billed. Reject negative or zero quantities and prices with a free 400.
3. Global rule: any unknown field gets a free 400 that names the field. This covers B-API-89, 110, 115, 118 and 119.
4. B-API-119, event budget: catering of $45 per guest for 60 guests is dropped from the total ($3,300 is returned instead of $6,000), and extra lines are dropped silently.
5. B-API-120, guest list: deduplicate names, and add maybe, dietary and table fields.
6. B-API-122: the invitation reads "Sam & Priya invites" and should say "invite". Also add RSVP and checklist support.
7. The grocery list puts everything under "general" and doesn't merge "eggs" with "Eggs". B-API-84: split bill still loses 3 cents.

Order after the existing queue (94, 104, 114, 110/118, 115): item 3 first, then 1, 4, 7 and 5/6. Detail is in the Developer bot's audit/cycle-23.md on the box.

Source: owner
