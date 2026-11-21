Sent: 2026-11-21 06:06 ET

# FDP-45 HTML to PDF: live functional findings (guest, 2026-11-21 05:23–05:50 EST)

**Intent:** check that a guest gets a faithful, searchable PDF from pasted or dropped HTML, that scripts never run, and that Download is gated once per result.
**Why:** this is a PDF Toolkit Professional Tool (L-243 rank 1); invoices, résumés and reports made here go straight to clients.

## Gate and trial uses (live/zero.json, live/left.json)
- **At 0 (10/10):**
  - Convert works (`gateAtDownload: !0`). "Preview first page" shows a 476×673 image of page 1.
  - Download and Save to Google Drive open the cap dialog ("Today's trial uses are done… Monthly $4.99 / Day Pass $1").
  - Save to my cloud storage opens "Sign in with your email first".
  - Day Pass → email prompt (stopped, nothing typed). Quick Buy monthly → Stripe Checkout (stopped; id redacted).
  - The status line says trial uses restart "at midnight UTC".
- **P1, per-page-load charging (gate gap):**
  - One page load, starting 0/10: L01 → 1, then **15 more downloads (L01b–L15, 13 different documents) stay at 1**.
  - After a reload, L17 → 2.
  - Same ToolPage wrapper (`vt`→`Sa`) as #44: it charges once per tool per page load, not per result.
- **Charging policy:** Download takes a trial use, so there's no uncounted-tool policy question.

## Conversion (live/downloads, checked with poppler/pikepdf; previews in live/previews)
| Case | Result |
|---|---|
| L01 sample | PASS. A4, 1 page; image 1360 px wide (about 190 dpi) plus an invisible Helvetica text layer; badge (a link to freedailypro.com) on every page. |
| L02 invoice (80 rows, style block, data-URL logo, external image, links) | PASS on looks. 3 pages, rows not sliced, external Wikimedia image loaded, mailto/https links clickable, `javascript:` not linked. **P2:** `href="#top"` became a link to `https://www.freedailypro.com/tool/html-to-pdf#top` (relative links resolve against the FDP page). **P3:** the table header doesn't repeat on page 2. 919 KB for 3 pages. |
| L03 page-break-before on the first section | **P2:** 5 pages, and **page 1 is blank** (only the badge). Sections 1–4 then each get their own page. |
| L04 script / onerror / noscript / form | PASS. SCRIPT-RAN and ONERROR markers absent. The noscript text and form field appear in the picture but not in the text layer (minor). |
| L05 meta refresh to example.com | PASS. Ignored; the page's own text converts. |
| L06 mixed scripts | PASS as documented. All scripts render in the picture, emoji included. The text layer covers only Western European words, so Łukasz/Żółć/₹, Greek, Cyrillic, CJK, Arabic and Hindi aren't searchable, as the FAQ says. |
| L07 2400 px wide table | Scaled into 1 portrait page, with text too small to read and no warning (P3; copy says it scales). |
| L08 9,000 paragraphs | PASS. "This document is longer than 200 pages — split it and convert in parts" in 1.5 s. |
| L09 windows-1252 .html | **P2:** the dropped file is read as UTF-8, so the box and the PDF show "Caf� cr�me � �quoted� �5". These words then drop out of the text layer. |
| L10 .htm, Letter + Landscape + margin 0 + page numbers | PASS. 792×612, "Page 1 of 1". |
| L11 .txt drop | PASS. "“H11_notes.txt” can't be used here. This tool takes .html and .htm files." The previous content is kept. |
| L12 Legal + margin 50, 2000 px image | PASS. 612×1008, 3 pages; a tall image is sliced only where it can't fit. |
| L13 relative image/stylesheet | Relative URLs resolve to freedailypro.com (favicon loaded). Expected, but undocumented. |
| L14 Google Fonts stylesheet | PASS. The Lobster webfont rendered. |
| L15 margin 99 | Clamped to 50 (field shows 50); 6 pages with page numbers. |
| L16 empty box | PASS. Convert disabled; "Paste some HTML or drop a .html file to enable Convert." |

- **P2, file name sticks to the first document's title:** after the invoice (`<title>Invoice INV-2026-045`), the next five documents (Breaks, Script test, Refresh, Scripts, Wide) all downloaded as **"Invoice INV-2026-045.pdf"**. After a dropped H10_resume.htm, the next five downloads were all "H10_resume.pdf". The name is only replaced while it is still "document". The PDF Title metadata is right each time. Someone converting several invoices can send the wrong file name to a client.
- **P1, WebKit hang (hang-webkit.json, subset-webkit.json):**
  - H02 with one external image never finishes in WebKit (120 s and 305 s runs, "Rendering page 1 of 3").
  - **Stop doesn't return control** (after 8 s: still rendering, no Convert button).
  - In the subset run, the stuck page then blocked the later cases (Convert never came back).
  - Without the external image (H02b) it converts in 5.9 s.
  - Console: only the sandbox script-blocking notice; no error surfaced to the user.
  - Chromium and Firefox finish H02 in about 2 s.
- **Cross-engine:** Firefox matches Chromium (sample, invoice, scripts, mixed scripts; >200-page error shown, toast not captured).
- **Privacy:** across a whole session, no request body or URL carried document text (no hits for INV-2026-045, Müller, Jane Doe or the script markers). Only resources the HTML links to were fetched, from their own hosts, as disclosed.
- **Keyboard:** Tab reaches the HTML textarea and then the drop zone; Enter opens the chooser.
