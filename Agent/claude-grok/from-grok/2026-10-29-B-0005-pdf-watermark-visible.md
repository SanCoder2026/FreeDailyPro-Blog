# B-0005 PDF watermark tool output nearly invisible
Priority: P1      Estimated effort: 20 min

## Goal / why
Blocks the ApyHub PDF Toolkit listing (watermark endpoint unticked until fixed) and the site's watermark feature looks broken.

## What to change
core/pdf/operations.ts around line 381: watermark text drawn light grey at 0.3 opacity, nearly invisible on white pages. Use a darker default (e.g. mid-grey ~#808080 or user colour) with opacity ~0.35–0.5, and honour user-set colour/opacity/size if the API/UI exposes them. Applies to the site tool and the /v1/pdf/watermark API.

## Acceptance criteria
- Watermark on a white Letter page is clearly readable in a rendered preview but does not hide text underneath.
- API /v1/pdf/watermark and the site tool produce the same result; existing tests pass, add one for default colour/opacity.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Resubmitting to ApyHub (owner action). Changing API pricing.
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot / API-MCP bot code review
