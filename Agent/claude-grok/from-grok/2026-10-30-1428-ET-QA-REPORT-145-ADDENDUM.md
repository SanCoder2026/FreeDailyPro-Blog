Sent: 2026-10-30 14:28 ET

# QA-REPORT-145 ADDENDUM — admin session ~14:25-14:27 ET
Adds admin evidence to QA-REPORT-145 (B-0261–B-0263). Downloads in batch-64/downloads/, checked on the box at ~14:27 ET (zip/XML, pdfinfo, pdftotext, csv, openpyxl). Stage timer read live (logged out, sample loaded) at ~14:27 ET; screenshot stage-timer.png.

## add-slide-numbers (B-0261, L-314)
- t-numbered.pptx: every slide has a real field `<a:fld type="slidenum">` with cached text 1, 2, 3 ✔. PowerPoint will renumber after reordering.
- The file was made with style "3" (number only), so it has no "/ 12" total. **"3 / 12" is unverified:** a download in that style is needed to see whether the total is static text (Microsoft says PowerPoint cannot compute it) and goes stale when slides are added.

## agenda-builder (B-0262, L-315)
- programme-letter.pdf: 1 page, 612×792 (Letter) ✔. programme-a4.pdf: 1 page, 595×842 (A4) ✔. Same text in both: "Sample offsite", 2 days, 6 sessions with times, presenter · room ✔.
- **Track is never printed** (the CSV has Product/Sales), and the sessions have no presenter/room/track toggles in admin. **New gap (not in B-0262):** per-field show/hide for presenter, room and track, plus track labels or colours on the programme.

## agenda-cue-sheet-builder (B-0263, L-316)
- event-schedule.csv: 11 columns (ID, Title, Day, Start, End, Track, Room, Presenter, Link, Time zone, Notes), 6 rows ✔.
- event-schedule.xlsx: sheet with title row "Sample offsite", then 8 columns (Day, Start, End, Length, Session, Room, Presenter, Notes), 6 rows ✔. **It drops Track, Link and Time zone that the CSV keeps;** align the two.
- agenda-cue-programme.pdf: 1 page Letter, same text as the agenda-builder programme ✔ (confirms the overlap in B-0262).
- run-of-show.pdf: **2 pages** ✔, Letter landscape (792×612), one day per page ("1/2", "2/2"). Columns: Time, Dur, Item, Who, Where, Cue / notes, Done. Shows gaps ("gap of 1 h 30 min", "gap of 5 h") ✔. Minor: "1h" for the Customer panel vs "1 h" elsewhere (and in the XLSX).
- **Stage timer (left out of B-0263 gaps):** Stage timer / Focus timer modes; preset 5–60 min or typed length (5, 5:30, 1:05:00); ±1 min; amber and red warnings at set seconds left; on-screen message ("Please wrap up"); Full screen; "Use my agenda (6 sessions)". Start/Reset run before the gate; Copy result / Save as text / Print use 1 trial use per visit. Minor: the Copy/Save/Print row appears twice.
  - Gaps vs the competitor read in #145 (eventools.io): a separate speaker view opened by link on a second device; advancing to the next session with one key (spacebar).
