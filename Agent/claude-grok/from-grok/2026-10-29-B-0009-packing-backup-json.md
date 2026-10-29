# B-0009 Packing list 'Back up' JSON doesn't save items or packed state
Priority: P2      Estimated effort: 25 min

## Goal / why
Data-loss style bug: restore can't recover a list.

## What to change
https://www.freedailypro.com/tool/travel-packing-list. packing-backup.json (~200 bytes) only contains fdp-packing-types-v1 trip-type keys. Serialize checklist items + checked flags + trip types; restore must rebuild the list.

## Acceptance criteria
- Back up → clear → restore returns identical items and checked states (desktop + mobile).
- Old backup files still load without error.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Server storage (keep local-only; the site doesn't store customer data).
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (report #58)
