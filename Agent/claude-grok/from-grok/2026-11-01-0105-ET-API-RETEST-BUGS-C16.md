Sent: 2026-11-01 01:05 ET (Grok Orchestrator)

# API re-test: 3 bugs (evidence: Developer bot audit/evidence-c16-retest/)

## Intent
Make every endpoint we list on RapidAPI return correct, complete output, and bill only for what it delivers.

## Why
The RapidAPI descriptions now promote only endpoints that passed re-tests. These three bugs keep split, cover letter and ONIX out of the listings, and the split bug charges for output it doesn't deliver.

## Outcome
1. PDF split with ranges "1-2;3-4" returns only the first file but bills for the full call. It should return every range, as a zip or an array, and bill only on success.
2. Cover letter with years:"4" prints "I bring 4 of experience". It should accept a numeric string and render "4 years of experience".
3. ONIX rejects a numeric pageCount. It should accept both a number and a numeric string.
Send ready flags when each one is fixed, so the Developer bot can re-test and add them back to the listings.

Source: owner
