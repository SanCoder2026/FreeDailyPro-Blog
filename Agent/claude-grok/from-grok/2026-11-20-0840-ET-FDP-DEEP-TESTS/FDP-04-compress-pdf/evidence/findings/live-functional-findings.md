Sent: 2026-11-20 08:40 ET

# Compress PDF: live functional findings

- **Written:** 2026-11-19 11:19:38 EST (box `date`, ET).
- **Method:** headless Chromium 159 (Playwright 1.65.1), fresh contexts only, guest, no sign-in, no ad clicks, nothing typed into payment or email fields.
- **Inputs:** 17 generated files (`testfiles/`, `scripts/make-testpdfs.py`).
- **Raw evidence:** `json/probe.json`, `capped.json`, `ui-dump.json`, `explore-*.json`, `battery-*.json`, `capped2.json`, `kbd.json`.

## 1. Trial uses: starting count (check 16)

| Time (EST) | Script | Fresh contexts | Strip on load | localStorage `fdp-usage-v1` |
|---|---|---|---|---|
| 10:58:12 | cp-probe | 1 | 0 remaining today | usageToday 10, allowed false, scope dev:… |
| 10:58:39, 10:58:56 | cp-capped ×2 | 2 | 0 remaining | 10 |
| 11:00:26 | cp-explore | 1 | 0 remaining | 10 |
| 11:07:18–11:07:43 | cp-battery (6 tries) | 6 | **all 0 remaining** | 10 |
| 11:08:05 | cp-capped2 | 1 | 0 remaining | — |
| 11:18:02 | cp-kbd | 1 | 0 remaining | — |
| 11:22:43–11:22:53 | cp-battery, WebKit (3 tries) | 3 | **all 0 remaining** | 10 |
| 11:09–11:21 | run-matrix (page load only) | 16 | **3 at 10 remaining** (iPhone SE, iPhone 14 Pro Max, geo ja-JP), 13 at 0 | — |

- **28 of 31 fresh contexts loaded at "0 remaining today"** (all 15 scripted contexts whose strip was recorded; 13 of 16 matrix ones). This is display-only evidence from one busy box IP; the same pattern was seen in FDP-02 and FDP-03.
- The 3 uncapped ones were matrix page loads, where no action was taken.
- I stopped after 6 Chromium and 3 WebKit battery attempts to avoid burning contexts.
- **Everything that needs a download is marked "needs re-run after midnight UTC" (7:00 PM ET):** per-download counting, output structure (text, links, bookmarks, forms, rotation), the watermark mark, the batch ZIP, and true byte size vs. target.
- Script ready: `node scripts/cp-battery.js 6`.

## 2. What is gated, and where (capped context; display-only)

- **Add, the size breakdown, Compress (all modes), Run anyway, Compare and the batch are all free.** Capped contexts ran every compression; the strip and `usageToday` stayed at 10. `usage.check` was called only when results rendered (`capped.json` usageReq).
- **Download is gated.** Each level row and the top button show "0 remaining today · Get a Day Pass to download". Clicking Download opened the cap dialog:

  > "Today's trial uses are done | Your input stays where it is, but downloading needs a pass. You've used today's 10 trial uses. Monthly for $4.99… Day Pass for $1… Either pass removes the **'Created with FreeDailyPro.com' mark** from your PDFs and images."

  So trial-use downloads carry the mark (as in merge-pdf). Unlike merge-pdf, this page does **not** claim "no watermark". It just never mentions the mark before download (MEDIUM: disclose next to Download).
- **Several files:** "Up to 5 files… counts as one use when you download". A 6th file gets the toast "1 file left out. A batch takes up to 5 files on the trial. A paid plan removes that limit."
- **Quick Buy:**
  - $1 opens "Day Pass, $1 | Enter your email and go straight to payment… Continue to payment" (stopped; typed nothing).
  - $4.99 goes straight to checkout.stripe.com ("Stripe Checkout") (stopped).
  - Same inconsistency as FDP-02 (`screens/live/quickbuy-*.png`).

## 3. Compression results (compress only; sizes as shown by the tool)

| Input | Mode | Levels shown | Final | Time | Verdict |
|---|---|---|---|---|---|
| A photos 6p, 18.04 MB | Balanced | L1 1.34 MB (93%), L2 326.8 KB (98%), text selectable | 326.8 KB | 4.6 s | PASS |
| A | Aggressive | stopped after L2: "already 98% smaller, next levels would turn pages into pictures…" | 326.8 KB | 6.1 s | PASS (sensible; Run anyway offered) |
| A | Extreme | same stop, then **Run anyway** → L3 "Photo and shaded areas at 70 dpi" 214.7 KB, pages are pictures | 214.7 KB | 12.2 s | **PARTIAL:** no grey or B/W level and no note why it stopped (`extreme-runanyway-crop.jpg`) |
| A | Target 1 MB | L2 1002.6 KB, "under your 1.00 MB target" | 1002.6 KB | 4.6 s | PASS (if KB = 1024, that is 1,026,662 bytes, **over a decimal 1,000,000-byte limit**; verify bytes after re-run) |
| A | Target 200 KB | L2 193.7 KB | 193.7 KB | 4.6 s | PASS |
| A | Target 20 KB, Balanced only | 48.7 KB, "Couldn't reach your 20.0 KB target… Only the Balanced steps were allowed… Choose Go as far as Aggressive or Extreme" | 48.7 KB | 6.1 s | PASS (excellent message) |
| B text 5p, 5.9 KB | Balanced / Aggressive | L1 "Tidy the file" 4.5 KB (24%), "Only the file's structure was tidied"; Aggressive "heavier levels… none came out smaller" | 4.5 KB | 1.5 s | PASS |
| B | Target 2 KB | "Couldn't reach… included the Extreme steps… about 409 B for each page" | 4.5 KB | 1.6 s | PASS |
| B | Target 2 MB (default) | "Your file is 5.9 KB, already under 2.00 MB. No compression needed." | — | — | PASS |
| C scan grey 4p, 3.60 MB | Balanced / Extreme | 282 KB → 60.3 KB (98%) | 60.3 KB | 4.7 s | PASS |
| D links/bookmarks/form 3p, 3.94 MB | Balanced | 634 KB → 58.4 KB (99%), "links, bookmarks and form fields are untouched" | 58.4 KB | 1.6 s | claim **unverified** (needs a download) |
| F owner-restricted 2p | Balanced | 2.95 MB → 40.7 KB; **no notice of the restriction** | 40.7 KB | 1.5 s | LOW |
| G non-Latin 2p | Balanced | 3.66 MB → 63.1 KB | 63.1 KB | 1.5 s | text extraction unverified |
| H mixed sizes, rotated p2 | Balanced | 3.53 MB → 65.3 KB | 65.3 KB | 1.5 s | sizes and rotation unverified |
| **I CMYK photos 2p, 10.26 MB** | Balanced | **no levels**: "This PDF is a scan that is already compressed: its pages are stored as scanner pictures (JBIG2 or JPEG 2000)… nothing was changed", plus "Try Aggressive" | unchanged | 1.5 s | **FAIL (wrong diagnosis)**: they are CMYK JPEG photos, and the breakdown above says "Balanced should shrink it a lot" (`cmyk-misdiagnosis-crop.png`) |
| K already small 3p, 107 KB | Balanced | 97.2 KB → 21.7 KB (80%) | 21.7 KB | 1.5 s | PASS |
| **J big 24p, 72.08 MB** | Balanced | 5.35 MB → 1.29 MB (98%) | 1.29 MB | **18.3 s** | PASS (over 50 MB, no crash, desktop) |
| Batch: A, B, C, I, G | Balanced | per file: 326.8 KB, 4.5 KB, 60.3 KB, **10.26 MB (unchanged)**, 63.1 KB; "5 of 5 done. 35.57 MB to 10.71 MB in total"; Download all (ZIP), Run again, Continue with Merge PDF, Clear | — | 9.4 s | PASS (ZIP not downloadable while capped) |

## 4. Input validation (no download needed)

| Input | Result | Verdict |
|---|---|---|
| L truncated / M garbage / N text renamed / O PNG renamed / P empty (.pdf) | All: '"X.pdf" can't be read — it looks damaged. Try the Repair PDF tool, then add the repaired file.' | PASS for damaged. **LOW** for N, O, P (not a PDF, or empty: "Repair" is misleading) |
| Q_image.jpg | "can't be used here. This tool takes .pdf files." | PASS (could point to JPG to PDF) |
| E password | Dialog "This PDF is password-protected… unlocked right here in your browser… your result won't have a password." Cancel / Unlock (single), Skip this file (batch) | PASS (wrong-password path not exercised in a capped context; it is in cp-battery S7) |
| Target 0 / −5 / empty / abc | Pressing Compress shows the toast "Enter a valid target size"; nothing runs. The field gets no aria-invalid or inline message (`target-invalid.json`) | PASS (LOW: inline error) |
| 6 files in batch | "1 file left out…" | PASS |

## 5. Result view layout (check 4): HIGH

- **Level rows don't wrap.** Each row puts the label, Compare, Download, the cap note (when capped), Save to Google Drive and Save to my cloud storage on one line.
  - **Desktop 1366 px:** the "Level 1: Pictures inside made smaller…" label is squeezed into a **48 px column** (one word per line, about 110 px tall) (`desktop-level-rows-crop.png`, `kbd.json` levelRowWidths).
  - **Pixel 7 (412 px):** after Compress the page widens to **958 px** (`scrollWidth` 958). The label is crushed and "Compare" overlaps the label text (`phone-level-rows-crop.jpg`, `phone-result-view.jpg`).
- Seen in capped contexts, where the "0 remaining today · Get a Day Pass" note adds width. The four buttons alone still exceed a phone width, so the fix applies either way.
- The top summary ("18.04 MB → 326.8 KB (98% smaller)"), the toast and the polite live region read well.

## 6. Keyboard and a11y (check 15)

- The drop zone has tabindex 0, and Enter opens the chooser ✔.
- Mode buttons expose aria-pressed and work with Enter ✔.
- The target input is labelled by `<label for>` "Target size" ✔. Preset chips: 500 KB, 1, 2, 5, 10 MB ✔.
- **Focus falls to \<body\> after a file is added and after Compress** (LOW).
- Live regions: "Compressed: 18.04 MB → 326.8 KB" and the step announcer ✔.
- Compare images have alt "Original, page 1" / "Compressed, page 1" ✔.
- axe on the result view (main): **0 violations**.

## 7. Sign-in-gated features (not tested)

All on https://www.freedailypro.com/tool/compress-pdf:
- **Open from Google Drive** and **Save to Google Drive:** a Google account. Not clicked.
- **Save to my cloud storage:** dialog "Cloud storage | Add cloud storage, $4.99 per month, 1 GB… Sign in with your email first… Not now | Sign in". Closed with Not now.
