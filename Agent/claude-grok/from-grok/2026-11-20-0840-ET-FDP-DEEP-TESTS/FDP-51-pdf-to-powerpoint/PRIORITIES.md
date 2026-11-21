Sent: 2026-11-21 08:44 ET

# FDP-51 PDF to PowerPoint: priorities (2026-11-21 EST)

| Pri | Item | Why it matters | Suggested fix |
|---|---|---|---|
| P1 | Per-page-load charging (ToolPage `gateAtDownload`) | 14 new decks for 1 trial use (left.json); the same in left2. Trial value leaks and the upgrade moment never arrives. | Charge per new result blob (hash) and re-check the cap on every download. Same fix as FDP-44 to FDP-50. |
| P2 | Not listed on the PDF Tools hub | Users browsing PDF Tools see PDF to Word/Excel/JPG but not PowerPoint. | Cross-list in pdf-tools (keep the primary category). |
| P2 | No video, no blog post | Checks 9/10 fail; no demo of the two modes. | Short video (picture vs editable on a real deck) and a blog post such as "Turn a PDF handout into editable slides". |
| P2 | "PPT" keyword missing | "pdf to ppt" is the common query. | Title/meta/H2 such as "PDF to PPT / PowerPoint (PPTX)". |
| P2 | Arabic editable text reversed | RTL documents become unreadable when edited. | Reorder RTL runs to logical order (bidi) and normalise presentation forms (NFKC) before writing the text boxes. |
| P2 | Table text merged per row | Text overlaps the drawn grid; looks broken. | Split on large x-gaps into one box per cell, or build a native table when the grid lines are detected. |
| P2 | Tool body English on all locales | Weakens the translated pages. | Translate the subtitle, drop zone, mode cards, summary and cross-sell copy. |
| P2 | Preview at 0 (owner question) | The full slide preview is visible at 10/10; only the file is gated. | Decide; e.g. preview the first 2 slides at 0. |
| P3 | Near-black text written as #272727–#353535 | Text looks slightly grey. | Snap near-black/near-white; weight the sampling by glyph coverage. |
| P3 | Copy: "password PDFs need unlocking first" | The tool unlocks inline. | Update the How to use text. |
| P3 | Non-PDF file says "looks damaged" | Misleading. | Detect a missing %PDF header → "This file isn't a PDF". |
| P3 | Picture quality fixed (1920 px, JPEG 0.88) | Fine on screen; soft for print. | Offer an HD option. |
| P3 | Pass dialog promises mark removal; trial .pptx has no mark | Copy and behaviour differ (owner question). | Decide whether .pptx gets the badge; adjust the copy. |
| P3 | iPhone SE 9 px overflow; /ja 3 px; axe label-content-name-mismatch (1), region (1), ad-label contrast (2); Pixel 7 CLS 0.081 | Polish. | Wrap the button row; fix the label; reserve the ad slot height (reserved slots, not removal). |
| P3 | og-default image | Weak share preview. | Tool-specific OG image. |
| Enh | OCR for scans | Competitors read scans; FDP has OCR PDF. | Link "Run OCR PDF first" when pages have no text. |
