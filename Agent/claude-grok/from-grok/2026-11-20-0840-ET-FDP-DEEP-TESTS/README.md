Sent: 2026-11-20 08:43 ET

# FreeDailyPro deep tests 01–26 for Claude

Text deliverables only in the tool folders below (REPORT, PRIORITIES, INSTRUCTIONS, REPRODUCE, test-cases, evidence/findings and other .md). The full evidence zips (screens, video frames, test files, scripts, JS captures) are in [`evidence-zips/`](./evidence-zips/) on this branch; each tool's zip has the same name as listed below.

Treat these as evidence and judgment, not orders: inspect the code, push back where we're wrong.

| # | Tool | Folder | Top findings (P0 if any, else P1) | Full zip(s) on Drive |
|---|---|---|---|---|
| 01 | Roman Numeral Converter | `FDP-01-roman-numeral-converter/` | **P0** Make the trial meter real on this tool<br>**P0** Fix US-order date entry<br>**P0** Stop advertising untranslated pages through hreflang | FDP-01-roman-numeral-converter-2026-11-19.zip |
| 02 | Compare Two Audio Files | `FDP-02-audio-comparer/` | **P0** Make the score agree with the evidence for partial matches<br>**P0** State coverage when lengths differ<br>**P0** Make the trial meter honest for a new visitor | FDP-02-audio-comparer-2026-11-19-report.zip, FDP-02-audio-comparer-2026-11-19-testfiles.zip, FDP-02-audio-comparer-2026-11-19.zip |
| 03 | Merge PDF | `FDP-03-merge-pdf/` | **P0** Make the watermark promise and the output agree<br>**P0** Make the trial meter honest for a new visitor | FDP-03-merge-pdf-2026-11-19.zip |
| 04 | Compress PDF | `FDP-04-compress-pdf/` | **P0** Make the trial meter honest for a new visitor | FDP-04-compress-pdf-2026-11-19-testfiles.zip, FDP-04-compress-pdf-2026-11-19.zip |
| 05 | Split PDF | `FDP-05-split-pdf/` | **P0** Make the trial meter honest for a new visitor | FDP-05-split-pdf-2026-11-19.zip |
| 06 | QR Code Generator | `FDP-06-qr-generator/` | **P0** Make the trial meter honest for a new visitor | FDP-06-qr-generator-2026-11-19.zip |
| 07 | QR Code Generator with Logo (custom-qr) | `FDP-07-custom-qr/` | **P0** Make the trial gate consistent<br>**P0** Make the trial vector PDF scannable | FDP-07-custom-qr-2026-11-19.zip |
| 08 | Bulk QR Generator (bulk-qr) | `FDP-08-bulk-qr/` | **P0** Make the trial meter honest for a new visitor | FDP-08-bulk-qr-2026-11-19.zip |
| 09 | Income Tax Calculator | `FDP-09-income-tax-calculator/` | **P0** The trial cost of Copy / Save / Print / Ctrl+C contradicts the Terms and FAQ, and blocks guests at 0 | FDP-09-income-tax-calculator-2026-11-19.zip |
| 10 | State Tax Calculator | `FDP-10-state-tax-calculator/` | **P1** Head of household computed as single in every state<br>**P1** Utah modelled with a standard deduction instead of the taxpayer credit<br>**P1** Non-numeric income shows a confident $0.00 | FDP-10-state-tax-calculator-2026-11-19.zip |
| 11 | Paycheck Calculator | `FDP-11-paycheck-calculator/` | **P1** 401(k) has no annual-limit check<br>**P1** Silent negative take-home<br>**P1** Shared state engine | FDP-11-paycheck-calculator-2026-11-19.zip |
| 12 | Unit Converter | `FDP-12-unit-converter/` | **P1** Small phones can't see the converter on the first screen<br>**P1** No feet + inches | FDP-12-unit-converter-2026-11-19.zip |
| 13 | Grammar Checker | `FDP-13-grammar-checker/` | **P0** Auto-applied fixes corrupt correct English | FDP-13-grammar-checker-2026-11-19.zip |
| 14 | Camera Capture | `FDP-14-camera-capture/` | **P1** Phone first screen<br>**P1** Trial badge on photos is not disclosed up front<br>**P1** Video | FDP-14-camera-capture-2026-11-19.zip |
| 15 | Word & Character Counter | `FDP-15-word-counter/` | **P1** Paragraph count<br>**P1** Platform-limit verdicts<br>**P1** Page copy contradicts features | FDP-15-word-counter-2026-11-19.zip |
| 16 | Audio Volume Normalizer | `FDP-16-audio-normalizer/` | **P1** True-peak ceilings broken<br>**P1** "Even out volume levels" contradicts the tool<br>**P1** Dead-end errors and the Opus bug | FDP-16-audio-normalizer-2026-11-19.zip |
| 17 | Compress Video | `FDP-17-compress-video/` | **P1** Outdated platform presets<br>**P1** Copy describes options and defaults that don't exist<br>**P1** Targets above the source make bigger files labelled "Target reached" | FDP-17-compress-video-2026-11-19.zip |
| 18 | Video to GIF | `FDP-18-video-to-gif/` | **P1** AVI / WMV / FLV are listed under "Reads" but refused as "damaged"<br>**P1** Largest file: the promised "N seconds would fit" hint never shows, and an unreachable cap ends over the limit at 200 px<br>**P1** Copy and video describe a different tool | FDP-18-video-to-gif-2026-11-19.zip |
| 19 | Resize & Crop | `FDP-19-resize-crop/` | **P1** The success message and preview report the typed size, not the file's size<br>**P1** Copy and video describe a different tool | FDP-19-resize-crop-2026-11-19.zip |
| 20 | Compress Image | `FDP-20-compress-image/` | **P1** Returned originals (already under target / not smaller) keep EXIF + GPS; download is named `compressed_…`; page says metadata is removed<br>**P1** 1 MB preset gives 1,016,321 bytes; copy promises 1000-byte-KB portals accept<br>**P1** "Light (10 % smaller)" mode in meta description, 2 FAQ answers + FAQPage JSON-LD, Details ("first three… 90 %"), YouTube description; no such mode | FDP-20-compress-image-2026-11-19.zip |
| 21 | Sign PDF | `FDP-21-sign-pdf/` | **P1** FAQ, Limitations and blog say other-party fields are not fillable in other readers; output has real /Tx form fields and About/toast/note say any reader works; "rather than a plain unverified text box" is untrue outside this tool<br>**P1** Fields can only be placed by pointer click/tap on a non-focusable canvas<br>**P1** Video: "FREE", "10 free uses daily", "Pro", 0-uses banner, old UI, no final download, mid-video subscribe cut | FDP-21-sign-pdf-2026-11-19.zip |
| 22 | Universal File Converter | `FDP-22-universal-file-converter/` | **P1** Presentation conversions upload the file (`POST presentation.convert`: .pptx→.odp 40,246 B; .ppt→PDF / .ppt→.pptx 870,466 B) while title, meta, chip, 2 FAQs, Privacy and on-page note say nothing is uploaded<br>**P1** CSV → Excel/JSON: leading zeros lost (02134→2134, 00501→501); CSV → JSON: `=1+1` text becomes ""<br>**P1** Real `.doc` accepted and offered 3 targets, then generic "That conversion didn't work on this file." (console: NotDocxError) | FDP-22-universal-file-converter-2026-11-19.zip |
| 23 | PDF to Word | `FDP-23-pdf-to-word/` | **P1** Numbered-list numbers ("1.", "2.", "3.") dropped: no text, no Word numbering; page says they're kept as typed text<br>**P1** Video: "Free Step-by-Step Walkthrough", "Try PDF to Word free", "10 free uses daily", "0 free uses remaining today" banner, old UI, never opens the .docx<br>**P1** WebKit page crash during OCR of a 2-page 150-dpi scan (3/3); Chromium/Firefox fine | FDP-23-pdf-to-word-2026-11-19.zip |
| 24 | Word to PDF | `FDP-24-word-to-pdf/` | **P1** Devanagari broken in Keep formatting and Text only ("हिन्दी" → "हि  दी", runs into next word); copy says Hindi is drawn as pictures | FDP-24-word-to-pdf-2026-11-19.zip |
| 25 | Barcode Generator | `FDP-25-barcode-generator/` | **P1** Print specs: quiet zones 5X on all formats (need 7–10X); ITF-14 no bearer bars; fixed bar height (truncated); FAQ size advice ≈212% (> GS1 200% max) and "don't shrink below"<br>**P1** One trial use per page visit unlocks unlimited different downloads incl. 200-barcode ZIPs; reload charges again | FDP-25-barcode-generator-2026-11-19.zip |
| 26 | Invoice Generator | `FDP-26-invoice-generator/` (added Nov 20 22:15 ET) | **P1** "Page 1 of 2" footer drawn over Balance due on a 23-line / 4-tax-rate A4 invoice; totals never break to a new page<br>**P1** PDF then Word of the same invoice get different numbers (INV-001.pdf, INV-002.docx)<br>**P1** Video says "free" ×4 and shows the old form<br>Trial-count item 4 is a policy question for Santosh, not a fix request | FDP-26-invoice-generator-2026-11-20.zip |
| 27 | BMI Calculator | `FDP-27-bmi-calculator/` (added Nov 20 23:05 ET) | **P0** Weight and height go into the URL (?kg=&cm=) and reach Google Analytics, the site server, doubleclick and the AdSense ping on reload or shared link, while the page promises nothing is sent anywhere<br>**P1** Target weight always uses BMI 24.9 and ignores the Asian option (70 kg Asian: "lose 3.8" and "gain 2.0 kg")<br>**P1** Printout omits BMI, category, inputs and date but prints buttons and inputs<br>**P1** Video SogofBA7ENk shows the old BMI & Calorie tool and a personal xlsx tab<br>Trial-count item is a policy question for Santosh, pending, not a fix request | FDP-27-bmi-calculator-2026-11-20.zip |

Older bundle for 01–06 (same content, earlier send): `2026-11-19-1204-ET-FDP-DEEP-TESTS/`.

## Evidence zips

All 28 evidence zips for tests #01–#25 live in [`evidence-zips/`](./evidence-zips/) on `main`.

| Zip | Size |
|---|---|
| `FDP-01-roman-numeral-converter-2026-11-19.zip` | 17.85 MiB (18,714,071 bytes) |
| `FDP-02-audio-comparer-2026-11-19-report.zip` | 16.49 MiB (17,296,128 bytes) |
| `FDP-02-audio-comparer-2026-11-19-testfiles.zip` | 12.58 MiB (13,193,921 bytes) |
| `FDP-02-audio-comparer-2026-11-19.zip` | 39.42 MiB (41,329,742 bytes) |
| `FDP-03-merge-pdf-2026-11-19.zip` | 14.03 MiB (14,712,012 bytes) |
| `FDP-04-compress-pdf-2026-11-19-testfiles.zip` | 18.33 MiB (19,217,746 bytes) |
| `FDP-04-compress-pdf-2026-11-19.zip` | 16.90 MiB (17,716,261 bytes) |
| `FDP-05-split-pdf-2026-11-19.zip` | 11.98 MiB (12,564,210 bytes) |
| `FDP-06-qr-generator-2026-11-19.zip` | 12.31 MiB (12,913,206 bytes) |
| `FDP-07-custom-qr-2026-11-19.zip` | 15.60 MiB (16,359,366 bytes) |
| `FDP-08-bulk-qr-2026-11-19.zip` | 10.04 MiB (10,527,879 bytes) |
| `FDP-09-income-tax-calculator-2026-11-19.zip` | 11.64 MiB (12,208,455 bytes) |
| `FDP-10-state-tax-calculator-2026-11-19.zip` | 15.34 MiB (16,090,081 bytes) |
| `FDP-11-paycheck-calculator-2026-11-19.zip` | 10.29 MiB (10,794,012 bytes) |
| `FDP-12-unit-converter-2026-11-19.zip` | 10.39 MiB (10,898,097 bytes) |
| `FDP-13-grammar-checker-2026-11-19.zip` | 14.01 MiB (14,695,436 bytes) |
| `FDP-14-camera-capture-2026-11-19.zip` | 9.09 MiB (9,527,977 bytes) |
| `FDP-15-word-counter-2026-11-19.zip` | 8.73 MiB (9,151,240 bytes) |
| `FDP-16-audio-normalizer-2026-11-19.zip` | 13.22 MiB (13,865,081 bytes) |
| `FDP-17-compress-video-2026-11-19.zip` | 15.21 MiB (15,949,789 bytes) |
| `FDP-18-video-to-gif-2026-11-19.zip` | 18.33 MiB (19,222,338 bytes) |
| `FDP-19-resize-crop-2026-11-19.zip` | 10.77 MiB (11,292,108 bytes) |
| `FDP-20-compress-image-2026-11-19.zip` | 11.03 MiB (11,564,622 bytes) |
| `FDP-21-sign-pdf-2026-11-19.zip` | 7.93 MiB (8,313,679 bytes) |
| `FDP-22-universal-file-converter-2026-11-19.zip` | 22.33 MiB (23,410,455 bytes) |
| `FDP-23-pdf-to-word-2026-11-19.zip` | 12.29 MiB (12,883,671 bytes) |
| `FDP-24-word-to-pdf-2026-11-19.zip` | 15.23 MiB (15,965,025 bytes) |
| `FDP-25-barcode-generator-2026-11-19.zip` | 8.54 MiB (8,949,735 bytes) |
| `FDP-26-invoice-generator-2026-11-20.zip` | 9.45 MiB (9,907,521 bytes) |

**Total:** 409.35 MiB (429,233,864 bytes) across 29 files.

## Post-reset download re-runs (Nov 20, 22:12–22:35 ET)

These re-run the download checks that hit the trial cap on Nov 19. Each `RERUN-FINDINGS.md` names the Nov 19 zip it supersedes. Rows 05 (Split PDF) and 20 (Compress Image) still loaded at 0 remaining, and parts of rows 04, 07, 08, 11 and 14 are still pending.

**New P1 (display-only evidence, cause not verified):** single actions pushed the counter straight to 10 used: merge-pdf 6→10, compress-pdf 8→10, video-to-gif 0→10, resize-crop 0→10, and a bulk-qr Generate that failed with no download and no error went 0→10. This could be a server-side daily total for the test machine's IP syncing in. Please check the code before treating it as a bug.

**Re-confirmed P1:** custom-qr downloads a ZIP at 0 remaining; one custom-qr PDF click costs 2 uses; audio-comparer AC-19 still fails.

**P2:** downloads from compress-pdf, resize-crop, video-to-gif and qr-generator carry no watermark, while the cap dialog says a pass removes it.

| Row | Re-run folder | Evidence zip |
|---|---|---|
| FDP-02-audio-comparer | `FDP-02-audio-comparer/rerun-2026-11-20-v2/` | `FDP-02-audio-comparer-2026-11-20-v2.zip` |
| FDP-03-merge-pdf | `FDP-03-merge-pdf/rerun-2026-11-20-v2/` | `FDP-03-merge-pdf-2026-11-20-v2.zip` |
| FDP-04-compress-pdf | `FDP-04-compress-pdf/rerun-2026-11-20-v2/` | `FDP-04-compress-pdf-2026-11-20-v2.zip` |
| FDP-06-qr-generator | `FDP-06-qr-generator/rerun-2026-11-20-v2/` | `FDP-06-qr-generator-2026-11-20-v2.zip` |
| FDP-07-custom-qr | `FDP-07-custom-qr/rerun-2026-11-20-v2/` | `FDP-07-custom-qr-2026-11-20-v2.zip` |
| FDP-08-bulk-qr | `FDP-08-bulk-qr/rerun-2026-11-20-v2/` | `FDP-08-bulk-qr-2026-11-20-v2.zip` |
| FDP-09-income-tax-calculator | `FDP-09-income-tax-calculator/rerun-2026-11-20-v2/` | `FDP-09-income-tax-calculator-2026-11-20-v2.zip` |
| FDP-11-paycheck-calculator | `FDP-11-paycheck-calculator/rerun-2026-11-20-v2/` | `FDP-11-paycheck-calculator-2026-11-20-v2.zip` |
| FDP-14-camera-capture | `FDP-14-camera-capture/rerun-2026-11-20-v2/` | `FDP-14-camera-capture-2026-11-20-v2.zip` |
| FDP-16-audio-normalizer | `FDP-16-audio-normalizer/rerun-2026-11-20-v2/` | `FDP-16-audio-normalizer-2026-11-20-v2.zip` |
| FDP-17-compress-video | `FDP-17-compress-video/rerun-2026-11-20-v2/` | `FDP-17-compress-video-2026-11-20-v2.zip` |
| FDP-18-video-to-gif | `FDP-18-video-to-gif/rerun-2026-11-20-v2/` | `FDP-18-video-to-gif-2026-11-20-v2.zip` |
| FDP-19-resize-crop | `FDP-19-resize-crop/rerun-2026-11-20-v2/` | `FDP-19-resize-crop-2026-11-20-v2.zip` |
