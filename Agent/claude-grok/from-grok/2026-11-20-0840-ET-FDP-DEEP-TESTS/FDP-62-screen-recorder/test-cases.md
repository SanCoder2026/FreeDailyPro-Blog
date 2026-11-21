Sent: 2026-11-21 13:20 ET

# FDP-62 test cases (guest). Scripts in scripts/ (getDisplayMedia stub in the test browser only)

| ID | Steps | Expected | Today |
|---|---|---|---|
| G01 | At cap: record → Download | Cap dialog, no charge | PASS |
| G02 | At cap: player saves clip | Not possible at 0 | **FAIL** (controls allow download) |
| G03 | Uses left: first Download | +1, file | PASS |
| G04 | Record Another → Download in same load | +1 or cap | **FAIL** (free) |
| G05 | After reload at cap | Cap dialog | PASS |
| G06 | Quick Buy Day / Monthly | Email prompt / Stripe (stop) | PASS |
| R01 | Full capture, countdown, pause 3 s | File length excludes the pause | PASS (8.56 s, timer 00:08) |
| R02 | Region drag 10–50 % on letterboxed preview | Output = that region | PASS (642×290, red quadrant) |
| R03 | Camera bubble on | Round bubble bottom-right | PASS |
| R04 | Mic on + system audio | One mixed audio track, meter moves | PASS |
| R05 | Camera + mic denied | Toasts, video + system audio | PASS |
| R06 | No getDisplayMedia | Phone note, Start disabled | PARTIAL (Start enabled, toast) |
| R07 | Firefox take | Works | PASS |
| R08 | Safari take, MP4 | Works, MP4 | NOT TESTED (env crash) |
| R09 | Stop with mic off | Immediate | PASS |
