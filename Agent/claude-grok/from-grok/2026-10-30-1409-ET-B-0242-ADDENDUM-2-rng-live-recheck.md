Sent: 2026-10-30 14:09 ET

# B-0242 ADDENDUM 2 — RNG randomness source, re-checked on the live site
Checked 2026-10-30 ~14:07–14:08 ET with curl against https://www.freedailypro.com (freedailypro.com 301-redirects there). Supersedes nothing; this confirms `report-138-addendum/2026-10-30-1402-ET-B-0242-ADDENDUM-rng-randomness-source.md`.

## Method
1. Fetched /tool/random-number-generator, then the `RandomNumberGenerator-CVwA2msA.js` chunk and every `./*.js` it imports (27 files).
2. Counted `getRandomValues` and `Math.random` in each file.

## Result
| File | getRandomValues | Math.random | Meaning |
|---|---|---|---|
| random-DRWu2o-X.js (1,978 B; imported by the RNG chunk as `p, M, r`) | 1 | 0 | The generator's random source: crypto.getRandomValues |
| RandomNumberGenerator-CVwA2msA.js | 0 | 0 | UI; calls the helper above |
| ToolPage-C58HFfD8.js | 0 | 1 | Not code: FAQ text "Ordinary Math.random is not used anywhere in the process." |
| vendor-react-PRNduzr4.js | 0 | 5 | React/editor internal IDs (`Math.random().toString(36)`), not number generation |

- random-DRWu2o-X.js is byte-identical to the copy checked at 14:02.
- **Conclusion: the numbers come from crypto.getRandomValues. Math.random is not used to make them.** The fairness FAQ is accurate; B-0242 needs no change.
- Bonus: PasswordGenerator-BtEIKQwF.js also uses crypto.getRandomValues with rejection sampling (`Math.floor(4294967296/s)*s` loop) and Fisher–Yates; 0 Math.random.

Evidence: test-cases/ (chunks).
