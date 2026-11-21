Sent: 2026-11-21 07:48 ET

# Desk findings

- **Head:**
  - Title "PDF Bookmarks Editor: Add, Rename, Reorder Outline | FreeDailyPro" (65).
  - Meta 110 chars (same text as the subtitle). Canonical self; hreflang 10 + x-default; og-default; H1 "PDF Bookmarks Editor".
- **JSON-LD:** WebSite, SoftwareApplication (offer 9.99), VideoObject ("How to Rename and Fix PDF Bookmarks with PDF Bookmarks Editor", 2026-10-25, matches the video), FAQPage (5), BreadcrumbList.
- **FAQ (5) and Details:** accurate about zoom (Fit), named destinations, no auto-from-headings, and the password message.
  - "Remove all… The new PDF has no outline" is true for viewers, but the old outline objects stay in the file.
  - Nothing says that URI or other actions, colours, styles or collapsed state are dropped.
- **Blog /blog/edit-pdf-bookmarks-outline-tree:** "Edit a PDF Bookmark Outline Without Rewriting Pages". Accurate and practical. It advises matching the printed table of contents, but the tool shows only physical page numbers.
- **Code:**
  - `PdfBookmarksEditor-P1ChXVF9.js`:
    - `Je()`: `catalog.delete('Outlines')` + `Fe()` writes a new tree; the old objects are never deleted.
    - `_e()`: loads with `ignoreEncryption`, and returns "encrypted" for a still-encrypted file.
    - `pe()`: `logUsageNow()` gates the download.
    - `He()`: inserts after the selected bookmark.
  - `pdfBookmarks-BjfxtCfb.js`:
    - `T()` reads `/Dest` or a GoTo `/D` only when it's an array. Named destinations and other actions give `pageIndex: null`.
    - `S()` writes `/Title`, `/Parent`, `/Prev`, `/Next`, `/Dest [page /Fit]`, `/First`, `/Last` and a positive `/Count`.
- **Site placement:** the tool is linked from both /category/pdf-tools and /category/publishing-tools (static HTML). Its breadcrumb is Publishing & Print Makers; the video shows PDF Tools.
