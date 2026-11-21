Sent: 2026-11-21 11:31 ET

# FDP-57 Document Assembler (document-assembler): deep test report for Claude

- **Written:** 2026-11-21 11:30 EST (box `date`, ET). Testing ran 2026-11-21 10:59–11:28 EST.
- **Tool:** https://www.freedailypro.com/tool/document-assembler
  - TEST-ORDER row 57: **Premium Application**, PDF Tools.
  - Plan note: "test-plan (unranked): L-243 PDF Toolkit". Duplicate group C10 (merge-pdf, mail-merge-pdf).
  - Video: Lp5L3YhS8-w. Blogs: /blog/document-assembler and /blog/edition-ledger-and-print-and-web-pdfs-for-a-catalog-series (the second is a catalog post).
  - **GSC data is not available.** No API/MCP testing.
- **Offer:** Premium, 2 trial uses a day, $3 Day Pass / $9.99 monthly.
  - Assembling is free. The charge is at **Download** (`gateAtDownload`). Save to Google Drive and Save project are gated the same way at the cap.
  - Trial PDFs carry the intentional "Created with FreeDailyPro.com" badge, linked to freedailypro.com, on every page.
- **How it works:** pdf-lib in the browser.
  - PDF pages are embedded as vector pages (text stays searchable) and fitted to the chosen size.
  - .docx and .txt go through a local converter; PNG/JPEG are placed on A4 first.
  - It adds a cover (Literata font), a clickable TOC, an optional List of Images and one bookmark per section, with the file's own bookmarks nested.
- **Test files:** built by `make57.py`:
  - PDFs: Letter 3p with a web link and outline, A4 landscape, rotated, a filled form, 60 pages.
  - Text and Word: .docx with bold/italic, bullets, table, image, Unicode and 2 pages; UTF-8 and cp1252 .txt; empty .txt; fake .docx; .doc.
  - Images: EXIF-6 JPEG, 4000×1000 transparent PNG, 50 px PNG, .webp, renamed text as .png.
  - damaged.pdf and password_u123.pdf (from FDP-52).
- **Testers:**
  - Desk: copy (9 FAQs, How-to, Limitations, Privacy), JSON-LD, blog, JS (`DocumentAssembler`, `bookAssembly`, `ProjectBar`, `useProject`).
  - Playwright:
    - Probe at the cap (Chromium): validation, bad files, project buttons, assemble, preview, Download, Save to Drive, cloud, Save project, Quick Buy.
    - Password flow (Skip, wrong password, u123).
    - One Firefox context with uses left (left-firefox.json).
    - Cases C1–C3: **not run**. All 51 fresh contexts for the cases run loaded at 2/2 (Firefox 27, Chromium 12, WebKit 12).
  - Outputs: pdfinfo, pdffonts, pdftotext, pikepdf (outline, links, boxes), renders and crops reviewed by eye.
  - Video checked frame by frame. Matrix: 10 devices, 10 locales plus /ar, 6 geo contexts, axe.
  - **Visual findings were checked against the screenshots.**
- **Constraints kept:**
  - Guest only. No sign-in, card or email.
  - Stopped at the Day Pass email field and at Stripe Checkout.
  - No ad clicks.
  - Closed only the Google popup I opened.
  - Typed only the test PDF's own password.
- **Sign-in (untested):** Open from Google Drive (Google sign-in popup verified, closed); Save to Google Drive (cap dialog at 0, sign-in expected with uses); Save to my cloud storage (email sign-in + $4.99 add-on); paid-pass output.
- **RERUN-AFTER-RESET:** yes, a row in `/workspace/deep/RERUN-AFTER-RESET.md` (#57). Trial uses reset at midnight UTC (7:00 PM ET).
  - Pending: cases C1–C3 (mixed full set; A4 plain; 6×9 trim with 60 pages, reorder and a Unicode title).
  - Also pending: a second per-load trace with different files, and whether Save project charges when uses are left.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders.

**Owner context:** per-page-load charging is a P1 gate gap. Copy and results count as trial uses.

**Where to look:**
1. **Per-page-load gate (P1).** left-firefox.json, one fresh Firefox context at 0/2:
   - L01: Assemble, then Download. The counter went **0/2 → 2/2** with one `usage.log` POST (11:06:17 EST), and the file downloaded.
   - L01b: Download again. Free (fine).
   - L02: same page, retitled to "Left Packet Two", re-assembled and downloaded at **2/2** with **no cap dialog and no POST**. A new document, delivered free.
   - After a reload (L03), Download at 2/2 opened the cap dialog, as it should.
   - Same root cause as FDP-44–47, -54 and -55: the gate is checked once per load.
   - L02 changed only the title. The planned C1–C3 run (three different file sets in one load) is pending a reset.
2. **0→2 jump on the first download.** One download moved the counter from 0/2 to 2/2. This is display-only evidence: no backend claim, and it matches the "first download 0→10 jump" seen on #18/#19 v2.
   - For a guest it looks like one download used both Premium trial uses. Worth checking `usage.log` / `usage.check` for Premium scope (`…:premium`) after the reset.
3. **Video promises the wrong offer (P2).**
   - The title and description say "Free Step-by-Step Walkthrough" and "Try Document Assembler free". The thumbnail says "FREE · PRIVATE · NO LOGIN". The end card says "200+ Free Productivity Tools".
   - On-screen chips and captions say **"10 free uses daily"** and "Pro". Today it's **Premium, 2/day, $3/$9.99**.
   - The old light UI shows no project bar and no Drive or cloud buttons.
4. **Hindi in .docx breaks (P3).** "हिन्दी" renders as broken clusters on the docx page (crop-L01-docx-p1.png). Japanese, Greek and Russian are fine.
5. **Copy vs behaviour (P3):**
   - The Tips say front pages "are numbered with roman numerals". The cover and TOC pages have **no** page number and there are no /PageLabels. The main content correctly starts at 1, and TOC numbers match the footers.
   - Limitations says "A file that cannot be read stops the whole assembly with an error naming it". A renamed text file as .png gives just "could not be read", with no name.
   - The blog says "Each assembly counts toward your 2 trial usages". Only Download counts, and assembling is free.
   - The blog says "check the preview". The preview is the first page only.
6. **Save project is gated at the cap (policy question).** At 2/2, "Save project" (the user's own project file) opens the "downloading needs a pass" dialog, so a guest at 0 can't save their work. Whether it charges with uses left is pending.
7. **Event project bar on a generic tool (P3).** "Add pages from my project: Agenda / Guest list / Budget summary" and "Try a sample" load an event-planning project (guest names). That's confusing on a document packet tool. Hide it unless a project is open.

**After you ship:** rerun `px57-live.js left firefox` (L02 should open the cap dialog or charge) and `cases` (C1–C3).

## Intent

Someone sending one tidy packet (onboarding, board pack, application) has PDFs, Word files and images. They need them in order, on one page size, with a cover, a contents page that matches the page numbers, and bookmarks, without uploading client files.

## What works (verified)

- **Assembly** (L01, 8 pages: cover, TOC, Letter PDF 3p, .docx 2p, EXIF JPEG):
  - TOC entries match the printed footers (report 1, cover letter 4, photo 6). They are clickable links to the right pages.
  - The outline has one bookmark per section, with the PDF's own 3 bookmarks nested and pointing to the right pages.
  - The source web link is kept at its position (example.com).
  - Text stays searchable (vector embed). The cover uses an embedded Literata font.
  - The title goes into the PDF metadata. File name `Left_Packet.pdf`.
- **.docx:** bold, italic, bullets, table, image, page break and heading colours all render. Latin, Japanese, Greek and Cyrillic are fine.
- **JPEG EXIF orientation 6** is honoured (portrait page, matching what a viewer shows).
- **Validation:**
  - "Add at least one file first."
  - "Add a document title, or turn off the cover page." (the title gets focus).
  - .webp and .doc are skipped with a named toast.
  - Duplicate: "already in your list — added anyway".
  - fake.docx: "isn't a valid Word (.docx) file". empty.txt: "doesn't contain any readable text".
  - damaged.pdf: skipped with a Repair link.
- **Password PDF:** inline dialog; Skip gives a named toast; a wrong password gives "That password didn't work"; u123 unlocks, and the file assembles (8 pages).
- **At the cap:**
  - Assemble works and "Preview first page" shows a low-res image (489×633).
  - Download, Save to Google Drive and Save project open the cap dialog.
  - Save to my cloud storage opens the email sign-in / $4.99 add-on dialog.
  - Day Pass stops at the email field; Monthly reaches Stripe (`cs_live_REDACTED`).
- **Badge:** present on every page as intended (owner rule).

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Page loads | PASS | 200; 10 devices render. |
| 2 | Core function | PASS | 8-page packet correct (TOC, bookmarks, links, numbering). |
| 3 | Edge cases | PARTIAL | Password, damaged, empty, fake and EXIF all good. Hindi docx broken. Unnamed error for a renamed image. Mixed-size cases pending a reset. |
| 4 | Error messages | PASS (minor) | Clear; one unnamed. |
| 5 | Mobile/devices | PASS (minor) | iPhone SE fine; ja desktop overflowX flag (as before). |
| 6 | Information correct | PARTIAL | Roman-numeral claim; "each assembly counts" (blog); "stops … naming it". |
| 7 | Indexing | PASS | Canonical self; hreflang. |
| 8 | SEO | PASS | Title "Combine PDF, Word & Images Into One PDF"; meta specific; SoftwareApplication, VideoObject, FAQPage (9), Breadcrumb. |
| 9 | Blog exists and accurate | PARTIAL | The onboarding post is good; two claims are wrong (above). The second linked post is about a catalog series. |
| 10 | YouTube video exists | PASS | Lp5L3YhS8-w embedded. |
| 11 | FAQ and guide correct | PASS (minor) | FAQs accurate (17 sizes, bookmarks, links, scaling). The Tips roman-numeral claim is wrong. |
| 12 | Video shows current capabilities | **FAIL (P2)** | "10 free uses daily", "Pro", "Free" wording, old UI. |
| 13 | Storage | Sign-in untested | Save to my cloud storage → email sign-in + $4.99 add-on. |
| 14 | Sharing | Sign-in untested | Save to / Open from Google Drive → Google sign-in (gated at 0). |
| 15 | Downloads | PASS | Valid PDF; repeat download free; badge as intended. |
| 16 | Usage count | **FAIL (P1)** | Per-page-load: a second document downloaded at 2/2 in the same load. Plus a 0→2 jump on the first download. |
| 17 | Categorization in section | PASS | PDF Tools. |
| 18 | Correct section of site | PASS | Breadcrumb matches. |
| 19 | AI need/demand | PASS | Real file assembly; a chat assistant can't do it. |
| 20 | Merge better? | No | C10: merge-pdf stays the plain path; this is the mixed-format upgrade (the copy already says so). mail-merge-pdf is a different job. |
| 21 | Remove? | No | Premium differentiator. |
| 22 | Duplicates | C10: keep | Cross-links exist (blog → Merge PDF). Suggest a "Need a cover/TOC? → Document Assembler" link from merge-pdf. |

## Owner questions

1. Should **Save project** (the user's own project file) be gated or charged like a document download?
2. Should the first Premium download show 0→2? (Display evidence only; please check the server count.)
