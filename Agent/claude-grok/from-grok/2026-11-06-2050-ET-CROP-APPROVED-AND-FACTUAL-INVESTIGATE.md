Sent: 2026-11-06 8:50 PM ET (America/New_York) — confirmed retry after GitHub access returned.
This file is the handoff. Local “UNSENT / SCM blocked / do not push” lines in the source drafts are stale and do not limit this send.

# Crop PDF reachability (approved) and seven factual checks

## How to work with us
Inspect the live FreeDailyPro page and the source that actually renders it. Restate what you find, challenge anything weak, and choose the implementation that fits existing tool patterns. Suggested markup and mockup pixels are evidence of intent, not a spec. If a claim below does not match the code, stop that item and say so.

## Intent
On a phone, Crop PDF’s primary action stays in reach: Apply Crop while the file is ready, then Download after the crop exists, with margin / Auto-trim / scope options folded and still available. Separately, seven bot observations need a look: two desktop ad-coverage cases on the existing L-004 / B-0041 family, and five help-copy contradictions. Confirm each one before changing copy or layout.

## Why this is in from-grok now
Santosh, Nov 6 2026, 8:46 PM ET: “Approve Crop PDF’s sticky Apply/Download controls and folded options.”
Santosh, Nov 6 2026, 8:48 PM ET: “Yes, retry sending the pending briefs and approved Crop PDF changes to Claude now.”
Those two statements are the only owner approval in this file. Every other finding is a named bot observation. The 8:48 PM statement authorizes sending the pending factual briefs. It does not approve held SEO, AI, pricing, or trial-policy work.

An earlier brief, `2026-11-06-0857-ET-QA409-TIP-ADS-BOOK-WORDING-CROP-JSONLD.md`, told you to leave Crop sticky bars alone until Santosh decided. That hold is lifted for sticky Apply, then Download, and folded margin / Auto-trim / scope options only. The JSON-LD price work in that brief stays where it is. Do not redo it here.

## Outcomes
1. Approved Crop reachability is implemented and checked at 375 and 390, with desktop left intact.
2. Each factual item is either confirmed and fixed with the smallest change, or reported as unconfirmed. An unconfirmed ad overlap stays open.
3. Held items below are untouched.
4. Ads, prices, tiers, trial charging, and crop output stay as they are today.

## Approved — Crop PDF sticky Apply, then Download, and folded options
Source of the audit measurements and mockups: Web Design local Crop PDF mobile draft, Nov 6 2026. Santosh approved the outcome. Web Design had not independently re-verified the mockups when that draft was written. The mockups are schematic composites, not live code, and they are not in this commit.

Intent on `/tool/crop-pdf`, phone widths 375 and 390: after a file loads, Apply Crop is visible without scrolling. Margin inputs, Auto-trim, and apply-to scope (all pages / this page / page range) sit in one compact disclosure that shows the current summary and still works when opened. Defaults and Auto-trim stay the fast path. After Apply, the result is what the user sees, and Download is the sticky primary. Options collapse to a short “applied” summary.

The draft’s measurements, for you to remeasure: ready-state Apply Crop (about 108×36) sat near y≈1340 at 375 and y≈1359 at 390, about 1.6 screens down, behind the preview, four margin fields, Auto-trim, and three scope chips. Done-state Download (about 115×44) sat at the same depth. The crop itself worked on that audit (CropBox 612×792 → 496.8×662.4 on both pages; a cropped PDF downloaded). Treat that as a reachability report, and confirm it.

Mockup files named in the draft, not shipped here: `fix1-sticky-apply-before-after.png`, `fix2-download-first-before-after.png`. They illustrate a sticky Apply bar and a sticky Download bar above an advertisement area. One “before” panel shows a control labeled New and a Save to Google Drive action. The “after” panel shows “Crop another” and does not show Save to Google Drive. That label drift is mockup noise. Keep the live secondary actions. Do not rename New, and do not drop Save to Google Drive, as part of this work.

A line in the local draft said Apply does not spend a trial use and Download does. That was read off the UI. It is not backend proof. Read the current charge point and leave it. Keep the live trial disclosure that already exists. Do not add a badge that appears only on the mockup, and do not change the button into a new metering promise.

Suggested direction, yours to discard: a disclosure of about one row for the options, and a sticky action bar sitting above the ad anchor with page padding so the bar and the anchor both remain visible. Reuse a sticky-action pattern from a sibling PDF tool if one already exists. Smallpdf was the audit’s benchmark for a bottom action, not a layout to copy.

Done when:
- At 375 and 390, after load, Apply Crop is on screen without scrolling, with the folded options summary visible.
- Opening the disclosure still changes margins, Auto-trim, and scope, and the crop uses those choices.
- After Apply, Download is on screen without a hunt, and the options read as applied.
- Sticky UI sits clear of the ad anchor and does not cover the last page content. Anchor, auto-ads, in-content, and “Discover more” still load. Keep `.tool-area.google-auto-ads-ignore` if that is the current exclusion.
- Desktop is unchanged or clearer.
- Cropped PDF output matches today’s crop for the same margins and scope.
- Trial pool, prices, and the moment a use is consumed are unchanged. Visible copy stays Professional Tools / trial uses: Trial 10/day, $1 day pass, $4.99/month, and whatever “uses 1 trial use” line is already live.

## Factual — investigate, then the smallest fix only if it is real
These seven are not owner instructions. Standing rules still apply: every ad and ad type stays enabled; protect controls by reserving or relocating space; Professional Tools and trial-uses wording; no price, tier, or charging change.

### 1. Passport Photo FAQ Q4 vs the live preset list
Source: Programmatic SEO bot, SEO N Section A, live check ~1:52 PM ET Nov 6 (`freedailypro-seo-engine/hourly/2026-11-06-1400-four-page-upgrades-n.md`).

FAQ Q4 (“Which countries' size presets are included?”) was reported as listing only US, UK/EU, Canada, India, and China visa. The same page’s live UI and FAQ Q10 were reported as twelve templates: US, UK, EU/Schengen, Australia, Japan, Canada, India, China Visa, New Zealand, Ireland, Singapore, South Korea (ids in the Passport Photo script).

If Q4, Q10, and the live template ids disagree, rewrite Q4 so all three tell the same list, or point Q4 at that full list. One accurate list is enough. Leave every other FAQ alone.

### 2. CSS/JS minifier desktop ad coverage — existing L-004 / B-0041, no new id
Source: Pinterest Manager batch11, desktop screenshot and notes ~1:50–2:57 PM ET Nov 6 (`/tool/css-js-minifier`, CSS mode after a synthetic `.css` upload). Screenshot name in that draft: `pinterest-plan/drafts/qa-batch11-css-js-minifier-upload-desktop.png` (local, not in this commit). About 1280×715, no device emulation.

The screenshot was read as: left rail over the Input edge and the upload affordance, right rail over the minified-output edge, anchor over the lower edge of both panes and the Download row. Batch11 also recorded HTML Copy and Download content as pass, and file upload as pass, and noted controls still clickable at some points. File this as desktop visual coverage and partial hit-target risk.

Testing Bot QA-419, cited as inconclusive in the QA-420 addendum: the Nov 6 retry evidence says that retest is inconclusive because ads were absent. Overlap is not cleared. Mobile coverage for this tool was not tested. There is no total-lockout claim.

If you still see ads over Input, Upload, Copy, Download, or either pane at a ~1280 desktop width, reserve or relocate those units so the controls and pane edges are fully visible, and leave every ad type enabled. If this load shows no overlap, say so and leave L-004 open. Do not mark it fixed from a single clear load. A shared reserve with the Reverse Video case is appropriate only if the code shows one cause.

### 3. India Income Tax FAQ vs a dual-regime UI
Source: Programmatic SEO bot, SEO P Section A row 1, ~3:50 PM ET Nov 6 (`freedailypro-seo-engine/hourly/2026-11-06-1600-four-page-upgrades-p.md`). Page `/tool/india-income-tax`, HTTP 200, Professional `co=10` in that audit.

The bot read the live What/How/UI as calculating and showing Old Regime and New Regime together (87A rebate with marginal relief, surcharge, 4% cess). It read the only FAQ as telling the visitor to check which single regime the calculator is estimating under.

This is a possible help-copy mismatch. It is not a proven tax-law defect, and it does not reopen the L-202 math check. Read the page and the script. If both regimes are actually shown, rewrite that FAQ to say so. If the page already says it is not tax advice, or tells the reader to confirm the current year, keep that caveat. If the UI does not show both, leave the FAQ and report what the UI does. No gazette certification, no new FAQ set.

### 4. Arrivals board FAQ Q7 vs Q2 on storage
Source: Programmatic SEO bot, SEO Q Section A row 1, ~4:55 PM ET Nov 6 (`freedailypro-seo-engine/hourly/2026-11-06-1700-four-page-upgrades-q.md`). Page `/tool/arrivals-departures-board`, HTTP 200, Professional `co=10` in that audit.

Reported copy: FAQ Q2 says flight numbers “are saved in the project file.” FAQ Q7 (“Is my data stored?”) says “No. It stays in your browser tab and is erased when you close it.” The bot says the page uses `ProjectBar` / `useProject`, and that sibling event tools already mention the project file in their storage FAQs.

Check Q2, Q7, and the project-file path before editing. If the guest can save or download a project file and the tab-close sentence ignores that, align Q7 (and its FAQ schema if the schema repeats Q7) with Q2 and with the sibling wording you confirm in code: cleared when the tab closes unless the guest saves or downloads the project file. State “nothing is uploaded” only if the code path shows that. If the code does not save a project file, do not invent one, and report the contradiction instead. Do not add server storage or live flight tracking.

### 5. Reverse Video desktop ad coverage — same L-004 / B-0041 family, separate page
Source: Testing Bot QA-420, 2026-11-06 5:51 PM ET, addendum prepared ~5:52 PM ET. Page `/tool/reverse-video`. Screenshot name: `qa420/shots/03-loaded-720p-ads-cover-left.webp` (local, not in this commit). Desktop, 1280×800 screen, 100% zoom, Guest, ~5:47 PM ET.

At 100% zoom the left fixed unit covered the loaded filename (only `…ood-720p.mp4` visible), the start of the 480p checkbox label (only `…o 480p so a longer clip fits in memory` visible; checkbox hidden), and most of Reverse (a thin teal sliver left of Reset). It also covered part of the trial line and the “Files never…” badge. QA-420 assigned the blockage to that left unit. A second unit sat over the About/video column and a third sat in the right gutter. Visual coverage confidence in the report is high. Those controls were not clicked at 100%, so click-through is unknown. Tester x-ranges are estimates. There is no total-lockout claim.

At 90% zoom the checkbox and Reverse were fully visible, and 480p → Reverse → Download passed (`reversed-480p.mp4`, 854×480). The counter moved 10 → 9 on Download. That zoom is a tester workaround, not a fix.

Testing Bot QA-421 is named only in the Nov 6 retry evidence update. The QA-421 report is not among the eight source drafts, and those drafts do not name its URL. The update says a later load showed ads clear of the controls and the exposed actions worked. A clear load does not clear intermittent coverage, and it does not clear QA-419 or QA-420. Do not guess which URL QA-421 used.

Desktop only. Mobile was not tested. If 100% zoom with ads on still paints over the filename, 480p checkbox, Reverse, or Reset, reserve or relocate so those controls are fully visible and the checkbox and Reverse respond at 100%. Ads stay on the page. If this load is clear, leave the page instance open and say so.

### 6. Base64 FAQ vs the file control
Source: Conversion Optimization bot, `freedailypro-growth-orchestrator/conversion-packages/2026-11-06-revenue-review/UNSAMPLED-PROFESSIONAL-COPY-PROPOSAL-1800.md`, ~5:45–5:47 PM ET Nov 6. Page `/tool/base64`, HTTP 200.

Reported How-to: “To encode a file, choose it under ‘Encode a file’ (up to 3.0 MB; it never leaves your browser)…” Reported FAQ (“What is Base64 encoding actually used for?”): “This tool converts text; it does not take image or other files.” Reported served script `Base64Tool-xhsXnyAY.js`: an `input` with `id:"b64-file"`, `type:"file"`, and an Encode-a-file label. Runtime encode success, privacy, and trial charging were not verified.

The copy conflict to check is the FAQ denying files while the page exposes “Encode a file.” Actual file support and the size limit need verification before the FAQ states them. If the control is real, replace the denial with a sentence that points at “Encode a file” and its displayed limit, and keep the rest of the Base64 explanation. If encode-a-file is absent or the limit differs, match the FAQ to what you verified. Do not add file types, server storage, or a metering change.

### 7. Lorem Ipsum FAQ sentence range vs the length labels
Source: Testing Bot QA-423 (`qa423/2026-11-06-2019-ET-QA-REPORT-423.md`), staged ~8:45 PM ET Nov 6. Page `https://www.freedailypro.com/tool/lorem-ipsum`, signed out, ads on.

Reported FAQ: “A paragraph contains between 3 and 7 sentences…” Reported UI: Short (2–3), Medium (4–6), Long (7–10). Observed Short runs produced 3 and 2 sentences; Long produced 7 and 9, which matches the labels. This is help copy. It is not a generator fault.

If the FAQ (or a mirrored tip/Details line) still states a fixed 3–7 range, make that sentence agree with Short / Medium / Long, or change the labels to one range the generator actually uses. Prefer the FAQ edit. Leave the generator, ads, and trial metering alone. QA-423’s separate note that Copy showed no trial debit (10→10) is held. Do not create an L-id for it.

## Excluded and held
Do not implement any of these from this file:

- SEO N, P, Q, L, and M Section B title, meta, H1, brand, and length proposals.
- Passport stale “free” wording inside a video recording. Live Passport DOM was already described as Trial 10. That item stays held.
- Lorem Copy 10→10 trial-debit / Copy-spend policy candidate.
- QA-414 metering and Copy-spend policy.
- Optional AI features, and any new capability (file types, storage, flight tracking, crop features).
- Older API backlog. It was not in the eight source drafts.
- The five factual items already sent in `61451d748f15afd2ec45513aecbde83e040ffed9` (`2026-11-06-1412-ET-FACTUAL-TIP-FAQ-L-M-SECTION-A.md`): email-extractor tip, audio-to-subtitles plain-text export, extract-pdf FAQ Q5 order, pdf-watermark logo formats, pdf-watermark Hindi/script. Leave them to that brief.
- Crop work outside sticky Apply / Download and the folded margin, Auto-trim, and scope options: 44px resizing, Feedback floater, JSON-LD / schema price, header overflow, new crop capabilities. Touch-drag (`2026-11-01-1511-ET-CROP-PDF-TOUCH-DRAG.md`) and the auto-trim FAQ accuracy brief (`2026-11-01-1456-ET-PDF-FAQ-ACCURACY-CROP-SPLIT-ROTATE.md`) are different briefs.

## Conflicts in the source drafts
Read these before treating a draft sentence as fact.

1. The Crop draft’s status line said direct owner approval was still pending, and it said “keep it private/on-device and free-first.” Approval is the two Santosh quotes above. Positioning stays Professional Tools and trial uses. “Free tools” and free-first wording stay out. Preserve on-device behavior only where the tool already works that way.
2. The same draft’s Apply-versus-Download trial split is an unverified UI reading. Preserve the runtime charge point you find in code.
3. Crop “after” mockups disagree with the “before” panel on secondary labels (New versus “Crop another”; Save to Google Drive visible in one before panel). Approved scope does not rename or remove those controls, and it does not add a mockup-only trial badge.
4. QA-419 “ads absent” is the reason given in this retry’s evidence update. The QA-420 addendum only calls that minifier retest inconclusive. Both agree the overlap is not cleared. The screenshot file itself is not in this commit.
5. QA-421 has no report and no URL in the eight drafts. Use it only as: a later clear load does not retire intermittent coverage.
6. Several drafts forbade git push because CloudAgent SCM was blocked. That block is over for this handoff. It does not add scope.

## Dedup
All eight source items are new to `from-grok/` as of this file. None of them are the five L+M items in commit `61451d7`. Minifier and Reverse Video join existing L-004 / B-0041. They do not get new bug ids. Minifier and Reverse Video are separate pages.

| # | Item | In this file | Already on main |
|---|---|---|---|
| 1 | Passport FAQ Q4 preset list | Factual, confirm then copy | No matching brief |
| 2 | CSS/JS minifier desktop ad coverage | Factual, L-004 / B-0041 | No minifier brief in Nov 6 from-grok |
| 3 | India Income Tax FAQ vs dual regime | Factual, confirm then copy | L-202 is a math check, not this FAQ |
| 4 | Arrivals FAQ Q7 vs Q2 storage | Factual, confirm then copy | B-0267 is times/exports, not this FAQ pair |
| 5 | Reverse Video desktop ad coverage | Factual, L-004 / B-0041 | No QA-420 brief on main |
| 6 | Base64 FAQ vs Encode a file | Factual, verify support then copy | B-0185 is charset/detect, not this FAQ |
| 7 | Lorem FAQ 3–7 vs Short/Medium/Long | Factual, help copy | No matching FAQ brief |
| 8 | Crop PDF sticky Apply/Download + folded options | Approved | 0857 held sticky; this file lifts that hold only |

## Constraints
- Keep every ad and every ad type enabled. Reserve or relocate so controls stay clear. Anchor ads stay off sticky action bars.
- Professional Tools: 10 trial uses/day, $1 day pass, $4.99/month. Say trial uses. Do not say “free tools.”
- Do not change pricing, tier, Premium, Workflows, or when a trial use is consumed.
- Do not treat a button label or a mockup as proof of backend charging.
- No title, meta, or H1 edits in this file. No AI. No uploads or publication. No database work.

## Process
Inspect the live page and source → restate the item → challenge the weak parts, including the conflicts above → implement only the approved Crop outcome and any factual fix you confirmed → verify Crop at 375 and 390 with a margin-heavy PDF (load → Apply → Download), ads still present, crop bytes and trial behavior unchanged → for the two ad pages, check a desktop width with ads on and leave a clear single load marked open → write what you did, and what you refused, in the next from-claude status. This handoff does not claim you have read it.
