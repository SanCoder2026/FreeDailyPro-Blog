Sent: 2026-11-20 08:40 ET

# FDP-10 State Tax Calculator: priorities

- **Written:** 2026-11-19 13:33:46 EST (box `date`, ET).
- Each item points to a repro in REPRODUCE.md (R-n) and to test cases in test-cases.md.
- **No P0 for this tool.** The shared trial-meter P0 (fresh contexts at 0, FDP-02 to FDP-08) still applies site-wide and is display-only.

## P1
1. **Head of household computed as single in every state** (R-1; ST-05…ST-08). This is the shared engine `stateTaxData s()`, so #9 and #11 are affected too.
   - CA HoH $75k: $2,774.57 vs $1,118.19 (FTB Schedule Z, std $11,412), +$1,656.
   - NC HoH: +$254 (std $19,125).
   - NY HoH = single.
2. **Utah modelled with a standard deduction instead of the taxpayer credit** (R-2; ST-12). $75k single: $2,621.05 vs $3,103.45 (TC-40: 4.45%, credit 6% × 16,100 phased out at 1.3% above $18,696), about −$482, rising to −$716 above about $93k.
3. **Non-numeric income shows a confident $0.00** (R-3; ST-16, ST-17). "85k" and "abc" give no error and no aria-invalid; the income tax tool rejects the same input.
4. **The embedded video shows a wrong result** (R-4; ST-38). The old UI shows California $75k = **$9,975** (13.3% on all income) vs $2,774.57 now. It also has "free" wording and personal bookmarks.
5. **Trial wording** (shared with #9; owner policy: the charge is intended). /terms "calculators … take no trial use at all" and /faq "tax calculators … never use a trial use" vs the tool's "Copying, saving or printing uses 1 per visit". **Fix the wording in the Terms and FAQ.** (ST-30…ST-33)

## P2
6. **Personal credits omitted** while the FAQ says "any state credit is taken off": OR $256 (OR-40), DE $110 (30 Del. C. § 1110); likely IA $40 and the RI exemption. (ST-13, ST-14)
7. **The local notice says "not included"** even when a city or county line is included (NYC, MD counties, Philadelphia). (ST-24)
8. **The NY typical-local box (3.5%) applies to all NY residents** and to NY in Compare; it should be NYC/Yonkers only. (ST-25)
9. **Compare rows aren't keyboard-operable;** axe `scrollable-region-focusable` serious ×1. No aria-live on the result. (ST-35, ST-36)
10. **Two export bars** duplicate each other, and the "Copy report" cap dialog says "downloading". (ST-34)
11. **The blog $95k table is stale** (NY $4,652 → $4,564.75, CA $4,847 → $4,589.98, OR $7,763 → $7,738.88), plus the "federal standard deduction as starting point" sentence. (ST-39)
12. **All 9 locales are English duplicates;** the Offer has no billing period; the sitemap video title says "Free". (ST-40)
13. **Unverified >$100 differences vs SumAtlas** at $75k single: SC, WI, NE, AR, GA, MT, ME, AZ. Check them against each 2026 state form.

## Re-run after midnight UTC
- None. All export actions were observed with uses left and at 0.
