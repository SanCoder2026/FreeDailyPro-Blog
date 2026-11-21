Sent: 2026-11-20 22:45 ET

# Test cases: Compress PDF (compress-pdf)

- **Tool:** https://www.freedailypro.com/tool/compress-pdf
- **For:** Claude's retest after a fix, and the browser tester's live pass.
- **Written:** 2026-11-19 11:24:20 EST (box `date`, ET).
- **Files:** `evidence/testfiles/` (the small ones) or `python3 scripts/make-testpdfs.py <dir>` for all 17 (seeded, so they are reproducible; A, I and J are large and not zipped).
- **Checking an output:** `python3 scripts/inspect-output.py <out.pdf>` (pikepdf + poppler) for bytes, pages, sizes, /Rotate, outline, links, AcroForm, images (filter/colourspace), encryption, metadata and stamped text.
- **Rules:** guest or fresh profile only. No sign-in, no payment (stop at the email prompt or Stripe), no ad clicks.
- **Trial uses:**
  - **Compress is free; each Download spends 1.** A batch of up to 5 is 1.
  - Record the strip on load. If it shows "0 remaining today", every compress case still runs, but download cases need another fresh context or a retest after midnight UTC (7:00 PM ET).
- **Results:** "Today" is the live result on 2026-11-19. "Currently: FAIL" should pass after the fix. "**Re-run**" means it was not observable today because every context was capped: needs re-run after midnight UTC.

## A. Compression (compress only, no download needed)

| ID | Input / setting | Expected | Today |
|---|---|---|---|
| CP-01 | A_photos_6p (18.04 MB), Balanced | Levels: L1 ≈1.3 MB "text still selectable", L2 ≈327 KB; summary "18.04 MB → … (98% smaller)"; toast; under 10 s | PASS (4.6 s) |
| CP-02 | A, Aggressive | Stops after L2 with "Stopped at level 2… Run anyway" | PASS |
| CP-03 | A, Extreme → Run anyway | Levels continue to grey and then B/W as the copy says, **or** a note explains why it stopped (e.g. "grey would not be smaller") | **Currently: FAIL** (ends at L3 "Photo and shaded areas at 70 dpi", colour, no note) |
| CP-04 | A, Target 1 MB | Result ≤ target; ideally ≤ 1,000,000 bytes (decimal) and the UI states which MB it uses | PASS on screen (1002.6 KB); bytes **Re-run** |
| CP-05 | A, Target 200 KB | ≤ 200 KB | PASS (193.7 KB) |
| CP-06 | A, Target 20 KB, Go as far as: Balanced only | Smallest result plus "Couldn't reach… Only the Balanced steps were allowed… Choose Go as far as Aggressive or Extreme" | PASS |
| CP-07 | B_text_only_5p, Balanced / Aggressive | "Tidy the file", "Only the file's structure was tidied"; Aggressive "none came out smaller than level 1" | PASS |
| CP-08 | B, Target 2 MB (default) | "already under 2.00 MB. No compression needed." | PASS |
| CP-09 | B, Target 2 KB | Smallest plus "included the Extreme steps… about 409 B for each page" | PASS |
| CP-10 | C_scan_grey_4p | 3.60 MB → about 60 KB | PASS |
| CP-11 | **I_cmyk_2p (10.26 MB, DCT CMYK photos)**, Balanced | The message names the real cause ("CMYK pictures are left as they are by Balanced") and suggests Aggressive. Better: CMYK photos are converted and shrunk | **Currently: FAIL**: "This PDF is a scan… stored as scanner pictures (JBIG2 or JPEG 2000)… nothing was changed" |
| CP-12 | K_already_small_3p | 107 KB → about 22 KB | PASS |
| CP-13 | J_big_24p (72 MB) | Completes without a crash on desktop; about 1.3 MB | PASS (18.3 s) |
| CP-14 | F_owner_restricted_2p | Compresses; ideally a notice that the original had restrictions | PASS / enhancement |
| CP-15 | Several files: A, B, C, I, G | Per-file results, "5 of 5 done. 35.57 MB to 10.71 MB", Download all (ZIP), Run again, Continue with Merge PDF, Clear | PASS |
| CP-16 | Several files: 6 files | toast "1 file left out. A batch takes up to 5 files on the trial…" | PASS |

## B. Input handling

| ID | Input | Expected | Today |
|---|---|---|---|
| CP-17 | L_truncated, M_garbage | toast "can't be read — it looks damaged… Repair PDF" | PASS |
| CP-18 | N_text_renamed, O_png_renamed, P_empty (.pdf) | Specific: "isn't a PDF" / "is a PNG picture" / "is empty"; no Repair suggestion | **Currently: FAIL** (all "looks damaged, try Repair") |
| CP-19 | Q_image.jpg | "can't be used here. This tool takes .pdf files." (ideally a link to JPG to PDF) | PASS |
| CP-20 | E_password (user123) | Dialog "This PDF is password-protected… your result won't have a password"; a wrong password shows an error; the right one unlocks | dialog PASS; wrong/right **Re-run** (cp-battery S7) |
| CP-21 | Target 0 / −5 / empty / abc | "Enter a valid target size"; ideally an inline field error with aria-invalid | PASS (toast only) |

## C. Output files (need a download: 1 trial use each)

| ID | Steps | Expected (inspect-output.py) | Today |
|---|---|---|---|
| CP-22 | CP-01, Download Compressed PDF | 6 pages, A4, text "FILE A P1…" extractable; bytes ≈ the shown size | **Re-run** |
| CP-23 | D_links_bookmarks_form_3p, Balanced, Download | outline "D chapter 1–3", 3 link annots, AcroForm 2 fields (client_name="Jane Example", agree) **kept**, as the page promises | **Re-run** |
| CP-24 | G_nonlatin, Balanced | Japanese, Cyrillic, Greek and Arabic text extract; Title "日本語テスト 資料", Author "山田 太郎" kept | **Re-run** |
| CP-25 | H_mixed_rotated, Balanced | sizes 595×842, 792×612 (/Rotate 90), 300×300 kept | **Re-run** |
| CP-26 | Any trial-use download | Either no mark, or the page says before Download that trial-use downloads carry a small "Created with FreeDailyPro.com" mark | **Re-run** (the cap dialog says passes remove it) |
| CP-27 | CP-15, Download all (ZIP) | ZIP with 5 PDFs (I unchanged); 1 trial use | **Re-run** |
| CP-28 | E unlocked, Download | Output not encrypted | **Re-run** |

## D. Trial uses and upgrade path

| ID | Steps | Expected | Today |
|---|---|---|---|
| CP-29 | Fresh context: record the strip | "10 remaining today" | **Currently: FAIL from this IP**: 28 of 31 fresh contexts at 0 |
| CP-30 | Uncapped: Compress any mode | Count unchanged | PASS (capped contexts compress freely; usageToday unchanged) |
| CP-31 | Uncapped: Download one level, then another level of the same run | −1 for the first; document whether a second level costs another use | **Re-run** |
| CP-32 | Capped: Download | Dialog "Today's trial uses are done… Either pass removes the 'Created with FreeDailyPro.com' mark…"; stop | PASS |
| CP-33 | Quick Buy $1 / $4.99 | $1 → email dialog "Day Pass, $1 — Enter your email…", $4.99 → Stripe Checkout. Stop; type nothing | PASS (inconsistent flows, as in FDP-02) |
| CP-34 | Save to my cloud storage | "Cloud storage — $4.99 per month, 1 GB… Sign in with your email first". Choose Not now | PASS (sign-in not attempted) |
| CP-35 | Open from / Save to Google Drive | Needs a Google login | **UNTESTED: sign-in** |

## E. Layout, a11y, content, locales

| ID | Check | Expected | Today |
|---|---|---|---|
| CP-36 | Result view at 1366 px (capped and uncapped) | Level label readable on one or two lines; buttons wrap below it | **Currently: FAIL** (label column 48 px wide) |
| CP-37 | Result view on Pixel 7 / iPhone SE | No horizontal scroll (`scrollWidth` = viewport); buttons stack | **Currently: FAIL** (958 px) |
| CP-38 | iPhone SE 320 px empty state | No overflow; drop zone reachable within about 1 screen | **Currently: FAIL** (329 px; drop zone below the fold) |
| CP-39 | Keyboard | Focus goes to the file card after Add and to the result summary or first Download after Compress | **Currently: FAIL** (\<body\>) |
| CP-40 | Video | Current modes (Balanced/Aggressive/Extreme/Target), levels and compare; trial-uses wording; one title across YouTube, JSON-LD and the sitemap | **Currently: FAIL** |
| CP-41 | Blog | Mentions Target size, levels, Compare, Several files; no "unlock first" | **Currently: FAIL** |
| CP-42 | /es title | No "gratis" | **Currently: FAIL** |
| CP-43 | pt, fr, de, ja, hi, zh, ko, id | Title, meta, H1 and UI translated in the server HTML | **Currently: FAIL** |

---

## Updates from the 2026-11-20 re-run (see RERUN-FINDINGS.md)

| ID | 2026-11-20 result |
|---|---|
| CP-04 | 200 KB target → 198,355 B (PASS); 1 MB target not re-run |
| CP-22 | PASS (6 pages, text extractable) |
| CP-23 | PASS (outline 3, links 3, form fields 2 kept) |
| CP-24 | PASS |
| CP-25 | PASS (sizes and /Rotate 90 kept) |
| CP-26 | PASS: no badge on trial downloads (copy mismatch with the cap dialog, P2) |
| CP-27 | **Still pending** (batch ZIP not downloaded) |
| CP-28 | PASS (not encrypted) |
| CP-31 | −1 for the first download; a second level of the same run is free. **S9 went 8 → 10 in one click** (display-only) |
