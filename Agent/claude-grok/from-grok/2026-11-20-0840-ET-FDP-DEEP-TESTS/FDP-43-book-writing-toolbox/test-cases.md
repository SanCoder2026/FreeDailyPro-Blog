Sent: 2026-11-21 05:21 ET

# FDP-43 Book Writing Toolbox: test cases (rerun after fixes)

Guest, fresh profile; test files in `evidence/testfiles`. "Now" is what we saw on 2026-11-21.

| ID | Case | Expected | Now |
|---|---|---|---|
| BW-01 | Chapter + Preview | Typeset PDF, watermarked, no trial use | PASS |
| BW-02 | Preview watermark strength | The mark is drawn over the content on every page; removing one object doesn't give a clean file | Owner question (intentional watermark) |
| BW-03 | Manuscript .docx preview watermark | The mark is in the body (or a sample) | Owner question (header only) |
| BW-04 | Preview EPUB | A watermarked .epub downloads | **P1 FAIL** (500) |
| BW-05 | Pre-flight | Print + EPUB rows; tells you if a check couldn't run | **P1** EPUB rows missing |
| BW-06 | Uses left: manuscript preview ×2, ONIX, reload, preview | Counter unchanged (previews unlimited) | **P1** +1 per page load |
| BW-07 | At 0: manuscript preview and ONIX | File downloads (unlimited / no subscription) | **P1** silent, nothing |
| BW-08 | Download / Export ×4 as guest | $29.99 dialog → Start trial → sign-in (stop) | PASS |
| BW-09 | Strip "Start 7-day trial" | Same dialog | PASS |
| BW-10 | Import C01 .docx | 1 chapter, table, image, list, accents | PASS |
| BW-11 | Import C07 (3×H1) / C08 (Chapter lines) | 3 / 4 chapters with the right titles | PASS |
| BW-12 | CJK chapter | Blocked with a named-script message; FAQ matches | Message PASS; **P2** FAQ mismatch |
| BW-13 | Arabic, Auto direction | RTL, shaped; boilerplate readable | PASS; P3 punctuation |
| BW-14 | 400-paragraph book | Preview < 20 s | PASS (257 pages, ~9 s) |
| BW-15 | Covers: low-res / high-res, Cover Preview, print cover preview | Warning / pass, wraparound, 1-page cover with bleed | PASS |
| BW-16 | Ebook (Draft2Digital) | Ebook only; Spine/Back Cover hidden | PASS |
| BW-17 | IngramSpark trim list | Platform-specific list | P3 same 18 (verify) |
| BW-18 | Reload | Chapter text kept | PASS |
| BW-19 | My Books / Clear everything | Lists books / clear warning | PASS |
| BW-20 | Save book project | Full backup, or clearly labelled metadata | **P2** metadata only |
| BW-21 | Invalid project file | Clear error | PASS |
| BW-22 | ONIX export (uses left) | Valid ONIX 3.0 | PASS |
| BW-23 | Preview dialog | One close button | P3 two |
| BW-24 | Video | Current product, clean profile | **P2 FAIL** |
| BW-25 | iPad Mini / iPhone SE | No overflow | P3 8 / 9 px |
| BW-26 | axe desktop | No critical issues | P3 button-name ×19, label ×1 |
| BW-27 | Locales | Translated title, correct name; /ar 200 or no hreflang | P3 |
| BW-28 | Signed-in subscriber: clean Download, EPUB, manuscript, print cover | Clean files | **Untested (sign-in)** |

Nothing is pending a usage reset.
