Sent: 2026-11-21 12:33 ET

# FDP-60 test cases (guest). Inputs in evidence/testfiles/cases.json; expected values from px60-expected.mjs (site code)

| ID | Input | Expected | Today |
|---|---|---|---|
| G01 | Convert with uses left | +1 use if counted (owner decision) | 0 (Owner question) |
| G02 | Convert/Copy/Download at 10/10 | cap dialog if counted | works (Owner question) |
| G03 | Copy/Download on empty box | disabled | PASS |
| G04 | Restore after 2 styles | original text; button hides | PASS |
| G05 | Style click on empty box | nothing | WEAK (Restore appears) |
| T01 | Title with colon subtitle | "…Rings: The Return…" (AP/Chicago) | WEAK ("the") |
| T02 | Title, mixed text with NYC/iPhone/API | kept | PASS |
| T03 | Title, ALL CAPS | acronyms lost (disclosed) | PASS (as documented) |
| T04 | Mc/O'/D' names | inner capital | PASS |
| T05 | Multi-line titles | per line | PASS |
| T06 | Hyphenated | State-of-the-Art | PASS |
| T07 | Sentence, mixed with NASA, i'm | NASA kept, I'm | PASS |
| T08 | Sentence with p.m./e.g./Dr. | no capital after abbreviation | **FAIL** |
| T09 | Sentence, ALL CAPS | nasa (disclosed) | PASS (as documented) |
| T10–T15 | camel/Pascal/snake/kebab/CONSTANT incl. apostrophes, XML, accents, Turkish, symbols | as FAQ | PASS |
| T16 | Alternating with ß/emoji | ß unchanged (disclosed) | PASS |
| T17 | UPPERCASE ß | SS | PASS |
| T18 | lowercase Greek | final ς | PASS |
| T19–T22 | Greek/Cyrillic/CJK title, quotes, per-line sentence | as code | PASS |
| Z | 202,500 chars Title | completes | PASS (~4 s) |
