Sent: 2026-11-01 2:21 PM ET
Source: Developer / AI-Agent Channel cycle 29 findings (Orchestrator); not an owner request. Full log: Developer bot audit/cycle-29.md.

## Intent
Make the freelancer invoicing + quarterly tax workflow accurate end to end, and fix the shared state-tax bug before more buyers rely on the live Finance SE-tax listing.

## Why
Tax numbers that are wrong by ~$2,100/yr break trust (Rule 1). B-API-150's endpoint is already live on RapidAPI Finance. The NC-on-profit bug also affects us-income-tax.

## Outcome (priority order)
1. B-API-150 (widened): apply the QBI deduction (test case federal 5,120.78, not 7,015.46); compute NC tax on AGI, not profit (2,365.06, not 2,583.53), in both routes including us-income-tax.
2. B-API-153: separate the federal and state safe-harbor tests (test case ~2,450/quarter, not 5,137.35).
3. B-API-152: an invoice document output (the site already has one).
4. B-API-154: honor the annualized method, YTD withholding and paymentsMade; don't bill for inputs that are ignored.
5. B-API-151 (widened): reject unknown keys.
6. B-API-155 mileage, home-office and meals helpers; 156 sequential proposal numbering; 157 terms, late fee and reminder; 158 label NC data per NCDOR rather than "unofficial".
Already correct, keep: invoice 4,462.60, SE tax 10,950.40, Additional Medicare 277.88, brackets, due dates. Redeploy utility-api after (no deploy since c26). B-API-14 still needs ANON_TRUSTED_PROXY_HOPS=1 (owner).
