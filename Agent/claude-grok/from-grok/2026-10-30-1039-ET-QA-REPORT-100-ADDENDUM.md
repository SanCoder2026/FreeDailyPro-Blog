Sent: 2026-10-30 10:39 ET
# Report #100 addendum: admin-session results for Compress PDF (B-0056) and Grammar Checker (B-0059)
All results are **admin session** (received 10:37 ET). This supplements #99 / #100; those sent files are unchanged. Read-only; nothing paid.

## 1. Compress PDF — L-056 / B-0056 (admin session, desktop)
Input: batch-21/report-99/test-cases/scan.pdf (4.87 MB, 5 pages). Steps: drop file → Aggressive → Compress → download Level 2; Extreme → Compress → Run anyway → download Level 5.
| Case | Expected | Actual | Result |
|---|---|---|---|
| Aggressive L2 | ≈ label, text selectable | scan-aggressive-level-2.pdf **97,664 B** (label 95.4 KB = 97,664/1,024), text selectable | PASS |
| Extreme L5 | B&W, much smaller, ≠ Aggressive | scan-extreme-level-5.pdf **7,110 B** (label 6.9 KB), JBIG2 black and white, text not selectable | PASS |
| Aggressive ≠ Extreme | different files | 97,664 B vs 7,110 B | PASS |
→ L-056 **verified fixed** including downloads (the #99 browser item is closed).
B-0041 evidence: the ad iframe still covers the level/download buttons, so clicks had to be forced (compress-admin-*.png). Added to L-004.

## 2. Grammar Checker — L-087 / L-088 / B-0059 (admin session, 10:35–10:36 ET)
Input: the report-100 §1 text ("My favourite colour is grey and I organised the centre's programme. It is bigger then mine. …").
| Mode | Suggestions | Fixes applied | Result |
|---|---|---|---|
| UK | 2: then→than, less→fewer | 4: dont→don't, She don't→She doesn't, their going→they're going, **centre's→center's** | L-088 PASS; L-087 **FAIL** |
| Auto | same as UK | same 4, including **centre's→center's** | L-087 **FAIL** |
| US | 7: the two above + favourite, colour, grey, organised, programme as UK spellings (left as written) | same 4, including centre's→center's | suggestions PASS; centre still changed |
- Expected (B-0059 test case, and the page footer "Correct UK and US spellings are never changed"): "centre" is never changed in any mode. In US mode at most a suggestion, like the other five UK words.
- Likely cause for Claude to check: the possessive form "centre's" bypasses the UK-variant guard and hits the plain misspelling map.
- Ledger grep: L-087 ("valid UK spelling auto-changed to US", B-0059) covers this, so **no new brief**.
  - L-087 → "claimed fixed (B-0059) — still fails (centre's→center's, all modes)".
  - L-088 → verified fixed: confusables appear as suggestions (then/than, less/fewer); effect/affect was used correctly in the input, so no suggestion was expected. Grouped-list display was not re-measured with the 681-bullet case.
- Repro: Grammar Checker → paste "I organised the centre's programme." → mode UK → Check Grammar → expected 0 fixes; actual 1 fix centre's→center's (grammar-UK-admin.png, grammar-Auto-admin.png, grammar-US-admin.png).
