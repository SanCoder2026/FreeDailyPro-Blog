Sent: 2026-11-20 08:40 ET

# Test cases: Split PDF (split-pdf)

- **Tool:** https://www.freedailypro.com/tool/split-pdf
- **For:** Claude's retest after a fix, and the browser tester's live pass.
- **Written:** 2026-11-19 11:45:14 EST (box `date`, ET).
- **Files:** `evidence/testfiles/` (all 14 inputs, about 260 KB), or regenerate them with `python3 scripts/make-testpdfs.py <dir>`. Every page prints "FILE <id> P<n>", so the page order can be read with pdftotext.
- **Checking an output:** `OUT_JSON=out.json python3 scripts/inspect-output.py <pdf>...` reports pages, the order markers, sizes, /Rotate, outline, links, AcroForm, encryption, stamped text and non-Latin text.
- **Rules:** guest or fresh profile only. No sign-in, no payment (stop at the email prompt or Stripe), no ad clicks.
- **Trial uses:**
  - **Split is free; Download is gated.** Every split case below ran at 0 remaining.
  - Download cases need an uncapped context.
- **Results:** "Today" is the live result on 2026-11-19, 11:28–11:43 EST.
  - "**Currently: FAIL**" should pass after the fix.
  - "**Re-run**" means it was not observable today because every context that could act was capped. These need a re-run after midnight UTC (7:00 PM ET) with `scripts/sp-battery.js`.

## A. Splitting (no download needed)

| ID | Input / action | Expected | Today |
|---|---|---|---|
| SP-01 | A 10p, "1-3, 4-6, 7" → Split | 3 rows: -pages-1-3.pdf, -pages-4-6.pdf, -page-7.pdf, each with "pages a-b · N pages · size · N bookmarks kept"; under 3 s | PASS (1.9 s) |
| SP-02 | A, Every page | 10 rows; "Download all 10 files as ZIP" | PASS |
| SP-03 | A, split every 3 + Apply | The field becomes "1-3,4-6,7-9,10", giving 4 files | PASS |
| SP-04 | A, Combine, "7, 1-2, 9-10" | One -combined.pdf, 5 pages, "5 bookmarks kept", toast "Combined 5 pages into one PDF" | PASS |
| SP-05 | A, "1-3, 2-4, 5, 5" | Splits, **and** a short note that ranges overlap or repeat | **Currently: PARTIAL** (4 files, duplicate auto-named "page-5 (2).pdf", no note) |
| SP-06 | B mixed sizes/rotation, "1-2, 3-5" | 2 files | PASS |
| SP-07 | G non-Latin, "1-2, 3-4" | 2 files | PASS (46.6 KB each; the font is repeated per part, expected) |
| SP-08 | H form, "1, 2-3" | "2 form fields kept" on the part with p2 | PASS |
| SP-09 | E owner-restricted | Splits, and says the author's restrictions won't carry over (or keeps them) | **Currently: PARTIAL** (toast 'Unlocked "…"' only) |
| SP-10 | F 300p, Every page | 300 rows, ZIP button, under 5 s | PASS (1.1 s) |
| SP-11 | C single page | "This PDF has only one page, so there is nothing to split." | PASS |
| SP-12 | D password: wrong, then user123 | Wrong: "That password didn't work — please try again."; right: unlocks inline | PASS |
| SP-13 | Thumbnails | Either clickable to select pages (as the Details copy says), or the copy no longer claims checkboxes | **Currently: FAIL** (plain img alt="Page N"; a click does nothing; copy claims checkboxes) |

## B. Range field

| ID | Input (A 10p) | Expected | Today |
|---|---|---|---|
| SP-14 | "3-1" | Inline "…starts after it ends", aria-invalid, button disabled | PASS |
| SP-15 | "11", "0" | "Page N is outside this PDF's 10 pages" | PASS |
| SP-16 | "abc", "-3", "1-3 4-6" | "isn't a valid page number / range" | PASS |
| SP-17 | empty | "Enter at least one page range" | PASS |
| SP-18 | "1–3" (en dash) | pages 1-3 | PASS |
| SP-19 | "8-" | pages 8-10 (open-ended). Documented in the hint or FAQ | PASS (works); **docs: FAIL** (not documented) |
| SP-20 | "1-3,,5", " 2 , 4 ", "1-3;4-6" | tolerated | PASS |
| SP-21 | "1-10" on a 10-page file | A note that the result equals the original | low; no note today |

## C. Bad inputs

| ID | Input | Expected | Today |
|---|---|---|---|
| SP-22 | L truncated, M garbage | "looks damaged, try Repair PDF" | PASS |
| SP-23 | N text renamed .pdf, O PNG renamed .pdf, P empty | "This isn't a PDF" / "This file is empty", **not** "damaged, try Repair" | **Currently: FAIL** (all "damaged… Repair PDF") |
| SP-24 | Q image.jpg | "can't be used here. This tool takes .pdf files." | PASS |

## D. Trial gate, offer, sign-in (capped context)

| ID | Action | Expected | Today |
|---|---|---|---|
| SP-25 | Load in a brand-new profile | Strip "10 remaining today" | **Currently: FAIL** (21 of 22 readable contexts at 0; display-only) |
| SP-26 | Before download | The row states the "Created with FreeDailyPro.com" badge | PASS (per row) |
| SP-27 | Download (row) at 0 | Cap dialog "Today's trial uses are done", input kept, no download | PASS |
| SP-28 | "Download all N files as ZIP" at 0 | Same cap dialog | PASS |
| SP-29 | Save to my cloud storage | Dialog "$4.99 per month, 1 GB… Sign in with your email first"; **Not now** closes it | PASS (sign-in not attempted) |
| SP-30 | Save to / Open from Google Drive | Sign-in. **Do not click in tests** | Untested (sign-in) |

## E. Downloads and outputs (needs re-run after midnight UTC, `scripts/sp-battery.js`)

| ID | Scenario | Verify | Today |
|---|---|---|---|
| SP-31 | S1: download file 1, file 1 again, file 2, then the ZIP | usageToday before/after each: does each file cost 1, does a repeat cost again, does the ZIP cost 1? Report the display only | **Re-run** |
| SP-32 | S1 outputs | order markers A1-3 / A4-6 / A7; outline entries per part = "N bookmarks kept"; link annots kept | **Re-run** |
| SP-33 | S2 combined | order A7, A1, A2, A9, A10; 5 outline entries | **Re-run** |
| SP-34 | S3 "8-" | A8–A10 | **Re-run** |
| SP-35 | S4 B every page ZIP | 5 PDFs; page sizes A4 / Letter landscape r90 / A3 / 300×300 / Letter r180 kept | **Re-run** |
| SP-36 | S5 G | Japanese/Cyrillic/Arabic text extractable; title/author metadata | **Re-run** |
| SP-37 | S6 H | AcroForm fields present and fillable in the part with p2 | **Re-run** |
| SP-38 | S7 D unlocked | parts **not** encrypted (the FAQ: "The split pages won't have a password") | **Re-run** |
| SP-39 | S8 E | restrictions dropped or kept; matches whatever the UI says | **Re-run** |
| SP-40 | All trial-use outputs | "Created with FreeDailyPro.com" badge bottom-right on **each page**, as the row says | **Re-run** |
| SP-41 | S9 F 300 every page ZIP | ZIP with 300 PDFs, time to build, size | **Re-run** |

## F. Layout and a11y

| ID | Check | Expected | Today |
|---|---|---|---|
| SP-42 | iPhone SE 320 px empty state | no horizontal scroll; drop zone visible without scrolling | **Currently: FAIL** (329 px; drop zone below the fold) |
| SP-43 | Result rows at 1366 px | File names readable (wrap or show the range first) | **Currently: PARTIAL** (names truncated to about 100 px, "A_10p_bookm…") |
| SP-44 | Pixel 7 result view | no overflow | PASS (412) |
| SP-45 | Focus after Add and after Split | Moves to the file card / result summary | **Currently: FAIL** (BODY) |
| SP-46 | axe result view | 0 violations | PASS |
| SP-47 | Locales: title and H1 | localized title/meta in the server HTML for es…id; UI headings translated | **Currently: FAIL** (English titles on 9 locales; mixed UI) |
