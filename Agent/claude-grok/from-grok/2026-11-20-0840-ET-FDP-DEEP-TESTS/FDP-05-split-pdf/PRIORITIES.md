Sent: 2026-11-20 08:40 ET

# FDP-05 Split PDF: priorities

- **Written:** 2026-11-19 11:46:52 EST (box `date`, ET).
- **Ordering:** by user-trust and revenue outcome. Each item gives its REPORT.md check and its REPRODUCE.md ID.

## P0: ship first

1. **Make the trial meter honest for a new visitor (checks 15, 16; R-01).**
   - **Outcome:** a fresh device shows 10 remaining, and the page says what one download costs (per file or per ZIP).
   - **Why:** 21 of 22 readable fresh contexts loaded at "0 remaining today", so visitors split successfully and then can't download.
   - This is display-only evidence from one box IP, and the same pattern as FDP-02 to FDP-04. Verify server-side; one fix covers every tool.
   - The per-file vs per-ZIP cost needs a re-run after midnight UTC (`scripts/sp-battery.js`).

## P1: next

2. **Fix the copy that contradicts the tool (checks 6, 11; R-02).**
   - Limitations says passwords must be removed first, but the tool unlocks inline (the FAQ says so too).
   - Details claims "checkboxes on thumbnails" and hedges ("typically", "often as a zip"), but thumbnails are plain previews.
   - Rewrite both from the real UI. This text is what WebSearch shows.
3. **Blog (checks 9, 18; R-03).**
   - Link /blog/split-pdf-multi-contract-client-packets from the tool page (0 links today).
   - Fix its "name the output ClientA-….pdf" step. There is no name field, so remove the step or ship per-range names.
   - Change "trial usages if you are testing ranges" to "downloads".
4. **Locales (check 8; R-04).** All 9 locale URLs, /es included, serve the English title and meta with self canonicals, and their UI headings are half English. Localize the server head and the headings, or drop them from hreflang.

## P2: enhancements and polish

5. **Small screens and result rows (check 4; R-05).**
   - Fix the 329 px overflow at 320 px (the header menu button).
   - Get the drop zone above the fold on iPhone SE and Galaxy S9+.
   - Lead each row with the range; desktop names are truncated to about 100 px.
6. **A11y (R-06):**
   - Focus to the file card after Add and to the result summary after Split.
   - Ad-caption contrast.
   - The desktop label-content mismatch.
   - Remove the duplicate "Split PDF" / "Split into N files" button.
7. **Messages (R-07):**
   - A note for overlapping or duplicate ranges.
   - "This isn't a PDF" / "This file is empty" instead of "damaged, try Repair" for text, PNG and 0-byte files.
   - An owner-restriction notice on unlock.
   - Document the "8-" open-ended range and semicolons.
8. **Product:** split by bookmarks (named per chapter) and by max size (email-sized parts). These are the competitors' main extras and fit the blog's multi-contract story. Optional: odd/even, tap-to-select pages.
9. **Packaging:**
   - Title brand suffix and a richer H1.
   - JSON-LD Offer billing period.
   - Tool-specific OG image.
   - Video: "Professional Tool" instead of "free tool" in the outro, and "300+" instead of "200+".
   - The video description and blog should say "trial uses".
10. **Output verification after midnight UTC (R-08):** run `scripts/sp-battery.js` (SP-31…SP-41) and file any defects in a -v2 note.
