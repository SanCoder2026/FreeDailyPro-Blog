Sent: 2026-10-30 14:02 ET

# B-0242 addendum: random-number-generator randomness source (live JS check)
Checked: live page /tool/random-number-generator, its tool chunk /assets/RandomNumberGenerator-CVwA2msA.js (5,287 B) and the imported /assets/random-DRWu2o-X.js (1,978 B), fetched with curl. Copies in report-138/test-cases/.

- **crypto.getRandomValues: 1 hit** (random-DRWu2o-X.js, the default source in the number function). **Math.random: 0 hits** in either chunk.
- Method: fills a Uint32Array, masks to the bit length of the range and redraws values that fall outside (rejection sampling), so there is **no modulo bias**. Ranges use BigInt, so very large ranges work.
- No repeats: for ranges up to 100,000 it shuffles (partial Fisher–Yates); larger ranges draw and skip duplicates. It errors clearly if the amount exceeds the range ("Range only has N possible unique values"). Decimals are rejected ("must be a whole number (no decimals)"), matching L-180. Amount limit in code: 10,000.

**Effect on B-0242:** the fairness FAQ is accurate. Use: "Is it truly random? → It uses your browser's secure random generator (crypto.getRandomValues) and avoids modulo bias, so every number in the range is equally likely." Drop "(confirm before publishing)". The admin check in QA-REPORT-138 item 1 is closed.
