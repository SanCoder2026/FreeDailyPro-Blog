Sent: 2026-10-30 15:13 ET

# B-0290 ASCII Art Generator: snippet rewrite, download as .txt, more fonts
Priority: P2 · Estimated effort: S · Report: QA-REPORT-154 · Source: live probe 2026-10-30 ~15:12 ET (headless, logged out, 1280/390 px), GSC Top 50 pages (analytics raw file), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Make the page the obvious pick for a README or terminal banner, and let users take the result away as a file.

## Why
GSC: 3 clicks / 427 impressions / 0.7% CTR / position 31.7.
Checked on the live page (15:12 ET): text box (one banner per line), 14 fonts (Standard, Big, Slant, Small, Mini, Banner3, Block, ANSI Shadow, Doom, Graffiti, Ghost, Bubble …), Left/Centre alignment, preview zoom, width readout ("23 characters wide"), and one action button, "Copy ASCII Art". Output matched FIGlet earlier (L-216).
Checked on the live page: no Download .txt or PNG button; Copy is the only export.
Open bug L-216 / B-0156: the toast said "Copied to clipboard" at 0 trial uses while the clipboard stayed empty — not retested this run (admin check). Copy counting against the trial stays as is.
Competitors (live search): patorjk TAAG offers 300+ FIGlet fonts; ascii-images.com previews 332 fonts with Download TXT or PNG per preview.
Ad text inside copy ("Find Song Lyrics") → L-004. /es title English → L-189. "Centre" spelling on a US-English page.

## Who uses this
Developers and hobbyists making banners for READMEs, code comments, CLIs and Discord.

## Outcomes (ranked)
1. Snippet as below (meta now 74 characters; title says "Free").
2. Download as .txt (and PNG) alongside Copy.
3. More FIGlet fonts with a searchable preview.
4. Fix the false "Copied" toast (B-0156).

## SEO
- Now: title "Generate ASCII Art From Text Online - Free | FreeDailyPro" (57, has Free); meta 74; H1 "ASCII Art Generator"
- Keywords: ascii art generator, text to ascii, ascii banner, figlet online
- Suggested Title: "ASCII Art Generator: Text to ASCII Banner | FreeDailyPro" (56)
- Suggested Meta: "Turn text into ASCII art banners in Standard, Slant, Big, ANSI Shadow, Doom and more FIGlet fonts. Preview, align and copy for a README, code or terminal." (154)
- Suggested H1: keep "ASCII Art Generator"
- FAQ: Which font is best for a README? · Will it line up in a terminal? · Can I download it as a text file? · What is FIGlet?

## Constraints
Do not raise copy limits; keep the trial counting as is.

## Test cases
1. "Hello", Standard → matches `figlet Hello` (regression).
2. Download .txt → file equals the preview text, LF line endings.
3. At 0 trial uses, Copy → no "Copied" toast unless the clipboard was written.
4. Two lines of input → two banners.
5. Title ≤60, meta 140–160; 390 px no overflow.
