# B-0060 Unit Converter and Grammar Checker never send tool_completed, so GA can't see their usage
Priority: P2      Estimated effort: 30–45 min      Report: #72      Source: Testing Bot      Related: B-0037 (analytics hygiene, open)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
We need to know which tools people actually finish using, so we can decide what to improve and where Day Pass prompts make sense. Two of our highest-impression tools are invisible in GA today.

## Why
- On compress-pdf, a download fires `tool_completed` (QA #68 and #71, comp-scan.json).
- On unit-converter, a result read plus 2× "Copy result" (which spends a trial use) sends **only page_view** (Oct 29, 22:33–22:34 ET, desktop + mobile; unit.json).
- On grammar-checker, 14 "Check Grammar" runs (which spend a trial use) send **only page_view** (22:36–22:37 ET; gram.json).
- These pages carry 4,782 + 8,397 GSC impressions (analytics/2026-07-10-to-now-raw.md). B-0037 already notes that tool_completed fires *too often* elsewhere (275 events from 14 users), so the event is inconsistent in both directions.

## Outcomes
- Every tool sends exactly one `tool_completed` (with tool_id) per completed run. "Completed" is the same action that spends a trial use: copy/save/print for the unit converter, Check for the grammar checker.
- A short audit lists which tools fire it today. Fix the missing ones in one shared hook rather than per tool, if the code allows.

## Constraints
No new consent banners; GA config and consoles stay read-only for QA. Follow B-0037's dedupe rule.

## Test cases
Fresh visitor → unit converter: type 5, Copy → one tool_completed; Copy again → none. Grammar: Check twice → one per run (or per visit; state which you choose). Compress: download → still exactly one.
