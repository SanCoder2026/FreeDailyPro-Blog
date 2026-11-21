Sent: 2026-11-21 07:48 ET

# FDP-49: how to reproduce (guest, fresh profile, no sign-in)

**Setup:** open https://www.freedailypro.com/tool/pdf-bookmarks-editor. The test files are in `evidence/testfiles/` (made by `make-files.py`).

## P1: per-page-load charging
1. Use a fresh context with uses left. `localStorage['fdp-usage-v1'].usageToday` should be < 2; fresh contexts often load at 2, so retry if needed.
2. Drop B01 → rename one bookmark → Download PDF with new bookmarks. The count goes +1.
3. Click New file → drop B02 → add "Intro" p1 → Download. Repeat with other files. The counter doesn't move: 9 PDFs for one use in left2.json, with 1 `usage.log` POST.
4. Reload → new PDF → Download. The count goes to 2/2. Then, in the same load, make another new PDF → Download. It still downloads with no dialog (left.json L15).

## P1: deleted bookmarks stay in the file
1. Drop `B01_nested_unicode.pdf` → Remove all → Download (`B01_nested_unicode-bookmarks.pdf`, toast "Bookmarks removed in the new file").
2. Run `python -c "import pikepdf;p=pikepdf.open('B01_nested_unicode-bookmarks.pdf');print([str(o.Title) for o in p.objects if isinstance(o,pikepdf.Dictionary) and '/Title' in o and '/Parent' in o])"`
3. Result: all 9 titles are still present, including "CONFIDENTIAL – Layoff list Q4 (delete me)" (object 37). You can also run `qpdf --show-object=37 file.pdf`.
4. Deleting one bookmark (L01/L13) leaves it the same way.

## P2: named destinations and URI bookmarks
1. Drop `B03_named_uri_xyz.pdf`. Three of the 4 bookmarks show an empty page and the warning "bookmarks have no target page…".
2. Add any bookmark → Download.
3. Check the output with check-outputs.py: the named-destination and URI bookmarks have no `/Dest` and no `/A`. The web link is gone.

## P3 items
- **Style and state lost:** `B08_closed_colour_labels.pdf` → move one bookmark → Download. `/C`, `/F` and the negative `/Count` are gone.
- **Physical page numbers:** B08 has page labels i–iii, then 1…. The editor shows only physical numbers.
- **Subtree delete:** "Delete Chapter 1 – Introduction and its sub-bookmarks" removes 4 bookmarks with one click and no confirm.

## Gate at 0 (works)
1. Drop and edit freely; the preview is a 520×672 page image.
2. Download → cap dialog ($3 Day Pass / $9.99 monthly).
3. Day Pass → email prompt (stopped there). Quick Buy monthly → Stripe Checkout (stopped there).
