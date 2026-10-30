Sent: 2026-10-30 08:45 ET

# B-0099 — Book Writing Toolbox: embedded fonts for left-to-right scripts (RTL stays out)

**Priority:** P2 (capability) · **Tool:** Book Writing Toolbox · **Related:** B-0112 (DOCX import flattens tables, drops images)

## How to work with us
You know this codebase and its deploy history better than any checklist. Read the real export pipeline (PDF, EPUB, DOCX) first, restate the problem in your own words, challenge anything below that's weak, and pick the implementation that fits how we've shipped before. The direction below is a suggestion, not orders.

## Intent
Authors writing in any **left-to-right** script should be able to write, preview and export a book that looks right: no tofu boxes, no missing glyphs, and good-looking typography. That puts us level with Atticus and Vellum on fonts, without opening up right-to-left layout.

## Why
- **Owner decision (Santosh):** we deliberately limited the toolbox to left-to-right scripts because right-to-left layout caused real problems. That limit stays. He's happy for us to add fonts so LTR scripts render properly.
- QA (Testing Bot, report #94 / B-0112 import test): accented Latin, Chinese and Arabic text survived import into the editor. But nothing confirms that exported files embed fonts covering CJK, Indic, Thai, Cyrillic or Greek. Without embedded fonts, readers and e-readers fall back to boxes.
- Right now Arabic and Hebrew input is accepted with no signal, so users get a quietly broken layout. Saying so honestly beats a silent failure (free-first, honest brand).
- Competitors (Atticus, Vellum) offer a curated font set with live preview. We don't.

## Outcomes (what "done" looks like)
1. **Embedded LTR coverage:** PDF and EPUB exports embed **subset** Noto Sans and Noto Serif fonts covering CJK (Chinese, Japanese, Korean), Devanagari and other Indic scripts (e.g. Bengali, Tamil, Telugu, Gujarati, Kannada, Malayalam), Thai, Cyrillic and Greek. Indic and Thai shaping (conjuncts, vowel marks) must render correctly. DOCX names the right fonts so Word picks them up.
2. **Small files:** fonts are subset to the glyphs actually used. A Latin-only book should not grow noticeably, and a mixed-script book should stay a reasonable size. Report before/after sizes.
3. **RTL detection:** when the text contains Arabic or Hebrew characters, a clear inline note appears: **"Right-to-left books aren't supported yet."** It should not block writing, and there's no RTL layout work.
4. **Font picker:** 6–8 curated book fonts (serif, sans, display) with a live preview in the editor and preview pane, carried through to every export format, at parity with Atticus and Vellum. All must have licenses that allow embedding (OFL or similar).
5. **Watermark unchanged:** the preview watermark is intentional. It stops people screenshotting their way past the paid download. Don't touch it, and keep paid downloads clean.

## Acceptance tests
- Sample chapters in each script (Latin with accents, Chinese, Japanese, Korean, Hindi/Devanagari, plus at least one other Indic script, Thai, Russian/Cyrillic, Greek) export to **PDF, EPUB and DOCX** with every glyph intact, with no tofu and correct shaping. Check PDF font embedding (e.g. `pdffonts`) and validate EPUB (epubcheck).
- A chapter containing Arabic or Hebrew shows the RTL inline note.
- Each picker font previews live and appears in all three exports.
- The preview watermark still shows. Download credit and metering behavior is unchanged.

## Constraints
- No RTL layout, bidi or mirroring work.
- Don't change the watermark or download-credit metering.
- Keep editor load time reasonable: lazy-load script fonts only when needed.
- Coordinate with **B-0112** (DOCX import keeping tables and images), since both touch the import/export pipeline.

## Process
Inspect → restate → propose (including font sourcing and the subsetting approach) → implement → verify with the acceptance tests above → report sizes and screenshots.

Source: owner
