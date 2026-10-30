Sent: 2026-10-30 15:41 ET

# B-0302 Invisible Text Generator: count 0 silently becomes 1, snippet says Free twice
Priority: P3 · Estimated effort: XS · Report: QA-REPORT-158 · Source: live probe 2026-10-30 ~15:37-15:41 ET (headless, logged out, 1280/390 px), GSC Top 50 pages (analytics raw file), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Users get exactly the count they asked for, or a clear message why not.

## Why
GSC: 2 clicks / 374 impressions / 0.5% CTR / position 14.3.
Checked live (15:41 ET): count 5 → "5 × Braille Blank (U+2800) ready to copy"; Copy → clipboard is exactly 5 × U+2800 and the toast "Copied! Paste it anywhere…" is true ✔.
- Count 501 → clamps to 500 with a "The most you can generate is…" message ✔.
- Count 0 → field keeps "0" but the status says "1 × … ready to copy", no message (checked). Same family as L-221.
Six characters offered: Braille Blank, Hangul Filler, ZWSP, ZWNJ, ZWJ, invisible line break; test box present.
Competitors (live search): invisibletext.io (1–1000, quick lengths 1/5/10/20/50/100, per-character ledger), copyblank.com (presets 1×–100×, tester), invisibletextcopy.com (up to 10,000, single-space character grid).
FreeDailyPro: quick-length preset buttons — not in the control list (checked).
Title 57 with "Free"; meta 96 with "Free". /es title English → L-189. Ad text ("Learn a Language" in the subtitle) → L-004.

## Who uses this
Social users making blank names, bios or messages.

## Outcomes (ranked)
1. Count 0 (or blank) → message "Minimum is 1" and field set to 1, matching the 501 behaviour.
2. Snippet as below.
3. Quick-length presets (1, 5, 10, 50).

## SEO
- Now: title "Invisible Text Generator - Free Blank Text | FreeDailyPro" (57, has Free); meta 96 (has Free); H1 "Invisible Text Generator"
- Keywords: invisible text, blank text copy paste, invisible character, empty character
- Suggested Title: "Invisible Text Generator: Blank Characters | FreeDailyPro" (57)
- Suggested Meta: "Copy invisible text: Braille Blank, Hangul Filler, zero-width space and more, 1 to 500 characters, with a test box to check it works before you paste it." (153)
- Suggested H1: "Invisible Text Generator (Blank Characters)"
- FAQ: Which character works on Instagram? · Why was my blank name removed? · What is U+2800? · How many can I copy?

## Constraints
Copy counting against the trial stays as is. Keep the responsible-use note.

## Test cases
1. Count 5 → clipboard 5 × U+2800 (regression).
2. Count 0 → message and field shows 1.
3. Count 501 → 500 with message (regression).
4. Title ≤60, meta 140–160; 390 px no overflow.
