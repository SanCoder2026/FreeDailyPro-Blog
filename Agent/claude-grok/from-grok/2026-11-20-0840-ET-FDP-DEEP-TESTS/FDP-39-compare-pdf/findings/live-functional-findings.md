Sent: 2026-11-21 03:05 ET

# FDP-39 Compare PDF: live functional findings (guest, headless Playwright, 2026-11-21 02:51–03:01 EST)

Raw: `evidence/json/gate.json`, `cases-chromium.json`, `cases-firefox-*.json`, `privacy.json`, `probe.json`. Counters are `fdp-usage-v1.usageToday` (display-only evidence).

## Gate run (2nd fresh context had 10 left; the 1st loaded at 0)
| Step | Action | Used before → after | Note |
|---|---|---|---|
| Compare | C01 vs C02 | 0 → **0** | Compare never takes a use (also at 0) |
| A | Report (PDF) | 0 → **1** | strip "Download uses 1 trial use" |
| A2 | Report (PDF) again | 1 → 1 | |
| T | Report (.txt) | 1 → 1 | |
| B | New Comparison, C08 vs C09 → Report (.txt) | 1 → **1** | no "uses 1 trial use" note |
| C | New Comparison, C06 vs C07 (50 pages) → Report (PDF) | 1 → **1** | |
| reload → D | C01 vs C03 → Report (.txt) | 1 → 2 | |
| reload → E | C13 vs C14 → Report (PDF) | 2 → 3 | |

- **P1 gate gap (conflicts with the Nov 20 decision):** after the first charged report, every later report in the same page load is free, including new comparisons (B, C). This uses the shared once-per-page-load set `Kt` (the same pattern as #35–38).
- The report buttons have no Save to Google Drive or cloud options, so no sign-in wall was hit after a result. Only "Open from Google Drive" exists on each slot; it was not clicked.

## The full result at 0 trial uses (P1)
- With the strip reading "0 remaining today", Compare ran on C06 vs C07 (50 pages) and on C01 vs C02. The screen showed the complete result:
  - counts ("6 changes · 1 added · 1 removed · 4 edited")
  - every changed paragraph with page numbers and word-level strike/underline
  - Unified and Side by Side views
  - Previous/Next navigation
  - Evidence: `evidence/screens/dialogs/zero-sidebyside.png` and `zero-result.png`.
- The text can be selected and copied (`copySel: true`, it includes "USD 14,000").
- Only Report (PDF) and Report (.txt) hit the cap dialog: "Today's trial uses are done … downloading needs a pass". The count stayed at 10.
- The answer the user came for (what changed, where) is fully delivered for free, so Download is only a convenience. Under the Oct 30 rule (results count as trial uses) and the current instruction, this is a P1 gate gap. Compare `onClick` doesn't call usage (`ComparePdf-DabDAhev.pretty.js`).
- **Payment and keyboard:**
  - Cap dialog → Buy Day Pass → "Day Pass, $1 | Enter your email…": stopped.
  - Quick Buy day → the same email prompt. Quick Buy monthly → Stripe Checkout (session id redacted): stopped.
  - 28 Tabs reach Quick Buy, then the Original drop zone; Enter opens the file chooser.
- After a blocked report, the strip says "Trial uses start again at midnight UTC". That is 7:00 PM ET, consistent with the reset.

## Accuracy (Chromium; Firefox subset matches)
| Case | Pair | Result |
|---|---|---|
| K01 | C01 vs C02 (6 planned edits) | **Exactly 6:** case "three→Three", fee "12,500→14,000", "30→45" + "1.5%→2%", added 4A, removed Liability, dropped full stop. The "REV 2" header change was ignored as a running header (documented). Word marks: red line-through / green underline. |
| K02/K03/K04 | views | Side by Side aligns rows; untick "Show unchanged text" hides context; Next/Next/Prev → 2, 3, 2 of 6. |
| K05 | identical | "These two files have the same text. Differences in layout, fonts or line breaks are not counted." |
| K06 | C01 vs C03 (Times 12 pt, blue, rewrapped, 4 pages instead of 3) | Same text: reflow, page breaks and styling ignored, as promised. |
| K07 | blank page inserted | Same text + "C10…: page 2 has no text (scanned?), so it was not compared." |
| K08/K17 | scanned original / both scanned | Names which file and points to OCR PDF. |
| K09 | two-column vs single | Columns interleaved line by line (documented limitation). |
| K10 | 50 pages, one edit on page 37 | 1 change. The report says "original page 37, revised page 37". |
| K11 | accented / Cyrillic / Greek / € | 1 edited paragraph; words marked correctly. |
| K12 | 3,200 short lines | Lines merged into page-sized paragraphs, so the 3,000-paragraph limit was not reached. 1 change found. **Unverified:** the limit message. |
| K13 | hyphenated "uninter-/rupted" vs joined | Same text (re-joining works). |
| K14 | U01 AES as Original (password old123) | The shared unlock dialog → compared. The blog says protected files "report that it could not compare". |
| K19 | U01, Cancel | Inline text "already password-protected… Unlock it with Unlock PDF" **plus** toast "it's in your list, locked. Use Unlock on its row". There is no list or row on this tool (P3, mixed message). |
| K15/K16 | corrupt / renamed text | "can't be read — it looks damaged. Try the Repair PDF tool". |
| K18 | swapped order | Mirrored counts (1 added / 1 removed). |

- **Reports:**
  - The PDF report (pdf-lib, "Created with FreeDailyPro.com" badge) has file names, page counts, date, counts, and each change with word marks (`evidence/screens/report-A-p1-1.png`).
  - The .txt report uses `[-old-]` / `[+new+]`. Both match the screen.
- **P2, dark-theme word marks:** the computed colours are red-700 and green-700, so the `dark:` variants don't apply on the default dark theme. The changed words measure about 1.7:1 (red) and 1.3:1 (green) against the row background (`evidence/screens/zoom-dark-marks.png`). These are exactly the words users need to read.
- **Privacy** (U01 unlocked + C02): 227 requests, 14.4 KB of POST bodies total (analytics/ads). No request carried %PDF, document text, file names or the password. Storage and cookies are clean. Share copies only the tool URL. Nothing is restored after a reload.
