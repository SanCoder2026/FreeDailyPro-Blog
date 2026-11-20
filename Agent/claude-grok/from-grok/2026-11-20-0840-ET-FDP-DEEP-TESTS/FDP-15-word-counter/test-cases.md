Sent: 2026-11-20 08:40 ET

# Test cases: FDP-15 Word & Character Counter (rerun after any fix)

"Today" = observed 2026-11-19 14:46–14:57 EST. The full counting list (W01–W30) with expected values is in `scripts/wc-cases.json`; run it with `node scripts/wc-live.js`.

| ID | Action | Expected | Today |
|---|---|---|---|
| WC-01 | W01–W30 counting cases | All match | 27/30 (W06, W07, W18 fail) |
| WC-02 | Single line breaks, 3 lines | Paragraphs 3 | FAIL (1) |
| WC-03 | Whitespace-only blank line | Paragraphs 2 | FAIL (1) |
| WC-04 | `He said "Stop." Then he left.` | Sentences 2 | FAIL (1) |
| WC-05 | Abbreviation set (Dr., U.S., e.g., p.m., No.) | Correct sentence counts | PASS |
| WC-06 | CJK / Thai / Korean / Arabic words | 9 / 6 / 4 / 2 / 2 | PASS |
| WC-07 | Emoji graphemes | 👍🏽 = 1, ZWJ family = 1 | PASS |
| WC-08 | Reading 250/300/1,000 words | 1 / 2 / 5 min | PASS |
| WC-09 | Speaking 1,000 words | 7 min 42 sec | PASS |
| WC-10 | 281 Latin chars, X row | "1 over" | PASS |
| WC-11 | 150 Japanese chars, X row | Over (weighted) or no verdict | FAIL ("OK: 130 left") |
| WC-12 | Emoji + 100 chars, SMS row | Over / 2 segments | FAIL ("OK: 55 left") |
| WC-13 | 224,000 characters | Counts in < 2 s; long-text note | PASS (0.7 s) |
| WC-14 | Word goal 50 / 10 / 5 | to go / reached / over; progressbar | PASS |
| WC-15 | Copy stats content | All stats, readability, goal, keywords | PASS |
| WC-16 | Copy stats at 0 remaining | Per Santosh's decision | POLICY QUESTION (ungated) |
| WC-17 | Details copy vs features | Consistent | FAIL |
| WC-18 | axe on main after typing | 0 serious | FAIL (12 color-contrast) |
| WC-19 | Counts announced (aria-live) | Yes | FAIL |
| WC-20 | iPhone SE: Words visible while typing | Yes | FAIL (y≈612 vs 584) |
| WC-21 | Idle text box height | ≈200 px | FAIL (38 px) |
| WC-22 | Clear | Empties text and counts; focus to box | PARTIAL (focus to body) |
