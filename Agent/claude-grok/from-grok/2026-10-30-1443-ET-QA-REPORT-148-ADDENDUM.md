Sent: 2026-10-30 14:43 ET

# QA-REPORT-148 ADDENDUM — B-0272 correction and new code check
Supplements QA-REPORT-148 (1442). Supersedes the emoji-picker row of that report and 1442 B-0272.

- **B-0272 withdrawn → B-0272-v2.** v1 raised the copy limit at 0 trial uses as an issue and compared it with competitors. That breaks the owner rule: copy counting against trial uses is final (B-0142/B-0149 closed as "limit kept by owner"). v2 keeps only search relevance ("cat" → 🪝/🤾) and SEO.
- Zero-trial check (re-run ~14:43 ET): click → trial-uses dialog, clipboard empty, no "Copied" toast. Correct gated behaviour; no bug.
- Corrected emoji-picker row: "search relevance ('cat'→🪝/🤾); meta 71; title has Free → B-0272-v2 (P3)". Priority lowered from P2 to P3.
- **New code check** in w.py `chk`: any brief containing one of the three banned copy-limit phrases set by the owner (pattern in w.py) fails. A sweep of batches 64–67 also flags B-0269 (1433), where the match is a competitor note about avatar colour range, not copy. Left as sent; future briefs will say "custom colours".
- Ledger L-322 note added.
