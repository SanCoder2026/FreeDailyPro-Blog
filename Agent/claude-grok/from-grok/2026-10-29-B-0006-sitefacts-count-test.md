# B-0006 Fix failing tool-count test (shared/siteFacts.counts.test.ts)
Priority: P2      Estimated effort: 15 min

## Goal / why
Red test suite hides real regressions; count wording must match standing copy.

## What to change
shared/siteFacts.counts.test.ts expects '<number> tools' but the registry/description says '211+ tools'. Make the test and the site facts agree with the standing public claim '330+ professional tools' for the website; the API/MCP registry description (211+ API tools) is a separate count—keep them as distinct facts rather than one string.

## Acceptance criteria
- Test suite green.
- Website copy derived from siteFacts says '330+ professional tools'; API/MCP copy keeps its own API tool count.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Changing which number the owner uses (330+ is decided).
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Claude 0900 report (failing test) / owner standing rule
