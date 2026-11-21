Sent: 2026-11-21 03:55 ET

# FDP-41 OCR PDF: live functional findings (guest, 2026-11-21 03:29–03:50 EST)

Raw data in `evidence/json/`: `probe.json`, `gate-12.json` (+ gate.log), `cases-chromium-V.json`, `cases-chromium-W.json`, `cases-chromium-K.json`, `cases-firefox-K.json`, `webkit.json`, `privacy.json`, `handoff.json`, `verify-all.json`, `verify-W.json`. The counter is `fdp-usage-v1.usageToday` in localStorage, which is display-only evidence.

## Gate and trial uses
- **P1: per-page-load charging (confirmed).** Run `gate-12.json` → `left` started 03:31 EST with 10 uses left.
  - Page load and two reloads: 0 → 0. Dropping the file: no change. Make Searchable: no change. Preview first page: no change.
  - The first Download cost 1 use (0 → 1). The second Download of the same result stayed at 1. A new file in the same load (S02, 3 pages) also downloaded at 1.
  - `cases-chromium-V.json` (03:36–03:38 EST) shows it at scale. One page load downloaded **14 different searchable PDFs** (V01–V13, including a 12-page file), all for 1 trial use. After a reload the next Download cost 1 more use (V14: 1 → 2), and the following one in that load was free again (V15: 2 → 2).
  - `cases-chromium-W.json` (03:41–03:43 EST) repeated it: 11 downloads in one load, 0 → 1.
  - Same pattern as #35–40: the shared once-per-load set `Kt` (`evidence/js/index-B1CTyGtY.excerpt-usage.js`) behind the shared Download button (`ToolPage` export `D`).
- **At 0 trial uses (`gate-12.json` → `zero`, 03:33–03:36 EST):**
  - Make Searchable still runs the whole OCR and reports "Recognised 36 words on 1 page." The counter stays at 10.
  - The only visual is "Preview first page": a 489×633 image of the original scan with no text layer. **That isn't a full-quality result: PASS.**
  - Download, Save to Google Drive and Continue with Compress PDF → Compress Download all open the cap dialog "Today's trial uses are done". Continue with Compress PDF hands the OCR result over ("Use the result from OCR PDF: searchable_S01…"), but Compress's Download is gated too (`handoff.json`).
  - Save to my cloud storage opens the "Cloud storage… Sign in with your email first" dialog.
  - Day Pass (from the cap dialog and Quick Buy) stops at the "Enter your email" prompt. Monthly Quick Buy goes to Stripe Checkout (session id redacted). I typed nothing.
- **Make Searchable never takes a trial use.** The OCR work itself is free and the PDF is charged at Download. Under the Oct 30 rule (results count) the Download is the result, so this follows policy. Flagged for awareness only.

## OCR quality (downloads checked by `testfiles/verify.py`; ground truth in `testfiles/truth.json`)
| Case | Input | Settings | Words recalled | Notes |
|---|---|---|---|---|
| W/V01, gate-A | Clean English invoice, 150 dpi | English, As scanned | 100% | Page unchanged visually (diff 0.0); badge added (intentional) |
| V02, gate-B | Scan / real text / scan, 3 pages | English | 100% | Real-text page 2 left untouched; "Recognised 48 words on 2 pages" |
| V03 | Sideways (90°) | Detect automatically | 100% | Turned upright; notice says so. **PASS** |
| V04 | Sideways (90°) | Turn 90° clockwise | 100% | **PASS** |
| W01 | Spanish | Spanish | 100% | Accents kept (año, Muñoz) |
| W02 | Spanish | English (default) | 71% | Accents lost ("Descripcién", "Ano"); expected with the wrong language |
| W03 | German | German | 100% | ß, ü, ö kept |
| W04 | English + Hindi | English + Hindi | 77% | **P2:** the Hindi text layer drops the reph/half forms: "मार्च" → "माच", "शर्मा" → "शम". Searching for those words fails. |
| W05 | English + Hindi | English | 45% | Hindi comes out as Latin junk ("feperan efi arf"); expected with the wrong language |
| W06 | 72 dpi, blurred and noisy | English | 75% | Expected for the quality |
| W07 | 12 pages | English | 100% | 7.4 s total |
| W08 | Monospace price table | English | 38% | **P2:** the QTY/PRICE number columns are missing from the text layer ("ITEM Widget A Widget B Cable 4"). The page's own next step is "PDF to Excel — extract the table data from the now-searchable PDF", so that bundle fails on this sample. |
| W09 | Upside-down | Turn 180° first | 100% | **PASS** |
| W10 | English page | French chosen | 100% | |
| V12 | Upside-down | Detect automatically | 100% text | **P2:** turned 270°, not 180°. The output page is **sideways** (`/Rotate 270`) while the notice says "turned 270° clockwise so it reads upright" (`live/renders/output-orientation-V03-V05-V12.png`). |

## P1: the orientation and language choices carry over to the next file
- V04 set "Turn 90° clockwise first". After **New**, V05–V11 loaded upright files without touching the menus, and the tool kept "Turn 90°".
  - Every one of those downloads came out **sideways** (`/Rotate 90`, page size swapped). Each notice said "Page 1 was turned 90° clockwise so it reads upright", and V10 said "12 pages were turned so they read upright".
  - Recall also fell (62–86%), because the upright pages were read sideways.
- Language carries over the same way. V07 set English + Hindi and V08 inherited it.
- Code: `OcrPdf-BJ90unSe.pretty.js`. The New handler resets file, result and messages but not `N` (orientation) or `C` (language). The loader `_` doesn't reset them either.
- **Why P1:** the tool promises "looks pixel-identical… nothing changes visually", and this silently rotates a correctly oriented scan in a common flow (one sideways page, then the rest of a batch). The notice then says the opposite of what happened.

## Messages and edge cases (Chromium K and Firefox K: identical results)
- Already searchable (P02): "This PDF is already searchable — every page has real text, so nothing needed OCR." No file. PASS.
- **P2: a scan with a small digital footer** (S04: an image page plus "Page 1 of 1" text, as scanner software or Bates stamping adds) is reported as "already searchable", and nothing is OCR'd.
  - Code: any page with ≥3 characters of text is skipped (`operations-B4LtHhm8.js`, `ocrPdf`/`Wn`).
  - Competitors offer "force OCR" or "skip pages with text only when they are fully text".
- Blank scan (S08): "The text read from 1 page was not usable… may be sideways or upside down…". P3: misleading for a blank page; say "no text found".
- Sideways or upside-down with As scanned (K06/K07): the same "not usable… Choose a page orientation above (or 'Detect automatically')" message. Good guidance.
- Damaged or renamed PDFs (P06/P07): toast "can't be read — it looks damaged. Try the Repair PDF tool". PASS.
- Password PDF (S13, AES-256): unlock dialog → password → OCR → download without a password, 100% recall. PASS. Cancel leaves no file (K05).
- Stop (K09, 12 pages): a Stop button appears, and pressing it returns to Make Searchable with no download. PASS.
- **P3: progress label.** The per-page % always says "Reading page 1 of N… NN%" after page 1, because the engine's progress callback captures page 1 (`startOcrEngine` is created once with `x` = 1). Seen in V10/W07: "Reading page 1 of 12… 27%" after page 6.
- Speed: 1 page takes about 2.2–3.3 s after the engine is cached; 12 pages take 7.4–10.4 s (Chromium, box).

## Browsers
- Chromium: everything above.
- Firefox K (03:41–03:43 EST): 11/11 identical to Chromium. PASS.
- **WebKit (Playwright's Linux build, not real Safari): the page crashed on Make Searchable** for both Desktop WebKit and iPhone 14 Pro Max emulation (`webkit.json`, 03:49–03:50 EST; also K02 in `cases-K-wk.log`). Loading and the "already searchable" path (no OCR) worked.
  - OCR loads `tesseract-core-relaxedsimd-lstm.wasm.js` from jsDelivr.
  - This is **unverified on a real iPhone/Mac Safari**. Check it on a device before treating it as a defect.

## Privacy
- After the file is dropped, the only requests are www.freedailypro.com (5 GET + 1 small POST, under 1 KB) and cdn.jsdelivr.net (3 GET: tesseract.js worker, core wasm, eng.traineddata). No request carried the file name or recognised words (`privacy.json`). PASS.
- The Privacy section names jsDelivr accurately.
