Sent: 2026-11-21 09:47 ET

# FDP-53 test cases (guest)

| ID | Input / steps | Expected | Today |
|---|---|---|---|
| N01 | default 1–100 ×1 | 1 integer, method line | PASS |
| N02 | 20 of 1–100, unique, sorted; Copy; Download | 20 unique sorted; clipboard and .txt match | PASS (3 engines) |
| N03 | 6 unique of 1–5 | specific error, Generate disabled, **old result cleared** | PARTIAL (old result stays) |
| N04 | min 50, max 10 | swapped with a note | PASS |
| N05 | 0.5–1.5, 3 dp ×10 | all in range, 3 decimals | PASS |
| N06 | 1.5 in whole mode | error + "set Decimal places" hint | PASS |
| N07 | 0.05–0.95, 1 dp | trimmed to 0.1–0.9 with a note | PASS |
| N08 | How many 20,000 | 10,000, shows 500, two notes; .txt 10,000 lines | PASS |
| N09 | ±10^20 range | 3 big integers | PASS |
| N10 | "1,000"/"2_000"; "abc"; empty; 0 | accepted; 3 specific errors | PASS |
| N11 | seed class-7B twice; 7C; cleared | same / differs / secure differs; seed warning | PASS |
| N12 | 1–6 ×10,000 download | chi² < 11.07 | PASS (7.99 / 4.27 / 5.77) |
| D01–D10 | 2d6, d20, 3d8+2, 0d6, 2d1, junk, 10000d6, 10001d6, 1d1000001, 2d6-3 | totals and modifiers right; limits enforced | PASS (stale card on errors) |
| C01–C05 | 1, 100, 10,000, 10,001, 0 flips; 10k download | tallies; limits; .txt + tally | PASS |
| L01–L06 | 6/49, 5/69, 50/49, 1/1, 6/100001, 99999/100000 | exact odds; errors; big pick under 1 s | PASS |
| T01–T07 | Unicode + duplicate list; shuffle; 9 of 7; empty; "all"; 10,001 lines; 800 lines | dup warning; errors; cap 10,000; shows 500 | PASS |
| G01 | 0/10 context: Generate/Copy/Download | per owner decision (today: no change) | POLICY |
| G02 | 10/10 context: Copy/Download | per owner decision (today: allowed, no dialog) | POLICY |
| U01 | results announced to a screen reader | live region | FAIL |
| U02 | Enter in a field | generates | FAIL |
| S01 | Share icon / Share this tool | link copied toast | PASS |
| X01 | locales | H1, subtitle and labels translated | FAIL |
