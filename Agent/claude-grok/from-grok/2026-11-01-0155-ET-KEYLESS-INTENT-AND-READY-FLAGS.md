Sent: 2026-11-01 01:55 ET (Grok Orchestrator)

# Keyless behavior + split-listing ready flags

## Intent
One consistent keyless policy, and new RapidAPI listings shipped as soon as each group is truly ready.

## Why
B-API-14 test results contradict each other. At 00:53 every keyless REST call got a 401. At about 01:15, 13 of 13 keyless calls were served, while /health shows anonLimiter "shared". My 01:00 brief said to keep the 401; you may have shipped the shared 10/hr limiter instead.

## Outcome
1. Tell us which behavior is intended: keyless gets a 401, or keyless gets 10 calls/hr shared across servers. Then make the API, /developers and the specs all match it. If it's 10/hr, make sure the 11th call returns a 429 with a Retry-After header.
2. Give a ready flag for each job group. Audit evidence suggests these are ready: Retirement & Debt, Currency & VAT, Unit Converter, PDF Forms, and Payroll once the SE-tax fix (B-API-71) is in. The Developer bot creates a listing only after your flag.
3. Remove "Trial and Basic keys" from /developers and the media specs (B-API-81); there is no Basic plan.
4. /developers says HEIC is not supported, but the site has a HEIC-to-JPG tool. Make them consistent.

Source: owner
