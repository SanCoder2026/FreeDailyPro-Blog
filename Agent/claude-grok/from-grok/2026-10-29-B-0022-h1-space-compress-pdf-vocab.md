# B-0022 Homepage H1 missing space; Compress PDF FAQ uses a mode name the UI no longer has
Priority: P2 (must-do)      Estimated effort: 20 min

## Goal / why
Search engines and screen readers read the homepage H1 as "Every Professional Task.One Browser Platform" (no space), which shows up badly in snippets. Compress PDF's FAQ and help text still say "Smallest", but the visible mode buttons are Balanced / Aggressive / Extreme / Target size, so the search snippet and FAQ rich result describe a mode users cannot find.

## What to change
- Homepage H1 (https://www.freedailypro.com/): live HTML is `Task.<br><span class="gradient-text">One`. Put a real space in the text (for example `Task. <br>`), not a CSS-only gap.
- https://www.freedailypro.com/tool/compress-pdf: live FAQ JSON-LD and visible FAQ/help text contain "Smallest" (e.g. "...Smallest and Target size?", "Smallest shrink the pictures inside..."). Change them to match the visible mode buttons. Check the meta description uses the same names.

## Acceptance criteria
- Text extraction of the homepage H1 reads "Every Professional Task. One Browser Platform".
- The compress-pdf page source contains no "Smallest" and the FAQ, FAQ JSON-LD, help text and meta description use only the visible mode names.
- Verification `live and checked`.

## Not in scope / do not decide
Hero design, other homepage copy, compression behaviour.

## Owner decisions needed
none

Source: SEO bot + Testing Bot (Oct 28 tech SEO flags); re-verified live by Grok 2026-10-29 ~5:15 PM ET.
