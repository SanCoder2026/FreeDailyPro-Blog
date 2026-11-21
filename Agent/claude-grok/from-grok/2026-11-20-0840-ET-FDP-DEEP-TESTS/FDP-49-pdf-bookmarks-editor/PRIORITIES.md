Sent: 2026-11-21 07:48 ET

# FDP-49 PDF Bookmarks Editor: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Suggested direction |
|---|---|---|---|
| P1 | Per-page-load charging: one trial use covered 9 different PDFs in one page load (left2.json, 1 `usage.log` POST). In left.json, after a reload took the 2nd use (2/2), another new PDF still downloaded with no dialog (L15) | json/left.json, json/left2.json, outputs/ | Charge per new result (hash of file + outline) and check the cap on every Download. Shared ToolPage/`logUsageNow`→`tryUse` fix (same as FDP-44–48) |
| P1 (privacy) | Deleted bookmarks are still inside the downloaded PDF. `Je()` deletes the catalog's `/Outlines` key but never deletes the old outline objects, and pdf-lib `save()` writes every object in the context. Deleting "CONFIDENTIAL – Layoff list Q4" or clicking "Remove all" leaves those titles readable with any PDF library (pikepdf/qpdf show object 37 with the title), while the page says "Remove all… The new PDF has no outline" | outputs/L16 (Remove all), L01/L13 (single delete), L07 (300 titles left after Remove all); json/orphans.txt | Before `save()`, walk the old outline tree (from the original `/Outlines`) and `context.delete()` each ref, or copy pages into a fresh document. Then retest with `scripts/check-outputs.py` (orphans = 0) |
| P2 | Named destinations aren't resolved: bookmarks that point at a named destination (`/Dest (name)` or GoTo with a named `D`) load with no page, and if the user doesn't fix each one by hand, they're saved as dead headings. LaTeX/hyperref and many exporters use named destinations for every bookmark | outputs/L03, testfiles/B03 | Resolve through `/Root /Names /Dests` (name tree) and `/Root /Dests`; keep the warning for anything still unresolved |
| P2 | Bookmarks that open a web link (URI action) or any other action lose it silently. The warning only says "no target page" | outputs/L03 "Website link (URI)" | Keep the original `/A` when the user hasn't changed the page; or say "this bookmark opens a web link; it will become a heading" |
| P3 | Style and state are lost: colour (`/C`), bold/italic (`/F`) and collapsed state (negative `/Count`) are dropped; every parent is saved expanded | outputs/L08 vs testfiles/B08 | Carry `/C`, `/F` and the open/closed flag through (and say so in Limitations if not) |
| P3 | Page numbers are physical only: a book with roman front matter (page labels i–iii, then 1…) shows "Page 4" where the printed number is 1; the blog advises matching the printed contents | testfiles/B08 | Show the page label next to the number in the preview ("Page 4 (printed 1)") |
| P3 | "Delete Chapter 1 and its sub-bookmarks" removes a whole subtree with one click and no confirm (Undo all exists, but it undoes everything) | json/left2.json L13 | Per-step undo, or a small "Deleted 4 bookmarks · Undo" toast |
| P3 | Meta description 110 chars; og-default image; video breadcrumb "PDF Tools" and "200+ tools" vs live "Publishing & Print Makers" / "300+" | html/ | Fuller meta, own OG image |
| P3 | Matrix/a11y items (see devices-locales findings) | json/matrix-results.json | |

- **Owner question:** downloads carry no "Created with FreeDailyPro.com" mark (checked page streams and raw bytes), while the cap dialog says a pass "removes the … mark from your PDFs". Decide whether this tool should carry the mark.
- **Owner question:** a PDF with only an owner (permissions) password is unlocked silently ("Unlocked …" toast) and the result drops the restrictions. This is a shared drop-zone behaviour; confirm it's intended.
- **RERUN-AFTER-RESET:** none (nothing pending a reset).
- **Sign-in-only, untested:** Open from Google Drive (Google sign-in popup); paid-pass behaviour. This tool has no Save to Drive / cloud save / copy / print button in any state (verified live; tools.csv lists "share;save;project-file;copy;print", which the page doesn't render).
