Sent: 2026-11-21 00:40 ET

# FDP-31 UUID Generator (uuid-generator): deep test report for Claude

- **Written:** 2026-11-21 00:38 EST (box `date`, ET). Testing ran 2026-11-21 00:17–00:36 EST.
- **Tool:** https://www.freedailypro.com/tool/uuid-generator. Row 31 of TEST-ORDER.md: Pro, Developer & Security Tools, grouped with test-plan rank 23 (JWT / UUID / Hash); no duplicate group. **GSC data is not available.**
- **Classification:** Professional Tool, tagged `absorbable:dev-text`. Live at 0 remaining, Generate and every copy still work with no cap dialog.
- **Testers:**
  - **Desk review:** expanded copy, JSON-LD, 10 locales + /ar, the blog, sitemap. JS chunks: `UuidGenerator`, `useShareGate`, `useExportGate`.
  - **YouTube video:** yt-dlp, 29 frames, 3 sheets and zooms.
  - **Headless Playwright:**
    - 12 count cases.
    - A 4,025-UUID quality check (format, uniqueness, distribution) and format toggles.
    - A request scan for generated values.
    - Gate run at 0 incl. selection copy; Share.
    - Print; keyboard order.
    - 10-device / 11-locale / 6-geo / axe matrix.
- **Starting counts (display-only):** every fresh context loaded at "0 remaining" (`usageToday` 10 of 10, day key 2026-11-21). Trial uses spent: **0**.
- **Constraints kept:** guest only, no sign-in, no email or card typed (no prompt appeared), no ad clicks, no API/MCP, no site or repo changes.
- **Sign-in:** nothing on this tool needs it. No URL was blocked by sign-in.
- **Pending:** the "context with uses left" count → **RERUN-AFTER-RESET row 31** (`ug-gate.js`).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

Code to look at (`evidence/js/`):
- `UuidGenerator-CmXHafTq.pretty.js`:
  - Generate (`b`) awaits `logUsageNow()` before `crypto.randomUUID()`.
  - Every per-row copy and Copy All runs through `gateShare`. If uses are charged, copying five single values could cost five trial uses; to confirm in the rerun.
- `useShareGate-BYBawloP.pretty.js`, `useExportGate-BU4jIFHF.pretty.js`: counted only when `known && !paid`. At 0 remaining nothing blocked live (display-only observation; no backend claim).

After you ship, rerun `scripts/ug-gate.js` (with uses left and at 0), `ug-live.js` (`leaks` must stay empty, all v4) and `ug-misc.js`, then test-cases.md (UG-01…UG-30).

## Intent

A developer filling a seed file, fixtures or test data wants:
- correct, unique UUIDs right now, in the format their system needs (hyphens, case, maybe braces, quotes or SQL)
- sometimes a newer version (v7 for database keys)
- a big batch they can download rather than copy

They need to trust that values are generated locally. They should see why the Professional Tools version is worth a trial use.

The core is solid and honest:
- `crypto.randomUUID()`; all 4,025 values are valid v4 with a uniform distribution and no repeats.
- Clear validation and a 1,000 cap with a note.
- Live hyphen/case toggles; accessible copy buttons.
- No value ever left the browser.

The gaps are policy, copy and depth:
- The trial gate is wired in code, and the blog says each Generate costs a trial use, but at 0 remaining everything works.
- Tips tell people to uppercase by hand although an Uppercase checkbox exists.
- Only v4, no format presets and no download.
- The video shows the old UI with a "free uses left" counter and no toggles.

## Why: what the evidence says

- **P1, policy question for Santosh (not a PASS):**
  - At 0 remaining, Generate (twice), Copy UUID 1, Copy All and selection copy all worked with no dialog. The count stayed 10 → 10, also after reload (`json/gate.json`, 00:19:02–00:19:48 EST; `json/try.json`).
  - The code calls `logUsageNow()` on Generate and `gateShare` on each copy.
  - The blog promises "Each press of the button counts as one of your 10 trial usages for the day", and the video shows "8 free uses left today".
  - Not in the Nov 20 uncounted list. With uses left: pending (RERUN row 31), including whether every single-row copy is charged separately.
- **P2 items:**
  - **Completeness:** no v7 (time-ordered, now common for DB keys), v1 or v5, or nil/max. No braces, quotes, comma, SQL or JSON array formats. No Download .txt/.csv for 1,000-row batches. No validator/decoder (desk vs uuidgenerator.net/uuidtools; not re-verified live).
  - **Copy contradiction:** Tips "Output is in the standard lowercase hyphenated form… so uppercase it yourself if a system insists" vs the Uppercase checkbox. The blog closing asks if readers want "uppercase output" (already exists).
  - **Video CuyJw3t7968 (59 s):**
    - Old UI: "10 free uses daily" and "8 free uses left today", "Security & Developer".
    - No Hyphens/Uppercase toggles.
    - "FREE" on the title card and the YouTube title; the embed name differs.
  - Locales: es is half-translated (title "gratis"); 8 others are English under their lang/hreflang; /ar 404. "v4"/"GUID" missing from the title/meta.
  - 1,000 rows render as 1,000 cards, each with a copy button. Copy All sits at the bottom, so keyboard users tab through 1,000 buttons first.
- **P3 items:**
  - iPhone SE 9 px overflow (same button as FDP-30); ja desktop 3 px.
  - 24 px checkboxes and 36 px controls on mobile.
  - The stale list stays under an invalid count; "1e3" is accepted.
  - "session tokens" in What-is-it vs "not as session tokens" in When-not-to-use.
  - "Keep the Count at 100" tip vs the default of 5.
  - Thumbnail alt; axe label-content-name-mismatch, region and ad-caption contrast; JSON-LD Offer 4.99.

## Outcomes we want

1. Santosh decides the trial-use policy for this tool. Code, blog, page and JSON-LD Offer then agree. If counted, a copy of a value already generated should not be charged again per row.
2. The copy, FAQ and blog match the tool: Uppercase exists, and the trial-use sentence is accurate.
3. A clear Premium step: v7 (and v1/v5/nil), format presets (braces, quotes, CSV, SQL, JSON), Download for big batches, and a validator.
4. Large batches are usable: a compact list or a textarea view, with Copy All and Download above the list.
5. A current video with the toggles and "trial uses" wording; localized pages or no hreflang.
6. P3 polish per PRIORITIES.md.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | **PASS** | 12/12 count cases as documented. 4,025 distinct valid v4 values; uniform hex and variant split (`json/cases.json`). |
| 2 | Completeness vs competitors | PARTIAL | v4 only; no format presets, download or validator (desk; not re-verified live). |
| 3 | Ease of use | PASS (minor) | One field and one button; clear messages. 1,000-row list is unwieldy; Copy All at the bottom. |
| 4 | Layout attractiveness | PASS (minor) | Clean. iPhone SE 9 px overflow; small checkboxes. |
| 5 | Payment process | N/A (untested) | No cap dialog, pass or Stripe appeared, even at 0 remaining. |
| 6 | Information correct | PARTIAL | Validation and privacy copy match. The Tips "uppercase it yourself" line and the blog's trial-use sentence conflict with live. |
| 7 | Indexing | PASS | 200; canonical self; in the sitemap. |
| 8 | SEO | PARTIAL | Good title/meta/FAQPage (6)/VideoObject. No "v4"/"GUID"; English pages under 8 hreflangs; es mixed; /ar 404; thumbnail alt; Offer 4.99. |
| 9 | Blog exists and accurate | PARTIAL | `/blog/uuid-generator` is practical and technically correct, but its trial-use claim isn't what happens at 0 and its uppercase request is stale. |
| 10 | YouTube video exists | PASS | CuyJw3t7968, 59 s, 34 views, uploaded 2026-09-23. |
| 11 | FAQ and guide correct | PARTIAL | 6 FAQs correct; the Tips uppercase line is wrong; "session tokens" mixed message. |
| 12 | Video shows current capabilities | **FAIL** | Old UI with a "free uses left" counter; no Hyphens/Uppercase; "FREE" wording. |
| 13 | Storage | PASS | Nothing stored; reload clears the list (as stated). |
| 14 | Sharing | PASS | Share copies only the tool URL (`json/share.json`). |
| 15 | Downloads | PARTIAL | Per-row copy and Copy All work. No download option at all. |
| 16 | Usage count | **Policy question** | At 0: Generate and all copies work, 10 → 10. The code and blog imply counting. With uses left: pending (RERUN row 31). |
| 17 | Categorization in section | PASS | Developer & Security Tools with JWT, Hash, Base64. |
| 18 | Correct section of site | PASS | Breadcrumb Home › Developer & Security Tools. |
| 19 | AI need/demand | PASS (demand steady) | "uuid generator" is an evergreen developer query; no AI needed. |
| 20 | Merge better? | No (consider later) | Could host a "UUID tools" page with a validator; keep separate from Hash/Password. |
| 21 | Remove? | No | |
| 22 | Duplicates | None | |

## Severity summary
- P0: 0. Privacy holds: no generated value in any request.
- P1: 1 (trial-use policy question; the code and blog imply counting).
- P2: about 5.
- P3: several.
