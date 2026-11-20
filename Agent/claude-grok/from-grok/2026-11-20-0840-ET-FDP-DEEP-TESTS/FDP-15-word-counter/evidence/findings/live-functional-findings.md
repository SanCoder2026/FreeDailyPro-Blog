Sent: 2026-11-20 08:40 ET

# Live functional findings: Word & Character Counter (FDP-15)

- **Run window:** 2026-11-19 14:46–14:56 EST (box `date`). Guest headless Chromium (plus a WebKit retry). Scripts: `scripts/wc-live.js` (30 cases + timings + platform rows + long text), `scripts/wc-gate-kbd.js`, `scripts/wc-goal.js`, `scripts/wc-webkit-retry.js`.
- **Starting counts (display-only, `fdp-usage-v1`):** every context loaded at 10 of 10 used (0 remaining): cases, gate/kbd desktop, iPhone SE, Pixel 7. Counts never moved.

## 1. Trial use: POLICY QUESTION for Santosh (not PASS)
- At 0 remaining, **Copy stats** copied the full stats block ("Stats copied" toast, clipboard filled, no dialog, count 10 → 10). Ctrl+A / Ctrl+C in the box: no dialog either. No trial strip on the page. (`json/gate-kbd.json`)
- /terms: "Text utilities, calculators and simple converters take no trial use", so the behaviour matches /terms.
- The Oct 30 owner policy says copy and results count in all tools, so this conflicts with the policy.
- The code does call `logUsageNow("download")` before Copy stats (`js/WordCounter-Bg7h0vss.pretty.js` L437); it returned true without charging. This is a display-only observation, not a backend claim.
- The blog says "stay aware of 10 trial usages a day", which matches neither.
- Santosh to decide; then align /terms, the blog and the page.

## 2. Counting accuracy: 27 of 30 cases as expected
`json/live-cases.json`. Two expected values in the first script run were my errors (W02 is 7 characters; W09 is 6 graphemes) and are corrected in `scripts/wc-cases.json`.

**Correct:**
- Words: basic text, hyphens/apostrophes (1 word), URLs and numbers, a spaced em dash not counted as a word.
- CJK counted per character (Japanese 9, Chinese 6, as Word does); Korean and Arabic by spaces; Thai via the segmenter (4).
- Characters: emoji counted as graphemes (👍🏽 = 1, ZWJ family = 1).
- Sentences: abbreviations Dr., Mr./Mrs., U.S./U.K., e.g./i.e., p.m. mid-sentence vs before "The", No. 5, decimals, "?!", "!!!", "Hello.World".
- Keywords: apple 3 (75%).

**Wrong:**
| Case | Input | Tool | Expected |
|---|---|---|---|
| W06 | `Para one.\nPara two.\nPara three.` (single line breaks, as pasted from Word or most editors) | **Paragraphs 1** | 3 (Word counts every Enter as a paragraph) |
| W07 | `Para one.\n \nPara two.` (blank line containing a space) | **Paragraphs 1** | 2 |
| W18 | `He said "Stop." Then he left.` | **Sentences 1** | 2 (a period inside a closing quote ends the sentence) |

- Code: paragraphs = `split(/\n\n+/)` (L147). It needs at least one truly empty line, so text separated by single newlines, or by "blank" lines containing spaces or tabs, collapses into one paragraph.
- The page's Details copy says paragraph counting works "the same way most word processors treat a paragraph break". That is not true of Word, which treats each line break as a paragraph.
- Sentence splitter (L84–116): a closing `"` / `'` / `)` after the terminator means the following text doesn't start with whitespace, so no split happens.

**Conventions to state, not bugs:**
- Newlines count as characters ("a\nb" = 3; Word shows 2). That suits platform limits; the FAQ could say so.
- Emoji-only tokens are not words.

## 3. Reading and speaking time
- Reading = words/200, rounded to minutes ("< 1 min" under 200): 250 → 1 min, 299 → 1 min, 300 → 2 min, 1,000 → 5 min.
- Speaking = 130 wpm: 1,000 → 7 min 42 sec. Both are as stated in "How to use it".
- **Copy contradiction:** the Details "Tips" still say the tool only gives a 200 wpm silent-reading estimate and that users should "mentally adjust" to 130–150 wpm for speech, but a Speaking Time card exists.

## 4. Platform limits (P1, accuracy)
The page counts plain graphemes for every row (`json/live-cases.json` → `platform`). The note only warns that X counts links as 23.

| Input | Tool says | Reality |
|---|---|---|
| 150 Japanese kana | X: "OK: 130 left" | X weights CJK characters as 2, so 150 kana = 300 > 280, which is **over** |
| "Hi 😀 " + 100 × "x" (105 chars) | SMS one segment: "OK: 55 left" | Any emoji or non-GSM-7 character switches SMS to UCS-2, where one segment is 70 characters, so this is **over** (2 segments) |
| 150 Japanese kana | SMS one segment: "OK: 10 left" | UCS-2, 70 per segment, so **over** |
| 281 Latin chars | X: "Over: 1 over" | correct |
| URL + 200 chars | X: 53 left | X counts the link as 23, so more is left; disclosed in the note |

Fix direction:
- Use X's weighting (CJK and emoji = 2, links = 23) for the X row.
- Make SMS GSM-7 aware (160/153 GSM-7, 70/67 UCS-2) and show segments.
- Or drop the "OK" verdict for scripts the row can't judge.

## 5. Other features
- **Word goal:**
  - 50 for 10 words gives "40 words to go" and a progressbar at 20%.
  - 10 gives "Goal reached"; 5 gives "5 words over the goal".
  - 0 or −3 is hidden; 2.7 is silently treated as 2 ("8 words over").
  - The input is labelled "Target words" and the progressbar has a role (`json/goal.json`).
- **Long text:**
  - 224,000 characters (above the 200,000 worker threshold) counted in about 0.7 s: 40,000 words, 8,000 sentences.
  - The note "The sentence-length view and reading score are skipped for very long text" is shown.
- **Copy stats content:** words, characters, sentences, paragraphs, reading/speaking time, "Reading ease: 91 (Very easy), Flesch-Kincaid grade 2.3", top keywords.
- **Readability and keywords exist,** but the Details "When not to use it" says "If you need … readability scoring, keyword density … this tool only counts". This contradicts the page's own features (P1 wording).
- **Clear:** empties the box and the counts, then focus drops to `<body>`.
- **No autosave:** reload loses the text, as stated. Competitors (WordCounter.net) autosave.
- **Network:** only telemetry POSTs (funnel.hit, insight.hit) were seen. No request carried the text in the filtered list (not a full network audit).

## 6. Keyboard and a11y (`json/gate-kbd.json`)
- **Tab order:** box → Clear → Copy stats → Include common words → Target words → "How this was calculated".
- **The textarea** has `aria-label="Text to count"` (good).
- **No aria-live region:** counts are not announced to screen-reader users (the "Counting…" status appears only above 200k characters).
- **axe on main:** 0 violations at idle. After typing, **12 `color-contrast` (serious)** on the green "OK: N left" texts in the platform list (`text-green-700` on the dark theme).
- **Focus after Clear** drops to `<body>`.
