Sent: 2026-11-21 18:03 ET

# FDP-79 Invisible Text Generator (invisible-text-generator): deep test report for Claude

- **Written:** 2026-11-21 18:02 EST (box `date`, ET). Testing ran 2026-11-21 17:52–18:02 EST.
- **Tool:** https://www.freedailypro.com/tool/invisible-text-generator
  - TEST-ORDER row 79: **Pro**, Text & Writing, "test-plan (unranked): GSC top-50 SEO backfill 16". No duplicate group.
  - **No trial strip, Quick Buy or prices on the page.** JSON-LD Offer $4.99. Video AIYW2os7qxE (97 s). Blog /blog/invisible-text-generator "Test a Sign-Up Form With Blank and Zero-Width Characters" (200, linked).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (`InvisibleTextGenerator-Cl_rBsOe.js`):** 9 characters (Braille Blank U+2800 default, Hangul Filler, ZWSP, ZWNJ, ZWJ, Word Joiner, Invisible Separator, Em Space, Braille Blank + newline), count 1–500 (box, 1/5/10/50 buttons, slider 1–20), Copy via `navigator.clipboard.writeText` after `logUsageNow("copy")`, and a Test box listing pasted code points.
- **Testers:** desk (page, 4 FAQs, JSON-LD, blog, JS); Playwright guest: `zero.json` (Chromium 10/10), `left-firefox.json` (0/10, try 20), `cases.json` (variants, count inputs, slider, Test box), `shift.json` (lost click on 4 engines), no-clipboard check; video frames; matrix of 10 devices, 10 locales + /ar, 6 geo, axe.
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested):** none. No Drive, cloud, account feature or paid path on this page.
- **RERUN-AFTER-RESET:** none (observed at 10/10 and 0/10).

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters to someone who wants a blank name or bio, or a developer testing their own form.

**Owner context:** copy and results count as trial uses (Oct 30). Unit Converter, Grammar Checker and Word Counter are uncounted on purpose; any other tool that takes no trial use is an owner question (#68, #74, #76, #77 filed the same way).

**P0 / P1:** none found.

**Owner question:**
- **No trial use at all.** 7 copies at 10/10 (clipboard filled) and 7 at 0/10 → 0 POSTs, no dialog. No strip because the tool isn't `known`; the JSON-LD still advertises $4.99. Register it, or list it as uncounted.

**P2 — where to look:**
- **Lost first click.** Clear the count box → the red note "Type a number from 1 to 500. Until then 1 will be used." appears → Copy. Mousedown blurs the input, `onBlur` clears the note, the button moves up 24 px (33 px on Pixel 7) before mouseup, and the click lands on nothing: no copy, no toast. Seen in Chromium, Firefox and a Pixel 7 tap (iPhone tap worked). The note even promises 1 will be used. Fix: keep the note's space reserved, or don't clear it on blur.
- **The copy fallback can't be followed.** If the browser refuses the clipboard, the toast says "Select the text and copy it by hand", but the characters are never on the page (0 text nodes). In-app browsers (Instagram/TikTok, where blank bios are made) often block the clipboard API. Fix: show the result in a read-only field (select-all on focus) or fall back to `execCommand('copy')`.
- **Blog** says six variants and a 1–20 slider (now 9 and 1–500); its byte and `trim()` facts are correct.
- **Video AIYW2os7qxE:** old 2-variant UI, slider only, no Test box; "Free" wording; personal bookmarks bar and a Notepad with tab names visible; ~45 s of end card.
- **Locale pages:** 10 hreflang pages 200 with `lang` set, but title, H1, labels, notes and FAQ English.

**P3:**
- Count box: typing a leading 0 turns into 1, so "007" → 107 and "05" → 15; "2.5" → 25, "1e2" → 12, "-3" → 3 with no note.
- Slider 1–20 vs count 1–500: at 50 it sits at 20, and one ArrowLeft makes the count 19. FAQ says "drag the slider" for the range.
- Invisible Line Break ends with a newline (trimmed by many fields); identical toasts stack.
- iPhone SE 9 px overflow; ja desktop 3 px; one 1920 CLS 1.0 sample at 0.4 s; axe desktop label-content-name-mismatch + region.

## Intent

Someone wants a "blank" name or bio that a form accepts, and to know it worked before they paste it. The tool gets the characters exactly right (all 9 code points verified), the Test box proves what landed, and the responsible-use note is in place. What fails is the moment of copying: a lost first click after editing the count, and no way out when the clipboard is blocked.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 9 variants, exact code points, 1–500. |
| 2 | Completeness | PASS | Count box, quick buttons, Test box. |
| 3 | Ease of use | PARTIAL | Lost first click; impossible manual fallback; leading-zero entry. |
| 4 | Layout | PASS (minor) | iPhone SE 9 px. |
| 5 | Payment process | N/A | No strip, prices or Quick Buy. |
| 6 | Information correct | PARTIAL | FAQ slider wording; fallback toast. |
| 7 | Indexing | PASS | 200, canonical self, hreflang. |
| 8 | SEO | PASS | Title 57 chars; meta ~150. |
| 9 | Blog | PARTIAL | Six variants / 1–20 out of date. |
| 10 | YouTube video | PASS | Embedded and linked. |
| 11 | FAQ / guide correct | PASS (minor) | Slider wording. |
| 12 | Video shows current capability | FAIL | Old UI, personal browser visible. |
| 13 | Storage | N/A | None; runs locally. |
| 14 | Sharing | N/A | "Share this tool" only. |
| 15 | Downloads | N/A | Copy only. |
| 16 | Usage count | **OWNER QUESTION** | Never counts. |
| 17 | Categorization in section | PASS | Text & Writing. |
| 18 | Correct section of site | PASS | Related: Word & Character Counter, Case Converter. |
| 19 | AI need and demand | PASS | "invisible text", "blank name" searches; chat AIs can't reliably output these characters. |
| 20 | Merge better? | No | Distinct. |
| 21 | Remove? | No | GSC top-50 backfill. |
| 22 | Duplicates | None | — |

## After fixes, rerun

- `px79-shift.js` (first click should copy on all engines), `px79-noclip.js` (a selectable fallback should exist), `px79-live.js cases` (N09 should give 7).
- `px79-live.js zero` / `left firefox` if the owner decides it should count.
