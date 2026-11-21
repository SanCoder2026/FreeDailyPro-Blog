Sent: 2026-11-21 10:12 ET

# FDP-54 PowerPoint to PDF: priorities (2026-11-21 EST)

| Pri | Item | Why it matters | Suggested fix |
|---|---|---|---|
| P1 | One trial use per page load (7 conversions incl. 60 slides and 2 server conversions = 1 use) | Gate gap by owner rule; gives away paid value | Charge per Convert of new content (hash file + options); re-check the cap every time. |
| P2 | .ppsx / .potx / .pptm (and .pps/.key) accepted, uploaded, then refused with "already PowerPoint (.pptx). Pick a different format…" | Real show files can't be converted; confusing message from another tool | Treat OOXML variants as .pptx locally; give a tool-specific message for anything still unsupported. |
| P2 | Handout blog contradicts the tool (.ppt "mistake", "don't expect selectable text", "unhide hidden slides") | Users skip features that work | Update the post. |
| P2 | Locale pages half translated | Mixed-language page | Translate the subtitle, privacy note, drop zone and options. |
| P3 | Hindi garbled in the text layer | Wrong search and copy results | Leave complex scripts out (as the FAQ says) or shape them correctly. |
| P3 | Text layer makes 60 slides take ~51 s vs ~6 s | Slow on big decks | Profile the text-layer step; build it lazily or in a worker. |
| P3 | .ppt path: pale hyperlink colour, caption moved | Small fidelity loss | Check the server conversion's theme and colour mapping. |
| P3 | .ppt/.odp uploaded and converted at 10/10 before the cap dialog | Server cost with no conversion possible | Check the cap before uploading (the preview can wait). |
| P3 | FAQ has 3 duplicated questions; 40 vs 50 MB; meta "Fast, right in your browser" | Copy quality | De-duplicate; pick one threshold; mention the server step for old formats. |
| P3 | Video: breadcrumb "PDF Tools", "200+", missing Save buttons | Small staleness | Refresh at the next re-record. |
| P3 | axe: label-name mismatch, region, ad-label contrast | A11y polish | Fix the label; caption contrast (reserved slots kept). |
| P3 (site-wide) | iPhone SE 9 px header overflow | Hamburger clipped | Header min-width. |
