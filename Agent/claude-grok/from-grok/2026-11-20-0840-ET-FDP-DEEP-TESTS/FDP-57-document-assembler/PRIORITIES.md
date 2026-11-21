Sent: 2026-11-21 11:31 ET

# FDP-57 Document Assembler: priorities (2026-11-21 EST)

| Pri | Item | Why it matters | Suggested fix |
|---|---|---|---|
| P1 | Per-page-load gate: after the first Download, a re-assembled document downloaded at 2/2 with no dialog or POST (same load); blocked only after a reload | Premium output given away; owner rule | Re-check the cap on every Download of new content (hash the sections + options). |
| P1 (check) | First Download moved the counter 0/2 → 2/2 (one usage.log POST) | Looks like one download used both Premium uses (display-only evidence) | Check the server count for the `…:premium` scope after the reset. |
| RERUN-AFTER-RESET | Cases C1–C3 and the different-files per-load trace not run (51 fresh contexts at 2/2); Save project with uses left | Output fidelity on mixed sizes, 6×9, 60 pages, Unicode titles; gate proof | `/workspace/deep/RERUN-AFTER-RESET.md` row #57 (after midnight UTC = 7:00 PM ET). |
| P2 | Video: "10 free uses daily", "Pro", "Free" title/description/thumbnail; old UI | Wrong offer (now Premium 2/day $3/$9.99); owner avoids "free" | Re-record; fix the title/description. |
| P2 | Save project blocked at 0 by the download cap dialog | Users can't keep their work at the cap | Owner decision; probably let the project file save without a charge. |
| P2 | Locale pages: only the H1 and strip are translated | Mixed language | Translate the tool strings (site-wide). |
| P3 | Hindi in .docx renders as broken clusters | Wrong output for hi users | Use shaping (harfbuzz) or a fallback note. |
| P3 | Tips: roman-numeral front pages (none printed; no /PageLabels) | Copy accuracy | Print i/ii or drop the sentence; consider /PageLabels. |
| P3 | Renamed non-image .png: "could not be read" (no file name) | Limitations promises a named error | Include the file name. |
| P3 | Blog: "Each assembly counts" (only Download counts); "check the preview" (first page only) | Copy accuracy | Edit the post. |
| P3 | Event project bar (Agenda/Guest list/Budget) + "Try a sample" on a generic packet tool | Confusing | Show only when a project is open. |
| P3 | axe critical: Page Size select trigger has no accessible name; label mismatch; ad-caption contrast | A11y | Add aria-labelledby. |
