Sent: 2026-11-20 08:40 ET

# FDP-22: reproduce

Guest, fresh browser profile, https://www.freedailypro.com/tool/universal-file-converter. Open DevTools → Network.

1. **Upload (P1):** drop `evidence/testfiles/deck.pptx`, press "OpenDocument .odp". Network shows `POST /api/trpc/presentation.convert?batch=1` (~40 KB body containing `fileBase64`). Repeat with `deck.ppt` → PDF (~870 KB). Compare with the title "No Upload" and FAQ "Are my files uploaded to a server?".
2. **CSV (P1):** drop `data.csv` → Excel / JSON; open the result (Preview data or the in-memory file): ZIP 02134 → 2134, 00501 → 501; JSON `"name": ""` for `=1+1`.
3. **.doc (P1):** drop `letter.doc` (real Word 97 file) → PDF → toast "That conversion didn't work on this file." Console: NotDocxError.
4. **.pptx dead end:** drop `deck.pptx` → "PowerPoint .pptx (from old formats)" → "This file is already a .pptx."
5. **.odp rejected:** drop `deck.odp` → "can't be used here".
6. **Compression names:** drop `contract.pdf` → Edit → Compress → level list.
7. **Script text:** drop `page.html` → Text → output contains `document.body.insertAdjacentHTML(…)`.
8. **Gate:** at 0 remaining, convert any file, press the converted file's Download → cap dialog → Buy Day Pass → email prompt. Stop.

Automated: `cd scripts && npm i playwright axe-core` then `node uf-battery.js U09,U10,U11`, `node uf-toasts.js`, `node uf-gate.js`, `node uf-dl.js` (set paths at the top of each script).
