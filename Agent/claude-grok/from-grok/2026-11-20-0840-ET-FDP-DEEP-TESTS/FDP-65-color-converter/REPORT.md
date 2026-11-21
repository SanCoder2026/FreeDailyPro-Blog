Sent: 2026-11-21 14:26 ET

# FDP-65 HEX / RGB / HSL Converter (color-converter): deep test report for Claude

- **Written:** 2026-11-21 14:24 EST (box `date`, ET). Testing ran 2026-11-21 14:09–14:23 EST.
- **Tool:** https://www.freedailypro.com/tool/color-converter
  - TEST-ORDER row 65: **Professional Tool**, Design & Marketing. Plan note "test-plan (unranked): SEO backfill 10". Duplicate group C21 (CSS/colour generators).
  - **No trial strip, no Quick Buy and no prices on the page** (all 6 geo contexts, desktop and phones).
  - Video Kuyt4omoYSg (embedded, 63 s, uploaded 2026-09-23). Blog /blog/color-converter "Convert a Brand Teal From HEX to RGB, HSL and CMYK" (200).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `ColorConverter-Fmg0nTvn.js`, `colorUtils`, `useLogToolUsage`):**
  - One input (HEX 3/4/6/8, rgb/rgba, hsl/hsla, hwb, oklch(), bare triples, CSS names) plus a native colour picker. Ten read-only rows with Copy: HEX, RGB, HSL, HSV/HSB, HWB, CMYK (screen estimate), LAB (D50), OKLCH, Nearest CSS name, CSS line. A swatch and contrast on white/black.
  - Invalid text keeps the last good colour with a red message; out-of-range values are clamped with an amber note.
  - Usage: the page wires `useLogToolUsage` (copy wrapped through `tryUse`), but the gate only runs when the tool is "known" to the usage system. Live, it never runs (below).
- **Testers:**
  - Desk: page copy (6 FAQs, how-to, limits, privacy), JSON-LD, blog, JS.
  - Playwright. The clipboard was read from a same-origin helper tab (robots.txt) so the tool's own clipboard wrapper was not touched.
    - `zero.json`: a context at 10/10. `left.json`: a context with 10 uses left. `alpha.json`: alpha round trips and Firefox at the cap.
    - `cases.json`: 23 inputs (formats, alpha, clamping, names, oklch/lab/display-p3, invalid). LAB values checked against an independent D50 calculation.
  - Video frame sheet; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested):** none. There is no Drive, cloud or account feature on this page (verified), and no paid path is offered on the page.
- **RERUN-AFTER-RESET:** none.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for a designer or developer who needs a colour in another format, and whether the page is set up to turn that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Unit Converter, Grammar Checker and Word Counter are uncounted on purpose; any other tool that takes no trial use is an owner question (Nov 20). Per-page-load charging is P1; a full-quality result at 0 is a pending owner question; a real save at 0 is P1 (Nov 21, corrected 1:19 PM).

**P0 / P1:** none found.

**Owner question:**
- **This tool takes no trial use at all.**
  - At 10/10 (zero.json, Chromium; alpha.json, Firefox) every Copy button copies (toast "Copied", clipboard verified), Ctrl+C from the read-only rows copies, and nothing opens a cap dialog. No `usage.log` POST is sent.
  - With uses left (left.json): typing, 5 s idle, Copy ×3, a new colour + copy, Ctrl+C, reload + copy: **0 POSTs, counter stays 0/10.**
  - The page shows no trial strip and no Quick Buy. Yet the blog says "each valid colour you convert can count towards your daily trial uses", JSON-LD carries an Offer of $4.99, and the code calls `useLogToolUsage` with a clipboard gate (it never activates because the tool isn't "known" to the usage system).
  - It isn't on the uncounted-on-purpose list (Unit Converter, Grammar Checker, Word Counter). Decide: count it (then the blog/code are right) or list it as uncounted (then fix the blog line).
  - If it becomes counted: the code's Ctrl+C guard uses `window.getSelection()`, which is empty for text selected inside an `<input>`, so Ctrl+C from the read-only rows would slip past it. Worth fixing at the same time.

**P2 — where to look:**
- **8-digit / 4-digit HEX alpha is changed on output** (alpha.json). Alpha is rounded to 2 decimals and back:
  - `#ff6600aa` and `#F60A` → `#ff6600ab`.
  - `#ff660001` → `#ff660000` (now fully transparent).
  - `#ff6600fe` → `#ff6600`, alpha dropped (now opaque).
  - `#ff660080`, `#ff66001a`, `#ff6600cc`, `#12345678` survive. The FAQ promises "the HEX row includes the extra pair of digits". Keep the input's alpha byte for the HEX row.
- **Page copy lags the tool:**
  - Limitations: "formats like lab(), oklch or display-p3 are rejected as unreadable", but oklch() is accepted (with a gamut note) and the error message itself suggests `oklch(70% 0.2 50)`. lab() and display-p3 are rejected, as stated.
  - How-to row list omits LAB and OKLCH, and doesn't mention the contrast lines.
  - "When not to use it" sends legibility checks to the Contrast Checker, while the page now shows contrast on white/black.
- **Video Kuyt4omoYSg:** older UI with four rows (no HSV, HWB, CMYK, LAB, OKLCH or contrast), title "Free Step-by-Step Walkthrough", description "Try … free", "Free daily uses", tags "free online tools", "PDF tools", end card "200+ Free Productivity Tools".
- **Locale pages:** chrome and breadcrumb translated; H1, subtitle, input label and all row labels stay English (es screenshot; H1 English in all 9 locales).
- **SEO:** meta description 69 chars ("Convert between color formats instantly. Fast, right in your browser."). The page's strengths (OKLCH, LAB, CMYK, 8-digit alpha, nearest name, contrast) aren't in the meta or title. Generic OG image.

**P3:**
- oklch input out of sRGB is clipped and the OKLCH row shows the clipped value (hue 50 → 46.8). Correct, but say "(clipped)" on that row so users don't paste back a different colour.
- The native colour picker drops alpha (`#ff660080` → picker `#ff6600`); expected for `<input type=color>`, worth a note.
- Phones: the swatch and contrast sit below all ten rows (Pixel 7 screenshot).
- iPhone SE 9 px overflow from the header menu button; axe desktop label-content-name-mismatch (serious), region (moderate); Pixel 7 color-contrast ×2 on the ad caption (keep reserved ad slots; fix the caption colour); ja desktop 1369 px (site-wide).

## Intent

A designer or developer has a colour in one notation and needs it in another (often several), quickly and exactly, ideally with a sense of legibility. The tool is excellent at this; the open question is whether it should be a counted Professional Tool at all.

## What works (verified)

- **Parsing:** #f60, f60, #ff6600, rgb/rgba (comma and space), hsl/hsla incl. `/ 50%`, hwb, bare `255 102 0` and `255,102,0`, CSS names (tomato, rebeccapurple, transparent), oklch().
- **Accuracy:** #ff6600 → rgb(255, 102, 0), hsl(24, 100%, 50%), hsv(24, 100%, 100%), hwb(24 0% 0%), cmyk(0%, 60%, 100%, 0%), lab(63.2% 57.1 72.6), oklch(69.6% 0.204 43.5). LAB for 4 colours matches an independent D50 calculation exactly.
- **Errors:** `#12345`, `notacolor`, lab(), display-p3 → red message with examples, last valid colour kept. `rgb(300, 0, 0)` → "Clamped red 300→255."
- **Contrast:** black 21.00:1 AAA; #808080 3.95:1 on white "AA large text only".
- **Layout:** tool at the top on desktop and phones; Firefox/WebKit/iPad fine. Consent banner in de-DE (screenshot) doesn't cover the input.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 10 formats, alpha, names, contrast. |
| 2 | Completeness | PASS | Beyond typical HEX/RGB converters (OKLCH, LAB, HWB). |
| 3 | Ease of use | PASS | Live conversion, clear errors, per-row Copy. |
| 4 | Layout | PASS (minor) | Swatch far down on phones; SE overflow. |
| 5 | Payment process | N/A | No trial strip / Quick Buy on this page (owner question). |
| 6 | Information correct | PARTIAL | oklch "rejected" claim; blog "counts towards trial uses". |
| 7 | Indexing | PASS | 200, canonical self, 10 hreflang + x-default. |
| 8 | SEO | PARTIAL | Meta 69 chars, generic OG. |
| 9 | Blog | PARTIAL | Accurate on formats/alpha; trial-use line contradicts live. |
| 10 | YouTube video | PASS | Kuyt4omoYSg embedded + VideoObject. |
| 11 | FAQ / guide correct | PARTIAL | 8-digit HEX promise broken for some alphas. |
| 12 | Video shows current capability | FAIL | Old 4-row UI; "free" wording. |
| 13 | Storage | N/A | None (verified). |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | N/A | Clipboard only; copies verified. |
| 16 | Usage count | Owner question | Takes no trial use (0 POSTs; copy works at 10/10). |
| 17 | Categorization in section | PASS | Design & Marketing / Professional. |
| 18 | Correct section of site | PASS | Part of "Building a basic CSS design system"; next Gradient Generator; Brand Studio CTA (200). |
| 19 | AI need and demand | PASS | High ("hex to rgb", "rgb to hex", "hex to hsl"). |
| 20 | Merge better? | No | Picker-from-image and palette generator are different jobs; cross-link. |
| 21 | Remove? | No | High-demand utility. |
| 22 | Duplicates | None | C21 members generate CSS/colours. |

## After fixes, rerun

- `px65-alpha.js` (8-digit HEX unchanged: aa, 01, fe).
- `px65-live.js zero` / `left` once the owner decides on counting.
