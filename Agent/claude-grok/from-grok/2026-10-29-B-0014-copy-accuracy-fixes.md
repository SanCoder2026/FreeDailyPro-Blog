# B-0014 Small copy and output accuracy fixes
Priority: P3      Estimated effort: 45 min

## Goal / why
Trust and accuracy on Premium/Pro tools.

## What to change
- https://www.freedailypro.com/tool/book-interior-maker empty-state tip says 150 pages needs inside margin ≥0.75in; KDP and our own table say 0.375in for 24–150 pages. Fix tip.
- https://www.freedailypro.com/tool/listing-photo-pack About says JPEG 'on a white background' but tool doesn't change background (Amazon tip says so). Align About with behaviour.
- https://www.freedailypro.com/tool/caption-generator: X drafts still include hashtags though About/FAQ say X drops them; drop hashtags for X.
- https://www.freedailypro.com/tool/product-description-writer: 'a Wireless Headphones' grammar from template; fix article/plural handling.
- https://www.freedailypro.com/tool/contract-templates: Services line ends with '..' in PDF.
- https://www.freedailypro.com/tool/paper-submission-desk: ORCID shown as bare digits; display https://orcid.org/xxxx-xxxx-xxxx-xxxx.
- https://www.freedailypro.com/tool/subtitle-adder soft subtitle track strips '<Tags>' text from cues; escape rather than strip, or note in About.

## Acceptance criteria
- Each item verified on the live page/output as described.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Legal wording beyond these lines.
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (reports #47, #48, #52, #53, #55, #57, #64)
