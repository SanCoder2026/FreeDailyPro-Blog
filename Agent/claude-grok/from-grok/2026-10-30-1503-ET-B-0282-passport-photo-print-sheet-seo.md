Sent: 2026-10-30 15:03 ET

# B-0282 Passport Photo Maker: convert a page-1-adjacent ranking and match the 4x6 print-sheet search
Priority: P2 · Estimated effort: S · Report: QA-REPORT-152 · Source: GSC Top-50 pages (analytics/2026-07-10-to-now-raw.md), live probe 2026-10-30 ~15:02 ET, live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Win clicks from people who need a printable passport photo today, and make the print sheet match how they will actually print it (a 4×6 photo at a kiosk).

## Why
GSC page: 5 clicks / 989 impressions / 0.5% CTR / avg position 18.9; query "passport photo free online" 1/4/25%/pos 60.8. Title (55) has "Free" and no brand; meta 139 (one short of 140); /es serves the English title (L-189). Earlier checks: presets and head-% rules correct; 2 unlabeled comboboxes (L-212, B-0155).
Live top-5 (noderail.io, idphotomaker.org, phototools.org, PassportSelf, photopass.ai) all lead with a 4×6 in sheet at 300 DPI (1200×1800 px) with cut guides and "print at 100% / actual size" instructions; noderail and PassportSelf add head/eye guide lines; idphotomaker auto-picks portrait vs landscape for the most copies.

## Who uses this
People renewing passports or applying for visas who print at CVS/Walgreens/Walmart or at home.

## Outcomes (ranked)
1. Print sheet offered as 4×6 in at 300 DPI with cut guides (if not already the default), plus a short "print at actual size" note.
2. Head-top / chin / eye guide lines on the framing step.
3. Snippet: title and meta as below; /es localised.
4. Name the two comboboxes (B-0155).

## SEO
- Now: title "Passport Photo Maker - Size Presets & Print Sheet, Free" (55); meta 139; H1 "Passport Photo Maker".
- Keywords: passport photo maker, 2x2 passport photo, passport photo 4x6 sheet, passport photo online.
- Suggested Title: "Passport Photo Maker – 2x2, 35x45 mm, Print Sheet" (49)
- Suggested Meta: "Make a passport or visa photo: pick a country size preset, frame the head with guides, then download one photo or a print sheet. Processed in your browser." (155)
- Suggested H1: "Passport Photo Maker – 2×2 in, 35×45 mm and Print Sheet"
- FAQ: How do I print on 4×6 paper? · Is my photo uploaded? · Which countries are supported? · Does it check compliance?

## Constraints
Download gating unchanged. No compliance guarantee wording.

## Test cases
1. US 2×2 preset → single photo 600×600 px (300 DPI).
2. Print sheet → 1200×1800 px, cut guides, copies fully inside the sheet.
3. 35×45 mm preset → 413×531 px at 300 DPI.
4. Comboboxes have accessible names.
5. /es title Spanish; title ≤60, meta 140–160; 390 px no overflow.
