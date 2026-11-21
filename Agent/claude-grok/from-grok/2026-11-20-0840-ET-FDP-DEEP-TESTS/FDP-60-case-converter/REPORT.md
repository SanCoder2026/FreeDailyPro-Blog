Sent: 2026-11-21 12:33 ET

# FDP-60 Case Converter (case-converter): deep test report for Claude

- **Written:** 2026-11-21 12:32 EST (box `date`, ET). Testing ran 2026-11-21 12:15–12:30 EST.
- **Tool:** https://www.freedailypro.com/tool/case-converter
  - TEST-ORDER row 60: **Professional Tool**, Text & Writing. Plan note "test-plan (unranked): SEO backfill 8 (GA top)". Site-map tag `absorbable:text`. Duplicate group C47 (text-paraphraser, grammar-checker, reading-level-checker, text-cleaner, find-replace, ai-prompt-optimizer).
  - Video qv3ivSaFGY8 (embedded, 118 s, 2026-09-24). Blog /blog/case-converter (Oct 17, 2026).
  - **GSC data is not available.** No API/MCP testing.
- **How it works:** one textarea; 10 buttons (UPPERCASE, lowercase, Title Case, Sentence case, aLtErNaTiNg, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE) each convert the **original** text (so styles can be tried in a row), Restore original, Copy, Download .txt (`converted-text.txt`). All in the browser.
- **Testers:**
  - Desk: copy (7 FAQs, How to, Limitations, Privacy), JSON-LD, blog, JS (`CaseConverter-CbuegihP.js`, `copyText-DPnES92p.js`).
  - Playwright: `probe.json` (Chromium, 10/10: convert, Copy, Download), `cases.json` (Chromium, 22 inputs + a 202,500-char Title Case run in one load), `left-firefox.json` and `left.json` (Chromium) — contexts at 0/10 (Firefox on try 29, Chromium on try 5): empty click, 3 conversions, restore, copy, download, reload, 2 conversions. An earlier Firefox attempt found no 0/10 context in 25 tries (`left-firefox-try1-nouses.*`).
  - `px60-expected.mjs` recomputes every case from the site's own conversion code: **all 22 match live output** (`expected-compare.json`).
  - Video frame sheet and crops reviewed. Matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only; no sign-in, card or email; no ad clicks; no site or repo changes.
- **Sign-in (untested):** none needed. No Drive, cloud or account feature (verified live). No trial strip or Quick Buy on the page (verified live), so no payment entry point here.
- **RERUN-AFTER-RESET:** none. Behaviour with uses left and at 10/10 both observed today.
- **P0/P1:** none.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders.

**Owner context (Nov 20):** copy and results count as trial uses. Only Unit Converter, Grammar Checker and Word Counter are uncounted on purpose. A tool that takes no trial use and isn't one of those three is a **policy question held for Santosh, not a P1 fix order** — see Owner question 1. Please don't change charging until he decides.

**Where to look:**
- **Usage (owner question, not a fix order):** no trial use is ever taken. At 10/10 (probe.json) conversion, Copy and Download all work, with no cap dialog. With uses left (left-firefox.json, left.json) 6 conversions, a copy and a download across a reload stayed 0/10, and **no `/api/trpc/usage.log` POST** was sent (posts: [] on every step). The page has no trial strip or Quick Buy. The conversion handler awaits `logUsageNow()`, but it returns "allowed" without logging, the same as Social Caption Generator (FDP-59).
  - Privacy copy says "The only thing the page reports is a usage count naming the tool, sent when you first click a conversion" — nothing is sent today. Align the copy with Santosh's decision.
- **Video (qv3ivSaFGY8) is outdated:** the recording shows 6 conversion buttons + Copy (no PascalCase, snake_case, kebab-case, CONSTANT_CASE, Download .txt or Restore original), the old "10 free uses daily" and "Pro" badges, a personal browser bookmarks bar and the Windows taskbar. Title "Free Step-by-Step Walkthrough", description "Try Case Converter free", "Free daily uses", tag "PDF tools", end card "200+ Free Productivity Tools", ~35 s of 118 s is outro.
- **Copy contradicts itself on acronyms:** "When not to use it" says Sentence case "lowercases everything first… so NASA becomes Nasa". The FAQ (correct) says acronyms are kept in mixed-case text. Live: "this is NASA calling" → "This is NASA calling" (T07); only all-caps text loses them (T09). Fix the "When not to use" paragraph.
- **Blog undersells:** it says iPhone, API, NASA "often need manual fixes because automatic title case mangles brand spelling", and that "about us" needed a manual "About Us". Live keeps iPhone/NYC/API in mixed text (T02) and Title Case gives "About Us". It doesn't mention Restore original or the programming styles beyond one FAQ line.
- **Title Case after a colon:** "the lord of the rings: the return of the king" → "The Lord of the Rings: the Return of the King" (T01). Most guides (AP, Chicago, APA) capitalize the first word after a colon. Treat the word after ":" (and "—") as a line start.
- **Sentence case after abbreviations:** "at 5 p.m. today" → "p.m. Today"; "e.g. this" → "E.g. This" (T08). Add a small abbreviation list (a.m., p.m., e.g., i.e., etc., Dr., Mr., Mrs.).
- **Small things:** clicking a style on an empty box shows "Restore original" for nothing (L00). Locale pages translate only nav, breadcrumb and badges (screenshots).

**After Santosh decides on usage:**
- Rerun `px60-live.js left firefox` and `probe` (expect +1 per conversion/copy and a cap dialog at 10/10 if counted).
- Rerun `cases` + `px60-expected.mjs` after the Title/Sentence fixes (T01, T08).

## Intent

A writer, marketer or developer pastes text with the wrong capitalisation and wants it fixed in one click — headline style, sentence style or a variable name — without retyping and without uploading anything.

## What works (verified)

- **All 10 styles** match the site's code on 22 inputs, including: small words lowercase mid-line with first/last word capitalised (T01, T05); acronyms and iPhone kept in mixed text (T02); McDonald, O'Neil, D'Angelo (T04); hyphenated "State-of-the-Art" (T06); "i'm" → "I'm" (T07); camelCase "user-id (new) for fox's tail" → userIdNewForFoxsTail and XMLHttpRequest → xmlHttpRequest (T10, T11); accents (T12); Turkish İ → i (T13); symbols dropped in kebab (T14); ß → SS in UPPERCASE (T17); Greek final sigma ς in lowercase (T18); Greek/Cyrillic Title (T19); CJK untouched (T20); quotes (T21); per-line Sentence case (T22).
- **Restore original** returns the text typed before the first conversion after several styles, then disappears (L02b). Each style converts the original, not the previous result (L02).
- **Copy** ("Copied!", clipboard = box) and **Download .txt** (UTF-8, exact text) work. Copy/Download disabled on an empty box.
- **Large text:** 202,500 characters through Title Case in ~4 s including fill (Chromium).
- **SEO:** title 54, meta 160 (specific), canonical self, hreflang 10 + x-default, JSON-LD SoftwareApplication, VideoObject, FAQPage (7), Breadcrumb; in sitemap.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 22/22 match the code. |
| 2 | Completeness | PASS (minor) | 10 styles + restore + download; competitors (convertcase.net etc.) also offer inverse/strikethrough/title-guide presets (AP/Chicago). |
| 3 | Ease of use | PASS | One box, one click; restore. |
| 4 | Layout | PASS | 10 devices fine (iPhone SE header 9 px, site-wide). |
| 5 | Payment process | N/A — no entry point | No strip or Quick Buy (verified live). |
| 6 | Information correct | PARTIAL | "When not to use" NASA line; Privacy usage-count line. |
| 7 | Indexing | PASS | 200, canonical, hreflang, sitemap. |
| 8 | SEO | PASS | Strong title/meta; FAQPage 7; VideoObject. |
| 9 | Blog exists and accurate | PASS (minor) | Generic, undersells acronym handling; "About Us" example. |
| 10 | YouTube video exists | PASS | qv3ivSaFGY8 embedded. |
| 11 | FAQ and guide correct | PASS (minor) | FAQ accurate; "When not to use" contradicts it. |
| 12 | Video shows current capabilities | **FAIL (P2)** | 6 of 10 styles, no restore/download, old badges, "free" wording. |
| 13 | Storage | N/A | None (verified live). |
| 14 | Sharing | PASS | Copy; Share this tool. |
| 15 | Downloads | PASS | converted-text.txt, exact. |
| 16 | Usage count | Owner question | Takes no trial use at all; works at 10/10; no strip. Not one of the 3 exempt tools → held for Santosh. |
| 17 | Categorization in section | PASS | Text & Writing. |
| 18 | Correct section of site | PASS | Breadcrumb Text & Writing. |
| 19 | AI need/demand | Low | Deterministic; chat assistants can do it but slower; strong search demand (GA top per plan). |
| 20 | Merge better? | No | High-traffic standalone intent. |
| 21 | Remove? | No | SEO backfill, GA top. |
| 22 | Duplicates | C47: keep | Distinct from text-cleaner/find-replace; cross-links to Word Counter/Paraphraser/Grammar present; Slug Generator (blog) could be linked. |

## Owner questions

1. **Policy (held for Santosh):** case-converter takes no trial use — conversions, Copy and Download work with uses left (0/10 stays 0/10, no `usage.log` POST) and at 10/10, with no cap dialog and no trial strip. It isn't one of the three exempt tools. Count it, or add it to the exempt list? The Privacy line about a usage count must match.
2. If it stays uncounted, should the page still show a pass/workflow CTA (no paid entry point today)?
