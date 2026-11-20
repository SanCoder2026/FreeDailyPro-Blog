Sent: 2026-11-20 08:40 ET

# Merge PDF: live functional, output, trial-use and paywall findings

- **Written:** 2026-11-19 10:47:24 EST (box `date`, ET).
- **Tester and method:** headless Playwright, Chromium 159, guest only. Fresh contexts, no sign-in, no ad clicks, no payment.
- **Test files:** generated with `scripts/make-testpdfs.py` (reportlab, pikepdf). Every page prints a unique marker, `FILE <id> P<n>`.
- **Output checks:** every downloaded file was checked with `scripts/inspect-output.py`:
  - pikepdf 10.18 / libqpdf 12.4.2 for page count, sizes, /Rotate, docinfo, outline, AcroForm and encryption
  - pdftotext for page-order markers and stamped text
  - pdfinfo, saved in `json/output-inspection.json`
- **Counters:** display-only evidence (strip plus localStorage `fdp-usage-v1`). No backend claims.

## 1. Starting trial count (record of every fresh context)

| Time (EST) | Script | Strip on load |
|---|---|---|
| 10:31:40 | mp-probe | **0 remaining today** (usageToday 10) |
| 10:32:15 | mp-try | **0 remaining** |
| 10:33:06 | mp-ui-probe | **0 remaining** |
| 10:37:05 / 10:37:10 | mp-battery attempts 1–2 | **0 remaining** |
| 10:37:15 | mp-battery attempt 3 | **10 remaining** (usageToday 0). This context was used for every download below |
| 10:41:07 | mp-kbd-cloud | **0 remaining** |

**6 of 7 fresh contexts loaded capped,** the same IP-pool pattern as FDP-02. A real first-time visitor behind a shared IP may see "0 remaining" before they've used the tool once. HIGH, display-only. This box IP was used heavily today.

## 2. Downloads and outputs: one uncapped context, 8 scenarios (`json/battery-*.json`, `downloads/`)

| # | Scenario | Live output (pikepdf/pdftotext) | Expected | Result |
|---|---|---|---|---|
| S1 | A(A4×3), B(Letter×2), C(A4 landscape×2), D(A4, Letter-landscape, A3, 300×300). **Move down** on A before merging | 11 pages, **B1 B2 A1 A2 A3 C1 C2 D1 D2 D3 D4**. Sizes kept exactly: 612×792, 595×842, 842×595, 792×612, 842×1191, 300×300. File named `B_letter_2p-merged.pdf` | order follows the list; sizes and orientation kept | PASS |
| S2 | E (5 bookmarks), G (Japanese/Cyrillic/Greek/Arabic text, Japanese title), I (AcroForm text + checkbox), H (page 2 /Rotate 90) | 11 pages E1–5 G1–2 I1 H1–3. Outline: "E_bookmarks_5p" › E chapter 1…5, then "G_nonlatin_2p", "I_form_1p", "H_rotated_p2_3p". H2 keeps /Rotate 90. Non-Latin text extracts intact. **AcroForm fields 0** (2 orphan widget annotations remain); the value "Jane Example" is still visible as text | as FAQ: per-file bookmarks with own children; forms not fillable | PASS (matches FAQ). Competitor gap: forms not kept fillable |
| S3 | Ranges A "2-3", B "1", S (all), plus "blank page after odd" | 5 pages: **A2 A3 B1 [blank] S1**. No blank after A (even) or after the last file | correct | PASS. Outline empty: no per-file bookmarks here, while S2 had them for files without their own (LOW, inconsistent) |
| S4 | Arrange all pages: move B1 earlier ×2, rotate A1 right, delete B2, Done | 4 pages **A1(/Rotate 90) B1 A2 A3** | correct | PASS. **Outline empty**, while the FAQ says "if you use Arrange all pages, only the per-file bookmarks are kept" (LOW) |
| S5 | Q.jpg (800×600), R.png (600×900), S.pdf | 3 pages: **792×612 (landscape Letter)**, **612×792**, A4. Title fell back to "Q_image-merged" | as FAQ | PASS |
| S6 | A + J (user password; wrong then right) + K (owner-only, no-modify/no-assembly) | 7 pages A1–3, J1–2, K1–2 (K was built from the same source as J, so its markers read J). **Output not encrypted**. K was "Unlocked" silently: its owner restriction (assembly not allowed) was not shown to the user | as FAQ; consider a notice for restricted files | PASS / LOW |
| S7 | F (500 pages) + A | 503 pages, F1…F500, A1–A3. Add/preview 3.0 s, merge 0.34 s, 653 KB | | PASS (fast) |
| S8 | Choose pages on A: leave out p2, rotate p3 right; + B | **A1 A3(/Rotate 90) B1 B2** | correct | PASS |

**Metadata (all outputs):**
- Title = the first file's title (or "<name>-merged" fallback).
- Author kept.
- Producer and Creator = "FreeDailyPro".
- PDF 1.7.
- CreationDate in UTC.
- This matches the FAQ's "document properties name FreeDailyPro".

### P0: every page carries a visible "Created with FreeDailyPro.com" badge

- pdftotext finds the text on **every** page: S1 11/11, S5 3/3, S7 503/503. The blank page in S3 is the exception.
- Rendered, it is a dark pill with the F logo and "Created with FreeDailyPro.com" at the bottom right (`screens/live/s1-page1-01.png`).
- On rotated pages (S4 A1) the badge rotates with the page.
- **This contradicts the page's own copy:**
  - Meta description: "download a clean PDF, **with no watermark**".
  - FAQ: "Does merging add a watermark? **No.** … nothing stamped on them".
  - H3 "No upload, no watermark": "Nothing is stamped on them and **no logo or text is added**".
  - CSV short description: "…with no watermark".
- Only the cap dialog is honest: "Either pass removes the 'Created with FreeDailyPro.com' mark from your PDFs".
- Whether a pass removes it was not verified (no purchase).
- Severity HIGH: a false claim in search snippets and the FAQ, about the output customers send to clients. The owner decides whether the badge stays for trial uses; either way, the copy must match.

## 3. UI validation (no download needed; capped contexts, `json/ui-probe.json`, `json/arrange-probe.json`)

| Case | Live behaviour | Result |
|---|---|---|
| Truncated PDF, garbage, text renamed .pdf, PNG renamed .pdf, 0-byte | Each file gets its own toast: "\"X.pdf\" can't be read — it looks damaged. Try the Repair PDF tool…". Each is left out; "1 file · 3 pages"; the button reads "Add at least 2 valid PDFs to merge" (disabled) | PASS. LOW: a renamed PNG/text/empty file isn't "damaged" and Repair won't help. Say "this isn't a PDF" |
| .txt (wrong extension) | "\"notes.txt\" can't be used here. This tool takes PDF, JPG or PNG files." | PASS |
| Password file | Dialog "This PDF is password-protected… never uploaded… your result won't have a password" with Skip this file / Unlock. Wrong password → "That password didn't work — please try again." Right password → toast "Unlocked…" | PASS |
| Duplicate | Toast "\"A_a4_3p.pdf\" is already in your list — added anyway…"; card tagged "Duplicate" | PASS (matches FAQ) |
| Form file | Card note "Has form fields — they won't stay fillable once merged" | PASS |
| Page range | "2-3" OK; "5" → "Page 5 is outside this PDF's 3 pages"; "3-1" → "\"3-1\" starts after it ends"; "abc" → "isn't a valid page number"; "0" → outside; "1,1,2" accepted (pages repeated). Invalid input marks the field red and removes Merge | PASS |
| Arrange all pages | Inline grid: "Arrange all pages — 5 pages in the merged file, in this order…". Per page: Move earlier/later, Rotate left/right, Delete (all labelled), plus Start over and Done. The blank-page option shows "— not used while pages are arranged by hand" | PASS |
| Choose pages | Per-page include toggle and rotate left/right, Done; card shows "Choose pages (edited)" | PASS |
| Reload | Clears the list (no persistence). Consistent with "Closing the tab clears everything" | PASS |

## 4. Trial-use counting in the uncapped context (check 16)

- **Load:** 10 remaining.
- **Per scenario:** add files and Merge left usageToday unchanged. **Each Download spent exactly 1** (0→1→…→8).
- The result area says "**Download uses 1 trial use**" before the click. This is clear.
- Reload kept "2 remaining". "Share this tool" copied the bare URL (`https://www.freedailypro.com/tool/merge-pdf`, toast "Link copied! Share it with anyone.") and didn't change the count.
- No jumps were seen here, unlike FDP-02.
- **Capped behaviour:**
  - Merge still runs ("PDFs merged successfully!").
  - The result area shows "0 remaining today · Get a Day Pass to download".
  - Download opens the cap dialog: "Today's trial uses are done — Your input stays where it is, but downloading needs a pass… Monthly $4.99 / Day Pass $1 / access code…".
  - Not paid; stopped there.
- **Needs re-run after midnight UTC:** none for counting. The second fresh-context count trace was not attempted, to save contexts.

## 5. Sign-in-gated features (untested)

| Feature | Where | What it shows | Status |
|---|---|---|---|
| Open from Google Drive | https://www.freedailypro.com/tool/merge-pdf (drop zone) | Not clicked. It connects a Google account | **UNTESTED: needs Santosh's Google login** |
| Save to Google Drive | Result area of the same page, after Merge | Not clicked. It connects a Google account | **UNTESTED: needs Santosh's Google login** |
| Save to my cloud storage | Result area | Dialog: "Cloud storage — $4.99 per month, 1 GB… Sign in with your email first…", with Not now / Sign in | **UNTESTED** (paid add-on plus sign-in) |
| Take photo with camera | Drop zone (`capture=environment`) | Not exercised headless | UNTESTED |

## 6. Accessibility of the tool area

- The drop zone is `role=button`, `tabindex=0`; Enter and Space open the file chooser when it's focused.
- "Move up / Move down / Remove <file>" and every Arrange control have accessible names.
- **Focus falls to \<body\> after Move down and after Merge** (LOW).
- axe on the result view: `aria-allowed-role` (minor, 5): `<figure role=listitem>` in the arrange grid.
- The drag handle has no `aria-roledescription` or instructions; the arrow buttons are the keyboard path.
