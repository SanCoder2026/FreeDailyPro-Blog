Sent: 2026-11-20 08:40 ET

# Split PDF: live functional findings (guest, no downloads)

Written: 2026-11-19 11:39 EST

**When:** guest contexts, 2026-11-19 11:28–11:38 EST. The scripts are in `scripts/` and the raw JSON and screens are in `evidence/live/`.

## Trial state (display-only evidence)

- Every fresh context opened for this tool loaded at **"Trial: 10 uses/day · 0 remaining today"**:
  - probe (`probe.json`, usageToday 10)
  - explore, kbd (desktop and Pixel 7), ranges-rows
  - the matrix (see devices-locales-findings.md)
- Starting count recorded: **0 remaining**.
- No context was uncapped, so **no output file could be downloaded**. Every output check is written as `scripts/sp-battery.js` and listed in `/workspace/deep/RERUN-AFTER-RESET.md`. **Needs re-run after midnight UTC (7:00 PM ET).**
- **Splitting is not gated.** All the splits below ran at 0 remaining; only Download is gated.

## Split scenarios (sp-explore.js, explore-1795106001431.json)

| ID | Input | Result (UI) | Time |
|---|---|---|---|
| S01 | A 10p, "1-3, 4-6, 7" | 3 rows: -pages-1-3.pdf (3 bookmarks kept), -pages-4-6.pdf, -page-7.pdf | 1.9 s |
| S02 | A, Every page | 10 files | <2 s |
| S03 | A, split every 3 + Apply | The field fills with "1-3,4-6,7-9,10", giving 4 files | <2 s |
| S04 | A, Combine, "7, 1-2, 9-10" | A_…-combined.pdf, 5 pages, "5 bookmarks kept", toast "Combined 5 pages into one PDF" | <2 s |
| S05 | A, "1-3, 2-4, 5, 5" | 4 files, duplicate named "…page-5 (2).pdf". **Overlaps and duplicates are accepted silently** | <2 s |
| S06 | B mixed sizes and rotations | 2 files (sizes and /Rotate unverified until download) | <2 s |
| S07 | G non-Latin (JP title and author) | 2 files of **46.6 KB each** (the embedded CJK font is duplicated in each part; expected) | <2 s |
| S08 | H form | "2 form fields kept" | <2 s |
| S09 | E owner-restricted | Toast 'Unlocked "E_owner_restricted_6p.pdf"'. No notice that the author's restrictions are dropped (P2) | <2 s |
| S10 | F 300p, Every page | 300 files in **1.1 s**, "Download all 300 files as ZIP" | 1.1 s |
| S11 | C single page | "This PDF has only one page, so there is nothing to split." Clear | — |
| S12 | D password | Dialog. Wrong password: "That password didn't work — please try again." Right password: unlocks, 2 files | — |

## Bad inputs

- **Truncated, garbage, text renamed to .pdf, PNG renamed to .pdf, empty 0-byte file.** All of them get "…can't be read — it looks damaged. Try the Repair PDF tool…".
  - For files that aren't PDFs at all, "damaged" and the Repair suggestion are misleading (P2).
- **JPG:** "can't be used here. This tool takes .pdf files." Good.

## Range field (sp-explore INVALID + sp-ranges-rows.js)

- **Invalid input** gets an inline message, the field gets aria-invalid=true, and the split button is disabled:

  | Input | Message |
  |---|---|
  | "3-1" | "…starts after it ends" |
  | "11", "0" | "Page N is outside this PDF's 10 pages" |
  | "abc" | "isn't a valid page number" |
  | empty | "Enter at least one page range" |
  | "-3" | "isn't a valid range" |
  | "1-3 4-6" | "isn't a valid range" |

- **Lenient, and sensible.** The row labels confirm the pages, with no download needed:

  | Input | Result |
  |---|---|
  | "1–3" (en dash) | pages 1-3 |
  | "8-" | **pages 8-10** (open-ended) |
  | "1-3,,5" | 1-3 and 5 |
  | "1-3;4-6" | 2 files |
  | " 2 , 4 " | 2 files |
  | "1-10" on a 10-page file | 1 file identical to the input, with no note (low) |

- Each row shows "pages a-b · N pages · size · N bookmarks kept". Good transparency.
- There are two split buttons ("Split PDF" and "Split into N files") that do the same thing.

## Mark disclosure (positive)

- Each file row says, before download: "This download will carry a small 'Created with FreeDailyPro.com' badge in the bottom right corner of each page. Go paid to avoid the mark."
- This is better than merge-pdf and compress-pdf, where the mark was only mentioned in the cap dialog.

## Capped download, cloud, Quick Buy (sp-kbd.js, kbd.json)

- **Clicking a row's Download or "Download all 3 files as ZIP" at 0 remaining:**
  - No download starts.
  - The dialog "Today's trial uses are done" appears: Monthly .99, Day Pass cd /workspace/deep/05-split-pdf && D=$(date "+%Y-%m-%d %H:%M %Z") && cat > live-functional-findings.md <<E
# Split PDF: live functional findings (guest, no downloads)

Written: $D

**When:** guest contexts, 2026-11-19 11:28–11:38 EST. The scripts are in \`scripts/\` and the raw JSON and screens are in \`evidence/live/\`.

## Trial state (display-only evidence)

- Every fresh context opened for this tool loaded at **"Trial: 10 uses/day · 0 remaining today"**:
  - probe (\`probe.json\`, usageToday 10)
  - explore, kbd (desktop and Pixel 7), ranges-rows
  - the matrix (see devices-locales-findings.md)
- Starting count recorded: **0 remaining**.
- No context was uncapped, so **no output file could be downloaded**. Every output check is written as \`scripts/sp-battery.js\` and listed in \`/workspace/deep/RERUN-AFTER-RESET.md\`. **Needs re-run after midnight UTC (7:00 PM ET).**
- **Splitting is not gated.** All the splits below ran at 0 remaining; only Download is gated.

## Split scenarios (sp-explore.js, explore-1795106001431.json)

| ID | Input | Result (UI) | Time |
|---|---|---|---|
| S01 | A 10p, "1-3, 4-6, 7" | 3 rows: -pages-1-3.pdf (3 bookmarks kept), -pages-4-6.pdf, -page-7.pdf | 1.9 s |
| S02 | A, Every page | 10 files | <2 s |
| S03 | A, split every 3 + Apply | The field fills with "1-3,4-6,7-9,10", giving 4 files | <2 s |
| S04 | A, Combine, "7, 1-2, 9-10" | A_…-combined.pdf, 5 pages, "5 bookmarks kept", toast "Combined 5 pages into one PDF" | <2 s |
| S05 | A, "1-3, 2-4, 5, 5" | 4 files, duplicate named "…page-5 (2).pdf". **Overlaps and duplicates are accepted silently** | <2 s |
| S06 | B mixed sizes and rotations | 2 files (sizes and /Rotate unverified until download) | <2 s |
| S07 | G non-Latin (JP title and author) | 2 files of **46.6 KB each** (the embedded CJK font is duplicated in each part; expected) | <2 s |
| S08 | H form | "2 form fields kept" | <2 s |
| S09 | E owner-restricted | Toast 'Unlocked "E_owner_restricted_6p.pdf"'. No notice that the author's restrictions are dropped (P2) | <2 s |
| S10 | F 300p, Every page | 300 files in **1.1 s**, "Download all 300 files as ZIP" | 1.1 s |
| S11 | C single page | "This PDF has only one page, so there is nothing to split." Clear | — |
| S12 | D password | Dialog. Wrong password: "That password didn't work — please try again." Right password: unlocks, 2 files | — |

## Bad inputs

- **Truncated, garbage, text renamed to .pdf, PNG renamed to .pdf, empty 0-byte file.** All of them get "…can't be read — it looks damaged. Try the Repair PDF tool…".
  - For files that aren't PDFs at all, "damaged" and the Repair suggestion are misleading (P2).
- **JPG:** "can't be used here. This tool takes .pdf files." Good.

## Range field (sp-explore INVALID + sp-ranges-rows.js)

- **Invalid input** gets an inline message, the field gets aria-invalid=true, and the split button is disabled:

  | Input | Message |
  |---|---|
  | "3-1" | "…starts after it ends" |
  | "11", "0" | "Page N is outside this PDF's 10 pages" |
  | "abc" | "isn't a valid page number" |
  | empty | "Enter at least one page range" |
  | "-3" | "isn't a valid range" |
  | "1-3 4-6" | "isn't a valid range" |

- **Lenient, and sensible.** The row labels confirm the pages, with no download needed:

  | Input | Result |
  |---|---|
  | "1–3" (en dash) | pages 1-3 |
  | "8-" | **pages 8-10** (open-ended) |
  | "1-3,,5" | 1-3 and 5 |
  | "1-3;4-6" | 2 files |
  | " 2 , 4 " | 2 files |
  | "1-10" on a 10-page file | 1 file identical to the input, with no note (low) |

- Each row shows "pages a-b · N pages · size · N bookmarks kept". Good transparency.
- There are two split buttons ("Split PDF" and "Split into N files") that do the same thing.

## Mark disclosure (positive)

- Each file row says, before download: "This download will carry a small 'Created with FreeDailyPro.com' badge in the bottom right corner of each page. Go paid to avoid the mark."
- This is better than merge-pdf and compress-pdf, where the mark was only mentioned in the cap dialog.

## Capped download, cloud, Quick Buy (sp-kbd.js, kbd.json)

- **Clicking a row's Download or "Download all 3 files as ZIP" at 0 remaining:**
  - No download starts.
  - The dialog "Today's trial uses are done" appears: Monthly $4.99, Day Pass $1, "Have an access code?", and the mark is mentioned.
  - The input is kept.
  - It was closed with Escape. No pass or email step was entered.
- **Hidden duplicate button.** "Download all (ZIP)" exists in the DOM with a 0×0 box (hidden duplicate). The visible one is "Download all N files as ZIP" (low).
- **Save to my cloud storage** opens "Cloud storage… \$4.99 per month, 1 GB… Sign in with your email first". Closed with **Not now**. **Sign-in blocked; untested.**
- **Not clicked:** Save to Google Drive and Open from Google Drive (sign-in). **Untested.**
- **Quick Buy** (\$1 / \$4.99 in the strip) is the same strip component as FDP-02/03/04. It was not clicked again here, to avoid payment pages.

## Outputs: NOT verified (download needed; re-run after midnight UTC)

- Page order per range, and the combined order 7,1,2,9,10.
- B's page sizes and /Rotate kept.
- Bookmarks and links in the parts.
- H's form fields fillable.
- G's text extractable.
- D's parts not encrypted (the FAQ: "The split pages won't have a password").
- E's restrictions dropped.
- The badge on every page.
- The 300-file ZIP.
- Whether each file, a repeat of the same file, and the ZIP each cost a use.
- Script: \`scripts/sp-battery.js\`.
E
tail -2 devices/matrix.log, "Have an access code?", and the mark is mentioned.
  - The input is kept.
  - It was closed with Escape. No pass or email step was entered.
- **Hidden duplicate button.** "Download all (ZIP)" exists in the DOM with a 0×0 box (hidden duplicate). The visible one is "Download all N files as ZIP" (low).
- **Save to my cloud storage** opens "Cloud storage… $4.99 per month, 1 GB… Sign in with your email first". Closed with **Not now**. **Sign-in blocked; untested.**
- **Not clicked:** Save to Google Drive and Open from Google Drive (sign-in). **Untested.**
- **Quick Buy** ($1 / $4.99 in the strip) is the same strip component as FDP-02/03/04. It was not clicked again here, to avoid payment pages.

## Outputs: NOT verified (download needed; re-run after midnight UTC)

- Page order per range, and the combined order 7,1,2,9,10.
- B's page sizes and /Rotate kept.
- Bookmarks and links in the parts.
- H's form fields fillable.
- G's text extractable.
- D's parts not encrypted (the FAQ: "The split pages won't have a password").
- E's restrictions dropped.
- The badge on every page.
- The 300-file ZIP.
- Whether each file, a repeat of the same file, and the ZIP each cost a use.
- Script: `scripts/sp-battery.js`.
