Sent: 2026-11-21 03:55 ET

# FDP-41 OCR PDF: priorities

1. **P1 (gate): one trial use per page load.**
   - The first Download costs 1 use, and every later Download in that page load is free: 14 different searchable PDFs, including a 12-page scan, for 1 use. Reload and it charges once more.
   - The shared `Kt` set behind ToolPage `D` is the same root cause as #35–40. Charge every Download (Nov 20 decision).
2. **P1 (function): orientation and language carry over to the next file after New.**
   - An upright file gets turned sideways in the download, and the notice claims "turned 90° clockwise so it reads upright".
   - Reset `N`/`C` on New and on a new file (`OcrPdf-BJ90unSe`), or show the carried-over choice.
3. **P2: "Detect automatically" turns upside-down pages sideways** (270° accepted before 180° is tried). Score all angles.
4. **P2: scans with a small text stamp or footer are skipped** as "already searchable" (≥3 chars rule). OCR image-dominant pages anyway, or offer "OCR anyway".
5. **P2: the table text layer drops the numeric columns** (38% recall), which breaks the page's own "Next: PDF to Excel" bundle.
6. **P2: Hindi loses reph/half forms** in the text layer ("मार्च" → "माच"), so search fails.
7. **P2 (verify on a device): OCR crashed Playwright WebKit** (desktop + iPhone emulation). Test on a real Safari.
8. **P2 copy and discovery:**
   - The FAQ says English only (8 languages work).
   - The tip says pages aren't turned (they are).
   - There's no blog post.
   - The video lacks the orientation menu, says "200+", and never shows search working in the output.
9. **P3:**
   - The blank-scan message talks about orientation; the progress % is stuck on "page 1".
   - Duplicate FAQ; generic OG image; JSON-LD only in the rendered DOM.
   - Title/meta English in locales; /ar 404.
   - iPhone SE 9 px / ja 3 px overflow; axe label mismatch / region / ad-caption contrast. Keep the reserved ad slots and fix only the caption contrast.
