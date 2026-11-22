Sent: 2026-11-22 06:34 ET

Sent: 2026-11-22 06:33 ET

# FDP-100 parser code review (BankStatementToCsv-DbLffQo0.js, csvParse-eP1CzDn2.js, utils Va())

Each rule below was seen live (P/T/V cases); the code explains why.

| Area | Code | Effect | Live case |
|---|---|---|---|
| Line building | utils `Va()`: items within ±3 pt y → one line, sorted by x, `join(" ")` | Column positions are lost; CJK and ligatures split; Arabic stays in visual order | L, A ("Spring fi eld") |
| Date at line start | `A()`: ISO `yyyy-mm-dd`, "Mon d[, yyyy]", "d Mon [yyyy]", `d[/.-]m[/.-yy(yy)]` | "d Mon yy": 2-digit year not consumed; "yyyy/mm/dd" not matched; period lines like "March 1, 2026 through…" count as dates | D, T06, T07, A |
| Date order | `me()`: votes only from slash dates with a part > 12; default "mdy" | dd.mm with days ≤ 12 → month-first, even when the number style is "eu" | F, G, H, T01 |
| Year | `Y()`: missing year → Year box (default current year) | Year-end statements mis-dated | K, V02 |
| Amount at line end | `ge()`: up to 3 trailing amounts, ".dd" (US) or ",dd" (EU) required; currency only before the number | "EUR"/"€" after → no amount; no cents → no amount; EU groups only with "." so "1 234,56" → "234,56" | T03, T08, H, T05 |
| Sign | `we()`: (), DR, trailing −, leading − → negative; "+" stripped and **not** recorded as explicit | "+150.00" treated as unsigned → keyword guess → negative | T04 |
| Sign repair | balance diff where previous balance known; otherwise keyword list `Ne` (deposit, credit, refund, payroll, salary, transfer from, … gehalt, gutschrift, salaire, virement reçu, nómina …) | Missing: "Zelle From", "Interest Payment", "Purchase Return", "Remise chèque" | B, C, H |
| Opening/closing | `W`/`V`/`ye`/`ve` lists | "Start/End balance", "Kontostand am …", "solde créditeur au …" (not "ancien/nouveau") and lines prefixed by "26 " are missed | D, E, G |
| Lines without a date | pending row gets a continuation only while it has no amount; after a row is complete, amount-bearing lines are **silently dropped**; text-only lines (≤80 chars, not header) are appended to the last description | HSBC-style same-day rows lost; section headers glued to descriptions | D, B, C |
| Skipped note | `h` only collects date lines with no amount | Dropped no-date rows are not reported | D |
| Card layout | only when no balances at all, no opening/closing, some explicit negatives look like payments | Never triggers on real card statements (Previous/New Balance printed) | J |
| Check `Re()` | rows with balance vs previous balance; else opening + sum vs closing; green if no mismatch | Rows without balance (phantoms) are not checked when other rows have balances; green even with sign-guessed rows | D, E |
| Cell edit | `Number(value.replace(/,/g,""))` on blur | "1.200,00" → 1.2; "1200,00" → 120000 | V03 |
| CSV | `T()` → BOM, CRLF, quote when needed; `'` before = + − @ tab CR unless numeric or phone-like | Safe (D01). A cell like "+1 555 0100 Store" isn't phone-only, so it is guarded too | L |
| Excel | SheetJS cells: date `t:n` + `yyyy-mm-dd`, description `t:s`, amount/balance `t:n #,##0.00` | Safe and typed | D02 |
| Usage | download → `logUsageNow()` (per page load) | P1 #1 | D01–D03 |
