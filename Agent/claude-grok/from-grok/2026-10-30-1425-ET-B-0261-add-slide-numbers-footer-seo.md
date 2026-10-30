Sent: 2026-10-30 14:25 ET

# B-0261 Add Slide Numbers: preview works before the gate; add footer text, "N of total" check and skip-slide choice; brand the title
Priority: P3 · Estimated effort: S · Report: #145 · Source: Playwright headless, logged out, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:23–14:25 ET. L-243: next 3 untested tools alphabetically (sitemap minus ledger/test plan). No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A presenter should number a deck in the right corner and style, see it on the slide, and download a file PowerPoint keeps up to date.
## Why (repro: t.pptx, 3 slides; 1280 px; 0 trial uses)
- **Works before the gate:** "29.2 KB · 3 slides", Add/Remove, corner (4), style (3 · Slide 3 · 3 / 12), start number, size 10–24 pt, colour, "Leave the first slide without a number", Before/After preview, "Numbers added to 3 slides (1 to 3)". Only "Download the new file" is gated ("Your result is ready… this download needs a pass") — owner's decision.
- Uses a real slide-number field (stays right after reordering). Microsoft says PowerPoint cannot compute "2 of 12" itself, so "3 / 12" must be static text: admin to confirm what happens when slides are added later.
- **Missing vs competitors (~14:24 ET):** footer text and date with the number (PowerPoint web Footer pane); number only selected slides (PowerPoint web "Apply to Selected Slides"); top-left/top-centre and font choice (SlideSpeak). SlideSpeak's tool is waitlist-only, so a working browser tool is a real opening.
- Accepts .pptx,.ppt,.odp: admin to confirm .ppt/.odp work. Unnamed controls → B-0155. No overflow at 390 px. "Compare Browsers" ad text glued to copy → L-004.
## Who uses this
Students, teachers and staff finishing a deck for print or handouts.
## Outcomes (ranked)
1. Footer text (and optional date) alongside the number.
2. Choose which slides get a number.
3. State on the page that "3 / 12" is fixed text.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD, all images have alt. /es English → **B-0123**. Site-wide → **B-0209**.
  - Title "Add Slide Numbers to PowerPoint Online - Any Corner, Free" (57): ends on "Free", no brand. Meta 156 ✔. H1 "Add Slide Numbers to PowerPoint".
- **Keywords:** "add slide numbers powerpoint", "slide number x of y", "number slides online", "powerpoint page numbers".
- **Suggested:**
  - Title: `Add Slide Numbers to PowerPoint – Any Corner | FreeDailyPro` (59)
  - Meta: keep current (156).
  - H1: `Add Slide Numbers to a PowerPoint`
  - FAQ: "Can I show 3 of 12?" · "Can I skip the title slide?" → "Yes." · "Is my file uploaded?" → "No."
## Constraints
Keep the download gated per the owner's decision.
## Test cases
1. Admin: download → ppt/slides/slide2.xml has a `<a:fld type="slidenum">` field.
2. Style "3 / 12" then add a slide in PowerPoint → note the shown total.
3. Title ≤ 60, no "Free".
