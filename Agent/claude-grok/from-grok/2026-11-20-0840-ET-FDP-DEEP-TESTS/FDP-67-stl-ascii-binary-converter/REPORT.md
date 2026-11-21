Sent: 2026-11-21 14:59 ET

# FDP-67 STL ASCII / Binary Converter (stl-ascii-binary-converter): deep test report for Claude

- **Written:** 2026-11-21 14:56 EST (box `date`, ET). Testing ran 2026-11-21 14:41–14:56 EST.
- **Tool:** https://www.freedailypro.com/tool/stl-ascii-binary-converter
  - TEST-ORDER row 67: **Professional Tool**, 3D & CAD Files. Plan note "test-plan (unranked): SEO backfill 11". Duplicate group **C46** (3D files: mesh-3d-converter, mesh-3d-viewer).
  - Trial strip "Trial: 10 uses/day", Quick Buy Day Pass $1 / Monthly $4.99 (all 6 geo contexts, desktop and phones).
  - Video oF-8Cve25zc (embedded, 61 s, uploaded 2026-09-23). Blogs: /blog/stl-ascii-binary-converter "Shrink an 11 MB ASCII STL to a 2.4 MB Binary File" (200), /blog/mesh-3d-viewer (200).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `StlAsciiBinaryConverter-qqsQjr6Z.js`, `mesh3d`):**
  - Drop one or more .stl files. Each is validated (format auto-detected; binary checked by size = 84 + 50 × count). The button for the format you already have is disabled with a hint.
  - Convert to ASCII STL / Convert to Binary STL builds the file in the browser and shows a card (Vertices, Triangles, size). One file → .stl, several → one ZIP.
  - Gate: the drop zone uses `gateAtDownload`. **Download** (and Save to Google Drive) charge one trial use through the shared download gate; Convert itself is free.
  - Also on the page: Open from Google Drive, Save to Google Drive, Save to my cloud storage (sign-in).
- **Testers:**
  - Desk: page copy, JSON-LD, both blogs, JS; peeked mesh-3d-converter's copy for the C46 overlap.
  - Playwright, guest contexts, 12 test STLs generated in testfiles/ (ASCII, binary, CRLF, upper-case .STL, two solids, binary with a "solid…" header, binary with colour bytes, a 14,160-triangle sphere both ways, truncated, empty, non-STL).
    - `zero.json` (at 10/10), `left.json`, `batch.json`, `perload.json` + `perload-2.json` (several files in one page load), `cases.json` (validation at the cap), `extra-cap.json` (Drive/cloud at the cap), `quickbuy.json`.
    - Every downloaded output was parsed and compared with its source in Python (triangle count, vertices, normals).
  - Video frame sheet; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered (Quick Buy stopped at the email box and at Stripe). No ad clicks. No site or repo changes. Downloaded files were parsed, never executed.
- **Sign-in (untested):** Open from Google Drive / Save to Google Drive (Google sign-in popup, closed), Save to my cloud storage (dialog "Sign in with your email first", $4.99/month add-on), paid-pass output. Rows added to SIGNIN-NEEDED.md.
- **RERUN-AFTER-RESET:** none.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for someone who needs an STL in the other encoding for a slicer, a size cap or a diff, and whether the page is set up to turn that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Per-page-load charging is P1; a full-quality result at 0 is a pending owner question; a real save or download at 0 is P1 (Nov 21, corrected 1:19 PM).

**P0:** none.

**P1:**
- **Charging is once per page load, and further downloads in the same page load are free, even at 0 uses.**
  - perload-2.json (start 0/10): download cube → **1/10**, one `usage.log` POST. Then, without reloading, Change file → sphere-binary → ASCII → Download (3,063,199 bytes) and Change file → colour cube → ASCII → Download: **no POST, counter stays 1/10**, both files saved.
  - perload.json: the first download's POST returned the device's server count, which was already **10/10**. The next two different files then still downloaded at 10/10, with no cap dialog and no POST (P02/P03 files in outputs/, byte-identical to the counted runs: md5 f1184e6b35f1, 43fa4a243a52).
  - A fresh page at the cap is gated correctly (zero.json: Download and Save to Google Drive open the cap dialog). So a user who keeps one tab open can convert any number of files after one charge. Same pattern as #64: charge per new result (per conversion output), not per page load.

**Owner question:**
- A multi-file ZIP (3 files, B03) costs one trial use, same as one file. That's likely intended; confirm. (Batch limits weren't tested beyond 4 files.)

**P2 — where to look:**
- **Thin page copy:** one FAQ ("ASCII or binary?") in the page and FAQPage JSON-LD. The useful facts (header and colour bytes dropped, normals recalculated, binary-with-"solid"-header handled, several files → ZIP, the trial use is taken at Download) are in the blog and the collapsed tip, not in FAQs. Add 4–5 FAQs from the blog.
- **Video oF-8Cve25zc:** older UI ("What is this tool?" layout, no trial strip, no Drive/cloud buttons), title "Free Step-by-Step Walkthrough", description "Try … free" and "Free daily uses … no account needed", tags "free online tools" and "PDF tools", end card "200+ Free Productivity Tools".
- **Cap dialog copy:** "Either pass removes the 'Created with FreeDailyPro.com' mark from your PDFs and images": not relevant to STL files.
- **C46 overlap:** 3D Mesh Converter already writes STL binary and STL ASCII from STL (its own copy says so). This page is a clean, lossless single-purpose landing page with batch ZIP; keep it for search, but say on both pages which to use (or make this a preset of the mesh converter).
- **Locale pages:** chrome, breadcrumb, badges, trial strip and Quick Buy translated (fr screenshot); title, meta, H1, subtitle, drop-zone text and FAQ stay English in all 9 locales.
- **SEO:** title "Convert STL ASCII to Binary Online | FreeDailyPro" (only one direction); meta 79 chars, no mention of batch ZIP, size savings or slicers. Generic OG image.

**P3:**
- Phones: drop zone reads "Tap to choose an STL file / or tap to choose" (repeated). Pixel 7 axe color-contrast on `.text-muted-foreground/50`.
- Blog step 1 says "Drop one .stl file", but several files work (ZIP).
- Output header is always "Binary STL by FreeDailyPro"; ZIP entries carry UTC times (19:50 for 14:50 ET).
- iPhone SE 9 px overflow (header action button); ja desktop 1369 px; axe desktop label-content-name-mismatch (serious), region (moderate).
- de-DE/fr-FR consent banner (screenshot) sits below the tool and partly covers the Feedback button.

## Intent

Someone has an STL in the wrong encoding: too big to send, refused by a tool, or needs reading as text. They want the other encoding, exact geometry, fast and private. The tool does that perfectly; the gate leaks after the first download in a page load.

## What works (verified)

- **Accuracy:** ASCII cube → binary: 12 triangles, vertices and normals identical. Colour cube (binary, attr bytes) → ASCII identical geometry (colour dropped, as documented). 14,160-triangle sphere ASCII → binary (708,084 bytes = 84 + 50 × 14,160) and binary → ASCII: **vertices match the float32 source exactly**. Binary file whose header begins "solid" is detected as binary and converts correctly.
- **Validation:** empty ("the file is empty"), non-STL ("no facets found …"), truncated binary ("header lists 50 triangles, the file holds 12"): red message, both Convert buttons disabled, "Choose a different file". CRLF, upper-case .STL and two solids in one file parse.
- **Batch:** 4 files (1 invalid) → "4 files (3 valid)", ZIP of 3 with the invalid one listed as left out; files already in the target format included unchanged; same base names from .stl/.STL kept apart.
- **Gate at a fresh page:** at 10/10 Convert still shows the stats card (no file); Download, Save to Google Drive and reload + Download open the cap dialog. Quick Buy: Day Pass → email dialog (stopped), Monthly → Stripe (stopped).
- **Layout:** drop zone above the fold on all devices; Firefox/WebKit/iPad fine.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | Both directions, batch ZIP, exact geometry. |
| 2 | Completeness | PASS | Validation messages are best in class. |
| 3 | Ease of use | PASS | Auto-detect, disabled same-format button with hint. |
| 4 | Layout | PASS (minor) | SE overflow; phone drop-zone wording. |
| 5 | Payment process | PASS | Strip + Quick Buy; email/Stripe reached (stopped). |
| 6 | Information correct | PARTIAL | Cap dialog mentions PDFs/images; blog "drop one file". |
| 7 | Indexing | PASS | 200, canonical self, 10 hreflang + x-default. |
| 8 | SEO | PARTIAL | One-direction title, meta 79 chars, generic OG. |
| 9 | Blog | PASS | Accurate and detailed (header, colour, "solid" trap, counting at download). |
| 10 | YouTube video | PASS | oF-8Cve25zc embedded + VideoObject. |
| 11 | FAQ / guide correct | PARTIAL | Correct but only one FAQ. |
| 12 | Video shows current capability | FAIL | Old UI; "free" wording; "PDF tools" tag. |
| 13 | Storage | Untested (sign-in) | Save to my cloud storage needs sign-in. |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | PASS | .stl and .zip correct; names keep the base + target. |
| 16 | Usage count | **FAIL (P1)** | One charge per page load; later downloads free, even at 10/10. |
| 17 | Categorization in section | PASS | 3D & CAD Files / Professional. |
| 18 | Correct section of site | PASS | Links to Mesh Converter / Viewer (200). |
| 19 | AI need and demand | PASS (niche) | "stl ascii to binary", "convert stl to binary". |
| 20 | Merge better? | Partial | Mesh Converter covers it; keep as landing or preset. |
| 21 | Remove? | No | Lossless, clear, niche demand. |
| 22 | Duplicates | C46 | Overlaps mesh-3d-converter (STL binary/ASCII output). |

## After fixes, rerun

- `px67-live.js perload` (each new file's Download should charge; at 10/10 the second file must hit the cap dialog).
- `px67-live.js zero` and `left` as a regression check.
