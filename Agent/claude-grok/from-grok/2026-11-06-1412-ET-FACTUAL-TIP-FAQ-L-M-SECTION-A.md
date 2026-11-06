Sent: 2026-11-06 2:15 PM ET (America/New_York) — Growth Orchestrator daytime sweep #2
Source: bot findings (Programmatic SEO hourly L + M Section A). Not an owner instruction.

# Factual tip / How / FAQ alignment — SEO L + M Section A only

## How to work with us
Inspect the real tip/How/FAQ strings and the cited live JS behaviors in the FreeDailyPro site repo first. Restate each gap. Prefer the smallest copy change that matches shipped UI. Never invent capabilities. Challenge any claim that goes beyond the evidence below.

## Intent
Make tip / How / FAQ text tell the truth about what these Professional Tools already do, so users are not misled by garbled or contradictory help copy — without SEO rewrites, pricing changes, ad removal, or new features.

## Why (evidence)

### SEO L Section A (factual)

1. **/tool/email-extractor — broken tip (live JS).** Tip ends mid-thought: `…bracketed forms such as name [at] domain [dot] com are found only when the "Also find" option is on, and any other as a real address.` Garbled/unfinished. FAQ Q3 + live "Also find name [at] domain [dot] com" toggle: bracketed forms only when on; plain "at"/"dot" words still ignored. **Fix tip** to that story.
2. **/tool/audio-to-subtitles — How/FAQ omit live plain-text export.** Live UI downloads SRT, VTT, **and** plain `.txt` (`J("txt")`); About `what` mentions plain text; How + FAQ only say SRT/VTT. **Align How and/or FAQ** with all three downloads.

Both tools: VERIFIED Professional (`co=10`) per L evidence. Tier/prices unchanged in this brief.

### SEO M Section A (factual)

1. **/tool/extract-pdf — FAQ Q5 vs How + live order.** FAQ: extracted pages "always come out in their original document order, regardless of the order you clicked or typed." How: typed lists like `5,1,3` keep **typed order**; thumbnail clicks sync the field as sorted. Live: `parseMultiRange` concatenates in typed order; thumbnail toggles rewrite with `.sort`. **Fix FAQ Q5** (and status hint if needed): typed order preserved; click-selection effectively document order because the field is sorted.
2. **/tool/pdf-watermark — FAQ Q10 vs Q11 on logo formats.** Q10: PNG/JPEG only (convert WebP/SVG first). Q11: PNG/JPEG direct; WebP/GIF/BMP/SVG → PNG; TIFF refused. Live: `normalizeImageFile` **throws on TIFF**; WebP convertible. **One logo-format FAQ** matching Q11 + live.
3. **/tool/pdf-watermark — FAQ Q2 (+ About tip) vs FAQ Q12 on Hindi/script.** Q2/tip: Chinese/Arabic/**Hindi** as picture. Q12: Hindi/Marathi/Nepali as real text with site font; Chinese/Arabic as picture. **One accurate story** aligned with live `drawTextAnywhere` / pdfFonts (glyph coverage not exhaustively re-proven beyond code-path review in M evidence).

All three tools: VERIFIED Professional (`co=10`) per M evidence.

Evidence sources (local): `freedailypro-seo-engine/hourly/2026-11-06-1200-four-page-upgrades-l.md` §A; `freedailypro-seo-engine/hourly/2026-11-06-1300-four-page-upgrades-m.md` §A; reviewed batch `freedailypro-growth-orchestrator/pending-briefs/2026-11-06-reviewed-factual-batch.md`.

## Outcomes
1. email-extractor tip matches FAQ Q3 + Also-find toggle (no garbled ending).
2. audio-to-subtitles How and/or FAQ name SRT, VTT, and plain text.
3. extract-pdf FAQ Q5 matches typed-order + sorted click-selection.
4. pdf-watermark has one logo-format answer (Q11 + live) and one Hindi/script story (Q12 + live draw path).
5. No title/meta/H1/brand/length edits; no schema `price: "0"`; ads retained; Professional 10 trial uses / $1 / $4.99 unchanged; no Premium retier; no AI; no QA-414 metering policy work; no uploads/publication; no Passport video overlay work.

## Freedom
Inspect real copy sources and the cited JS helpers. Choose the existing FAQ/tip pattern used on sibling tools. If live strings already match after a deploy you discover, say so and stop.

## Constraints
- Do **not** implement SEO L/M **Section B** title/meta/H1/brand/length rewrites (owner-gated).
- Do **not** edit JSON-LD / schema price `"0"` (Conversion / owner track).
- Do **not** remove ads; do not change pricing, tiers, Premium, or Workflows.
- Do **not** add AI features.
- Do **not** touch QA-414 metering / Copy-spend policy (separate hold for owner).
- Do **not** publish YouTube / video metadata overlays. Passport stale "free uses" in **video** recording is **held** — live Passport DOM already shows Trial 10; do **not** treat as a live site-banner bug from run25 alone.
- Never say "free tools"; leave Professional Tools / trial wording correct.
- Prefer smallest copy-only fixes.

## Process
Inspect → restate each included gap → minimal tip/How/FAQ copy → implement → verify live tip/How/FAQ after deploy.
