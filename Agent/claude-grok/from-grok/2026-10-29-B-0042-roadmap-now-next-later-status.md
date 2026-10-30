# B-0042 Roadmap: order the open briefs (Now / Next / Later) and keep a per-brief STATUS file
Priority: P1      Estimated effort: 20 minutes (STATUS file) + ongoing one-line updates

How we work with you: you are the implementation partner, not an order-taker. Read the referenced briefs, inspect the code, challenge any ordering that the codebase makes wrong, and tell us in your report.

## Intent
Turn 20+ open briefs into one revenue-ordered queue so each night's ~2 h goes to what earns money first, and make status visible in one file so the Orchestrator and Testing Bot can verify without guessing.

## Why / evidence
- Since Jul 10 2026: GA shows 3 purchases ($6.99) and AdSense $0.39 since Oct 24 (19% viewability). GSC: 575 clicks from 163K impressions, CTR 0.4%, avg position 18.1. Revenue today depends on (1) checkout working, (2) tracking being trustworthy, (3) search traffic feeding ads.
- B-0001..B-0023 are reported done in your reports; B-0024 onward have no status yet.
- RapidAPI sample code currently returns "missing API key" when run as written; live API testing (B-0040a/b) found parameters silently ignored. Launching new listings on top of that would burn the first impression.
- The owner wants a continuous loop: Claude marks done → Testing Bot retests independently → only then verified.

## Work queue (reference by number; content lives in each brief)
**Now** (tonight's must-do = first three)
1. **B-0041** ads never block tools on mobile, search Enter affordance, consent/GA fixes — protects the traffic we have and the owner's top UX ask.
2. **B-0037** analytics hygiene + key events + site-search event — every later experiment and the week-4 gate depend on trustworthy numbers.
3. **B-0027** checkout flow — the direct revenue path.
4. **B-0035** GSC indexing cleanup — 1,180 pages not indexed.
5. **B-0036** CTR lift (roman numeral converter: ~49K impressions at position 9).
6. **B-0040a/b bug section only** (Split PDF second file, ignored params in QR/Video-to-GIF/Merge/Image Resize/Audio, QR PNG, Invoice PDF) + RapidAPI sample-code "missing API key" fix — prerequisite for any listing work.
7. **B-0024** owner decisions and **B-0026** homepage video swap (small).

**Next**
8. **B-0038** AdSense placement/viewability — after B-0037 gives a clean baseline and consistent with B-0041 (B-0041 wins on any conflict).
9. **B-0028** listing generator, then **B-0029** RapidAPI platform check.
10. **B-0039 + B-0040** new task-level endpoints for the 20 wave-1 tools.
11. **B-0030** RapidAPI wave 1 — only after 6, 9 and 10 are verified by the Testing Bot.

**Later**
12. **B-0031** Postman sync, **B-0032** API.market copy, **B-0033** /developers per-API pages (all need B-0028).
13. **B-0034** weekly rank report + week-4 gate (clock starts when B-0030 is live).
14. **B-0025** off-topic blog heroes (after the hero agent delivers images).

Superseded: B-0015 (by B-0019).

## Status file (the main ask)
Create and maintain `Agent/claude-grok/from-claude/STATUS.md` (your folder; or tell us if an equivalent exists). One row per brief B-0001 onward:
`B-00NN | not started | in progress | done-pushed | live-and-checked | blocked | superseded | commit | one-line note/blocker | date ET`
- Update it in the same push as the work. Keep reports as they are; STATUS is the single current view.
- "blocked" must name the blocker (owner decision, dependency brief, access).
- The Testing Bot will mark verification in its own ledger; do not mark "verified" yourself.

## Outcomes
- STATUS.md exists with all briefs B-0001..B-0042 and is current after each night.
- Nights follow the queue above unless you explain a better order in the report.
- No listing launches (B-0030) before its prerequisites are verified.

## Constraints
- Standing owner decisions hold: Premium 2 trial uses/day, Professional 10/day; default marketplace pricing; "free" kept in SEO titles/meta, removed from visible copy only.
- No secrets in the repo; no deleting data or publishing externally without a recorded owner decision.

## Process
Inspect → restate the queue in your next report (agree or propose changes) → create STATUS.md → work Now items → verify live → update STATUS.

Owner decisions needed: none for this brief (open owner items stay in their own briefs).
Source: owner
