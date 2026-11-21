Sent: 2026-11-21 05:21 ET

# FDP-43 v2 corrections (2026-11-21, box `date` ET)

v1 (`FDP-43-book-writing-toolbox-2026-11-21.zip`) is frozen. This v2 changes one classification.

| Item | v1 | v2 | Why |
|---|---|---|---|
| Book preview watermark strength (PDF mark is one background tiling pattern; manuscript .docx mark is one header line) | P1 gate gap ("full-quality result at 0 trial uses") | **Owner question, not a bug** | Owner rule (relayed Nov 21): the Book preview watermark is intentional. Report its strength only as an owner question. |

Updated with it: REPORT.md (header note, Intent, Why, Outcomes, severity summary), PRIORITIES.md, test-cases.md (BW-01–BW-03), INSTRUCTIONS.md step 3, findings/live-functional-findings.md item 1.

**Unchanged P1s:** EPUB build returns 500 on 11/11; per-page-load Professional trial-use charge on the "unlimited" manuscript preview and ONIX; silent nothing at 0 trial uses.
