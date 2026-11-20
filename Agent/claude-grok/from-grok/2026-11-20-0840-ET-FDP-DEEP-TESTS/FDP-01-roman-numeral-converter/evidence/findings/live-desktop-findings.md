Sent: 2026-11-20 08:40 ET

# Live desktop Chrome run (fresh profile), Nov 19 2026 ~9:20-9:28 AM ET
The tester's context was compressed partway through, so this is a partial record. The verbatim edge-case outputs are re-collected by the headless run (see edge-usage-findings.md).
- Breadcrumb "Home / Unit, Date & Everyday Calculators / Roman Numeral Converter". H1 "Roman Numeral Converter — Numbers, Years and Dates". Badges "Files never stored", "Runs on your device".
- 3 labelled inputs: Number→Roman (2026→MMXXVI), Roman→Number (MMXXVI→2026), Date→Roman (19.11.2026→XIX.XI.MMXXVI). Day.Month.Year / Month.Day.Year (US) radios, Separator dropdown (default dot). The note covers 1–3,999 plain letters and up to 3,999,999 with a bar.
- Live conversion as you type, a copy icon per result, and a collapsible "How 2,026 is written" step-by-step section. Chart tabs "1 to 100" and "Years 1950 to 2050" render correctly.
- NOT present: swap control, Share, history, value-in-URL. The title bar download icon is the PWA install prompt, not a CSV export.
- BUG (MEDIUM): in US (Month.Day.Year) mode the heading changes to "(month, day, year)", but the first field is still treated as the day. Typing 11 then 19 gives "Month must be between 1 and 12"; 19 then 11 works. FAQ input-order wording does not match the behavior.
- USAGE (HIGH, verify): the trial strip "Trial: 10 uses/day · N remaining today" was NOT seen. After Copy, Download CSV and Print, then a reload, localStorage fdp-usage-v1 = {"allowed":true,"usageToday":0,"limit":10,...,"scope":"dev:9852341c-..."}. No trial use was spent, against owner policy that copy/results count.
- Ads: one right-rail "Advertisement" (HELOC creative) that appeared shortly after load (possible layout shift); no overlap with inputs seen. No cookie banner.
- Reload shows default values (persistence unconfirmed); scroll position restored.
- Payment (/pricing): "$1 Buy Day Pass" opens an email prompt; "$4.99 Subscribe Monthly" goes to checkout.stripe.com. Stopped at both, nothing typed.
- Console: PWA warning "Banner not shown: beforeinstallpromptevent.preventDefault() called...".
