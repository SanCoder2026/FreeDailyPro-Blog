Sent: 2026-11-20 08:40 ET

# FDP-15 Word & Character Counter (word-counter): deep test report for Claude

- **Written:** 2026-11-19 14:58:02 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/word-counter. Row 15 of TEST-ORDER.md: Pro, Text & Writing. Test-plan rank 14: "179 views; 'word count characters' 2,320 impr 0 clicks" (quoted from TEST-ORDER, not re-verified). **GSC data is not available.**
- **Classification:** Professional Tool, Text & Writing. **Takes no trial use:** Copy stats works at 0 remaining. That matches /terms ("text utilities … take no trial use") but conflicts with the Oct 30 owner policy, so it is a **POLICY QUESTION for Santosh**, not a PASS (check 16).
- **Testers:**
  - **Desk review:** tool page, 9 locales and /ar, blog, /terms; the WordCounter code; WebSearch.
  - **YouTube video:** metadata, 32 frames, contact sheet, crop.
  - **Headless Playwright:**
    - 30 counting cases with expected values
    - reading/speaking timings and platform-limit rows
    - 224k-character text
    - gate, Ctrl+C, Clear, word goal, keyboard, axe, phones
    - matrix: 10 profiles, 10 locales + /ar, 6 geos, axe; plus a WebKit retry
- **Constraints kept:** guest only, no sign-in, no card or email entered, no ad clicks, no API or MCP calls, no site or repo changes.
- **Sign-in:** none needed. **No URLs were blocked by sign-in.**
- **Nothing pending:** the gate was observed at 0 remaining. No RERUN-AFTER-RESET row was added.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real component, restate the problem, challenge anything that looks wrong, and pick the fix that fits how FreeDailyPro has shipped similar work.

Components to look at (`evidence/js/WordCounter-Bg7h0vss.pretty.js`, `WordCounterExtras-CS5kAwSF.pretty.js`):
- the paragraph count (`ne`, L147)
- the sentence splitter `P` (L84–116: closing quotes)
- the platform rows (`ie`/`Se`, L192–243: X weighting, SMS encoding)
- the Copy stats usage call (L437)
- the textarea min-height
- result announcements
- page copy (Details "When not to use it" / "Tips" / paragraph text, FAQ), the es title, the blog, the video

After you ship, rerun `scripts/wc-live.js` (30 cases, built-in expected values) and `test-cases.md` (WC-01…WC-22).

## Intent

People paste an essay, abstract or post and want to trust one number before they submit. This counter is already one of the better ones:
- correct words and characters across scripts, including CJK per character, Thai segmentation and emoji graphemes
- an abbreviation-aware sentence splitter
- readability with shown formulas, keywords, a goal, platform limits
- fully local processing

The trust breaks in a few places:
- Paragraphs pasted from Word (single line breaks) count as 1.
- The platform rows say "OK" for Japanese posts on X and emoji SMS that the platforms would reject or split.
- The page's own Details text says the tool doesn't do readability or keyword density, which it does.

## Why: what the evidence says

- **Counting core (PASS):** 27 of 30 cases as expected. 224k characters count in about 0.7 s through a worker.
- **P1: paragraphs.** `split(/\n\n+/)` gives Paragraphs 1 for "Para one.\nPara two.\nPara three." and for blank lines containing a space. The page claims "the same way most word processors" count.
- **P1: platform rows.**
  - Grapheme count for every row: 150 Japanese kana shows "X: OK, 130 left", but X weights CJK as 2 (so it is over).
  - "Hi 😀" + 100 characters shows "SMS one segment: OK, 55 left", but emoji forces UCS-2 with 70 per segment (so it is over).
- **P1: copy contradicts features.** "When not to use it: … readability scoring, keyword density … this tool only counts" sits next to Reading ease and Top keywords. "Tips" say there is only a 200 wpm estimate, yet a Speaking Time card exists.
- **P1: trial-use policy question.** Ungated at 0 remaining. /terms agrees. The Oct 30 policy disagrees. The blog says "10 trial usages a day".
- **P2:**
  - Sentence split misses a period inside closing quotes.
  - The idle text box is one line (min-height 0).
  - On iPhone SE the counts sit below the fold while typing.
  - No aria-live; 12 serious contrast nodes on "OK: N left"; focus lost after Clear.
  - Single-question FAQ; "gratis" in the es title; 8 English locale copies.
  - The video shows the old UI, personal bookmarks and a PUMA sample.
  - The blog's reading-time figures don't match the tool's display.
  - No autosave.

## Outcomes we want

1. Paragraph counts match what a writer sees in Word.
2. Platform rows never say "OK" for a post the platform would reject. Rows are either platform-accurate (X weighting, SMS segments) or clearly marked as plain-character guides.
3. The page, FAQ, blog and video describe the current features (readability, keywords, speaking time, limits, goal) and the actual trial-use rule once Santosh decides.
4. Counts are visible and announced while typing on any phone.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | Words, characters and sentences are strong (27/30). Paragraphs are wrong for single line breaks; quote-ended sentences missed. `findings/live-functional-findings.md`, `json/live-cases.json` |
| 2 | Completeness vs. competitors | **PASS (minor gaps)** | LOW | Has more than most (limits, readability steps, goal, keywords, CJK). Lacks autosave, unique words, phrases, pages estimate. `findings/desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Live counts and clear cards. The one-line idle box; counts below the fold on small phones. |
| 4 | Layout attractiveness | **PARTIAL** | LOW | Clean grid. Tiny idle box; 9 px header overflow at 320 px (site-wide). |
| 5 | Payment process | **N/A (policy question)** | — | No gate, strip or pass buttons on the page. Depends on check 16. |
| 6 | Information correct | **FAIL** | HIGH | Platform-row verdicts wrong for CJK on X and for non-GSM SMS. Details copy denies features the tool has; paragraph claim false; outdated speaking-time tip. |
| 7 | Indexing | **PASS** | — | 200, self-canonical, in the sitemap with the blog. **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Good title and meta for "word count characters". The FAQPage has 1 question; unused long-tail features (X/SMS/reading time); es-only translation with "gratis"; 8 English locale copies. |
| 9 | Blog post | **PARTIAL** | LOW | /blog/word-counter: strong workflow; "10 trial usages a day" line; reading-time decimals the tool doesn't show. |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | AVCllh6Nih8, 97 s, 2 views, embedded. |
| 11 | FAQ / usage guide | **PARTIAL** | MEDIUM | Guide is detailed but contradicts the features; the FAQ has one question. |
| 12 | Video shows current capabilities | **FAIL** | MEDIUM | Old 6-card UI; personal bookmarks; PUMA sample; 32 s outro; "Free" wording. `findings/video-findings.md` |
| 13 | Storage | **PASS** | — | Local; no request carried text (filtered list); no autosave (stated). |
| 14 | Sharing | **N/A** | — | No share-result feature; none promised. |
| 15 | Downloads | **N/A** | — | Copy stats only; no download promised. Copy stats content is complete. |
| 16 | Usage count | **POLICY QUESTION for Santosh (not PASS)** | HIGH | Copy stats at 0 remaining: copied, no dialog, count 10 → 10 (14:47 EST). Matches /terms ("text utilities … take no trial use"); conflicts with the Oct 30 owner policy; the blog says 10 trial usages a day. Counters are display-only. All starting counts were 10 used. |
| 17 | Categorization | **PASS** | — | Text & Writing. |
| 18 | Location in site | **PASS** | — | Breadcrumb, category, Book Writing Toolbox link, two guides. |
| 19 | AI need / demand | **PASS (no AI needed)** | — | Deterministic; steady demand (rank 14). |
| 20 | Merge? | **N/A: keep** | — | Distinct; cross-link Reading Level. |
| 21 | Remove? | **N/A: keep** | — | Demand plus a strong core. |
| 22 | Duplicates | **PASS** | — | No duplicate tool; some overlap with Reading Level (keep, cross-link). |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`.
- All profiles return 200. The iPhone 14 Pro Max matrix crash was a harness event; three retries were clean.
- Desktop Firefox and WebKit show a side-rail ad beside the tool (fine).
- Locales are English except the es title, meta and H1.

**Ads:** keep them in reserved fixed-height slots after the stats and limits (and side rails). Never put them between the text box and the counts.

## Suggested direction (interpret freely)

1. **P1: paragraphs.** Count non-empty lines separated by `\n` (Word-like), or offer "Paragraphs (line breaks)" next to "Paragraphs (blank lines)". At minimum, treat whitespace-only lines as blank (`/\n\s*\n/`).
2. **P1: platform rows.**
   - Implement X's weighted count (CJK, emoji and most non-Latin = 2; URLs = 23).
   - Make SMS encoding-aware: GSM-7 160/153, UCS-2 70/67, show "N segments".
   - Otherwise, show "plain characters" without an OK/Over verdict for scripts the row can't judge.
3. **P1: copy.** Rewrite "When not to use it" and "Tips" to describe readability, keywords and speaking time as they are. Fix the paragraph sentence (after 1). Add 5–6 FAQ answers (newlines counted, CJK and emoji rules, platform-row method, reading/speaking rates, privacy).
4. **P1: policy question.** Santosh decides; then align /terms, the blog line and the page.
5. **P2:**
   - Treat closing quotes and brackets after `.!?` as sentence ends.
   - Restore a ~200 px idle box.
   - Add a sticky compact count on phones and a polite aria-live summary (debounced).
   - Darken the green "OK" text.
   - Return focus to the box after Clear.
   - Optional autosave (local only, with a clear toggle).
   - Re-record the video in a clean profile.
   - Fix the blog reading-time numbers.
   - Drop "gratis" from the es title; translate or de-list the locales.

## Constraints

- Say "Professional Tools", "Premium Applications" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Don't change the trial-use behaviour until Santosh answers.
- Counters are display-only evidence.

## Process

Inspect WordCounter → restate → propose → implement → verify with `scripts/wc-live.js` (cases, timings, platform rows, long text), `scripts/wc-gate-kbd.js` (gate, keyboard, axe, phones), `scripts/wc-goal.js` and `test-cases.md`.
