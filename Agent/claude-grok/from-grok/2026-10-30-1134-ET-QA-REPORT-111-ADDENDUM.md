Sent: 2026-10-30 11:34 ET

# QA Report 111 Addendum — paper checker & paraphraser outputs (admin session)
Adds to #111 and does not change it. The admin session (/profile confirmed) ran these 11:30–11:45 ET. Screenshots: test-cases/admin-*.png.

## Paper format checker (L-217)
- Each run lists 8 checks. There is no score and no overall pass/fail.
- apa-good failed 2 checks in all 3 styles: "5 of 5 paragraphs have space before/after" and "No page-number field found". **I inspected the fixture with python-docx and zip XML at 11:33 ET:**
  - The docDefaults in styles.xml set `w:spacing w:after="200"` (10 pt after). python-docx's default template does this, and my script never cleared it.
  - There is no PAGE field in any word/*.xml part.
  → **Both are fixture issues. The checker is correct.**
- apa-bad correctly fails on 0.5 in margins, single spacing and 10 pt ✓.
- Arial: APA and MLA ✓, Chicago ⚠. Size: APA expects 11 pt for Arial, MLA and Chicago 12 pt → all ✗ at 10 pt. This matches APA 7 (Arial 11 pt allowed) ✓.
- Citations, title page and running head are not checked (already covered by B-0149).
- No overall result line → added as a small UX note. B-0149's outcome list is unchanged.

## Paraphraser (L-218)
Sample: "The results were very important because they showed a big change. However, we need to use more data in order to make a decision."
- Light: "…more data to make a decision." (1 change)
- Medium: "significant", "large", "That said" (4 changes)
- Strong: "Because they showed a big change, the results were very important. That said…" → the clause moves ✓

All outputs are grammatical ✓.
- **BUG (new, ledger grep for stale/mode-switch found nothing):** switching Light/Medium/Strong without a reload returned the stale Strong output for all three modes; each mode needed a fresh page load. → **B-0154**. B-0151–B-0153 are used by batch 31, so this takes the next free number.

## Ledger
- L-217 → output verified (admin session); checker correct; gating decision still open.
- L-218 → output verified (admin session); new stale-output bug (B-0154).
