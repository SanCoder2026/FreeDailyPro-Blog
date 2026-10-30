Sent: 2026-10-30 08:37 ET
# B-0120 Merge PDF: page thumbnails with rotate/delete, mixed file types, and ads out of the subtitle/About text (capability gap)
Priority: P2      Estimated effort: 1–2 days      Report: #97      Source: Testing Bot (capability-gap sweep)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Match Smallpdf/iLovePDF for the everyday "combine these attachments" job, building on the new per-file page choice.

## Why
- Demand (analytics file): /tool/merge-pdf GA 235 views (74 users, 3.18 views/user, 1m04s), the #2 tool page. GSC page 1 click / 601 impressions / pos 35.2, which means it barely ranks. Query "merge pdf files free no sign up" 1/2/pos 111.
- Verified #97 (no download, so no trial use): 2 files loaded → "2 files · 4 pages — drag to reorder"; sizes 3.0 KB / 2.6 KB match the files on disk (3,063 B / 2,620 B); per-file "Choose pages", ↑/↓, and an odd-page blank-page option. This is progress on L-043/B-0054. The result-size label (L-042) still needs the admin carry-over because download costs a trial use.
- Live competitor fetch (08:34 ET):
  - **Smallpdf**: "Preview and Organize with Thumbnails… Rearrange PDF pages… delete… rotate"; it also merges Word, Excel, PowerPoint, JPG and PNG; saves to Google Drive.
  - **iLovePDF**: drag-and-drop ordering (the fetch returned little else).
- B-0041 evidence: a "Try Office Apps" ad pill renders inline next to the subtitle and inside the About paragraph (merge-pdf-1280.png). It reads as part of the product. The analytics file (line 168) also records side-rail ads overlapping content on this page.

## Who uses this
Office workers combining contract attachments, students combining scanned assignments, and anyone sending one PDF instead of five.

## Outcomes (ranked)
1. A page-thumbnail grid across all files, with drag reorder, rotate and delete per page.
2. Accept JPG/PNG (and optionally DOCX) in the same merge, converted locally.
3. Ads in labelled slots only, never inline in the subtitle or copy (B-0041).
4. Search: the page ranks at position 35 for a high-intent query; review title/H1/FAQ for "merge PDF" (SEO "free" is fine).

## Constraints
Local processing. Charge a trial use only on download (L-040 behaviour verified earlier).

## Test cases (ET)
- 08:33 TC-1: two PDFs load with correct sizes and page counts. PASS
- 08:33 TC-2: per-file Choose pages + reorder + blank-page option. PASS
- 08:33 TC-3: per-page thumbnails with rotate/delete. ABSENT
- 08:32 TC-4: inline "Try Office Apps" ad in subtitle/About. FAIL (B-0041)
- TC-5: merged download size label (L-042). BLOCKED → admin carry-over
