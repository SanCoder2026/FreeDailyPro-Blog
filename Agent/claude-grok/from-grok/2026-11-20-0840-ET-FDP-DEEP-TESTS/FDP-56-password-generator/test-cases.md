Sent: 2026-11-21 10:59 ET

# FDP-56 test cases (guest)

| ID | Input / steps | Expected | Today |
|---|---|---|---|
| G01 | Page load | password shown, no charge | PASS |
| G02 | Generate ×5 | 5 distinct, no charge | PASS |
| G03 | Copy at 10/10 | cap dialog if counted / copy if uncounted | Copies, no dialog, no POST (policy question) |
| G04 | Copy with uses left | per owner decision | NOT RUN (all contexts 10/10) → RERUN-AFTER-RESET |
| P04 | How many 10 | 10 distinct, length 16 | PASS |
| P05 | Exclude look-alikes ×500 | no I l 1 O 0 o \| | PASS (0/500) |
| P06 | Empty symbols box | alert + default set | PASS |
| P07 | Spaces-only symbols box | default set (as the alert says) | **FAIL**: spaces used |
| P08 | "abc#" in symbols box | only symbols | WEAK: letters accepted |
| P09 | Length 4 / 64 | 22.0 bits Weak / 413.4 bits | PASS |
| P10 | Only numbers, length 4 | last type locked; 13.3 bits | PASS |
| P12 | Hide, then Copy | masked; real text copied | PASS |
| P13 | Passphrase default / 10 caps none / 3 no number | 73.6 / 139.2 / 38.8 bits | PASS |
| D01 | Brute-force entropy count | equals the site's Z() | PASS (10,720) |
| M01 | 10 devices, 10 locales, 6 geo | renders, banner in EU | PASS (banner de/fr verified in screenshots); locale UI English |
