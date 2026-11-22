Sent: 2026-11-22 02:14 ET

# Remove PDF Pages: output analysis

## How removal works (code)
`_e(file, keepIdx)`: `U.load(src)`, `U.create()`, `Pt(src, dst, keepIdx)`:
- pdf-lib `dst.copyPages(src, keep)`. This deep-copies every object reachable from each kept page dict, including `/Annots` → Link `/Dest [pageRef …]` and Widget `/P` / `/Parent /Kids`.
- `Nt(_t(src), map)` keeps bookmarks whose target is a kept page. `xt` writes them as `[newPage /Fit]`.
- `ue(src, dst)` builds a new AcroForm with `Fields` (fields whose widgets sit on kept pages), `DA`, `NeedAppearances true`. /DR is not copied.
- `Q()` sets Title and Author only.
- pdf-lib then writes **every object in the context**, so pages that were copied only because a link or widget points at them end up in the file without being in /Pages.

## Results (verify93.py)
| Tag | Input → removed | Size in → out | Hidden /Page copies | Secrets anywhere vs on visible pages |
|---|---|---|---|---|
| A01r2 | book, p5 | 2,727,326 → 2,731,716 | p5, p10, p2 | 1–20 vs all but 5 → **p5 leaked** (text, photo, gone_ssn) |
| A05r2 | book, p20 | → 2,596,028 | p5, p10, p2 (link targets) | none leaked; links dead |
| A07r2 | book, 5-7 + 20 | → 2,322,588 | p5, p10, p2 | **p5 leaked**; p6, p7, p20 gone |
| L01 | toc-links, p7 | 8,316 → 12,617 | all 11 linked pages | **p7 "PII-PAGE-7 … SSN 078-05-1120" recovered** |
| S01 | split-field, p3 | 2,811 → 3,408 | p1, p3 | **p3 + p3_secret=P3-FIELD-SECRET recovered** |
| E03 | 300p, 2-299 | 2,866,511 → 19,172 | none | none |
| R01 | rotated-inherit, p1 | 2,813 → 5,285 | none | rotation 90 (inherited) / 180 / 0 and MediaBox kept |
| F01 | form.pdf, p1 | 18,977 → 4,903 | none | p2field, rotfield kept with values; /DR dropped |

Recovered pages are in `files/recovered-*.pdf` and renders in `screens/recovered-*`.

## Links
In every book/toc output, internal links resolve to `NOT-A-PAGE-IN-THIS-FILE` (PDFium −1; MuPDF jumps to page 1), including links to kept pages.

## Outline (A01r2)
`Cover p1 → 1, Part A p2 → 2, A.1 p3 → 3, Part B p5 → 5 (re-pointed to B.1), B.1 p6 → 5, B.2 p7 → 6, Middle p10 → 9, Last p20 → 19, Action GoTo p3 → 3`. "Named dest p10" is missing although p10 is kept.

## Catalog / info
Lost: /Names (Dests, EmbeddedFiles), /PageLabels, /Lang, /PageMode, Subject, Keywords. Creator and Producer are FreeDailyPro.

## Blank finder
- blanks.pdf ticks 2, 4, 5, 6 (4 = only "- 4 -"; 5 = faint show-through).
- blanks2.pdf ticks 2 ("7" alone, labelled "Blank (no ink)") and 5. "Page 8" (0.02 %) and a stamp (0.3 %) were kept.
- book.pdf: "No page looks blank". Slider at 0 → 2, 5, 6 on blanks.pdf.
