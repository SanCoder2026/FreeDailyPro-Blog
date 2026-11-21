Sent: 2026-11-21 15:18 ET

# FDP-68 Emoji Picker & Copy (emoji-picker): deep test report for Claude

- **Written:** 2026-11-21 15:16 EST (box `date`, ET). Testing ran 2026-11-21 14:58–15:15 EST.
- **Tool:** https://www.freedailypro.com/tool/emoji-picker
  - TEST-ORDER row 68: **Professional Tool**, Text & Writing. Plan note "test-plan (unranked): SEO backfill 11". No duplicate group (cross-links Emoji to Unicode Converter).
  - **No trial strip, no Quick Buy and no prices on the page** (all 6 geo contexts, desktop and phones).
  - Video HMhO1yS49Zs (embedded, 83 s, uploaded 2026-09-30). Blogs /blog/emoji-picker "Pick One Emoji for a Help-Article Heading and Copy It Cleanly" (200) and /blog/emoji-unicode-converter (200).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `EmojiPicker-DAHM4kZZ.js`, data `compact-yUvgKgo9.js`, 541 KB):**
  - Search box, 9 category chips + All, skin-tone select (6 options), grid of 1,915 emoji. Click (or Enter) copies one emoji; toast + status line "Copied X to your clipboard".
  - Search: every typed word must match the **start of a word** in the label (6/4 points) or tags (3/1); results sorted by score.
  - Copy runs through `logUsageNow("copy")`, but the gate only acts when the tool is "known" to the usage system. Live it never charges (below).
- **Testers:**
  - Desk: page copy (6 FAQs, how-to, when/when not, tips, limits, privacy), JSON-LD, both blogs, JS and the data file (tone variants, variation selectors).
  - Playwright. Clipboard read from a same-origin helper tab (robots.txt).
    - `zero.json` (10/10) and `left.json` (0/10): 8 and 13 copies by click, Enter, Ctrl+C, after search and after reload.
    - `cases.json`: 29 searches + 9 categories; `blogq.json`: the blog's search-count claims; `tones.json` + tone screenshots; `net-copy.json`: requests sent by one copy.
  - Video frame sheet; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested):** none. No Drive, cloud or account feature on this page (verified), and no paid path offered on the page.
- **RERUN-AFTER-RESET:** none.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for a writer or marketer who needs the right emoji, in the right tone, pasted cleanly, and whether the page is set up to turn that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Unit Converter, Grammar Checker and Word Counter are uncounted on purpose; any other tool that takes no trial use is an owner question (Nov 20). Per-page-load charging is P1; a full-quality result at 0 is a pending owner question; a real save at 0 is P1 (Nov 21, corrected 1:19 PM).

**P0 / P1:** none found.

**Owner question:**
- **This tool takes no trial use at all.**
  - At 10/10 (zero.json): 8 copies (click, Enter, after search, after reload, Ctrl+C on a tile) all reach the clipboard (verified), toast "Copied …", no cap dialog, **0 `usage.log` POSTs**.
  - With uses left (left.json): 13 copies → **0 POSTs, counter stays 0/10**. One copy sends only the generic `insight.hit` dwell/engaged beacon (net-copy.json).
  - Yet the blog says "**Each copy counts as one trial use**", the Privacy text says "The site notes that a copy took place", the video shows a "free uses remaining today" box, and JSON-LD carries an Offer of $4.99.
  - Not on the uncounted-on-purpose list. Decide: count it (then wire the gate) or list it as uncounted (then fix the blog line, Privacy line and video).

**P2 — where to look:**
- **Skin tone gives mixed tones on 7 two-person emoji.** With Medium-light, Medium, Medium-dark or Dark selected, "people holding hands", "kiss: woman, man / man, man / woman, woman" and "couple with heart: woman, man / man, man / woman, woman" show and copy a **light + chosen** pair (e.g. Medium → 👩🏻‍❤️‍👨🏽, U+1F3FB + U+1F3FD). Screenshots T-kiss-medium.png, T-holding-hands-dark.png. Cause: the code takes `skins[tone-1]` from a 25-variant list. Pick the variant whose modifiers all equal the chosen tone. (Handshake, kiss, couple with heart and the hand-holding pairs with matching order come out right.)
- **Search copy doesn't match how search works.** FAQ "checks whether your text appears **anywhere** in the name or tags … a fragment like sun can match several". Live, matching is word-prefix: "lower" doesn't find "sunflower", "lock" returns **7** (blog says 44, "catches clock, block"), "pin" returns **15** (blog says "nearly 50 … sleeping"). The blog's "Searching well: substring matching works against you" section is outdated. "warning" 1, "idea" 2, "calendar" 3, "check" 6 match the blog.
- **Video HMhO1yS49Zs:** old light-theme UI with a starter set only (no categories, no skin tone), a "free uses remaining today" box and caption "10 free uses daily!", title "Free Step-by-Step Walkthrough", description "Try … free", "Free daily uses … no account needed", tags "free online tools", "PDF tools". About half the 83 s is end cards.
- **Locale pages:** chrome, breadcrumb and one badge translated (es screenshot); title, meta, H1, search placeholder, chips, skin-tone menu and FAQ stay English, and search is English only, which matters more on a picker than on most tools.
- **SEO:** title "Emoji Picker Online - Search and Copy | FreeDailyPro" good; meta 62 chars ("Search and copy emoji by keyword. Fast, right in your browser."), no mention of 1,900 emoji, skin tones or flags. Generic OG image.

**P3:**
- Search ranking/relevance: "smile" puts "cat with wry smile" first; "uk" returns only Ukraine (UK flag is tagged GB); "thumbsup"/":+1:"-style shortcodes don't work; "+1" returns 41 loosely related emoji.
- All shows the 9 "Components" (5 lone skin-tone swatches, 4 hair parts); copying 🏻 alone is rarely wanted. Hide them as the chip list already does.
- Some copied emoji carry an extra U+FE0F where the base already has emoji presentation (👍 → 1F44D FE0F, 😐, 👽, 🐈, 👈–👇): pastes fine but breaks exact-match lookups and some character counters.
- Phones: the whole 1,915-tile grid sits before the info sections (page ~23,000 px tall on Pixel 7). iPhone SE / Galaxy S9 tiles are below 44 px; SE 9 px overflow (header action button); on iPhone SE (WebKit) the skin-tone select renders as a light box on the dark theme.
- axe: desktop label-content-name-mismatch (serious), region (moderate); Pixel 7 color-contrast ×2 on the ad caption (keep reserved ad slots; fix the caption colour). ja desktop 1369 px.
- de-DE/fr-FR consent banner (screenshot) partly covers the Feedback button; the tool is usable.

## Intent

A writer, marketer or developer needs one specific emoji (often in a given skin tone) and wants to find it by word and paste it cleanly. The picker is fast and complete; tone handling and the search copy need fixing, and the owner needs to decide whether copies count.

## What works (verified)

- **Data:** 1,915 emoji (Unicode 16 incl. 🫩, 🙂‍↔️, 🍋‍🟩), flags incl. England/Scotland/Wales; categories sum to 1,906 + 9 components.
- **Search:** case-insensitive; multi-word ("flag india" → 🇮🇳 first, "heart eyes" → 😍 😻); "tada" → 🎉, "lol", "shrug", "united states", "gb"; empty/space shows all; clear "No emoji found for …" message.
- **Copy:** click and keyboard Enter both copy the exact character; status line is `aria-live`; tiles have "Copy <name>" labels and hover titles.
- **Skin tones:** single-person and hand emoji (👍, 👋, 🏄 incl. ZWJ gender sequences) get the right modifier in all 5 tones; faces/objects unchanged as documented.
- **Layout:** search and grid at the top on all devices; Firefox/WebKit/iPad fine.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | Full set, categories, tones. |
| 2 | Completeness | PASS (minor) | No recent list / multi-select (documented). |
| 3 | Ease of use | PASS | One click copy, clear status. |
| 4 | Layout | PASS (minor) | Very long phone page; small tiles on 320–360 px. |
| 5 | Payment process | N/A | No trial strip / Quick Buy (owner question). |
| 6 | Information correct | FAIL | Blog "each copy counts"; search "anywhere"/counts; Privacy logging line. |
| 7 | Indexing | PASS | 200, canonical self, 10 hreflang + x-default. |
| 8 | SEO | PARTIAL | Meta 62 chars, generic OG. |
| 9 | Blog | PARTIAL | Useful scenario; outdated search section and trial-use line. |
| 10 | YouTube video | PASS | HMhO1yS49Zs embedded. |
| 11 | FAQ / guide correct | PARTIAL | Search FAQ wrong; tone FAQ misses mixed-tone bug. |
| 12 | Video shows current capability | FAIL | Old UI, "10 free uses daily", "PDF tools" tag. |
| 13 | Storage | N/A | None (verified). |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | N/A | Clipboard only; copies verified. |
| 16 | Usage count | Owner question | Takes no trial use (0 POSTs at 10/10 and 0/10). |
| 17 | Categorization in section | PASS | Text & Writing / Professional. |
| 18 | Correct section of site | PASS | Cross-link to Emoji to Unicode Converter; related links 200. |
| 19 | AI need and demand | PASS | High ("emoji copy paste", "emoji picker"). |
| 20 | Merge better? | No | Converter is a different job; keep the cross-link. |
| 21 | Remove? | No | High-demand utility. |
| 22 | Duplicates | None | No duplicate group. |

## After fixes, rerun

- `px68-live.js tones` and `px68-tone-shot.js` (all two-person emoji uniform).
- `px68-blogq.js` after the copy is updated; `px68-live.js zero` / `left` once the owner decides on counting.
