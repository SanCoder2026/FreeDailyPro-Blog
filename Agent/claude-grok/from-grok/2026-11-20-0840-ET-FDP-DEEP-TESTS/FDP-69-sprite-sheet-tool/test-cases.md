Sent: 2026-11-21 15:35 ET

# FDP-69 test cases

| ID | Input / action | Expected | Result |
|---|---|---|---|
| Z01–Z03 | 2/2: combine 8 frames, Generate, Download PNG | Gate | Cap dialog at Generate (PASS) |
| Z04–Z07 | 2/2: split 4×2, frame tiles, ZIP | Gate | **Split + full tiles free (P1)**; ZIP gated |
| Z08 | Reload, split padded sheet, ZIP | Gate | Tiles free (P1); ZIP gated |
| L01–L10 | Uses left: Generate (+JSON), PNG×2, JSON, new Generate pad/extrude, PNG, JSON, split + ZIP | 1 use per result | **1 POST for all (P1)**; outputs exact |
| L11 | Reload, mixed sizes, Generate | Gate at 2/2 | Cap dialog (PASS); mixed sizes → RERUN |
| C01 | Odd 130×65 split 4×2 | Warning | PASS |
| C02 | Split non-image | Error message | Nothing happens (P2) |
| C03 | Combine with non-image | Error | "Couldn't read …" PASS |
| C04 | Columns 0, 999, padding 500 | Clamp / guard | Guard PASS; advice wrong (P2) |
| C05 | Split Columns −3, Rows 0 | Message | Silent 1×1 (P3) |
| Ctx | Tile context menu / drag | — | Allowed (supports P1) |
| Q / Drive | Quick Buy; Open from Google Drive | Email / Stripe; sign-in | Stopped; popup closed |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | PASS (P2/P3 above) |
