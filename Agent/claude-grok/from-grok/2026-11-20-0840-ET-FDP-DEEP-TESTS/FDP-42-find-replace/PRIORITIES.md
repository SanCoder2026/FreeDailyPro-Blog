Sent: 2026-11-21 04:17 ET

# FDP-42 Find & Replace: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Suggested direction |
|---|---|---|---|
| P1 | Full-quality results at 0 trial uses; the tool is uncounted ("absorbable") and isn't in the Nov 20 exempt list, so it's a **policy question for Santosh** | gate-2.json / gate-1.json, zero-*.png, index excerpt | Ask Santosh. At minimum, route file Downloads (.docx) through the gated `D`. |
| P1 | No conversion path on the page: no trial strip, pass offer, Quick Buy or cloud save | screens/cases/initial.png, gate logs | Show the standard trial strip and pass offer for Professional Tools; Save to Drive/cloud on results. |
| P2 | Preserve case lower-cases multi-word Title Case ("Acme Corp" → "globex") | T21, verify.json | Per-word title case in `utils M()`; FAQ note until fixed. |
| P2 | .docx FAQs contradict each other about split-format phrases | tool-expanded.txt, T20 | Delete or rewrite "Why might a replacement be missing…". |
| P2 | Video: personal bookmarks and taskbar, old UI, "free" wording, pasted text only | video/z40-*.png, sheet*.png | Re-record on a clean profile, cropped, showing .docx + regex. |
| P3 | .doc/.png get a generic toast; the promised specific messages are unreachable | T17/T18 | Let FindReplace's own messages show, or fix the FAQ. |
| P3 | Broken .docx shows the raw "Corrupted zip…" error | T19 | Friendly message. |
| P3 | CSV comma replacement breaks columns, no warning | T15 | Warn, as for JSON/XML. |
| P3 | Catastrophic regex freezes the tab (~11 s) | T25 | Run in a Worker with a timeout. |
| P3 | No live counter for .docx | T20 | Count after load. |
| P3 | Blog static HTML: `$&` expanded by the prerender `String.replace` | curl/blog-find-replace.html, blog-dollar-amp.png | Use a replacer function. |
| P3 | VideoObject name ≠ YouTube title; generic OG image | tool.html | Align; tool-specific OG. |
| P3 | Locales: H1, title and UI English; /ar 404; ja 3 px and iPhone SE 9 px overflow | matrix-results.json | Translate strings; check the full-width button. |
| P3 | axe: label-content-name mismatch, region, ad-caption contrast | matrix-results.json | Fix the label and the caption contrast; keep the reserved ad slots. |

- **RERUN-AFTER-RESET:** none (nothing pending a reset).
- **Sign-in-only, untested:** "Open from Google Drive" on https://www.freedailypro.com/tool/find-replace.
