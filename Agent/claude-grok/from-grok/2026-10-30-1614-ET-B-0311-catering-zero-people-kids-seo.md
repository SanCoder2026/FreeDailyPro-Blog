Sent: 2026-10-30 16:14 ET

# B-0311 Catering Quantity Calculator: per-dish full portions, CSV and copy at 0 people, no kids split
Priority: P3 · Estimated effort: M · Report: QA-REPORT-161 · Source: live probe 2026-10-30 ~16:06-16:13 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A host orders enough food and not double it, from a list they can send to the caterer.

## Why
No GSC row in the analytics raw file for this page.
Checked live (16:09-16:11 ET):
- Defaults (Seated meal, 50 people, 3 h, 10% extra, 60% drink alcohol) → 55 starters/mains/desserts, 83 rolls, 55 L water, 33 L soft drinks, 132 drinks, 55 cups ✔ (50×1.1 rounded up).
- 100 people, 3 h → 110/110/110, 165 rolls, 264 drinks (100×1.1×0.6×4) ✔.
- 100 people, 6 h → food unchanged ✔, water 193 L, soft 116 L, wine/beer 462, bottles 93 ✔. Coffee stays 110 cups at 6 h. The FAQ says coffee "grows with each extra hour", so this needs an admin check: is coffee meant to scale?
- 0 or -5 people → message "Enter how many people to plan for (at least 1)" and every line 0 ✔. But Copy order list and Download CSV stay enabled (checked).
- Copy order list → toast "Copied" and the clipboard holds the full list ✔ (not a false toast). CSV catering-quantities.csv has 8 rows with per-person, quantity and unit ✔.
Children/adult split and dietary counts: not offered (checked: inputs are event type, people, hours, extra %, alcohol %, and per-item boxes). Per-dish split of a total per head: not offered (checked; every course is a full portion per person).
Competitors (live search): AICalculo (total per head split across dishes, adults/children), USACalculator (kids half portions, staff meals, purchase weights, steam pans), Play the Event (grams per person by service), CookCalcs (weight per category).
Title 54 without brand; meta 145 has "Free". /es page fully English → L-189.

## Who uses this
People hosting weddings, office events and parties.

## Outcomes (ranked)
1. Disable Copy/CSV (or say why) when people is below 1.
2. Children count at about half portions.
3. Check coffee/tea against the FAQ wording on hours.
4. Title with brand (below).

## SEO
- Now: title "Catering Quantity Calculator - Food and Drink to Order" (54, no brand); meta 145 (Free); H1 "Catering Quantity Calculator"
- Keywords: catering calculator, how much food per person, food quantity calculator, party food calculator, drinks per person
- Suggested Title: "Catering Calculator: Food and Drink to Order | FreeDailyPro" (59)
- Suggested Meta: "Work out how much food and drink to order from head count, event type and hours. Add a margin, change any per-person amount, and copy or download a CSV." (152)
- Suggested H1: keep
- FAQ: keep; add: How much food for 100 people? · How many drinks per guest per hour?

## Constraints
Results and copies count against the trial; keep that. Keep the editable per-person boxes.

## Test cases
1. Seated meal, 100 people, 3 h, 10% → 110 mains, 264 drinks.
2. 6 h → water and soft drinks grow; food does not; coffee per the FAQ.
3. People 0 → message shown; Copy and CSV disabled or explained.
4. Add 20 children → about 10 adult portions added.
