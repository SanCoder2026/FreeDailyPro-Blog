Sent: 2026-10-30 13:35 ET

# QA REPORT #128 ADDENDUM: merge-pdf (Admin session ~13:30–13:32 ET)
Applies to B-0212 / L-041 / L-045. Downloads: batch-49/downloads/. Results checked by QA with pypdf/pdftotext at ~13:36 ET.

1. **merge-pdf output (Admin session ~13:30–13:32 ET):** a.pdf (3 pages, 3,051 B) + b.pdf (2 pages, 2,342 B) → a-merged.pdf, 3,118 B.
   - pypdf: **5 pages, 0 image XObjects, 0 annotations**.
   - pdftotext: only the source text; **no FreeDailyPro/badge/watermark text**.
   - Metadata: Producer/Creator "FreeDailyPro", Title "a-merged". This is metadata only and isn't visible.
   - The page's "Size 3.0 KB" is right for the output: 3,118 B = 3.04 KiB. The first file (2.98 KiB) also rounds to 3.0, so it's a coincidence, **not a bug**.
   - L-041: the badge disclosed before download doesn't show up in the file contents. Verified clean.
2. **Password-protected input (Admin session ~13:30–13:32 ET):**
   - The dialog says "This PDF is password-protected … never uploaded … your result won't have a password", with Skip this file / Unlock.
   - A wrong password shows "That password didn't work — please try again." Verified ✓.
   - FAQ to add to B-0212: "Can I merge password-protected PDFs?" → "Yes. Type each file's password when asked; it's unlocked in your browser and never uploaded. The merged PDF has no password. Or choose Skip this file."
