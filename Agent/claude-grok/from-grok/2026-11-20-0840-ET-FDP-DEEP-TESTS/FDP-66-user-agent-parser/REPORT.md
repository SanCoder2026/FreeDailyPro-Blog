Sent: 2026-11-21 14:42 ET

# FDP-66 User-Agent Parser (user-agent-parser): deep test report for Claude

- **Written:** 2026-11-21 14:40 EST (box `date`, ET). Testing ran 2026-11-21 14:26–14:40 EST.
- **Tool:** https://www.freedailypro.com/tool/user-agent-parser
  - TEST-ORDER row 66: **Professional Tool**, Developer & Security Tools. Plan note "test-plan (unranked): SEO backfill 11". No duplicate group.
  - **No trial strip, no Quick Buy and no prices on the page** (all 6 geo contexts, desktop and phones).
  - Video -iWoAjyeKOY (embedded, 91 s, uploaded 2026-09-24). Blog "Decode a User-Agent String From a Bug Report" (200).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `UserAgentParser-BymHlzBs.js`):**
  - One textarea, pre-filled with your own browser's UA; results refresh on every change (no Parse button). Eight cards: Browser, Version, OS, Device type, Device, Engine, CPU, Bot / script. Actions: Copy result, Save as text (.txt), Print.
  - Parsing is ua-parser-js in the browser. A full log line is accepted (the quoted UA is extracted). **Pasted Sec-CH-UA headers are parsed**, and "Use My Browser's User-Agent" reads Client Hints in Chromium.
  - Usage: `useLogToolUsage` is wired, but the gate only runs when the tool is "known" to the usage system. Live, it never runs (below).
- **Testers:**
  - Desk: page copy (6 FAQs, how-to, when/when not, tips, limits, privacy), JSON-LD, blog, JS.
  - Playwright. Clipboard read from a same-origin helper tab (robots.txt); `window.print` stubbed.
    - `zero.json`: a context at 10/10. `left.json`: a context with 10 uses left.
    - `cases.json`: 22 inputs (phones, tablets, desktops, IE11, 8 bots/clients, smart TV, log line, Sec-CH-UA ×2, garbage, empty). `hints.json` (Chromium) and `hints-firefox.json`: the "Use My Browser's User-Agent" button.
  - Video frame sheet; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.** (The script's Windows-note flag was a false positive from FAQ text; the note was verified on C-windows.png.)
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested):** none. There is no Drive, cloud or account feature on this page (verified), and no paid path is offered on the page.
- **RERUN-AFTER-RESET:** none.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for a developer or support person decoding a UA from a bug report or log, and whether the page is set up to turn that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Unit Converter, Grammar Checker and Word Counter are uncounted on purpose; any other tool that takes no trial use is an owner question (Nov 20). Per-page-load charging is P1; a full-quality result at 0 is a pending owner question; a real save at 0 is P1 (Nov 21, corrected 1:19 PM).

**P0 / P1:** none found.

**Owner question:**
- **This tool takes no trial use at all.**
  - At 10/10 (zero.json): Copy result (toast "Result copied", clipboard verified), Save as text (`user-agent-parser-result.txt`, 173 bytes), Print, Ctrl+C on the cards, a new string + copy, and reload + save all work. No cap dialog, **0 `usage.log` POSTs**, counter stays 10/10.
  - With uses left (left.json): the same steps → **0 POSTs, counter stays 0/10.**
  - Yet the Privacy section says "Once you interact with the results, the site logs the tool name and a device identifier for usage counting", which is not what happens, and JSON-LD carries an Offer of $4.99.
  - It isn't on the uncounted-on-purpose list. Decide: count it, or list it as uncounted and fix the Privacy line.

**P2 — where to look:**
- **Page copy says the tool can't do what it does best (Client Hints).**
  - FAQ "Can it read a Client Hints header? **No** … Sec-CH-UA … will not parse meaningfully", Limitations "Newer client hint headers are not read", and the blog says the same.
  - Live: pasting Sec-CH-UA headers gives Google Chrome 131.0.6778.135, Android 14.0.0, Pixel 8 Pro, each "(from Sec-CH-UA headers)" (C-secchua.png), and a Windows header set with platform-version 15.0.0 gives **Windows 11**. "Use My Browser's User-Agent" in Chromium shows "(from Client Hints)" values (H-hints.png); Firefox shows a clear note that it has none (H-hints-firefox.png).
  - The tool's own error message says "Pasted Sec-CH-UA headers work too." So the FAQ "Why can it not tell Windows 10 from Windows 11?" undersells it: it can, with hints. Rewrite the FAQ, Limitations and blog to say how to paste the hint headers; this is the page's strongest differentiator and the main search angle ("windows 11 user agent", "sec-ch-ua parser").
- **OS card says "Windows 10" for every NT 10.0 string** (Edge on Windows, C-windows.png), with the small note below that 10 and 11 can't be told apart. A Windows 11 user sees a wrong answer in the big card. Show "Windows 10 / 11" in the card when no hints are present.
- **Video -iWoAjyeKOY:** older UI with four cards (now eight; no Copy/Save/Print, no hints), title "Free Step-by-Step Walkthrough", description "Try … free", tags "free online tools" and "PDF tools", thumbnail "FREE · PRIVATE · NO LOGIN", end card "200+ Free Productivity Tools". About 45 of 91 s are end cards.
- **Locale pages:** nav, breadcrumb and one badge translated; title, meta, H1, subtitle, button and card labels and all FAQ headings stay English (es screenshot; title/H1 English in all 9 locales).
- **SEO:** title "Parse a User Agent String Online | FreeDailyPro"; meta 89 chars, says nothing about bots, log lines or Client Hints/Windows 11. Generic OG image.

**P3:**
- Empty box falls back to your own browser's UA and shows its results; with a headless UA that fallback says Bot / script **No**, while the same UA pasted says **Yes**. Make the empty state blank (or run the same bot check).
- GPTBot: Browser "WebKit 537.36" (show GPTBot 1.2). Googlebot smartphone: Device "LG Nexus 5" (it's Googlebot's fixed Nexus 5X token; label it as crawler emulation). Sec-CH-UA results: Engine "Unknown" (Blink is implied for Chromium brands).
- Smart TV Device type shows "Smarttv" (should be "Smart TV").
- Copied/saved text puts the value before its label ("Mobile Safari / Browser") and leaves out the input string, so a pasted result in a ticket loses the original UA.
- Reduced Android UA shows Device "K" (correct per the string; a hint "Chrome hides the model; paste Sec-CH-UA-Model" would help).
- iPhone SE 9 px overflow (header action button, right=329); ja desktop 1369 px (site-wide). axe desktop: label-content-name-mismatch (serious), region (moderate); Pixel 7 clean.
- de-DE/fr-FR consent banner (screenshot) sits below the actions and partly covers the Feedback button; the tool is usable.

## Intent

A developer, QA person or support agent has a raw UA from a bug report or server log and needs to know browser, OS, device and whether it's a bot, quickly and correctly. The tool does this well and goes further (log lines, Client Hints, Windows 11), but the page copy tells people it can't.

## What works (verified)

- **Parsing:** iPhone iOS 17.4, Android reduced UA, Samsung tablet SM-X710 (Tablet), Pixel 8 Pro, Edge/Windows 10 amd64, Firefox/Mac 14.4, IE11/Windows 7 (Trident), smart TV (Tizen), full Apache log line → UA extracted.
- **Bots:** Googlebot smartphone, bingbot, GPTBot, curl, python-requests, Wget, HeadlessChrome, facebookexternalhit → Bot / script Yes.
- **Client Hints:** Sec-CH-UA paste (Android and Windows 11), browser hints in Chromium, honest note in Firefox.
- **Errors:** garbage text → amber "This doesn't look like a user-agent string …" with an example and where to copy one.
- **Actions:** Copy result, Save as text (.txt download), Print all work in guest contexts.
- **Layout:** tool at the top on desktop and phones; Firefox/WebKit/iPad fine.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 8 fields, bots, log lines, Client Hints. |
| 2 | Completeness | PASS | Beyond typical UA parsers (hints, log extraction). |
| 3 | Ease of use | PASS | Live results, pre-filled example, clear error. |
| 4 | Layout | PASS (minor) | SE 9 px overflow. |
| 5 | Payment process | N/A | No trial strip / Quick Buy on this page (owner question). |
| 6 | Information correct | FAIL | Client Hints "No"/"not read"; usage-logging privacy line; "Windows 10" card. |
| 7 | Indexing | PASS | 200, canonical self, 10 hreflang + x-default. |
| 8 | SEO | PARTIAL | Meta 89 chars, misses hints/bots/Windows 11; generic OG. |
| 9 | Blog | PARTIAL | Useful triage guide; repeats the wrong Client Hints claim. |
| 10 | YouTube video | PASS | -iWoAjyeKOY embedded. |
| 11 | FAQ / guide correct | FAIL | Client Hints and Windows 10/11 FAQs contradict the tool. |
| 12 | Video shows current capability | FAIL | Old 4-card UI; "free" wording; long outro. |
| 13 | Storage | N/A | None (verified). |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | PASS | .txt 173 bytes; content format P3. |
| 16 | Usage count | Owner question | Takes no trial use (0 POSTs at 10/10 and 0/10). |
| 17 | Categorization in section | PASS | Developer & Security / Professional. |
| 18 | Correct section of site | PASS | Related: Password Strength Checker, Password Generator, Base64 (all 200). |
| 19 | AI need and demand | PASS | Steady ("user agent parser", "what is my user agent", "sec-ch-ua"). |
| 20 | Merge better? | No | Distinct job. |
| 21 | Remove? | No | Useful developer utility. |
| 22 | Duplicates | None | No duplicate group. |

## After fixes, rerun

- `px66-live.js cases` (Sec-CH-UA, Windows card, Smarttv, GPTBot) and `hints`.
- `px66-live.js zero` / `left` once the owner decides on counting.
