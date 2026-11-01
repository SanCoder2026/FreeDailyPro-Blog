Sent: 2026-11-01 11:22 AM ET

# API cycle 26: the keyless limit is off, plus teacher workflow gaps

**Intent:** The API must meter exactly, enforce trials, and fully cover the real jobs we list. Full details: /workspace/freedailypro-api-mcp-growth/audit/cycle-26.md

**Why:**
- B-API-14 is worse. The keyless trial limit isn't enforced: 54 of 54 calls from one IP were served, and the caller ID changed 33 times. The owner's Railway setting (ANON_TRUSTED_PROXY_HOPS=1) is pending, but please also make the code safe if that value is missing.
- Billing is holding. Metering is exact, and 400, 404 and 422 responses aren't charged.

**Outcome, in this order:** 14, then one unknown-field 400 rule for all routes, then 104, 123, 134, 129, 136, 115, 119/121/122, 128, 130, 135, 138, 137, 139.

New items from the teacher workflow:
- **B-API-134 to 136:** weighted grade, letter grade and "score needed on the final" (reuse the site's Final Grade Calculator logic).
- **Grammar check:** it fixes only about 5 of 11 typical errors.
- **Classroom-jobs split:** 2 of 6 students end up with no job.
- **Missing:** a rubric builder and a field-trip checklist.
- **B-API-122:** it now also produces the "the team invites you" wording.

Also mark B-API-94 FIXED; it's verified live.

Source: owner
