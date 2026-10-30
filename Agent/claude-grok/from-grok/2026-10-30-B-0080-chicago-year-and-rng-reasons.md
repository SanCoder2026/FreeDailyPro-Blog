# B-0080 Chicago website citation drops the year; Random Number gives no reason for disabled Generate
Priority: P3      Estimated effort: 15–30 min      Report: #83, #84      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Citations should include every date the user typed, and users should always see why a button won't work.

## Why
- Citation Generator, Chicago, Website, Year 2025 (both widths, 00:20 ET): `Smith, Jane. "Understanding Climate Change." National Geographic. Accessed October 30, 2026. https://example.com/article.` The year is missing. APA/MLA/Harvard include it. Chicago 17 (14.206) uses the publication date when one is given.
- Random Number Generator: min "a" or min 0.5 → Generate is disabled with no message. The same tool already explains the unique-count case well ("Only 5 unique values exist…").

## Outcomes
Chicago website includes the year/date when given (keep "Accessed" for undated). RNG shows "Enter whole numbers" for non-integer/invalid min/max/count.

## Constraints
No change to the other styles.

## Test cases
Chicago + website + Year 2025 → output contains "2025". RNG min "a" → message visible; min 0.5 → message.
