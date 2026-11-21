Sent: 2026-11-20 22:45 ET

# Test cases: Merge PDF (merge-pdf)

- **Tool:** https://www.freedailypro.com/tool/merge-pdf
- **For:** Claude's retest after a fix, and the browser tester's live pass.
- **Written:** 2026-11-19 10:50:16 EST (box `date`, ET).
- **Files:** `evidence/testfiles/` (or `scripts/make-testpdfs.py`). Every page shows `FILE <id> P<n>`.
- **Checking an output:** run `python3 scripts/inspect-output.py <merged.pdf>` (needs pikepdf and poppler) for page order, sizes, /Rotate, outline, AcroForm, encryption, metadata and stamped text.
- **Rules:** guest or fresh profile only. No sign-in, no payment (stop at the email prompt or Stripe), no ad clicks.
- **Trial uses:**
  - Merging is free; **each Download spends 1 trial use**.
  - Record the strip on load. If it shows "0 remaining today", merges still work but downloads hit the cap dialog: use another fresh context or retest after midnight UTC (7:00 PM ET).
- **Results:** "Today" is the live result on 2026-11-19. "Currently: FAIL" should pass after the fix.

## A. Merge output (needs a download)

| ID | Setup | Expected (checked with inspect-output.py) | Today |
|---|---|---|---|
| MP-01 | A, B, C, D; press **Move down** on A | 11 pages B1 B2 A1 A2 A3 C1 C2 D1–D4; sizes 612×792, 595×842, 842×595, 792×612, 842×1191, 300×300 unchanged; name `B_letter_2p-merged.pdf` | PASS |
| MP-02 | E, G, I, H | E1–5 G1–2 I1 H1–3; outline E_bookmarks_5p › E chapter 1–5, then G, I, H entries; H2 keeps /Rotate 90; Japanese and Cyrillic text extract | PASS |
| MP-03 | Same output as MP-02 | Form I: no fillable fields (FAQ). Target after an enhancement: fields stay fillable | PASS vs. FAQ (competitor gap) |
| MP-04 | A "2-3", B "1", S; tick the blank-page option | A2 A3 B1 [blank] S1 (no blank after the last file) | PASS |
| MP-05 | A, B → Arrange all pages: move B p1 earlier twice, rotate A p1 right, delete B p2, Done | A1(/Rotate 90) B1 A2 A3 | PASS |
| MP-06 | Output of MP-05 | Outline has per-file bookmarks (A_a4_3p, B_letter_2p), as the FAQ says | **Currently: FAIL** (no outline) |
| MP-07 | A, B, S (no bookmarks anywhere) | Per-file bookmarks behave the same as when one file has bookmarks (MP-02 adds them) | **Currently: inconsistent** (none) |
| MP-08 | Q.jpg, R.png, S | 3 pages: 792×612, 612×792, 595×842 | PASS |
| MP-09 | A, J (password user123), K (owner-only restricted) | Prompt for J; wrong password → "That password didn't work…"; output 7 pages, **not encrypted** | PASS |
| MP-10 | K added | A notice that the file had an owner restriction (e.g. assembly not allowed) before merging | **Enhancement** (silently "Unlocked" today) |
| MP-11 | F (500 pages) + A | 503 pages, F1…F500 A1–A3, merge < 2 s | PASS (0.34 s) |
| MP-12 | A, B; Choose pages on A: leave out p2, rotate p3 right | A1 A3(/Rotate 90) B1 B2; card "Choose pages (edited)" | PASS |
| MP-13 | Any trial-use output | **Copy and output agree.** Either no badge, or the copy (meta, FAQ "Does merging add a watermark?", H3 "No upload, no watermark") says trial-use downloads carry a small "Created with FreeDailyPro.com" mark that a pass removes | **Currently: FAIL** (badge on every page, copy says "no watermark… no logo or text is added") |
| MP-14 | Any output | Producer and Creator "FreeDailyPro"; Title = first file's title or "<name>-merged"; Author kept | PASS |

## B. Input handling (no download needed)

| ID | Setup | Expected | Today |
|---|---|---|---|
| MP-15 | A + L_truncated | toast "can't be read — it looks damaged… Repair PDF"; L left out | PASS |
| MP-16 | A + N_text_renamed, O_png_renamed, P_empty | A **specific** message: "isn't a PDF" / "is a PNG picture renamed .pdf" / "is empty"; no Repair suggestion | **Currently: FAIL** (all "looks damaged, try Repair") |
| MP-17 | Only 1 valid file | Button "Add at least 2 valid PDFs to merge", disabled | PASS |
| MP-18 | notes.txt | "\"notes.txt\" can't be used here. This tool takes PDF, JPG or PNG files." | PASS |
| MP-19 | J, then Skip this file | J left out; the card says "Locked — left out of the merge" | not run (expected from JS) |
| MP-20 | A, then A again | toast "…already in your list — added anyway…"; card tag "Duplicate" | PASS |
| MP-21 | I | card note "Has form fields — they won't stay fillable once merged" | PASS |
| MP-22 | Range on A: `5`, `3-1`, `abc`, `0` | Messages: "Page 5 is outside this PDF's 3 pages", "\"3-1\" starts after it ends", "\"abc\" isn't a valid page number", outside; field red; Merge unavailable | PASS |
| MP-23 | Range `1,1,2` | Accepted, page 1 twice (the count shows +3) | PASS (by design?) |
| MP-24 | Reload after adding files | List cleared (no persistence) | PASS |

## C. Trial uses and upgrade path

| ID | Steps | Expected | Today |
|---|---|---|---|
| MP-25 | Fresh context: record the strip | "10 remaining today" for a new visitor | **Currently: FAIL from this IP**: 16 of 17 fresh contexts loaded at 0 |
| MP-26 | Uncapped: Merge | Count unchanged; result area says "Download uses 1 trial use" | PASS |
| MP-27 | Download | Exactly −1 per download (8 downloads: 10 → 2), persists after reload; Share doesn't count | PASS |
| MP-28 | Capped: Merge then Download | Merge works; "Get a Day Pass to download"; cap dialog "Today's trial uses are done — …downloading needs a pass…". Stop | PASS |
| MP-29 | Quick Buy $1 / $4.99 | $1 opens the email dialog, $4.99 goes to Stripe (as in FDP-02). **Stop. Type nothing** | not re-run here (same strip component as FDP-02) |
| MP-30 | Save to my cloud storage | Dialog "Cloud storage — $4.99 per month, 1 GB… Sign in with your email first". Choose Not now | PASS (sign-in not attempted) |
| MP-31 | Open from Google Drive / Save to Google Drive | Needs a Google login | **UNTESTED: sign-in** |

## D. Content, SEO, locales, layout

| ID | Check | Expected | Today |
|---|---|---|---|
| MP-32 | FAQ "What doesn't carry over…" | The answer starts with what doesn't carry over (forms, signatures), then says bookmarks do | **Currently: FAIL** ("Bookmarks do:") |
| MP-33 | /blog/merge-pdf | No "Bookmarks may drop" / "unlock first"; mentions Arrange, Choose pages, pictures, the duplex blank page and trial uses | **Currently: FAIL** |
| MP-34 | Video | Current UI, trial-uses wording, one title across YouTube, JSON-LD and the sitemap; the sitemap has no literal "\u2013" | **Currently: FAIL** |
| MP-35 | /es title | No "gratis" (free) | **Currently: FAIL** |
| MP-36 | pt, fr, de, ja, hi, zh, ko, id | Title, meta, subtitle, stepper, drop zone and accordions translated, also in the server HTML | **Currently: FAIL** |
| MP-37 | iPhone SE 320 px | No horizontal scroll; the drop zone reachable within about 1 screen | **Currently: FAIL** (329 px; drop zone at y=856) |
| MP-38 | Keyboard | After Move up/down, focus stays on the moved card's button; after Merge, focus goes to Download | **Currently: FAIL** (focus to \<body\>) |
| MP-39 | axe result view | 0 violations (`figure` without role=listitem, or use `li`) | **Currently: FAIL** (minor ×5) |

---

## Updates from the 2026-11-20 re-run (see RERUN-FINDINGS.md)

| ID | 2026-11-20 result |
|---|---|
| MP-13 | **Currently: FAIL** (badge text on every page of all 7 downloads; copy still says "no watermark") |
| MP-25 | The first fresh context loaded at 10 at 22:16 EST (PASS for that context) |
| MP-26 | PASS (merge free, S1–S7) |
| MP-27 | −1 per download for S1–S6; **S7 download went 6 → 10 in one click** (display-only, P1) |
