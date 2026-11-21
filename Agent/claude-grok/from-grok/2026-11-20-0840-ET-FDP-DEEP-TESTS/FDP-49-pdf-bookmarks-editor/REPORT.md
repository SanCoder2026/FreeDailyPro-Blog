Sent: 2026-11-21 07:48 ET

# FDP-49 PDF Bookmarks Editor (pdf-bookmarks-editor): deep test report for Claude

- **Written:** 2026-11-21 07:47 EST (box `date`, ET). Testing ran 2026-11-21 07:22–07:45 EST.
- **Tool:** https://www.freedailypro.com/tool/pdf-bookmarks-editor. Row 49 of TEST-ORDER.md: **Premium Application**, Publishing & Print Makers ("Scan, Convert & PDF" group), plan note "test-plan (unranked): L-243 rank 1 (PDF Toolkit API live)". No duplicate group.
  - Video: 2POndkNYCkc. Blog: /blog/edit-pdf-bookmarks-outline-tree.
  - **GSC data is not available.** The API side ("PDF Toolkit API live") was not tested (no API/MCP testing).
- **Offer:** 2 trial uses a day (Premium scope), charged at "Download PDF with new bookmarks". Loading, editing and page preview (520×672) are open. $3 Day Pass / $9.99 monthly.
  - Everything runs in the browser with pdf-lib:
    - It reads the outline into a tree you can rename, reorder, indent/outdent, delete and add to at a page number.
    - It writes a new outline with Fit destinations and PageMode UseOutlines.
    - Password PDFs are unlocked locally through the shared drop-zone dialog.
- **Testers:**
  - **Desk review:** copy, FAQ (5), Details, JSON-LD, blog, JS (PdfBookmarksEditor, pdfBookmarks, ToolPage gate).
  - **Headless Playwright:**
    - at the cap (zero.json)
    - two loads with uses left (left.json: charging and reload; left2.json: 12 functional cases)
    - Firefox/WebKit subsets
  - **Checks:**
    - 12 test PDFs (pikepdf)
    - every output inspected with `check-outputs.py` (outline tree, styles, orphaned objects, forms/links/metadata/page labels, badge)
    - a network scan for uploads
    - the matrix (10 devices, 10 locales + /ar probe, 6 geo contexts, axe)
    - the video, frame by frame
- **Constraints kept:** guest only. No sign-in, card or email. Stopped at the Day Pass email prompt and Stripe Checkout. No ad clicks, no API/MCP calls, no site or repo changes. The only password typed was the test PDF's own password.
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup); paid-pass output and limits.
  - There is no Save to Drive, cloud save, copy or print button in any state (verified live). tools.csv lists "share;save;project-file;copy;print" for this tool; only "Share this tool" (page link) renders.
- **Nothing pending a usage reset**, so there's no RERUN-AFTER-RESET row.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Push back where the product intent differs.

**Owner context:** Santosh treats per-page-load charging and full-quality results at 0 trial uses as P1 gate gaps. The "Created with FreeDailyPro.com" badge is intentional, so badge points are owner questions only.

**Code to look at:**
- **ToolPage `la()` → `logUsageNow` → `tryUse()`:** charges once per tool per page load and doesn't re-check the cap afterwards. Same root cause as FDP-44 to FDP-48.
- **`PdfBookmarksEditor-P1ChXVF9.js` `Je()`:** `r.catalog.delete("Outlines")`, then `Fe()` (write) and `r.save()`. pdf-lib's `save()` serialises every object in `context`, including the old, now unreachable outline dictionaries with their `/Title`s. Fix: collect the refs of the old tree first (walk `/First`/`/Next` from the original `/Outlines`), then `context.delete(ref)` each before saving.
- **`pdfBookmarks-BjfxtCfb.js` `T()`:** `g()` only handles array destinations. A string or name `/Dest`, or a GoTo with a named `D`, gives `null`, and URI/Launch/Named actions are ignored. `S()` writes only Title/Parent/Prev/Next/Dest/First/Last/Count; `/C`, `/F` and the sign of `/Count` are not carried.

**After you ship:**
- Rerun `scripts/pb-live.js left` (expect +1 per new PDF and the cap dialog at 2/2 without a reload).
- Rerun `pb-live.js left2`, then `check-outputs.py` on the downloads (expect "orphan outline titles: [] 0").
- Work through test-cases.md.

## Intent

An author, paralegal or report writer has a long PDF whose bookmarks are missing, messy ("Page 1", "Page 2") or partly wrong. They want a clean, navigable outline without Acrobat, and without uploading a confidential document.

The core delivers that well:
- **Editor:** a clear tree editor (rename, move, indent/outdent, delete subtree, add after the selected item with a hint that says where it goes), page preview, "Use page N for the new bookmark", Undo all, Remove all.
- **Validation:** out-of-range pages block Download with a precise message; empty titles and missing targets get warnings.
- **Robustness:** Unicode (é, 日本語, Arabic, emoji) round-trips; 300 bookmarks load in 3.5 s; a cyclic outline doesn't hang; damaged files point to Repair PDF; password PDFs unlock locally with a clear wrong-password message.
- **Preservation:** forms, links, metadata and page labels are kept. Nothing is uploaded.

What undercuts it:
- **Charging per page load:** one trial use gave 9 different PDFs.
- **"Removed" bookmarks aren't removed from the file:** the titles you deleted (or all of them, after "Remove all") are still inside the PDF you send on. For the paralegal persona, a deleted "CONFIDENTIAL – Layoff list" bookmark that is still recoverable is exactly the wrong surprise.
- **Named destinations show no page:** PDFs from LaTeX and many exporters use them for every bookmark, so those files open with every page blank and need each one re-typed.

## Why: what the evidence says

- **P1, per-page-load charging (gate gap).**
  - **left2.json:** M01 0→1. Then M02, L07, L08, L09, L10, L11, L13 and L16 all downloaded new PDFs with the counter at 1: 9 PDFs and 1 `usage.log` POST.
  - **left.json:** L01 0→1; L02 and L03 stay at 1. After a reload, L14 took it to 2/2, and **L15 then downloaded a new PDF at 2/2 with no dialog**.
  - **Firefox:** S02 was free after S01.
  - In fresh contexts at 2/2 (zero.json, WebKit), Download opens the cap dialog correctly.
- **P1, privacy: deleted bookmark titles survive in the output.**
  - **L16** (B01 → Remove all → Download; toast "Bookmarks removed in the new file"): the catalog has no `/Outlines`, but all 9 outline dictionaries are still in the file. Object 37 still holds "CONFIDENTIAL – Layoff list Q4 (delete me)", readable with pikepdf/qpdf (json/orphans.txt).
  - **The same applies elsewhere:** after deleting one bookmark (L01, L13), after Remove all on 300 bookmarks (L07: 300 titles left), and for every edited file (old titles kept beside the new ones).
  - **What users are told:** the FAQ says "Click Remove all and download. The new PDF has no outline." Viewers won't show the old titles, but anyone who opens the file with a PDF library, a forensic tool or an "extract all strings" step will see them.
- **P2 items:**
  - **Named destinations:**
    - B03 loads "Named dest sec-a" and "GoTo named sec-b" with an empty page and the warning "bookmarks have no target page…". If the user downloads without typing pages, they become dead headings (L03 output).
    - The FAQ admits this, but it's the common case for LaTeX/hyperref PDFs and some exporters. Resolving `/Names /Dests` would remove most of the manual work.
  - **URI bookmarks:** "Website link (URI)" is silently saved as a plain heading with no action. The warning only talks about a target page.
  - **Locale pages:** the H1/tool name, title, meta, section headings, "Watch: … in Action" and the video title stay English on all 10 locales. Only shared buttons are translated.
- **P3 items:**
  - **Styles and state lost:** colour, bold/italic and collapsed state are dropped (L08 vs B08); every parent saves expanded.
  - **Physical page numbers only:** B08 has page labels i–iii, then 1, so "Page 4" in the editor is printed page 1. The blog advises matching the printed contents.
  - **Subtree delete:** one click deletes a parent with all its children, with no confirm and only "Undo all".
  - **Copy and metadata:** meta 110 chars (repeats the subtitle); og-default; the video shows the old "PDF Tools" breadcrumb and "200+ tools".
  - **Layout and a11y:** iPhone SE 9 px overflow; /ja 3 px; axe label-content-name-mismatch (1), region (1), color-contrast on the ad label (1).
- **Owner questions:**
  - **No mark on outputs:** downloads carry no "Created with FreeDailyPro.com" mark, but the cap dialog sells mark removal.
  - **Owner-password PDFs:** a PDF with only an owner (permissions) password is unlocked without asking, and the restrictions are dropped (shared drop-zone behaviour).

## Outcomes we want

1. Each new PDF takes one trial use, and a re-download stays free. At the cap, the dialog shows without a reload.
2. Deleted and removed bookmarks are really gone from the output (0 orphaned outline objects).
3. Named destinations resolve to pages. Bookmarks with web links keep them, or the user is told before they're dropped.
4. Translated tool name, title, meta and strings on locale pages.
5. Optional polish: keep styles and collapsed state, show printed page labels, per-step undo.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | Rename, reorder, indent/outdent, delete, add, Remove all, password unlock, 300 bookmarks: all work; outputs correct in viewers. |
| 2 | Completeness vs competitors | PARTIAL | Compared with Acrobat Pro, PDF-XChange, jPdfBookmarks and online editors: core tree editing matches; missing named-destination resolution, URI/action bookmarks, styles/collapsed state, auto-from-headings (documented). |
| 3 | Ease of use | PASS | Clear tree, insert hint, preview, precise validation messages. One-click subtree delete. |
| 4 | Layout attractiveness | PASS (minor) | Clean two-column editor; iPhone SE 9 px overflow. |
| 5 | Payment process | PASS / stopped | Cap dialog → Day Pass $3 email prompt (stopped); Quick Buy monthly → Stripe (stopped); $3/$9.99 in all 6 geo contexts. |
| 6 | Information correct | PARTIAL | "Remove all… The new PDF has no outline" is true in viewers only (titles stay in the file); action/style loss not mentioned. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Title 65; meta 110 (repeats subtitle); five JSON-LD types; og-default; English locale titles/H1. |
| 9 | Blog exists and accurate | PASS | Accurate and practical; "match the printed contents" but the tool shows physical pages only. |
| 10 | YouTube video exists | PASS | 2POndkNYCkc embedded; VideoObject matches. |
| 11 | FAQ and guide correct | PASS (minor) | 5 accurate answers; Remove-all answer needs the file-level caveat fixed (or the bug fixed). |
| 12 | Video shows current capabilities | PASS (minor) | Current UI and "2 trial uses"; old breadcrumb "PDF Tools", "200+ tools". |
| 13 | Storage | N/A / sign-in untested | No save-to-cloud on this tool (verified live); Open from Google Drive needs sign-in. |
| 14 | Sharing | PASS | "Share this tool" only. |
| 15 | Downloads | PARTIAL (privacy P1) | Correct outline; forms/links/metadata/labels kept; deleted titles remain inside the file. |
| 16 | Usage count | **FAIL (P1)** | Per page load: 9 PDFs for one use; a new PDF at 2/2 without dialog. |
| 17 | Categorization in section | PASS | Premium Application in Publishing & Print Makers. |
| 18 | Correct section of site | PASS (suggestion) | The static HTML of /category/pdf-tools also references it (rendered listing not checked); video shows a PDF Tools breadcrumb. Keep both, decide one breadcrumb. |
| 19 | AI need/demand | PASS | L-243 rank 1; chat assistants can't rewrite a PDF's outline locally. |
| 20 | Merge better? | No | Distinct from Organize PDF / Add Page Numbers; could be offered as a next step after Merge PDF. |
| 21 | Remove? | No | Demand rank 1 in its plan list. |
| 22 | Duplicates | None | No duplicate group. |
