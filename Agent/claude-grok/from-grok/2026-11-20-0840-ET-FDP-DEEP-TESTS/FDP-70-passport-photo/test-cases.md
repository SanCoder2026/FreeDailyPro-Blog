Sent: 2026-11-21 15:54 ET

# FDP-70 test cases

| ID | Input / action | Expected | Result |
|---|---|---|---|
| Z01–Z02 | 10/10: upload FDR, preview | Preview | 300 px canvas (below output size) |
| Z03–Z04 | 10/10: Download Single / Print Sheet | Gate | Cap dialog, nothing saved (PASS) |
| Z05–Z06 | 10/10: auto-fit, then Download | Framing free; download gated | PASS |
| L01–L03 | 0/10: US single + sheet | 1 use each | 1 POST for both (P1); 600×600, 1200×1800 6-up |
| L04–L08 | UK single/sheet, Canada sheet, India 50 KB, China | Correct sizes, charged | Sizes PASS; no POST (P1); India 79,577 B > 50 KB (P1) |
| L09–L11 | Auto-fit + US; Upload Different Photo + download | Charged | No POST (P1); head ~42 % (P2) |
| L12–L13 | Reload + download; sheet again | 1 use each | 1 POST, then free (P1) |
| S01–S07 | Chromium: US 50/100, UK 50/240, Canada 100/500 KB | ≤ limit | 50/100 KB over in 3 of 4 (P1); DPI missing (P1) |
| C01 | Non-image | Error | PASS |
| C02–C03 | 300×200 photo; Zoom 400 % | Low-res warning | PASS |
| C04 | Template spec lines (US, SG, Canada, China) | Canvas aspect, unverified note | PASS |
| C05 | Auto-fit with no person | Message | PASS |
| F | Auto-fit on 3 photos × US/UK | Head in range | Outside range, message claims middle (P2) |
| Q / Drive / Camera | Quick Buy; Open from Google Drive; camera | Email / Stripe; sign-in; picker | Stopped; popup closed; native picker (not automatable) |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | PASS (P2/P3 above) |
