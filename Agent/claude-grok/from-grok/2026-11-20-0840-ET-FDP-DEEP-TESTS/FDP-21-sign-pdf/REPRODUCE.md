Sent: 2026-11-20 08:40 ET

# FDP-21 Sign PDF: how to reproduce

Box: `/workspace/deep/tools-env` (scripts copied in `scripts/`; paths point to `/workspace/deep/21-sign-pdf/`). Test PDFs: `evidence/testfiles/contract.pdf` (reportlab) and the 03-merge-pdf set (password, rotated, non-Latin, restricted, truncated).

1. **Other-party fields (P1):** https://www.freedailypro.com/tool/sign-pdf → add contract.pdf → name → Fields: Signature, set "Assigned to" = Other party, click the page → Download (or `node sp-battery.js S02` at 0). Open the PDF in any reader: an empty fillable text field "Sign here". Then read Common questions → "How does the other person actually sign their part?" and Details → Limitations.
2. **Keyboard (P1):** add a PDF, Tab to Fields → Signature → Enter; keep tabbing: the preview is never focused and "Click page to place" needs a pointer (`node sp-gate.js`, `kbdPlace`).
3. **Video (P1):** play bP3uV1CNIwM 0:30–1:30: "10 free uses daily", "0 free uses remaining today".
4. **Count:** in a context with uses left: Download Signed PDF twice (`node sp-battery.js S01 spend`): count +1 then +0.
5. **Round trip:** `node sp-otherparty.js` opens `out-S02.pdf`: toast "2 fields are waiting for you".

Scripts: `sp-probe.js`, `sp-copy.js`, `sp-battery.js [IDs|all] [spend]` + `sp-cases.json`, `sp-import.js`, `sp-otherparty.js`, `sp-gate.js`, `sp-browsers.js` (`GIO_EXTRA_MODULES=$PWD/giomods`), `run-matrix.js config.json`.
