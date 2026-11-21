Sent: 2026-11-21 14:26 ET

# FDP-65 test cases

| ID | Case | Expected | Result |
|---|---|---|---|
| Z01 | Type at cap | Values | PASS (no POST) |
| Z02 | Copy ×3 at cap | Cap dialog (if counted) | Copies, no dialog (owner Q) |
| Z03 | Ctrl+C from row at cap | Same as Copy | Copies (owner Q) |
| L01–L05 | Uses left: type, copy, new colour, Ctrl+C, reload | Charge per policy | 0 POSTs (owner Q) |
| C | #f60, f60, rgb/rgba, hsl/hsla, hwb, triples, names, transparent | Correct | PASS |
| C | rgb(300,0,0) | Clamp note | PASS |
| C | oklch(70% 0.2 50) | Accepted | PASS (copy says rejected) |
| C | lab(), display-p3, #12345, notacolor | Error, last colour kept | PASS |
| A1 | #ff6600aa | #ff6600aa | FAIL: #ff6600ab |
| A2 | #ff660001 | #ff660001 | FAIL: #ff660000 |
| A3 | #ff6600fe | #ff6600fe | FAIL: #ff6600 |
| A4 | #ff660080 / 1a / cc, #12345678 | Unchanged | PASS |
| LAB | 4 colours vs D50 reference | Equal | PASS |
| FF | Firefox at cap, Copy | — | Copies, no dialog |
