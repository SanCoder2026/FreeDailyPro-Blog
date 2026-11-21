Sent: 2026-11-21 04:17 ET

# FDP-42 Find & Replace: test cases (rerun after fixes)

Test files: `evidence/testfiles` (built by `scripts/make-files.py`). Guest, fresh profile. Expected results are for after the fixes; "Now" is what we saw on 2026-11-21.

| ID | Case | Expected | Now |
|---|---|---|---|
| FR-01 | Default find "acme corp" → "Globex" in mixed text | 5 matches, live count | PASS |
| FR-02 | Whole word "cat" | catalog untouched | PASS |
| FR-03 | Whole word + Preserve case cat/CAT/Cat | dog/DOG/Dog | PASS |
| FR-04 | Case sensitive | only exact case | PASS |
| FR-05 | Regex date `$3/$2/$1` | 12/03/2026 | PASS |
| FR-06 | Invalid regex `(` | message, button disabled | PASS |
| FR-07 | `\n` in the replacement (regex) | real line break | PASS |
| FR-08 | `^Call` with/without multiline | 1 / 0 | PASS |
| FR-09 | Named groups `$<m>` | swapped | PASS |
| FR-10 | Empty replacement | deletes | PASS |
| FR-11 | café/CAFÉ/Café whole word + preserve | tea/TEA/Tea | PASS |
| FR-12 | Emoji, Cyrillic whole word | correct | PASS |
| FR-13 | JSON broken by edit | warning, still downloadable | PASS |
| FR-14 | XML broken | warning | PASS |
| FR-15 | CSV "Globex, Inc" | warning about columns | P3 no warning |
| FR-16 | HTML / MD | correct, `_edited` name | PASS |
| FR-17 | .doc dropped | "save as .docx" message | P3 generic toast |
| FR-18 | .png dropped | lists supported types | P3 generic toast |
| FR-19 | Broken .docx | friendly error | P3 raw zip error |
| FR-20 | Rich .docx | split runs found; formatting, table and image kept | PASS |
| FR-21 | .docx Preserve case "acme corp"→"globex" | Acme Corp → **Globex** | P2 → globex |
| FR-22 | .docx regex `\{\{name\}\}` | Jane | PASS |
| FR-23 | 6.4 MB .txt | <10 s, download OK | PASS 5.1 s |
| FR-24 | Undo | restores | PASS |
| FR-25 | `(a+)+$` on 28 a + b | no freeze >1 s (worker/timeout) | P3 ~11 s freeze |
| FR-26 | `x*` | -a-b-c- | PASS |
| FR-27 | `$&!` literal vs regex | literal / match | PASS |
| FR-28 | Firefox + WebKit subset | same as Chromium | PASS |
| FR-29 | **At 0 trial uses:** .docx Replace + Download | cap dialog / gated per policy decision | **P1:** downloads in full |
| FR-30 | **At 0:** .txt and pasted Replace All | per policy decision | **P1:** full result |
| FR-31 | With uses left: one Download | counter +1 per Download (if counted) | counter stays 0 |
| FR-32 | Trial strip / pass offer on page | visible; stop at the email prompt or Stripe | absent |
| FR-33 | FAQ copy | no contradictions | P2 |
| FR-34 | Blog static HTML | contains `$&`, no stray root div | P3 |
| FR-35 | Locales /de etc. | H1/UI translated; /ar 200 or removed from hreflang | P3 |
| FR-36 | iPhone SE | no horizontal overflow | P3 9 px |
| FR-37 | axe | no serious violations | P3 |

**Untested (sign-in):** "Open from Google Drive". Nothing is pending a reset.
