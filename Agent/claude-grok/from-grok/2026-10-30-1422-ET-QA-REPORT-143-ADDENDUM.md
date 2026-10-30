Sent: 2026-10-30 14:22 ET

# QA-REPORT-143 ADDENDUM — admin session
Adds admin evidence to QA-REPORT-143 (B-0255–B-0257). Downloads in batch-62/downloads/, checked on the box at ~14:22 ET (csv, openpyxl, pdftotext, ffprobe).

## accessibility-checker-powerpoint (B-0255, L-311)
- t-accessibility-report.csv: header `Severity,Slide,Problem,Shape,How to fix` + 1 row: `tip, whole file, "The file has no document title…"`. Matches the screen: 0 problems, 0 items to check, 1 tip.
- **Only a CSV is offered; the fix action is disabled, so there is no fixed .pptx.** This resolves B-0255 Outcome 1: it is a capability gap. Add a "Set document title" fix (writes dc:title to docProps/core.xml) and a fixed-.pptx download.

## accommodation-manager (B-0256, L-312)
- guest-list.csv: 15 columns (ID, Name, Email, Phone, Organisation, Role, Status, Dietary, Access needs, Needs stay, Arrival, Departure, Table, Plus ones, Notes), 8 sample guests ✔.
- guest-list.xlsx: sheet "Guest List", 15 columns (no ID; adds "People coming"), 8 guests + a summary (Total 8, Confirmed 5, Invited 1, Declined 1, Waitlist 1, People coming 5, Need a room 4, Dietary 4, Access 1) ✔ — counts match the CSV.
- labels-5160.pdf: 1 page, Letter, Avery 5160 3-across grid. Each label is Name / Organisation / Table and the text lines up with the CSV ✔.
- **Minor:** the button says "Use guest names from my project (8)" but the PDF has **7 labels**: declined Daniel Smith is left out (invited and waitlisted are kept). Leaving out declined guests is reasonable, but the count on the button should match (or say "7 not declined").

## acx-audiobook-checker (B-0257, L-313)
- At admin level the measurements show. "Fix and re-check" raised the bit rate to 192 kbps CBR and that line passed. acx_a.mp3 by ffprobe: 192 kbps, 44.1 kHz, mono, 6.03 s ✔.
- **Still failing after the fix:** room tone 6.0 s at the head and 0.0 s at the tail, noise floor −21.0 dB. The auto-fix does not trim or pad room tone and does not reduce noise.
- Gap: trim/pad head (0.5–1 s) and tail (1–5 s) to ACX spec, and optional noise reduction (or a clear "can't fix noise floor" note).
- The noise-floor warning confirm before fixing is good. The confirm closed on the first try: possible flakiness, not filed as a bug unless it repeats.
