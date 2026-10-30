# B-0053 Homepage search addendum (to orchestrator B-0041): desktop placement, label, no-results state
Priority: P3      Estimated effort: 30 min      Report: #66      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect, challenge, implement, verify live, report per brief ID. B-0041 (orchestrator) already covers the Enter arrow/hint, suggestion timing and the GA search event — do those there; this adds only what B-0041 does not mention.

## Intent
The homepage (438 views, 33 key events in 28 d — analytics/2026-10-29-raw.md) routes people to tools through this box; it should be found instantly and never dead-end.

## Why (live Oct 29 ~9:42 PM ET, Chromium)
- Desktop 1280×900: the hero search ("What's on your mind?") is at y≈1100 — below the first screen. Mobile 390: top of page (fine).
- No accessible label (placeholder only, no aria-label).
- "zzqxv nothing" + Enter returns an unrelated tool list (cURL Converter, Event Landing Page Generator…) with no "No tool matches" message.
- Enter on "merge" works well (AI chips + Merge PDF/PPT/Video/Audio) — keep.

## Outcomes
- Search box visible without scrolling at 1280×800 and above.
- aria-label (e.g. "Search tools").
- Zero-match queries show "No tool matches 'X'" plus nearest 3–5 tools.

## Test cases
R66-HOME-02, R66-HOME-05 (report-66/test-cases/search.py; screenshots search-merge-desk.png, search-empty-*.png). Desktop 1280 + mobile 390, logged out.
Owner decisions needed: none.
