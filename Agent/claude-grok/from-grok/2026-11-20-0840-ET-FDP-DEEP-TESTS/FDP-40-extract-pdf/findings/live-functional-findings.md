Sent: 2026-11-21 03:27 ET

# FDP-40 Extract Pages & Text: live functional findings (guest, headless Playwright, 2026-11-21 03:06–03:21 EST)

Raw: `evidence/json/probe.json`, `gate.json`, `cases-chromium-VK.json`, `cases-firefox-K.json`, `privacy.json`, `corrupt.json`. Counters are `fdp-usage-v1.usageToday` (display-only evidence).

## Counting with uses left (probe, 03:06 EST: the only context that loaded with uses left)
- Load E01, Extract Text (page 1, the default): 0 → **0**. "Text extracted"; the full text appears in a read-only textarea with Copy, Download Text File, Save to Google Drive, Save to my cloud storage.
- Copy: 0 → **1** (`usage.log` request; clipboard got the text). The code wraps Copy in `gateShare` (`ExtractPdf-C5BRKXT9.pretty.js` `G`).
- **Pending (RERUN-AFTER-RESET row 40):** per-page-load behaviour of Download/Copy. After the probe, 22 fresh contexts (03:07–03:20 EST) all loaded at "0 remaining today", so the A/A2/B/C/D/E sequence (`ex-gate.js` part 1) could not run. The page-output download checks (`ex-live.js V`, `verify.py`) are also pending.

## At 0 trial uses (03:09–03:10 EST)
- **P1, full text at 0:** with the strip at "0 remaining today", Extract Text with an empty box returned all 8 pages (2,210 chars) in the read-only textarea; the count stayed at 10.
  - Click in the box, Ctrl+A, Ctrl+C put all 2,210 chars on the clipboard, including "PAGE-8 MARKER" (`manualCopy`).
  - The Copy button and Download Text File both opened the cap dialog ("Today's trial uses are done … downloading needs a pass"), and the clipboard stayed "EMPTY".
  - Under the Oct 30 rule (copy and results count as trial uses), the text product is fully delivered for free and the gate only blocks the convenience buttons.
- **Pages mode at 0 (PASS, not a leak):**
  - P03 "37" → "1 page extracted"; Download PDF → cap dialog.
  - The only on-screen preview is "Preview first page" at 489×633 JPEG (scale 0.8) of the first output page, and thumbnails are 244×316. Neither delivers the PDF.
- **Payment and keyboard:**
  - Cap dialog → Buy Day Pass → "Day Pass, $1 | Enter your email…": stopped.
  - Quick Buy day → the same email prompt. Quick Buy monthly → Stripe Checkout (session id redacted): stopped.
  - 28 Tabs reach Quick Buy, then the drop zone; Enter opens the file chooser.

## Live cases (Chromium; no paid downloads)
| Case | Input | Result |
|---|---|---|
| V1 | E01 "5,1,3" | 3 pages extracted. The output's first page is PAGE-5 with the "Jane Roe" field and checkbox (`evidence/screens/preview-order-grid.png`), so typed order is honoured on page 1 of the output. |
| V2 | "2,2" | "2 pages extracted" while the counter says "1 page selected" (P3 counter wording). |
| V3 | "6-" | 3 pages (6–8); output starts with PAGE-6. |
| V4/V5 | Odd / Even buttons | Box 1,3,5,7 / 2,4,6,8; outputs start with PAGE-1 / PAGE-2. |
| V6 | P01 "1; 3" | 2 pages; semicolons accepted. |
| K16 | "1,,3;;5 , 7" | 4 pages; tolerant parsing. |
| K01/K03 | "9" / "0" | "Page 9 is outside this PDF's 8 pages" / "Page 0 is outside…". The counter still says "1 page selected" (stale). |
| K02/K04 | "3-1" / "abc" | ""3-1" starts after it ends" / ""abc" isn't a valid page number". |
| K05 | Pages, empty | "Choose at least one page…" (as the FAQ says). |
| **K06** | **Text, default** | **Only page 1 (227 chars).** The box is pre-filled with "1" on load. The How-to says "the selectable text of the pages you choose (all of them by default)". Users get 1 of 8 pages without noticing (P2). |
| K07/V7 | Text, empty box / Select all | All 8 pages, 2,210 chars. `--- Page N ---` markers, table rows tab-separated (`Item\tQty\tPrice`), form values ("Name: Jane Roe", "Agree: ☒"), running header and page numbers kept, as documented. |
| V8 | C05 two columns | Left column read before the right (as documented); some line breaks mid-paragraph. |
| K15 | Unicode | Accents, €, Cyrillic, Greek intact. |
| K08 | Scanned, text mode | "No selectable text on these pages: this looks like a scanned image. Run it through OCR PDF first… Open OCR PDF". |
| K09 | Scanned, pages mode | Extracts fine (pages don't need text). |
| K10 | U01 AES (old123) | The shared unlock dialog → text extracted (184 chars). The Limitations say "A password-protected PDF cannot be opened for either mode" (P3, stale copy). |
| K12/K13 | corrupt / renamed text | Toast "can't be read — it looks damaged. Try the Repair PDF tool…" (`corrupt.json`). |
| K14 | 50 pages, text all | 2,880 chars in about 3.9 s. |

- **Firefox** (K cases, finished 03:24 EST): all 16 cases match Chromium exactly: same error messages (K01–K05, K08), same text lengths (227 / 2210 / 184 / 2880 / 209 chars), the same tolerant parsing (K16 gives 4 pages). PASS.
- **Privacy** (U01 unlocked text, then E01 all-pages text): 248 requests, 13.9 KB of POST bodies total (analytics/ads/usage). No request carried %PDF, extracted text, form values, file names or the password. Storage and cookies are clean. Share copies only the tool URL. Nothing is restored after a reload.
