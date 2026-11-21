Sent: 2026-11-21 00:40 ET

# FDP-31 UUID Generator: test cases

- **URL:** https://www.freedailypro.com/tool/uuid-generator, guest. Default Count 5, Hyphens on, Uppercase off.
- **"Live"** = 2026-11-21 00:17–00:36 EST.
- **Scripts:** `ug-live.js` (U ids), `ug-gate.js`, `ug-share.js`, `ug-misc.js`, `run-matrix.js`.

| ID | Step | Expected | Live |
|---|---|---|---|
| UG-01 | Count 5, Generate | 5 v4 UUIDs | PASS |
| UG-02 | Count 1 | 1 | PASS |
| UG-03 | Blank | Disabled + "Enter how many UUIDs you want." | PASS |
| UG-04 | 0 | Disabled + "Enter 1 or more…" | PASS |
| UG-05 | -3 | Same | PASS |
| UG-06 | 2.5 | "Enter a whole number, such as 5." | PASS |
| UG-07 | 1001 | Note + 1,000 | PASS |
| UG-08 | 1000 | 1,000 in < 1 s | PASS (~0.38 s) |
| UG-09 | 1e3 | Reject or 1,000 | 1,000 (P3) |
| UG-10 | 999999999 | Note + 1,000 | PASS |
| UG-11 | 007 | 7 | PASS |
| UG-12 | " 12 " | 12 | PASS |
| UG-13 | All output | Valid v4 pattern; unique | PASS (4,025 distinct) |
| UG-14 | Distribution | Variant 8/9/a/b about equal; hex uniform | PASS |
| UG-15 | Hyphens off | Same values, 32 hex | PASS |
| UG-16 | Uppercase on | Same values uppercase | PASS |
| UG-17 | Copy All after toggles | Displayed form, newline-separated | PASS |
| UG-18 | Copy UUID 1 | That value; toast | PASS |
| UG-19 | Network scan | No generated value in any request | PASS |
| UG-20 | Reload | List cleared (as documented) | PASS |
| UG-21 | Share | Tool URL only | PASS |
| UG-22 | At 0: Generate | Per policy | **Policy question**: works, 10 → 10 |
| UG-23 | At 0: Copy UUID 1 / Copy All / Ctrl+C | Per policy | Policy question: work, 10 → 10 |
| UG-24 | With uses: Generate | One use? (blog says yes) | **PENDING** (RERUN row 31) |
| UG-25 | With uses: 5 single-row copies | Not 5 extra uses? | **PENDING** |
| UG-26 | Invalid count after a batch | List cleared or dimmed | FAIL (P3): stale list stays |
| UG-27 | Tips copy vs the Uppercase checkbox | Consistent | FAIL (P2) |
| UG-28 | 10 devices | No overflow | PARTIAL: iPhone SE 9 px |
| UG-29 | Locales + /ar | Translated or no hreflang | PARTIAL: es mixed, 8 English, /ar 404 |
| UG-30 | axe | No serious issues | PARTIAL: label-content-name-mismatch; ad-caption contrast |
