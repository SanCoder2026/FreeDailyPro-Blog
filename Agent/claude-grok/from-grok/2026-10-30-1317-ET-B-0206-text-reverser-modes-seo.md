Sent: 2026-10-30 13:17 ET

# B-0206 Text Reverser: emoji-safe reversal, all modes at once, and a title that matches "reverse text"
Priority: P2 · Estimated effort: S · Report: #127 · Source: QA sweep + SEO curl check + live Google top-3 (WebSearch) 2026-10-30 13:14 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People searching "reverse text" should land on a page that clearly does that, show every mode at once, and never break emoji or accents.
## Why
- It has 8 actions (Reverse Text, Each Word, Lines, Words, dedupe lines/words, Sort A–Z/Z–A).
- At 0 trial uses, Reverse → the trial-uses dialog, so whether `Héllo 👋 wörld / é` (combining accent) survives is **untested**. Limit kept by owner, so that isn't a gap.
- Top Google results (13:14 ET):
  - textreverse.io shows 6 modes live side by side, including upside-down and mirror.
  - hirantha.me reverses grapheme clusters so emoji and accents stay intact.
  - codeshack and browserling: live as you type.
- Labels → B-0155. Status → B-0187.
## Who uses this
Social-media users making backwards or upside-down text, puzzle makers and developers.
## Outcomes (ranked)
1. Reverse by grapheme cluster (Intl.Segmenter): emoji, flags and combining accents stay whole.
2. Show all reverse modes live, each with its own Copy.
3. Add upside-down and mirror modes.
4. Split dedupe into its own clearly named section, or link to Remove Duplicate Lines.
## SEO
- **Now:**
  - Title "Reverse Text, Dedupe Lines - Free | FreeDailyPro" (48 chars).
  - Meta is 87 chars, below 140.
  - H1 "Text Reverser / Deduplicator".
  - H2s are generic ("About…", "Common questions").
  - JSON-LD has SoftwareApplication, FAQPage, BreadcrumbList and VideoObject (valid).
  - Canonical and 11 hreflang are present; locale pages carry English title/H1/meta.
  - In the sitemap; 200 with 0 redirects.
  - (site-wide items: generic OG image, generic H2s, boilerplate meta, empty video alt → B-0209; English metadata on locale pages → B-0123/L-189)
- **Best result** (textreverse.io): H1 "Text Reverser to Reverse Text Online"; FAQ on "How do I make my text backwards?", "Can I reverse text in any language?", "Does it work on mobile?"; examples like "Hello World"→"dlroW olleH".
- **Suggested:**
  - Title: `Reverse Text Online – Backwards, Words & Lines | FreeDailyPro` (59)
  - Meta: `Reverse text instantly: flip letters backwards, reverse word or line order, or reverse each word. Emoji and accents stay intact. Remove duplicate lines too.` (155)
  - H1: `Reverse Text – Write Text Backwards`
  - H2s: "How to reverse text", "Reverse words vs reverse each word", "Does it work with emoji and accents?"
  - FAQ: "How do I write text backwards?" → "Paste it and choose Reverse Text: 'Hello World' becomes 'dlroW olleH'." / "Will emoji break?" → "No — each emoji and accented letter moves as one character."
## Constraints
Keep the existing actions and URL.
## Test cases
1. `Héllo 👋` → `👋 olléH` (the accent stays on e).
2. `e\u0301` → unchanged as one grapheme.
3. Live output for each mode with no extra click.
