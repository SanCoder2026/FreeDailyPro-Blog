Sent: 2026-11-06 10:48 AM ET

# B — Citation Generator: brand in title + empty-field validation

**Intent:** Fix SERP branding and stop junk citations so the Professional Tool looks complete and trustworthy.

**Why:** Testing Bot QA-412 (2026-11-06 ~10:26 ET, `from-grok/2026-11-06-1026-ET-QA-REPORT-412.md`). Live title ends with “Harvard - Trial” and has **no FreeDailyPro brand**. Empty form still enables Copy / Add to Reference List and outputs junk like `"." Accessed 6 Nov. 2026.` Chicago year issue (L-146) did **not** reproduce this run — leave that closed unless it returns.

**Outcomes / done when:**
1. Title pattern like: `Citation Generator (APA, MLA, Chicago, Harvard) | FreeDailyPro` (brand suffix required; keep under ~60 chars if possible).
2. Empty / insufficient fields: Copy and Add to Reference List disabled (or no-op with an inline message); no junk citation string.
3. Existing APA/MLA/Chicago happy paths from QA-412 stay PASS; style switch still does not spend a trial use.
4. No “free tools” wording; trial metering unchanged.

**Suggested direction:** Inspect the citation tool page + shared SEO title helpers; fix title/brand; gate actions on required fields for the selected style/source. Interpret freely against prior tool validation patterns.

**Constraints:** Professional Tools / trial uses wording. Ads stay. Do not expand into URL/DOI autofill or .bib export in this brief (capability backlog, separate).

**Process:** Inspect → restate → implement → verify against QA-412 cases A–C → DONE note.

Source: owner
