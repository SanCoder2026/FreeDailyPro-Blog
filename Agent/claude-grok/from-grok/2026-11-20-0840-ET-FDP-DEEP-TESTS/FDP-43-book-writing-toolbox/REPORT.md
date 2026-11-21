Sent: 2026-11-21 05:21 ET

# FDP-43 Book Writing Toolbox (book-writing-toolbox): deep test report for Claude (v2)

> **v2 correction (2026-11-21, EST):** per the owner rule, the Book preview watermark is intentional. Its strength is now an **owner question**, not a bug or P1. See CORRECTIONS-v2.md. Everything else is unchanged from v1.

- **Written:** 2026-11-21 04:55 EST (box `date`, ET). Testing ran 2026-11-21 04:17–04:49 EST.
- **Tool:** https://www.freedailypro.com/tool/book-writing-toolbox. Row 43 of TEST-ORDER.md: **Workflow Product**, Publishing & Print Makers, plan note "GA top-traffic".
  - Duplicate group C38. Video: C2e9b_ROuk8. Blog: /blog/book-writing-toolbox.
  - **GSC data is not available.**
- **Offer:**
  - $29.99 a month with a 7-day trial, sign-in first.
  - Previews and Pre-flight are advertised as unlimited (watermarked).
  - Clean PDF/EPUB/manuscript/print-cover downloads need the subscription.
  - The $1 Day Pass and the $4.99 plan don't cover it.
  - The draft lives in the browser (IndexedDB); previews and exports are typeset on the server.
- **Testers:**
  - **Desk review:** copy, FAQ (9), Details, JSON-LD, locales, JS chunks (BookMaker, BookProjectBar, ToolPage helper).
  - **Headless Playwright:** 25 live cases (B01–B14, C01–C08, D01–D03) in Chromium, with Firefox and WebKit subsets. Every preview file the browser received was inspected (`verify.json`).
  - **Matrix:** 10 devices, 11 locales, 6 geo contexts, axe.
  - **Video:** downloaded and watched frame by frame.
- **Test files:** `scripts/make-files.py`:
  - chapter .docx (heading, bold/italic, list, table, image, scene break), three-Heading-1 .docx
  - .txt with "Chapter" lines; .md, CJK and Arabic text
  - a 400-paragraph book; low- and high-resolution covers; an invalid project file
- **Constraints kept:**
  - Guest only. The trial button led to /profile sign-in; I stopped there and typed nothing.
  - No card, no email, no ad clicks, no API/MCP calls, no site or repo changes.
  - The watermark check was done offline on our own preview file, and that file isn't distributed.
- **Sign-in (untested):**
  - "Start 7-day trial" → https://www.freedailypro.com/profile (sign-in).
  - Everything after it is untested: trial start, Stripe, the clean Download, Export EPUB/manuscript/print cover (`preview:false`), and the server-side entitlement check.
- **Nothing pending a usage reset**, so there's no RERUN-AFTER-RESET row.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Push back where the product intent differs.

**Owner context:**
- Santosh treats per-page-load charging and full-quality results at 0 trial uses as P1 gate gaps.
- This is a paid Workflow Product whose whole conversion lever is "watermarked previews, clean files with the subscription". The watermark is intentional (owner rule); how strong it should be is Santosh's call (owner question below). The lever also needs the previews themselves to work.

**Code to look at:**
- **Server preview renderers** (`bookMaker.renderBook/renderManuscript/renderCoverWrap/renderManuscriptDocx`, `preview:true`): the PDF mark is one tiling-pattern fill drawn *under* the content; the docx mark is one header paragraph.
- **`bookMaker.renderEpub`:** returns 500 for every call.
- **`BookMaker-0ysxrwOr.js`:** previews/ONIX saved via `bt` = ToolPage `d` (`vt` → `Sa`), the Professional trial-use wrapper. That causes per-page-load charging and a silent block at 0. Pass `{free:true}` (or the product rule) for previews and ONIX.
- **`BookProjectBar`:** the project file is metadata only.

**After you ship:**
- Rerun `scripts/bw-live.js`, `bw-live2.js`, `bw-live3.js` (D01/D02 need a context at 0 and one with uses left) and `testfiles/verify.py` (expect: EPUB files present, no 500s; PDF mark not a lone background pattern; docx mark in the body).
- Then work through test-cases.md.

## Intent

A self-publishing author wants to write or import a book, see a real typeset proof, catch KDP problems before paying, and then pay once for clean, submission-ready PDF, EPUB and manuscript files.

The editor, typesetting, import, Pre-flight print checks, covers, RTL and the script check deliver that well:
- A 257-page preview in about 9 s.
- Accurate KDP checks.
- Correct Shunn format.

Four things undercut both the "wow" and the move to paid:
- **Owner question, not a bug:** how strong the intentional preview watermark should be (PDF background mark; .docx header line).
- **The ebook half is broken:** the EPUB build returns 500 every time, and Pre-flight hides it.
- **"Unlimited" previews that aren't:**
  - The manuscript preview and ONIX take a Professional trial use per page load.
  - At 0 they silently do nothing.
- **A video that shows a different, older free product.**

## Why: what the evidence says

- **Owner question (not a bug): preview watermark strength.** The watermark is intentional per owner rule; these are facts for Santosh to decide on.
  - At 0 (counter 10/10), Preview returns the exact paid typeset PDF; the only difference is one tiling-pattern fill under the content.
  - Emptying that single object leaves a clean book (`screens/cases/B01-pattern-emptied-pages.png`). The same holds for the manuscript PDF and print-cover previews.
  - The manuscript .docx preview (with uses left) is the full manuscript with a single editable header line.
- **P1, per-page-load charging.**
  - Manuscript .docx preview: 0→1/10 on the first preview; the second preview and ONIX in the same load are free; after a reload it charges again (1→2).
  - This happens on a product whose copy says previews are unlimited and ONIX needs no subscription.
- **P1, silent failure at 0.**
  - The manuscript .docx preview and ONIX export do nothing: no file, no message, no offer.
  - The server still renders the file.
- **P1, EPUB broken.**
  - `renderEpub` returned 500 on 11 of 11 calls (04:26–04:47 EST, three engines).
  - Preview EPUB fails, and Pre-flight reports "complete" with no EPUB checks.
  - The paid Export EPUB uses the same mutation (unverified behind sign-in).
- **P2 items:**
  - **Video:** it is the old "Book Maker" with "10 free uses daily"; it shows a personal macOS file picker (home folder "chaithra", tag "Anu ma'am"); the description says "no account needed".
  - **Copy conflict on Indic scripts:** the FAQ says not supported, the live checker says supported.
  - **"Save book project":** saves metadata only, next to an "Erase everything, no other copy" warning.
- **P3 items:**
  - **Preview dialog:** double close buttons.
  - **Sidebar:** front-matter rows overlap after scrolling.
  - **Overflow:** iPad Mini 8 px, iPhone SE 9 px, /ja 3 px.
  - **axe:** button-name ×19 and label critical.
  - **Locales:** English titles; H1s translate "Book Maker"; /ar 404.
  - **Old name:** OG image `book-maker-launch.webp`; VideoObject name.
  - **Placement:** not on the Publishing category page.
  - **Arabic book:** the English boilerplate's punctuation flips in RTL.
  - **Trim lists:** the same 18 sizes for Default and IngramSpark (unverified claim).
  - **/profile:** an ad overlays the sign-in card (give it a reserved slot).

## Outcomes we want

1. Santosh decides whether the intentional preview watermark is strong enough. Options if he wants it stronger: mark over the content, rasterised previews, or a docx mark in the body or a sample.
2. EPUB builds succeed. Pre-flight shows the EPUB checks, or says plainly that they couldn't run.
3. Previews and ONIX never take Professional trial uses and never fail silently at 0, matching "unlimited" and "no subscription needed".
4. A new video of the current Toolbox on a clean profile, with correct offer wording.
5. Copy is consistent (Indic scripts); "Save book project" is renamed or becomes a real backup; the old "Book Maker" name is gone from the OG image, locales and VideoObject.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PARTIAL | Editor, import, typesetting, Pre-flight (print), covers, manuscript and RTL work. **EPUB 500 on every call.** |
| 2 | Completeness vs competitors | PASS (strong) | Compared with Atticus, Vellum and Reedsy Studio: platform-aware trims and margins, Pre-flight, ONIX, Shunn, print cover. Missing: cloud sync/backup, collaboration (documented), a working EPUB. |
| 3 | Ease of use | PARTIAL | Clear sections and messages; previews silently do nothing at 0; the preview dialog has 2 close buttons. |
| 4 | Layout attractiveness | PARTIAL | A clean dark desk; sidebar rows overlap after scrolling; small overflow on iPad Mini and iPhone SE. |
| 5 | Payment process | PARTIAL / stopped | Download/Export → $29.99 dialog → Start trial → /profile sign-in (stopped). Stripe is untested (sign-in). |
| 6 | Information correct | PARTIAL | "Unlimited" previews charge or block; Indic-script contradiction; EPUB claims. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Good title, meta, Offer JSON-LD and FAQ; OG image and VideoObject carry the old name; locale titles are English. |
| 9 | Blog exists and accurate | PASS | /blog/book-writing-toolbox is accurate (two minor wording slips). |
| 10 | YouTube video exists | PASS | C2e9b_ROuk8, embedded. |
| 11 | FAQ and guide correct | PARTIAL | See check 6. |
| 12 | Video shows current capabilities | **FAIL** | Old "Book Maker", "10 free uses daily", personal file picker. |
| 13 | Storage | PARTIAL | IndexedDB drafts, My Books and reload all PASS; the project file holds metadata only; no backup of the content. |
| 14 | Sharing | PASS | Share this tool. |
| 15 | Downloads | PARTIAL | Preview files are correct. Clean downloads are untested (sign-in). EPUB fails. ONIX/manuscript preview are blocked silently at 0. |
| 16 | Usage count | **FAIL (P1)** | Per-page-load Professional charge on the manuscript preview and ONIX; book preview and Pre-flight uncounted (as advertised). |
| 17 | Categorization in section | PASS | Publishing & Print Makers / Workflow Products. |
| 18 | Correct section of site | PARTIAL | Missing from the Publishing category page (SITE-MAP). |
| 19 | AI need/demand | PASS | High demand. Chat assistants can't typeset a KDP-ready PDF/EPUB, so the value is clear. |
| 20 | Merge better? | No | It's the hub; cross-link the C38 Premium Applications to it. |
| 21 | Remove? | No | GA top-traffic, paid product. |
| 22 | Duplicates | C38 overlap | Overlaps manuscript-formatter, epub-maker, book-interior-maker and copyright-page-maker. Keep them, and clarify plan coverage and cross-links. |

## Severity summary
- **P0:** 0. (The EPUB failure may affect paying subscribers; confirm signed in and raise it to P0 if export fails too.)
- **P1:** 3 (per-page-load charging; silent block at 0; EPUB 500).
- **Owner question:** 1 (how strong the intentional Book preview watermark should be).
- **P2:** 3 (video; Indic-script copy; project file isn't a backup).
- **P3:** several.
