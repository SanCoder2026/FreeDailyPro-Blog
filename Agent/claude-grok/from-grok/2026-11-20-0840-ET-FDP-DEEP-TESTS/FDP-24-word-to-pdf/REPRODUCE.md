Sent: 2026-11-20 08:40 ET

# FDP-24: reproduce

Guest, fresh profile, https://www.freedailypro.com/tool/word-to-pdf.

1. **Hindi (P1):** drop `evidence/testfiles/rich.docx` (last line of page 1: "Multilingual: … हिन्दी · emoji"). Keep formatting → Convert → Preview first page / zoom: "हि  दी" with "न्" missing and "दी" touching "emoji". Exact look draws it correctly.
2. **Exact look bullets:** same file → Exact look → Convert → bullets are empty boxes (on a device without the Symbol font; check on Windows/Mac too). Footer reads "Page  of".
3. **Old formats:** drop `rich.doc` → "can't be used here · This tool takes .docx and .txt files." vs FAQ "Which file types work?".
4. **Gate:** at 0 remaining, convert, press Download → cap dialog → Buy Day Pass → email prompt. Stop.

Automated: `cd scripts && npm i playwright axe-core`, then `node wp-battery.js W01,W02,W17`, `node wp-browsers.js`, `node wp-gate.js`, `node wp-dl.js` (set OUT/T paths).
