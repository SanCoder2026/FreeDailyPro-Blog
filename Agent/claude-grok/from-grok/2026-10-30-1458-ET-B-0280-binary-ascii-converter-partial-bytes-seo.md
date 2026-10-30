Sent: 2026-10-30 14:58 ET

# B-0280 Binary / Hex / ASCII Converter: flag partial bytes and fix the snippet
Priority: P3 · Estimated effort: S · Report: QA-REPORT-151 · Source: live probe 2026-10-30 ~14:55 ET (headless, logged out) + live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Never show a plausible but wrong decode; tell the user how their binary was read.

## Why
Live check: "Hé😀" → binary 01001000 11000011 10101001 11110000 10011111 10011000 10000000, hex 48 c3 a9 f0 9f 98 80, decimal 72 195 169 240 159 152 128 (correct UTF-8). But binary "01000001 0100001" (second group 7 bits) silently decodes to "A!" with no warning. Competitors toolkit.codes, PagesTools and filetity reject or flag non-8-bit groups and invalid UTF-8, and toolkit.codes offers an explicit 7-bit ASCII mode. Title is 65 chars (over 60) and contains "Free"; meta 104.

## Who uses this
Students doing classroom binary exercises, CTF players, developers.

## Outcomes (ranked)
1. Groups that are not 8 bits → visible message naming the group; offer "decode as 7-bit ASCII" when every group is 7 bits.
2. Invalid UTF-8 byte sequences → visible error, not replacement characters.
3. A status line such as "2 groups × 8 bits → 2 bytes".
4. Snippet rewrite.

## SEO
- Now: title "Binary to ASCII Converter Online - Free, Both Ways | FreeDailyPro" (65); meta 104; H1 "Binary / Hex / ASCII Converter".
- Keywords: binary to text, binary translator, binary to ascii, text to binary.
- Suggested Title: "Binary to Text Converter – Binary, Hex, ASCII | FreeDailyPro" (60)
- Suggested Meta: "Convert text to binary, hex and decimal bytes and back, with full UTF-8 so accents and emoji work. All four views stay in sync as you edit, in your browser." (156)
- Suggested H1: "Binary to Text Converter (Binary, Hex, ASCII)"
- FAQ: How do I read binary? · Why 8 bits? · Does it handle emoji? · What is 7-bit ASCII?

## Constraints
Keep the four synced fields and UTF-8 behaviour.

## Test cases
1. "Hé😀" → bytes exactly as above (regression).
2. "01000001 0100001" → error on group 2, no silent "!".
3. "1000001 1000010" (all 7-bit) → 7-bit option → "AB".
4. Hex "c3" alone → invalid UTF-8 message.
5. Title ≤60, meta 140–160; 390 px no overflow.
