Sent: 2026-11-21 17:50 ET

# FDP-78 test cases

IDs: dQw4w9WgXcQ (all 5 sizes), jNQXAC9IVRw (first YouTube video: no Max/Standard), lDBgQDbgHmY (FDP's own video), aaaaaaaaaaa (fake).

| ID | Action | Expected | Result |
|---|---|---|---|
| X01–X11 zero (Chromium 10/10) | Get, Download ×3 sizes, ZIP ×2, old video Get/Download/ZIP, reload + Download/ZIP | Gated | Get + preview shown (owner rule P1: save-as); every Download/ZIP → cap dialog, 0 files. PASS for the buttons |
| X01–X11 left (Chromium 0/10, try 13) | Same | 1 use per Download/ZIP | **2 uses for 9 files (P1)** |
| left Firefox | Same | — | No uses-left context in 30 tries (all 10/10) |
| P01–P12 | watch, &t/&list, youtu.be?si, shorts, embed, live, m., music., nocookie, bare ID, no scheme, app=desktop | Parsed | PASS (ID found; tiles) |
| P13 / P14 | channel / playlist | Message | PASS |
| P15 | attribution_link | Parsed ideally | Error message (P3) |
| P16 | vimeo with ?v= | Rejected | PASS |
| P17 | aaaaaaaaaaa | Not found | PASS |
| P18 | jNQXAC9IVRw | Max/Standard left out with a line | PASS |
| P19 | youtube.co.uk | Parsed ideally | Error (P3) |
| P20 | spaces around link | Trimmed | PASS |
| P21 | hello-world | Error | "Video not found" (treated as ID, P3) |
| P22 | v=abc | Error | PASS |
| P23 | gaming.youtube.com | — | Error (P3, legacy host) |
| P24 | /v/ID path | Parsed | PASS |
| P25 | `<script>` | Error, no injection | PASS |
| S01–S04 | Same ID twice / other form / other video then back | Same result | **S02/S03 stuck "Checking sizes…" (P2)**; S04 PASS |
| QB | Quick Buy Day / Monthly | Email dialog / Stripe | PASS (stopped; nothing typed) |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | iPhone SE 9 px; locales English |
