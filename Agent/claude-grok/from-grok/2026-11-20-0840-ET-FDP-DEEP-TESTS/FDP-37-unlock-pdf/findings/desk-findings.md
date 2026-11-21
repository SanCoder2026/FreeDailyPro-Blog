Sent: 2026-11-21 02:36 ET

# FDP-37 Unlock PDF: desk findings (2026-11-21 02:23–02:33 EST)

## Page and SEO
- **Basics:** 200, canonical self, in the sitemap. No pair pages.
- **Title and meta:** title "Unlock PDF - Remove a PDF Password Online | FreeDailyPro" (good). The meta description is 73 chars, "Remove the password from a PDF you can open. Fast, right in your browser." (P2: short; no AES/RC4 or restriction removal).
- **H1 and JSON-LD:**
  - H1 "Unlock PDF".
  - JSON-LD: WebSite, SoftwareApplication (Offer 4.99), FAQPage (**5**), BreadcrumbList. **No VideoObject** (there's no video).
  - og:image is generic.
- **Locales:** 9 return 200 with html lang set. The **H1 stays "Unlock PDF" in every locale** (pdf-password's H1 is translated; P3). Title and meta are English. ja desktop 3 px overflow. `/ar` 404.
- **Blog:** `/blog/unlock-pdf` → 404. No unlock post in the sitemap (only `/blog/pdf-password`, linked under Guides). **No blog** (FAIL, live-verified).
- **Video:**
  - The page has no "Watch" section; the only YouTube link is the footer channel link.
  - A YouTube search for "FreeDailyPro unlock PDF" (yt-dlp, 02:29 EST) returned other FDP PDF videos, none for Unlock PDF.
  - tools.csv also lists it as missing in VIDEOS.md. **No video** (FAIL).

## Copy vs behaviour
- **Accurate (live):**
  - needs the password, no cracking
  - owner-only restrictions removed without prompting
  - layout, links, bookmarks and title kept
  - unprotected file passed through unchanged and labelled
  - spaces count
  - the dialog lets you retry
  - nothing uploaded
- **Untested:** Limitations say "checked with … 128-bit and 256-bit AES and owner-only". Live, RC4-40 and RC4-128 also unlock; the copy could say so.
- **Ethics framing:** "Use it only on documents you are allowed to change" appears three times (good). Removing owner-only restrictions with no password at all is a common industry feature, but it's worth a deliberate decision (P3 policy note).
- **Missing guidance:** no mention of the trial cost, i.e. that unprotected files are free but unlocks use a trial use (the result status says it).

## Code notes (`evidence/js/`)
- **`UnlockPdf-C2SvH1Cm.pretty.js`:**
  - The actual unlock happens in the shared drop zone (`ToolPage` `x`/`y`), which hands over an already-unlocked file.
  - The page shows a status line, thumbnails (≤12, ≤60 pages) and the gated Download `j` with `freeDownload: !unlocked`.
  - Hand-off "Continue with …" buttons come from the shared download area.
- **Per-page-load counting:** shared `index-B1CTyGtY.js` `RA`/`xI`/`Kt` (excerpt shipped).

## Completeness vs competitors (desk; Smallpdf, iLovePDF, Adobe online unlock, PDF24: general knowledge, not re-verified live)
- **Strong:** in-browser, AES-256/128 and RC4 support, owner-only removal, thumbnails, hand-off to Merge, Compress and Remove Pages.
- **Gaps (live UI shows no control for these):**
  - no batch / "Several files" (Add Password has one)
  - no "keep restrictions but remove open password" option
  - no explicit "verified: opens without a password" line like Add Password's Checked line
