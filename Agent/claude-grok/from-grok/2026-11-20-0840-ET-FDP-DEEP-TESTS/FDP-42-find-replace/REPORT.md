Sent: 2026-11-21 04:17 ET

# FDP-42 Find & Replace (find-replace): deep test report for Claude

- **Written:** 2026-11-21 04:15 EST (box `date`, ET). Testing ran 2026-11-21 03:55–04:12 EST.
- **Tool:** https://www.freedailypro.com/tool/find-replace. Row 42 of TEST-ORDER.md: Pro, Text & Writing. Plan note "GA top-traffic".
  - Duplicate group C47 (text-paraphraser, grammar-checker, reading-level-checker, text-cleaner, case-converter, ai-prompt-optimizer).
  - Video: ZRbu9e3kDO4. Blog: /blog/find-replace.
  - **GSC data is not available.**
- **Classification:** Professional Tool. Pasted text and files (.txt .json .csv .md .html .xml .docx) are edited in the browser; nothing is uploaded (`evidence/json/privacy.json`).
- **Testers:**
  - **Desk review:** copy, 11 FAQs, JSON-LD, 10 locales + /ar, JS chunks, the blog's static vs rendered text.
  - **Headless Playwright:**
    - a gate run at 0 and one with uses left (one fresh context with 10 left at 03:59 EST)
    - 28 cases in Chromium plus a 10-case subset in Firefox and WebKit, with every download checked by `verify.py`
    - a privacy check and the 10-device / 11-locale / 6-geo / axe matrix
- **Test files:** `scripts/make-files.py` builds:
  - text, JSON, CSV, Markdown, HTML and XML files
  - a Unicode/emoji file and a 6.4 MB file
  - a fake .doc and a PNG
  - a rich .docx (split bold/italic runs, a red 16 pt run, a table, an image, header/footer, a {{name}} template, a phrase split across paragraphs)
  - plus a broken .docx
- **Constraints kept:**
  - Guest only and no sign-in. No email or card typed. There is no payment path on this page to stop at.
  - No ad clicks, no API/MCP, no site or repo changes.
- **Sign-in (untested):** "Open from Google Drive" (drop zone; not clicked). There's no Save to Google Drive or Save to my cloud storage on results.
- **Nothing pending a usage reset**, so there's no RERUN-AFTER-RESET row.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

**Owner context:**
- On Nov 20 Santosh decided that only Unit Converter, Grammar Checker and Word Counter are uncounted on purpose, and any other tool that takes no trial use is a policy question.
- Full-quality results at 0 trial uses are P1 gate gaps.
- Find & Replace takes no trial use at all, including the .docx file round-trip, which delivers a finished Word file at 0.

**Code to look at:**
- **`index-B1CTyGtY.js` `Ps`:** `"find-replace":["absorbable","text","Text utility on pasted text; a chat assistant does this for free"]`, with `TA()` making it uncounted (`evidence/js/index-B1CTyGtY.excerpt-absorbable.js`, which also lists all 99 absorbable tools for the policy review).
- **`FindReplace-DrPESoBx.pretty.js`:**
  - Replace All (`q`) calls `logUsageNow` only for pasted text.
  - Download (`G`) uses ToolPage `d` (plain save), not the gated `D`.
  - **Option:** keep pasted text uncounted if Santosh agrees, but route file downloads (at least .docx) through the gated Download, which also brings Save to Drive/cloud and the pass offer.
- **`utils-CRM_dY3d.pretty.js` `M()`:** preserve-case treats "Acme Corp" (multi-word title case) as "use as typed". Apply title case per word.
- **Prerender of blog posts:** a string `String.replace` expands `$&` in post bodies (static `/blog/find-replace` HTML contains `<div id="root"></div>amp;`).

**After you ship:** rerun `scripts/fr-gate.js 12`, `fr-live.js chromium`, `testfiles/verify.py live/downloads`, then test-cases.md (FR-01…FR-34).

## Intent

Someone renaming a product across a long Word manual, fixing a CSV export, or reformatting dates with regex wants:
- the count before committing
- control over case and whole words
- formatting kept in Word
- one-step undo
- nothing uploaded

The engine delivers:
- Exact counts and replacements across 28 cases: whole word and preserve case in any script, regex groups/named groups/`\n`, live invalid-pattern handling.
- JSON/XML break warnings, and .docx edits that keep runs, colours, tables and images.
- A 6.4 MB file with 120,000 matches in about 5 s, and identical results in Firefox and WebKit.

Revenue and trust break in four places:
- **Gate and upsell:** no trial use is ever taken, and there is no trial strip, pass offer or upgrade prompt, so the .docx file job is free at 0 and the page never moves anyone toward paid.
- **Preserve case:** misses Title-Case names ("Acme Corp" → "globex").
- **Copy:** contradictory .docx FAQs and promised .doc/other-type messages that never appear.
- **Video:** old UI, "free" wording, and personal bookmarks/taskbar on screen.

## Why: what the evidence says

- **P1 gate gap + policy question: full-quality results at 0 trial uses; the tool is uncounted.**
  - At 0 (03:57–03:58 EST): pasted Replace All, .txt Replace All (the full text is editable and copyable), **Download Corrected File** and **Download Corrected .docx** all worked with no cap dialog.
  - With 10 uses left (03:59–04:00 EST): 5 replaces, 3 downloads and reloads left the counter at **0**.
  - It's marked "absorbable" in code. That isn't one of the three tools Santosh exempted, and the reason given ("pasted text; a chat assistant does this for free") doesn't cover .docx round-trips.
- **P1 (conversion): no trial strip, Quick Buy, pass offer, badge note, or Save to Drive/cloud anywhere on the page.** Check 5 has nothing to test, and the "moved toward paid" goal fails.
- **P2: preserve case and multi-word Title Case** (T21: "Acme Corp" → "globex"; ACME CORP → GLOBEX works). The FAQ promises capitalised replacements.
- **P2: contradictory FAQ.** "won't be found at that exact split point" vs "a phrase split across several formatted pieces is still found". Live, it's found.
- **P2: video.** Personal bookmarks ("Jain Notes", "Cloths Aestetic", Gmail, Netflix, "Anikoto - Stream A…") and taskbar visible; old "10 free uses daily" UI; "Free" title and "200+ Free Productivity Tools" end card; never shows files, .docx or regex.
- **P3 items:**
  - .doc and other types get the generic drop-zone toast, not the promised specific messages; a broken .docx shows "Corrupted zip: can't find end of central directory".
  - CSV comma insertion gives no warning; catastrophic regex freezes the tab (11 s at 29 chars); .docx has no live counter.
  - Blog static HTML `$&` prerender artefact; VideoObject name mismatch; generic OG image.
  - Locales leave the H1 and UI English; /ar 404; iPhone SE 9 px and ja 3 px overflow; axe label mismatch / region / ad-caption contrast.

## Outcomes we want

1. Santosh decides whether Find & Replace stays uncounted. If it stays uncounted, at least the file round-trip (.docx especially) goes through the gated Download, so a finished Word file isn't free at 0.
2. The page shows the trial strip and pass offer like other Professional Tools, and file results offer Save to Drive/cloud.
3. Preserve case turns "Acme Corp" into "Globex" (title case per word).
4. One consistent .docx FAQ; the promised .doc/unsupported-type messages actually appear.
5. A re-recorded video on a clean profile, showing .docx + regex, with Professional Tools / trial uses wording.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS (minor) | 22 of 28 Chromium cases pass outright. The exceptions are T21 preserve case (P2) and T15/T17/T18/T19/T25 (P3 messages and edge cases). |
| 2 | Completeness vs competitors | PASS (strong) | Regex, whole word (Unicode), preserve case, .docx in place, 7 text formats, JSON/XML checks. Could add a match list/preview with per-match skip, multi-step undo, and headers/footers in .docx. |
| 3 | Ease of use | PASS (minor) | Live counter, clear errors, Undo; no counter for .docx. |
| 4 | Layout attractiveness | PASS (minor) | iPhone SE 9 px, ja 3 px. |
| 5 | Payment process | **FAIL / N/A** | No strip, Quick Buy, pass offer or cap dialog on this page; nothing to stop at. |
| 6 | Information correct | PARTIAL | Contradictory .docx FAQ; preserve-case promise; .doc message promise. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Strong title/meta (156); full JSON-LD; VideoObject name mismatch; generic OG; untranslated H1/title in locales; /ar 404. |
| 9 | Blog exists and accurate | PASS | /blog/find-replace is accurate and honest; static-HTML `$&` artefact (P3). |
| 10 | YouTube video exists | PASS | ZRbu9e3kDO4, embedded. |
| 11 | FAQ and guide correct | PARTIAL | See check 6. |
| 12 | Video shows current capabilities | **FAIL** | Old UI, pasted text only, "free" wording, personal bookmarks/taskbar. |
| 13 | Storage | PASS | Nothing stored; no cloud save offered. |
| 14 | Sharing | PASS | "Share this tool" only. |
| 15 | Downloads | PASS | `_edited` names, same format, UTF-8 no BOM, .docx formatting kept (`verify.json`). |
| 16 | Usage count | **FAIL (P1, policy question)** | Never counted; full .txt/.docx downloads at 0. |
| 17 | Categorization in section | PASS | Text & Writing. |
| 18 | Correct section of site | PASS | Breadcrumb Home › Text & Writing. |
| 19 | AI need/demand | PASS (demand) | High search volume. Chat assistants do pasted-text replace but not formatting-safe .docx edits, which is the paid angle. |
| 20 | Merge better? | Consider | Pair with find-replace-powerpoint as one document find-and-replace entry. |
| 21 | Remove? | No | GA top-traffic. |
| 22 | Duplicates | C47 low overlap | Distinct from the paraphraser/cleaner/case tools; cross-link find-replace-powerpoint. |

## Severity summary
- **P0:** 0.
- **P1:** 2 (full-quality results at 0 / uncounted policy question; no upsell path on the page).
- **P2:** 3 (preserve case, contradictory FAQ, video privacy and wording).
- **P3:** several.
