Sent: 2026-11-20 08:40 ET

# FDP-11 Paycheck Calculator (paycheck-calculator): deep test report for Claude

- **Written:** 2026-11-19 13:55:40 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/paycheck-calculator. Row 11 of TEST-ORDER.md. Cluster C25 with income-tax-calculator (#9) and state-tax-calculator (#10), which share the stateTaxData engine. **GSC data is not available.**
- **Classification:** Professional Tool, Finance, Tax & Retirement. 10 trial uses a day, $1 day pass / $4.99 monthly.
  - Reading results is free. Copy result, Save as text and Print: the page note says the first costs **1 use per visit**; all three are blocked at 0 (observed).
  - Per owner policy, copying and results may count as trial uses, so only wording that promises otherwise is a defect.
- **Testers:**
  - **Desk review:** curl of the tool, 10 hreflang locales and /ar, the blog, /terms, /faq; JS bundles (PaycheckCalculator, calcChecks, useLogToolUsage); WebSearch for competitors (ADP, PaycheckCity, SmartAsset) and the brand query.
  - **YouTube video:** metadata, 44 frames, 2 contact sheets, crops.
  - **Headless Playwright:** 30 calculation cases + 8 blog cases + 1 video case (federal/FICA checked against an independent 2026 reference script); export gate in 12 contexts; keyboard, axe, phones; matrix: 10 profiles, 10 locales + /ar, 6 geos, axe.
- **Constraints kept:** guest only, no sign-in, no card or email entered (stopped at the cap dialog), no ad clicks, no API or MCP calls, no site or repo changes.
- **Sign-in:** nothing on this tool needed sign-in. **No URLs were blocked by sign-in.**
- **Pending:** all 12 fresh gate contexts (13:40–13:41 EST) loaded at 0 remaining (display-only; the only context with uses, at 13:39, was the read-only cases run), so the cost of the first export with uses left was not observed. **Needs re-run after midnight UTC (7:00 PM ET).** Row 11 was added to RERUN-AFTER-RESET.md (copy in `scripts/`).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real components, then restate the problem, challenge anything that looks wrong, and pick the fix that fits how FreeDailyPro has shipped similar work.

Components to look at:
- **PaycheckCalculator** (`evidence/js/pc.pretty.js`): input parsing for 401(k) %, state rate, HSA/FSA, hours; the default state "CUSTOM"; the result region.
- **calcChecks** (`evidence/js/calcChecks-BMsAp5Al.js`): export `p` already implements the 2026 401(k) limit with catch-up groups; this tool imports only `a` (the number check).
- **stateTaxData `s()`** (shared with #9/#10): HoH, Utah, state-specific pre-tax treatment (PA 401(k), CA/NJ HSA).
- **The Terms and FAQ trial wording.**

After you ship, rerun `test-cases.md` (PC-01…PC-29).

## Intent

Someone holding a job offer, or budgeting rent, wants the number that will actually land in their account each payday. The page gets federal tax and FICA exactly right. It loses trust when it accepts impossible inputs (a $60,000 401(k), a 150% rate) and shows a confident, sometimes negative, take-home, and when its state side lags the sister State Tax Calculator.

## Why: what the evidence says

- **The core is exact.** Federal tax, Social Security (wage-base cap), Medicare and Additional Medicare (incl. MFS $125k) match the independent 2026 reference in all 30 cases; section 125 vs 401(k) FICA treatment is right; hourly overtime is right. Blog TX figures match to the cent.
- **No 401(k) limit (P1).** $200k × 30% deducts $60,000 with no warning (2026 limit $24,500). The check exists in the shared calcChecks module but isn't wired in.
- **Silent negative take-home (P1).** 401(k) 150% → −$220.67 per check; Custom state rate 150% → −$1,957.98. No message.
- **Shared engine (P1, same fix as #10).** HoH = single (CA HoH $85k $3,660); Utah deducts instead of crediting ($2,621 vs ≈ $3,103 at $75k).
- **Wording (P1, shared).** /terms and /faq say calculators never use a trial use; the page note says copy/save/print uses 1 per visit (intended). Fix the Terms/FAQ wording.
- **Smaller issues (P2):** PA 401(k) and CA HSA state treatment; no HSA/FSA limit; 200 h/week accepted; 401(k) "abc" → 0; default state Custom 0%; payroll programs and local taxes missing although #10 has them; stale blog CA paragraph; old video; weak meta/FAQ; 8 untranslated locales; axe critical on the tabs; no aria-live; 9 px overflow at 320 px (header).

## Outcomes we want

1. Impossible or over-limit inputs get a clear message; take-home is never silently negative.
2. The state side matches the State Tax Calculator for the same person (filing status, Utah, payroll programs, local taxes, state pre-tax rules).
3. Video, blog, meta and Terms/FAQ match what the tool does now.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | Federal/FICA exact in 30 of 30 cases. Wrong or unvalidated: P07 (HoH), P09 (PA), P10 (UT), P11 (401(k) limit), P12/P17 (negative net), P13 (HSA), P15 (CA HSA), P21, P26. `findings/live-functional-findings.md`, `json/cases.json` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | Has 51 states, hourly/OT, 401(k), section 125, HSA. Behind ADP/PaycheckCity/SmartAsset on local taxes, payroll programs, limits, post-tax/Roth, bonus, W-4. `findings/desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Instant and clear; salary/hours validation good. Default state Custom 0%; deduction fields accept anything; on iPhone SE the result is below the fold. |
| 4 | Layout attractiveness | **PASS** (minor) | LOW | Clean on all 10 profiles. 9 px horizontal overflow at 320 px from the header menu button. `findings/devices-locales-findings.md` |
| 5 | Payment process | **PASS** | LOW | Cap dialog clear ($1 / $4.99); the test stopped there. Two headings for the same state ("Today's trial uses are done" / "You've used today's trial uses"). |
| 6 | Information correct | **PARTIAL** | HIGH | Footer honestly lists missing programs. Video shows an old UI and $19,236.18 vs $19,047.53; blog CA stale; Terms/FAQ trial wording vs the page note; meta says "federal tax and FICA" only. |
| 7 | Indexing | **PASS** | — | 200, self-canonical, #1 for the brand query (WebSearch index). **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Title generic, meta omits state/401(k)/hourly, H1 bare, FAQPage with 1 question, Offer without period, 8 of 9 hreflang alternates untranslated. es is translated and stronger. |
| 9 | Blog post | **PARTIAL** | LOW | /blog/paycheck-calculator: TX/401(k)/health/hourly/frequency figures exact; CA paragraph stale (no SDI). `json/blog-cases.json` |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | jNpP2-R9-eM, 132 s, 6 views, embedded. |
| 11 | FAQ / usage guide | **PARTIAL** | LOW | The 1 FAQ and How-to are accurate; no limits guidance; only 1 question. |
| 12 | Video shows current capabilities | **FAIL** | MEDIUM | 3-field old UI, pre-Additional-Medicare figure, "free" wording, internal sheet tab and bookmarks visible. `findings/video-findings.md` |
| 13 | Storage | **PASS** | — | Runs on the device; inputs not persisted (unverified absence of a network call: not network-audited). Trial state in localStorage `fdp-usage-v1` (display-only). |
| 14 | Sharing | **PARTIAL** | LOW | "Share this tool" only; no shareable result link. Exports trial-gated (intended). |
| 15 | Downloads | **N/A: pending** | — | Save as text / Print not observed with uses left (all contexts at 0). RERUN row 11. |
| 16 | Usage count | **PARTIAL** (behaviour pending) / wording **FAIL** | MEDIUM | At 0, all three exports are blocked (observed). First-export cost pending. Terms/FAQ say calculators take none: fix the wording (owner policy). Starting counts (display-only): the cases context (13:39 EST) loaded with 10 remaining and stayed at 0 used after 30 read-only cases (reading is free, as the note says); the 12 gate contexts (13:40–13:41) and the blog, video and kbd contexts loaded at 0 remaining. |
| 17 | Categorization | **PASS** | — | Finance, Tax & Retirement. |
| 18 | Location in site | **PASS** | — | Breadcrumb, link to Income Tax Calculator, blog. No link to State Tax Calculator from the result (suggest one). |
| 19 | AI need / demand | **PASS** (no AI needed) | — | Deterministic. High-demand query class (competitors are major brands). |
| 20 | Merge? | **N/A: keep** | — | Distinct job (per-check take-home). Share the payroll/local module with #10. |
| 21 | Remove? | **N/A: keep** | — | Exact federal core; #1 for its brand query. |
| 22 | Duplicates | **PARTIAL** | LOW | Same engine as #9/#10 (good), but the payroll-program and local-tax logic is duplicated only in #10, so results differ for the same person. |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`. 10 profiles all 200; only the 320 px header overflow. Geo contexts identical (USD, en-US numbers). Locales: only es is translated.

**Ads:** keep them in reserved fixed-height slots below the tool (as now). Never put one between the inputs and the result.

## Suggested direction (interpret freely)

1. **Limits (P1).** Import calcChecks `p` for 401(k) dollars (add an age group), cap % at 100, state rate at ~15%, HSA/FSA at the 2026 limits (warn), hours at 168. If deductions exceed pay, show a message instead of a negative net.
2. **Shared engine (P1).** The HoH and Utah fixes from #10 cover this tool too; add per-state flags for 401(k) (PA) and HSA (CA, NJ).
3. **Wording (P1, shared).** Align /terms and /faq with "Copying, saving or printing uses 1 per visit" (owner policy).
4. **P2:** prompt for a state instead of Custom 0%; reuse #10's payroll programs and local taxes; refresh the blog CA paragraph; re-record the video in a clean profile with trial-use wording; rewrite the meta ("…after federal, state and FICA taxes, 401(k) and HSA, salary or hourly"), add 4–6 FAQs and an Offer period; translate or drop the 8 English locale copies; fix the tab `aria-controls` and add aria-live to the result.

## Constraints

- Say "Professional Tools", "Premium Applications" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Owner policy: copying and results can count as trial uses. Fix the wording, not the gate.
- Don't change pricing in this work. The book watermark is intentional and separate.
- Counters are display-only evidence; no backend claims.

## Process

Inspect PaycheckCalculator input handling and stateTaxData `s()` → restate → propose → implement → verify with `scripts/pc-live.js`, `scripts/ref_federal.py` and `test-cases.md`; after midnight UTC run `scripts/pc-gate.js`.
