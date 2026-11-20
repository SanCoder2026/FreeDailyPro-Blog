Sent: 2026-11-20 08:40 ET

# FDP-05 Split PDF: reproduce

- **Written:** 2026-11-19 11:46:52 EST (box `date`, ET).
- **Setup:** guest or fresh profile, no sign-in, no ad clicks.
  - **Inputs:** `evidence/testfiles/` (all 14), or `python3 scripts/make-testpdfs.py <dir>`.
  - **Check outputs:** `OUT_JSON=out.json python3 scripts/inspect-output.py <file.pdf>...`.
- **Trial uses:** Split is free; Download is gated. At "0 remaining today", every split step still works, but downloads open the cap dialog.
- **Automation:** run from a folder with Playwright installed (`cd /workspace/deep/tools-env`). The scripts write to `/workspace/deep/05-split-pdf/live/`; edit `OUT`/`T` at the top.

## R-01: fresh contexts load at 0 remaining

1. Open https://www.freedailypro.com/tool/split-pdf in several fresh incognito profiles, or run `node scripts/sp-probe.js`.
2. Read the strip "Trial: 10 uses/day · N remaining today" and localStorage `fdp-usage-v1` before any action.
3. **Seen 2026-11-19 11:28–11:43 EST:** 21 of 22 readable contexts at 0 (`usageToday 10`). One geo hi-IN load showed 10. See `json/probe.json`, `kbd.json`, `ranges-rows.json`, `matrix-results.json`.
4. **Expected:** 10.
5. Display-only evidence; verify server-side.

## R-02: Limitations and Details contradict the tool

1. Open the page, expand "Details: when to use it, limits, privacy" and "Common questions".
2. Limitations: "Password-protected PDFs need their password removed first, same as with merging." The FAQ: "you'll be asked for it… unlocked right in your browser."
3. Add `D_password_user123_6p.pdf`. A password dialog appears; enter user123 and it is unlocked inline (SP-12).
4. Details: "checkboxes on thumbnails". Add `A_10p_bookmarks_links.pdf` and click a thumbnail: nothing happens, and the range field is unchanged. The thumbnails are `<img alt="Page N">` (`json/kbd.json` thumbs, thumbClick).

## R-03: blog not linked, and it promises per-range names

1. On the tool page, search the HTML for "split-pdf-multi-contract-client-packets": 0 hits (`html/tool.html`).
2. Open https://www.freedailypro.com/blog/split-pdf-multi-contract-client-packets. Its steps say "Enter range 1–12, name the output something like ClientA-purchase-2026-10-22.pdf".
3. In the tool, after Split there is no name field. The outputs are `<base>-pages-1-12.pdf`, etc.

## R-04: locales serve an English head

1. Run `curl -s https://www.freedailypro.com/es/tool/split-pdf | grep -o '<title>.*</title>'` (repeat for pt, fr, de, ja, hi, zh, ko, id).
2. All show "Split PDF by Page Range or Every Page - Private, On-Device", while the client H1 is localized (Dividir PDF, PDF分割…). /ar returns 404.
3. Evidence: `html/tool-*.html`, `json/matrix-results.json` locales, `screens/locales/`.

## R-05: small-screen empty state and truncated row names

1. **iPhone SE (320×568):** `scrollWidth` is 329, caused by the header menu button. The drop zone is below the fold (`screens/devices/iphone-se-fold.png`).
2. **Desktop 1366:** split A with "1-3, 4-6, 7". Every row name shows as "A_10p_bookm…" (about 100 px wide; `json/kbd.json` rowLabelWidths, `screens/live/kbd-result-view.jpg`).

## R-06: focus and a11y

1. Use the keyboard: Tab to the drop zone and press Enter; the chooser opens. After the file loads, `document.activeElement` is BODY. After Split it is BODY again (`json/kbd.json`).
2. axe on the empty page: desktop label-content-name-mismatch; Pixel 7 ad-caption contrast. The result view has 0 violations.

## R-07: messages

1. "1-3, 2-4, 5, 5" gives 4 files with no note, including "page-5 (2).pdf" (SP-05).
2. `N_text_renamed.pdf`, `O_png_renamed.pdf` and `P_empty.pdf` all say "…looks damaged. Try the Repair PDF tool" (SP-23).
3. `E_owner_restricted_6p.pdf` shows the toast 'Unlocked "…"' with no restriction notice (SP-09).

## R-08: outputs (needs re-run after midnight UTC)

1. After 7:00 PM ET, run `node scripts/sp-battery.js 6`. It skips capped contexts and stops once a context reaches 0.
2. Then run `OUT_JSON=live/output-inspection.json python3 scripts/inspect-output.py live/downloads/*.pdf live/downloads/unz/*/*.pdf`.
3. Check SP-31…SP-41 in test-cases.md.
