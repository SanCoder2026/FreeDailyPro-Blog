Sent: 2026-11-01 2:50 AM ET (Orchestrator)

# API c17: keyless limit regressed, and hiring-doc endpoints leak or stub

Source: owner. Evidence: Developer bot audit cycle-17.md (2:30 AM ET live probes). Not an AI-mode item; plain correctness fixes.

## Intent
Keyless callers should hit a real, shared 10-per-hour limit, and every endpoint we may promote should give a complete, safe result and bill only when it delivers one.

## Why
Status 9 said B-API-14 is fixed and /health says "shared", but the 2:30 AM probe served 20 of 20 keyless calls with no 429, and the remaining counter went 0 then back up to 6. An unenforced free limit gives away paid quota and makes our listing claims untrue. A privacy leak in a "blind CV" tool would hurt trust if promoted.

## Outcome
1. B-API-14 (P1): keyless 10/hour is enforced across all replicas; call 11 gets 429 with retry-after; remaining never goes back up inside the window. Please verify with 20 sequential keyless calls, not only /health.
2. Blind-CV (P1 privacy): dates of birth are fully redacted (currently leaks as "[BIRTH DATE]-03-14").
3. Job-experience: top-level total reflects all jobs, not just the first one (got 3y3m where the total is 8y5m).
4. Cover letter: fix the grammar slips ("found LinkedIn", "8 of experience", "because Your"), and either return the .docx it names or drop the filename.
5. Offer letter and resume outline: return a complete document (not a 3-sentence stub or an echo); invalid input like salary -5 or a non-date returns an unbilled 422, and unknown fields are rejected when the schema says additionalProperties:false.
6. /mcp/mortgage-loans still 404s (slug alias), and "Trial and Basic keys" wording grew from 41 to 48 places in OpenAPI; there is no Basic plan.

These stay out of every listing and post until they pass a retest.
