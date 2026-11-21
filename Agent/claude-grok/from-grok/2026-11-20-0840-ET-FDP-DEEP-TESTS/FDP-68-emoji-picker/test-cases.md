Sent: 2026-11-21 15:18 ET

# FDP-68 test cases

| ID | Input / action | Expected | Result |
|---|---|---|---|
| Z A01–A08 | 10/10: click, again, search+click, Enter, Ctrl+C, reload+click | Gate or count | All copy, 0 POSTs (Owner question) |
| L A01–A13 | 0/10: 13 copies | Counted | 0 POSTs, stays 0/10 (Owner question) |
| S | 29 searches (heart, flag india, sun, flower, thumbs up, +1, case variants, non-English, nonsense, shortcodes, flags) | Relevant results | PASS; ranking/"uk"/shortcodes P3 |
| Cat | 9 categories + Flags+"india" | Correct groups | PASS (sum 1,906 + 9 components) |
| T0–T5 | Tones on thumbs up, wave, family, couple, handshake, person | Uniform tone | Single-person PASS; 7 two-person emoji mixed (P2) |
| Blog | lock, pin, warning, idea, calendar, check | Blog counts | lock/pin differ (P2) |
| Net | One copy | Usage log? | Only insight.hit beacon |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | PASS (P2/P3 above) |
