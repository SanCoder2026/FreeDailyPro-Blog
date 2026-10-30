Sent: 2026-10-30 13:10 ET

# B-0189 URL Encoder: live output and clear component vs whole-URL results
Priority: P2 · Estimated effort: S · Report: #122 · Source: QA sweep + live competitor fetch 2026-10-30 12:47 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Encoding should show its result as you type, and make it obvious which mode produced it.
## Why
- The tool has a "Whole URL mode" option and a "Decode + as a space" option.
- At 0 trial uses, Encode opens the "You've used today's trial uses" dialog, so the output couldn't be checked → B-0156.
- urlencoder.org mentions "live" ×16 and "charset" ×17 (live fetch).
- Website tool for a live paid encoding API (selection rule 1).
## Who uses this
Developers building query strings and debugging links.
## Outcomes (ranked)
1. Show the result in a separate output box with a Copy button.
2. Optional live mode.
3. Clear errors for invalid input like `%E0%A4%A` ("Incomplete percent-escape at position 7") instead of a silent failure → B-0187 pattern.
4. Optional charset choice (UTF-8 default).
## Constraints
UTF-8 stays the default. Component encoding must match encodeURIComponent.
## Test cases
1. `a b&c=ü/?` (component) → `a%20b%26c%3D%C3%BC%2F%3F`.
2. Whole URL mode on `https://x.y/a b?q=ü` → `https://x.y/a%20b?q=%C3%BC`.
3. Decode `%E0%A4%A` → an error naming the position, with no crash.
4. With "Decode + as a space" on, `a+b` → `a b`.
