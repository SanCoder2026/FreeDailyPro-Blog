Sent: 2026-11-20 22:15 ET

# FDP-26: reproduce

Guest, fresh profile, https://www.freedailypro.com/tool/invoice-generator (2 trial uses).

1. **Footer over Balance due (P1):** Business "Acme Studio", Client "Bob Ltd", Paper A4, Discount 10, Tax 18, Shipping 20, Paid 50, Notes "Notes line " ×60, 23 line items ("Line item n", qty 1, price 10+n, line tax 5/12/18/28 rotating) → Generate PDF → page 1 bottom: "Page 1 of 2" over "$471.55".
2. **Number mismatch (P1):** any valid invoice → Generate PDF (INV-001.pdf) → Word (INV-002.docx).
3. **Usage (policy):** with 2 uses: Excel (0 → 1), PDF (1 → 1). Reload, PDF (1 → 2).
4. **Notes bidi:** Notes `धन्यवाद! Bank: HDFC 0001 · IFSC HDFC0000001 · شكرا · Ευχαριστώ` → PDF shows "IFSC HDFC · شكرا · 0000001Ευχαριστώ".
5. **Parsing:** unit price "1.500" → Total uses 1.50.
6. **Gate:** at 0 remaining → Generate PDF → cap dialog → Buy Day Pass → email prompt. Stop.

Automated: `cd scripts && npm i playwright axe-core`; `OUTDIR=/tmp/ig/ node ig-spend.js A|B|C` (`PWB=firefox` / `webkit`; don't rely on the `BROWSER` env var — on our box it points at a Chrome binary), `node ig-ui.js` (runs only in contexts already at the cap), `node ig-profile.js`, `node run-matrix.js config.json`.
