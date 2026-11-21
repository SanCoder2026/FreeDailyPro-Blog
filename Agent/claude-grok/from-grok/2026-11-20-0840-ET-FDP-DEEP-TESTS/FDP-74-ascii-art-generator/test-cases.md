Sent: 2026-11-21 17:04 ET

# FDP-74 test cases

| ID | Input / action | Expected | Result |
|---|---|---|---|
| Z A01–A21 | 10/10: type, Copy ×8, Ctrl+C ×3, reload | Gate or charge (owner) | **All copied, 0 POSTs, no dialog (owner question)** |
| Z-ff | Same in Firefox | Same | Same |
| L A01–A21 | 0/10: Copy ×16, Ctrl+C ×3, reload | 1 use per copy (owner) | **0 POSTs, stays 0/10** |
| F ×12 | "Hello World" in each font | figlet art, width note | PASS (7 identical to pyfiglet, 5 with +1 lead column) |
| T:multi / centre | 2 lines, Centre | Stacked, centred | PASS; **blank line has trailing spaces (P3)** |
| T:sixty | 75 × "x" | Cut to 60 | Cut silently (P3) |
| T:accents / german / curly | Café Zürich; Straße Œuvre æ; “Smart” – … | FAQ: refused | **Transliterated (page copy wrong, P2)** |
| T:emoji / hindi / mixedLine | 😀; नमस्ते; OK + नमस्ते | Error, no art | PASS |
| T:empty / spaces | "", "   " | Nothing | PASS |
| T:punct / script / tabs / trailing / wide | Symbols; `<script>`; tab; trailing spaces; 16 letters | Drawn as text; width warning | PASS |
| zoom | Slider 22 | Preview 22 px, copy unchanged | PASS |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | iPhone SE 9 px; locales English (P2) |
