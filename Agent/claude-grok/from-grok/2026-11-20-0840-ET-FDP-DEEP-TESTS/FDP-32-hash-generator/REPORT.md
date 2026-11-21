Sent: 2026-11-21 00:58 ET

# FDP-32 Hash Generator (hash-generator): deep test report for Claude

- **Written:** 2026-11-21 00:56 EST (box `date`, ET). Testing ran 2026-11-21 00:38–00:54 EST.
- **Tool:** https://www.freedailypro.com/tool/hash-generator. Row 32 of TEST-ORDER.md: Pro, Developer & Security Tools, grouped with test-plan rank 23 (JWT / UUID / Hash). Duplicate group C50 (Passwords and hashes); the merge suggestion there concerns the two password tools, not this one. **GSC data is not available.**
- **Classification:** Professional Tool, tagged `absorbable:dev-text`. Live at 0 remaining, everything still works with no cap dialog.
- **Testers:**
  - **Desk review:** expanded copy, JSON-LD, 10 locales + /ar, the blog, sitemap. JS chunk: `HashGenerator`.
  - **YouTube video:** yt-dlp, 44 frames, 4 sheets and a zoom.
  - **Headless Playwright:**
    - 7 text vectors and 4 files (up to 60 MB), checked against Python hashlib.
    - Compare-box formats; stale-result and file-vs-text checks; keyboard reach.
    - A request scan for text, file content and digests.
    - Gate and uses-left runs; Share; print.
    - 10-device / 11-locale / 6-geo / axe matrix.
- **Starting counts (display-only):** fresh contexts loaded at "0 remaining" (`usageToday` 10 of 10, day key 2026-11-21). The exception was one context that read 0 used (see check 16). Trial uses spent: **0 observed**.
- **Constraints kept:** guest only, no sign-in, no email or card typed (no prompt appeared), no ad clicks, no API/MCP, no site or repo changes.
- **Sign-in:** nothing on this tool needs it. No URL was blocked by sign-in.
- **Pending:** the "context with uses left" count → **RERUN-AFTER-RESET row 32** (`hg-gate.js`, `hg-uses.js`).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

Code to look at (`evidence/js/HashGenerator-B91DxNzs.pretty.js`):
- **Textarea `onChange`:** `s(value), l("")` sets the text and clears the error but keeps the results `r`, so the digests and the Compare verdict go stale. The file `onChange` does clear the results.
- **File input:** `className: "hidden"` inside a `<label>`, so it can't be reached by keyboard.
- **Generate:** `H` awaits `logUsageNow()` before hashing. Copy uses `copyText` (no gate).
- **Hashing:** `_()` runs hash-wasm in 4 MB slices; `U()` is the Compare normaliser.

After you ship, rerun `scripts/hg-stale.js` (expect no "Match" after editing), `hg-live.js` (all digests = `testfiles/vectors.json`; `leaks` empty; Tab reaches the file picker) and `hg-gate.js`, then test-cases.md (HG-01…HG-30).

## Intent

Someone who just downloaded an installer, ISO or dataset, or who is comparing two copies, wants to:
- choose the file
- paste the publisher's checksum
- get an unambiguous Match / No match they can trust

Developers also want quick digests of text. Everything must stay on their device. The page must make the trusted answer obvious, never a misleading one.

The engine is excellent:
- Every digest of every vector and file (up to 60 MB, under 1 s) matched hashlib.
- Unicode is right, and large files are chunked with progress.
- Compare forgives case and spaces.
- Nothing leaves the browser.

Trust breaks in three places:
- **False Match:** after the text is edited, the old digests and verdict stay, so Compare can say "Match" for different content.
- **Keyboard:** keyboard users can't pick a file.
- **Policy and video:** the trial gate is wired but nothing is counted at 0, and the video shows a text-only old UI with the recorder's bookmarks bar.

## Why: what the evidence says

- **P1: a false "Match" for different content.**
  - Hash "abc", change the text to "abd", then paste abc's SHA-256 into Compare: "Match (SHA-256)" (`json/stale-compare.json`, 00:40:36 EST; `screens/live/stale-compare.png`).
  - No stale notice appears.
- **P1: the file picker is not keyboard accessible.**
  - Tab goes from the text box straight to Generate. The input is `display:none` (`json/cases.json`).
  - File integrity is the page's lead use case.
- **P1, policy question for Santosh (not a PASS):**
  - At 0 remaining, Generate (text and file), Copy, Compare and selection copy all worked, 10 → 10, also after reload (`json/gate.json`, 00:40:52–00:41:50 EST).
  - One context loaded with 0 used and stayed at 0 after 2 Generates. This is unconfirmed: 6 follow-up contexts were at 10 (`json/uses-left.json`).
  - The code calls `logUsageNow()`, and the blog says "remember 10 trial usages a day".
  - Not in the Nov 20 uncounted list. With uses left: pending.
- **P2 items:**
  - **Video 7vHVmGVIeWA (88 s):**
    - Old UI with no file picker and no Compare.
    - "10 free uses daily".
    - The personal bookmarks bar and taskbar are visible.
    - "Free" titles.
  - **Completeness:** no HMAC, SHA-3, CRC32 or BLAKE; no Base64 output; no multi-file or `.sha256` manifest verification; no drag-and-drop.
  - **Blog:** doesn't mention Compare and tells readers to pick an algorithm first. es is half-translated; 8 English locale pages; /ar 404.
- **P3 items:**
  - Compare rejects `sha256:` prefixes and `sha256sum` lines.
  - CRLF is silently hashed as LF.
  - The empty string can't be hashed.
  - There is no on-screen notice that the file wins over the text.
  - All five buttons are named "Copy".
  - iPhone SE 9 px overflow; ja desktop 3 px.
  - The mobile text box is about 42 px tall.
  - Thumbnail alt; axe items; JSON-LD Offer 4.99.

## Outcomes we want

1. The verdict always describes what is in the box. Results clear or are marked out of date when the input changes, and Compare never matches stale digests.
2. File hashing is fully keyboard and screen-reader accessible: a real button, plus drag-and-drop.
3. Santosh decides the trial-use policy. Code, blog, page and JSON-LD agree.
4. A current, clean video showing file + Compare, with "trial uses" wording.
5. A Premium step: HMAC, SHA-3 and manifest verification.
6. P3 polish: Compare accepts common checksum formats, a CRLF note, labelled Copy buttons, and the mobile layout.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PARTIAL | Every digest is correct (7 texts, 4 files up to 60 MB). The stale-result false Match breaks the core verify use (`json/stale-compare.json`). |
| 2 | Completeness vs competitors | PARTIAL | 5 algorithms, file + Compare. No HMAC, SHA-3, CRC32, manifest or multi-file (desk; not re-verified live). |
| 3 | Ease of use | PARTIAL | Simple. The file picker looks like plain text and isn't keyboard reachable; Compare appears only after a first Generate; no stale notice. |
| 4 | Layout attractiveness | PASS (minor) | Clean cards. iPhone SE 9 px overflow; small mobile text box. |
| 5 | Payment process | N/A (untested) | No cap dialog, pass or Stripe appeared. |
| 6 | Information correct | PARTIAL | Most copy is accurate. "Exactly what you typed" (CRLF), "paste exactly as copied" (prefixes) and the blog's trial and algorithm lines are off. |
| 7 | Indexing | PASS | 200; canonical self; in the sitemap. |
| 8 | SEO | PARTIAL | Strong title/meta/FAQPage (6)/VideoObject. English pages under 8 hreflangs; es mixed with no brand; /ar 404; thumbnail alt; Offer 4.99. |
| 9 | Blog exists and accurate | PARTIAL | `/blog/hash-generator` gives sound advice but omits Compare; the "algorithm choice" and trial-use lines are off. |
| 10 | YouTube video exists | PASS | 7vHVmGVIeWA, 88 s, 25 views, uploaded 2026-09-23. |
| 11 | FAQ and guide correct | PASS (minor) | 6 FAQs accurate; Tips overstate paste tolerance. |
| 12 | Video shows current capabilities | **FAIL** | Text-only old UI (no file, no Compare), "10 free uses daily", personal bookmarks visible. |
| 13 | Storage | PASS | Nothing stored; no URL state. |
| 14 | Sharing | PASS | Share copies only the tool URL (`json/share.json`). |
| 15 | Downloads | PASS | Copy per digest works (exact); print shows the digests. No export file (none promised). |
| 16 | Usage count | **Policy question** | At 0, everything works, 10 → 10. One unconfirmed uses-left context stayed at 0 after 2 Generates. Pending (RERUN row 32). |
| 17 | Categorization in section | PASS | Developer & Security Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home › Developer & Security Tools. |
| 19 | AI need/demand | PASS (demand steady) | Evergreen "sha256 / md5 checksum" queries; no AI needed. |
| 20 | Merge better? | No | Distinct from the password tools (C50). |
| 21 | Remove? | No | |
| 22 | Duplicates | None for this tool | C50's duplicate is password-strength vs password-generator. |

## Severity summary
- P0: 0. Privacy holds: no text, file content or digest in any request.
- P1: 3 (false Match from stale results; keyboard can't pick a file; trial-use policy question).
- P2: about 4.
- P3: several.
