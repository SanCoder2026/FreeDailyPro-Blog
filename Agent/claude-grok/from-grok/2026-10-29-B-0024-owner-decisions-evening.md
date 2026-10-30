# B-0024 Owner decisions from Oct 29 evening

Priority: P2
Estimated effort: ~60 min

## Goal/why
Santosh gave these decisions on the evening of Oct 29. They close open questions from the QA backlog and the morning report. Shipping them keeps plan copy, trial counting and tool behavior in line with what he decided.

## What to change
1. **Team/Organization plans.** These are higher-priced tiers.
   - The Professional organization plan includes all Professional Tools.
   - The Premium organization plan costs more and includes everything in Professional plus all Premium Applications.
   - Update the purchase/confirmation emails and the plan copy to match. The emails currently say "All 250+ Professional Tools". Use the standing tool-count wording.
   - Do not invent prices. Use the prices already configured. If an organization plan has no configured price, flag it in your report and don't make one up.
2. **Trial counting.** Any download, share, save or print counts as one trial use.
   - Check that this holds across all tools, including Universal File Converter and Random Number Generator.
   - Santosh already gave you direct guidance on #4/#5. Follow that guidance; this item only confirms the rule.
3. **Small breadcrumb/footer SEO link section.** Do NOT enlarge it to 24px. It is small on purpose and is there for search engines.
   - If you can collapse or minimize it further without hurting crawlability or indexing, do it. The links must stay in the HTML as real `<a href>` anchors and must not be hidden from crawlers with `display:none`.
   - If you can't minimize it safely, leave it as is.
   - Close the accessibility-audit item on these links as won't-fix.
4. **Ringtone maker.** The maximum length is 1 minute for both iPhone and Android. This replaces the earlier 30s/40s caps. Update the limits, the UI copy and any validation.
5. **Privacy Policy wording and homepage tiles (#1, #2).** Follow Santosh's direct guidance to you.

## Acceptance criteria
- Each item (1–5) is verified live and reported in `Agent/claude-grok/from-claude/` with a status (done / partial / blocked / not started) and a verification status.
- Purchase emails and plan copy describe the Professional and Premium organization tiers correctly, with no invented prices.
- A download, share, save or print uses exactly one trial use on every tool you checked. List the tools you checked.
- The SEO link section is unchanged in size or minimized. Its links are still real anchors in the server HTML.
- The ringtone maker accepts clips up to 60s on iPhone and Android and rejects or trims clips longer than that.

## Not in scope / do not decide
- Do not set or change prices or billing configuration.
- Do not remove the SEO links or hide them from crawlers.
- Do not change the trial limits: Premium Applications get 2/day, Professional Tools get 10/day.
- No database changes beyond normal app behavior. No secrets in files.

## Owner decisions needed
None. All decisions are recorded above.

## Source
owner
