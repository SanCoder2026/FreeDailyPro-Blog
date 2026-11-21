Sent: 2026-11-21 17:04 ET

# FDP-74 ASCII Art Generator (ascii-art-generator): deep test report for Claude

- **Written:** 2026-11-21 17:04 EST (box `date`, ET). Testing ran 2026-11-21 16:52–17:01 EST.
- **Tool:** https://www.freedailypro.com/tool/ascii-art-generator
  - TEST-ORDER row 74: **Pro** (tools.csv "Professional Tool"), Text & Writing. Plan note "test-plan (unranked): GSC top-50 SEO backfill 14". No duplicate group (binary-ascii-converter and banner-sign-maker are different jobs).
  - **No trial strip, no Quick Buy and no prices on the page** (all 6 geo contexts, desktop and phones). JSON-LD SoftwareApplication still carries an Offer of $4.99.
  - Video knX3VOJhhuo (embedded, 89 s, uploaded 2026-09-23). Blog /blog/ascii-art-generator "A README Banner That Fits 80 Columns, Made From Plain Text" (200, linked).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `AsciiArtGenerator-ZgJPcy0H.js`, figlet.js with 12 lazy font chunks, `useLogToolUsage`):**
  - Textarea (cut at 60 characters; one banner per line), Font select (12), Left / Centre, Preview zoom 8–22, width note (warns past 80), **Copy ASCII Art**.
  - Accented Latin letters are transliterated ("Café Zürich" → "Cafe Zurich", with a status note). Other scripts and emoji show an error and no art.
  - Copy goes through `useLogToolUsage(…, { ownActions: true })`: the clipboard and copy-event gate only acts when the tool is "known" to the usage system. Live, it never charges.
- **Testers:**
  - Desk: page copy (6 FAQs, how-to, when / when not, tips, limitations, privacy), JSON-LD, blog, JS.
  - Playwright, guest. The clipboard was read back from a same-origin helper tab (robots.txt).
    - `zero.json`: 10/10, Chromium; 8 Copy-button copies + 3 Ctrl+C, before and after a reload.
    - `zero-firefox.json`: the same run at 10/10 in Firefox (clipboard not readable).
    - `left.json`: 0/10; 16 copies + 3 Ctrl+C.
    - `cases.json`: 12 fonts on "Hello World", 17 text cases, Centre, zoom. The art was read from the `<pre>` and saved to `art/`.
  - Each font's output was compared with pyfiglet. The blog's "NOVA CLI" widths were re-measured.
  - Video frame sheet; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested):** none. There's no Drive, cloud or account feature on this page, and no paid path is offered.
- **RERUN-AFTER-RESET:** none. Copying was observed both with uses left (0/10) and at the cap (10/10).

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for a developer who wants a README or terminal banner that survives pasting, and whether the page is set up to turn that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Unit Converter, Grammar Checker and Word Counter are uncounted on purpose; any other tool that takes no trial use is an owner question (Nov 20; Emoji Picker #68 was filed the same way). Per-page-load charging is P1. A full-quality result at 0 is a pending owner question. A real save at 0 is P1 (Nov 21, corrected 1:19 PM).

**P0 / P1:** none found.

**Owner question:**
- **This tool takes no trial use at all.**
  - At 10/10, 8 Copy-button copies and 3 Ctrl+C copies all reach the clipboard (verified text), with the toast "Copied to clipboard", no cap dialog and **0 `usage.log` POSTs**. That held before and after a reload, and in Firefox too.
  - With uses left (0/10), 16 copies + 3 Ctrl+C → **0 POSTs**, and the counter stays at 0/10.
  - The page shows no strip, tier badge or prices, but the TEST-ORDER/tools.csv tier is Professional, and JSON-LD has an Offer of $4.99. The video shows a "Pro" chip and "10 free uses daily".
  - It's not on the uncounted-on-purpose list. Decide: count it (register the tool so `known` is true and Copy is gated), or list it as uncounted (then drop the Offer and the video's "Pro / 10 free uses").

**P2 — where to look:**
- **The page and blog say accented letters are refused; the tool converts them.**
  - FAQ: "If any character falls outside that range the tool shows a message and draws nothing". When not to use it: "text with accents … is rejected". Limitations: "Accented letters … produce an error message".
  - The blog says the same: "If your text includes accented letters … draws nothing".
  - Live: "Café Zürich" draws "Cafe Zurich" with the note "Accented letters were drawn without their accents"; "Straße Œuvre æ" → "Strasse OEuvre ae". The error text itself even says "(Accented Latin letters are converted automatically.)".
  - Update the four places to say accents are dropped, and that other scripts and emoji are refused.
- **Video knX3VOJhhuo is out of date and exposes personal browser tabs.**
  - It shows the old UI (a "Style" toggle and a "Size" slider instead of 12 fonts, Centre, zoom and width note), a "10 free uses daily" chip, a "Pro" chip and "Search 200+ tools".
  - The browser tab strip shows **"Inbox - chetankannur…" (Gmail)** and a "FreeDailyPro_All_Tools" sheet (frame at 0:40, `video/f40c.png`).
  - The title says "Free Step-by-Step Walkthrough" and the description "Try … free… no account needed". The VideoObject name "How to Create ASCII Art from Text Online" doesn't match the title.
  - Re-record in a clean browser profile.
- **Locale pages are fully English:** the H1, title, meta, controls, FAQ and how-to on es/pt/fr/de/ja/hi/zh/ko/id (englishWordRatio is low only because the art and the nav count). Only the navigation is translated.

**P3:**
- Centre alignment pads the blank separator line with spaces (29 trailing spaces in `art/T-multi-centre.txt`). The page says "Trailing spaces are removed from every line".
- Every banner has one extra leading space column compared with figlet (Standard "Hello World" is 53 wide vs pyfiglet 52; Big, Small, Block and Bubble are also +1), and the width note counts it. Mini is drawn at full width (37 vs figlet 26 smushed). Harmless, but it costs a column against the 80 limit.
- The transliteration note says "Accented letters were drawn…" for curly quotes, dashes and the ellipsis too (“Smart” – quotes…).
- Pasting more than 60 characters is cut silently (75 → 60), with no message.
- Meta is 65 characters ("Turn any text into ASCII banner art. Fast, right in your browser.").
- iPhone SE: 9 px overflow (329/320, a button in the header row). ja desktop 1369 px.
- axe desktop: label-content-name-mismatch (serious, `.right-2`) and region (moderate). Pixel 7 clean.

## Intent

A developer wants a project-name banner that stays aligned in a terminal or README. The art matches figlet (7 of 12 fonts identical; the rest differ by one leading column or by spacing), the width note and the 80-column warning work, and refusals are clear. The open points are whether the tool should count uses at all, page copy that's out of date about accents, and a video that leaks a personal inbox name.

## What works

- **All 12 fonts render.** Slant, Banner3, ANSI Shadow, Doom, Graffiti and Ghost match pyfiglet exactly. Standard, Big, Small, Block and Bubble differ only by the extra leading space. ANSI Shadow uses `█╗║╔═╝╚` (non-ASCII, as documented).
- **The blog's "NOVA CLI" widths are correct** (Bubble 32, Small 38, Standard 44, Doom 47, Slant 48, Big 50, ANSI Shadow 59, Graffiti 63, Banner3 64, Block 75, Ghost 82).
- **Width note** "N characters wide", plus the warning past 80 (Banner3 99, Block 91, ANSI Shadow 88, Ghost 111 for "Hello World").
- **Multi-line:** one banner per line, a blank line between. Centre pads the shorter banner. Several blank input lines still give two banners.
- **Refusals:** emoji, Hindi and a mixed line → clear error, no art, no Copy button. Empty and spaces-only → nothing. `<script>` is drawn as text (no injection). Tab and punctuation work. Trailing input spaces are ignored.
- **Zoom 22** sets the preview font to 22 px; the copied text is unchanged.
- **Copy:** button and Ctrl+C both put the exact art on the clipboard.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 12 fonts, multi-line, alignment, width check. |
| 2 | Completeness | PASS | No image→ASCII (documented). |
| 3 | Ease of use | PASS | Live preview, clear errors. |
| 4 | Layout | PASS (minor) | iPhone SE 9 px. |
| 5 | Payment process | N/A | No strip, prices or Quick Buy on the page. |
| 6 | Information correct | **FAIL** | Accents "refused" in 4 places; they're converted. |
| 7 | Indexing | PASS | 200, canonical self, hreflang set. |
| 8 | SEO | PASS (minor) | Title fine; meta 65 chars. |
| 9 | Blog | PARTIAL | Widths right; accent section outdated. |
| 10 | YouTube video | PASS | knX3VOJhhuo embedded. |
| 11 | FAQ / guide correct | FAIL | Accent FAQ. |
| 12 | Video shows current capability | FAIL | Old UI; personal tabs; "10 free uses". |
| 13 | Storage | N/A | None. |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | N/A | Copy only. |
| 16 | Usage count | **OWNER QUESTION** | Never counts (0 POSTs in 30 copies). |
| 17 | Categorization in section | PASS | Text & Writing. |
| 18 | Correct section of site | PASS | Related: Word Counter, Case Converter, Paraphraser. |
| 19 | AI need and demand | PASS | "ascii art generator", "text to ascii", "figlet online". |
| 20 | Merge better? | No | Distinct job. |
| 21 | Remove? | No | GSC top-50 backfill. |
| 22 | Duplicates | None | — |

## After fixes, rerun

- `px74-live.js zero` and `left` (Copy is gated or charged if the owner decides to count it), and `cases` (Centre blank line without trailing spaces; widths).
