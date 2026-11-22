Sent: 2026-11-21 19:08 ET

# FDP-83 test cases (guest)

| ID | Check | Expected | Result |
|---|---|---|---|
| G01 | Gate DOM (Chromium, Firefox) | Paywall, price, terms, no tool | PASS: testids workflow-paywall/subscribe/terms; 0 file inputs |
| G02 | Start 7-day trial | Sign-in first | PASS: /profile sign-in, autoBuy return. Stopped |
| G03 | `?checkout=success` as guest | No payment message | **Message shown, 20 polls, then gone (P3)** |
| G04 | 11 page links | 200 | PASS (all 200) |
| G05 | Keyboard | CTA reachable | PASS (24 Tabs) |
| G06 | Share this tool | Share | Button present (no dialog in headless) |
| G07 | Workflow Products page | Card | PASS |
| G08 | Universal File Converter cross-link | Links to Studio | PASS (3 links) |
| D01 | FAQ vs Studio code | Match | PASS: 5 starter recipes, {n:3}, 200 MB audio/video, Pause/Stop/Retry, CSV columns, run log, recipe pack, GIF first frame |
| D02 | Guide blog vs code | Match | PASS |
| D03 | Meta / title / JSON-LD | Clean | Meta truncated (P2); Offer 29.99 USD monthly OK |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable, translated | iPhone SE 9 px; **locales English (P2)**; $29.99 everywhere |
| S | Studio functions | — | UNTESTED (sign-in + trial) |
