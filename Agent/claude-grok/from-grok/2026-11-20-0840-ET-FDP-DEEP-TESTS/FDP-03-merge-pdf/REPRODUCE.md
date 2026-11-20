Sent: 2026-11-20 08:40 ET

# FDP-03 Merge PDF: reproduce

- **Written:** 2026-11-19 10:52:05 EST (box `date`, ET).
- **Setup:** guest or fresh profile, no sign-in, no ad clicks. Inputs are in `evidence/testfiles/`, or run `python3 scripts/make-testpdfs.py <dir>` (reportlab, pikepdf).
- **Check outputs:** `python3 scripts/inspect-output.py <file.pdf>...` (pikepdf + poppler pdfinfo/pdftotext).
- **Trial uses:** each **Download** spends 1 (Merge is free). If the strip shows "0 remaining today", Merge still works but Download opens the cap dialog; use another fresh context or wait for midnight UTC (7:00 PM ET).
- **Automation:** run from a folder with Playwright installed (`cd /workspace/deep/tools-env`). The scripts write to `/workspace/deep/03-merge-pdf/live/`; edit `OUT`/`T` at the top.

## R-01: "no watermark" copy vs. stamped badge (P0)

1. Open https://www.freedailypro.com/tool/merge-pdf with uses remaining.
2. Add `A_a4_3p.pdf` and `B_letter_2p.pdf` → Merge 2 PDFs → Download Merged PDF.
3. Open the output: every page shows a bottom-right "Created with FreeDailyPro.com" badge with the F logo. `pdftotext out.pdf - | grep -c "Created with FreeDailyPro.com"` = page count.
4. Compare with the page:
   - meta description "…download a clean PDF, with no watermark"
   - FAQ "Does merging add a watermark? No…"
   - H3 "No upload, no watermark… no logo or text is added"
5. **Evidence:** `evidence/screens/live/s1-page1-01.png`, `s5-page1-1.png`; `evidence/json/output-inspection.json` (`watermark_text_found`); `evidence/downloads/`.
6. Script: `node scripts/mp-battery.js 6 S1_order_reorder`, then `inspect-output.py`.

## R-02: fresh contexts load at 0 remaining

1. Open the tool in 3–5 fresh incognito profiles, or run `node scripts/mp-probe.js`.
2. Record the strip "Trial: 10 uses/day · N remaining today" and localStorage `fdp-usage-v1` before any action.
3. **Seen 2026-11-19 10:30–10:50 EST:** 16/17 matrix and geo contexts and 6/7 probe contexts at 0 (`evidence/json/matrix-results.json`, `probe.json`, `battery-*.json`).
4. **Expected:** 10 for a new visitor. Display-only evidence; verify server-side.
5. Uncapped counting: `node scripts/mp-battery.js 6`. Seen: Merge 0, each Download −1 (8 → used 8), reload persists, Share 0.

## R-03: bookmark output inconsistent

1. Merge A, B, S (no bookmarks) → output has **no outline**.
2. Merge E (bookmarked), G, I, H → per-file entries for every file, with E's chapters nested.
3. Merge A, B via **Arrange all pages** → no outline, although the FAQ says per-file bookmarks are kept.
4. Script: `node scripts/mp-battery.js 6 S2_bookmarks_meta_nonlatin_form_rotate,S4_arrange_move_rotate_delete` → `inspect-output.py` (`outline`).

## R-04: video outdated

https://www.youtube.com/watch?v=0FjbjU4eDVw: see frames f05–f10 and f17 in `evidence/video/frames/` ("0 free uses remaining today", "10 free uses daily!", "200+ Free Productivity Tools"). Compare the three titles (YouTube, JSON-LD, sitemap with a literal "\u2013").

## R-05: blog stale

https://www.freedailypro.com/blog/merge-pdf: "Bookmarks may drop on merge", "Encrypted parts must be unlocked first" (`evidence/html/blog-visible.txt`).

## R-06: locales

- `curl -s https://www.freedailypro.com/pt/tool/merge-pdf | grep -o "<title>[^<]*"` → English title (same for fr, de, ja, hi, zh, ko, id).
- /es title "Fusionar PDF gratis…".
- Screens: `evidence/screens/locales/`.

## R-07: non-PDFs called damaged

Add `N_text_renamed.pdf`, `O_png_renamed.pdf` and `P_empty.pdf` → each gets the toast "…can't be read — it looks damaged. Try the Repair PDF tool…". `evidence/screens/live/ui-errors.png`, `json/ui-probe.json`.

## R-08: form fields not fillable

Merge `I_form_1p.pdf` with A → output AcroForm fields 0, 2 widget annotations remain, "Jane Example" visible but not editable (`output-inspection.json`, S2). The card warns in advance ("Has form fields — they won't stay fillable once merged").

## R-09: owner-restricted file silently unlocked

Add `K_owner_only_restricted_2p.pdf` → toast 'Unlocked "K_owner_only_restricted_2p.pdf"' with no prompt and no notice of the restriction. Output unencrypted. Note: K's page markers read "FILE J" (same source as J).

## R-10: mobile fold and overflow

`node run-matrix.js scripts/config.json` → iPhone SE scrollWidth 329 > 320; key input at y=856 (viewport 568). `evidence/screens/devices/`.

## R-11: focus and axe

`node scripts/mp-kbd-cloud.js` → after Move down and after Merge, `document.activeElement` is \<body\>; axe on the result view: aria-allowed-role ×5 (`evidence/json/kbd-cloud.json`).

## Sign-in-gated (not tested)

On https://www.freedailypro.com/tool/merge-pdf: "Open from Google Drive", "Save to Google Drive" (Google login), "Save to my cloud storage" (email sign-in plus a $4.99/month add-on). Santosh would need to sign in to test these.
