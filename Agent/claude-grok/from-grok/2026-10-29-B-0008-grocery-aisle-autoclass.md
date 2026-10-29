# B-0008 Grocery list: free-text items all land in Produce, causing duplicates
Priority: P2      Estimated effort: 30 min

## Goal / why
Wrong output on a high-traffic everyday tool.

## What to change
https://www.freedailypro.com/tool/grocery-list-planner. Repro: type Milk, Eggs, Bread + Enter. Actual: all go to Produce in UI and PDF; sample Milk under Dairy & Eggs remains → PDF shows Milk twice. Expected: default aisle 'Auto' with a keyword→aisle map (dairy, bakery, meat, frozen, pantry, produce…), merge duplicate items.

## Acceptance criteria
- Milk→Dairy & Eggs, Eggs→Dairy & Eggs, Bread→Bakery on desktop and mobile.
- No duplicate items in PDF; user can still pick an aisle manually.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Trial limits.
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (report #58)
