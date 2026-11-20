Sent: 2026-11-20 08:40 ET

# FDP-23: reproduce

Guest, fresh profile, https://www.freedailypro.com/tool/pdf-to-word.

1. **Numbered list (P1):** drop `evidence/testfiles/rich.pdf` → Convert to Word. In the preview and in the .docx, "Step one / Step two / Step three" have no "1. 2. 3." (the PDF shows them; `pdftotext rich.pdf -`).
2. **Table (P2):** drop `table.pdf` → Convert → the Word table row 2 reads "### North | | 3 | 9.99 02134 | | 630".
3. **WebKit crash (P1 verify):** in Safari (Mac/iPhone) drop `scan_rich_2p.pdf` → Convert. In Playwright WebKit the tab crashes.
4. **Video:** open https://www.youtube.com/watch?v=K61zcnXg6sU — title, description and the "0 free uses remaining today" banner.
5. **FAQ:** expand Common questions → compare "Which languages can scanned pages be read in?" with "What languages does the OCR support?".
6. **Gate:** at 0 remaining, convert, press Download Word File → cap dialog → Buy Day Pass → email prompt. Stop.

Automated: `cd scripts && npm i playwright axe-core`, then `node pw-battery.js P01,P14`, `node pw-webkit-ocr.js`, `node pw-gate.js`, `node pw-dl.js` (set OUT/T paths at the top).
