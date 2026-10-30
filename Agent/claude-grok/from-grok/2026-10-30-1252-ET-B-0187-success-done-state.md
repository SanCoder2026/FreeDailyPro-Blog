Sent: 2026-10-30 12:52 ET

# B-0187 One shared success / done state for every tool
Priority: P2 · Estimated effort: M · Report: #118–#121 (site-wide) · Source: QA retest cycle 2, Orchestrator 12:48 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
After any action, a person should know in one glance that it worked, what changed, and what to do next. If it didn't run, they should know why. Build this once as a shared component and use it on every tool, so tools stop inventing (or forgetting) their own.

## Why
The outputs are correct (admin-verified #118–#121), but several tools give no sign that anything happened:
- **Success with no status text:** watermark (L-242), extract-audio (L-246), fillable-forms (L-247) and flip-rotate-image (L-249). Each shows only a Download button after the action. All four outputs were verified correct in admin sessions.
- **Good existing models to copy:**
  - repair-pdf: "Recovered 2 pages… best-effort" (L-245).
  - flatten-pdf: "Flattened 3 fields — these values are now permanent" (L-250).
  - remove-pdf-pages: "1 page will be removed; 2 stay" (L-241).
  - color-picker-image: copy toast "Copied #fe0000" (L-235).
- **Silent no-ops (the button does nothing, with no reason given):**
  - Watermark with empty text (L-242).
  - Extract audio from a video with no audio track (L-246).
  - Required form field left blank (L-247).
  - Audio-merger silently drops files at 0 trial uses (L-224).
  - Audio-trimmer silently resets the end time (L-222).
  - Color-converter blanks on invalid input (L-238).
- **False confirmations** (a "Copied" toast with an empty clipboard, L-216) stay in **B-0156**; this brief must not reintroduce them.

## Who uses this
Everyone, but especially first-time visitors on trial uses, who judge the site by whether the first action visibly worked.

## Outcomes (ranked)
1. **A shared `ResultStatus` component**, shown right after an action completes. It has:
   - a success line naming what changed, with counts ("Watermark added to 1 of 3 pages", "Extracted 3.1 s of audio as MP3", "Filled 3 fields", "Rotated 90° clockwise — now 200×300");
   - the output size or format where useful;
   - the primary next action (Download / Copy) and optional "Continue with…" links.
   It's announced to screen readers (`role="status"`, aria-live polite) and placed next to the action button.
2. **No silent no-ops.** If an action can't run, the same component shows a reason line and focuses the field to fix, and the button is disabled with an explanation where possible. Examples: "Type the watermark text", "This video has no audio track", "1 required field is empty: agree".
3. **A done confirmation for downloads and copies:**
   - after a real download starts: "Downloaded <filename>";
   - after a real clipboard write succeeds: "Copied";
   - never shown when it was blocked or gated. B-0156 owns the gated wording.
4. **Consistent placement and style** across all tools, using the existing tokens; it doesn't cover the output.

## Affected tools / ledger rows
| Row | Tool | Gap |
|---|---|---|
| L-242 | pdf-watermark | no success text; empty-text silent no-op |
| L-246 | extract-audio | no success text; no-audio silent no-op |
| L-247 | fillable-forms | no success text; required-field silent no-op |
| L-249 | flip-rotate-image | no success text |
| L-222 | audio-trimmer | end time silently reset |
| L-224 | audio-merger | files silently dropped (0 trial uses; gating part → B-0156) |
| L-238 | color-converter | invalid input blanks with no message |
| L-245, L-250, L-241, L-235 | repair, flatten, remove-pages, color-picker | reference implementations — migrate to the shared component without changing their wording |

Per-tool briefs B-0172, B-0177, B-0180, B-0181 and B-0183 reference this brief for the status/no-op parts. Their other outcomes stand.

## Constraints
- Copy describes what actually happened; never claim a success that didn't occur.
- Gating, trial counters and paywall copy are out of scope (B-0156; policy is an OWNER DECISION pending Santosh). Labels are out of scope (B-0155).
- No layout shift over 0.1 CLS when the status appears (B-0041 history).

## Acceptance tests
1. Watermark t3.pdf, pages "2" → "Watermark added to 1 of 3 pages" plus Download; screen reader announces it.
2. Watermark with empty text → "Type the watermark text"; focus moves to the field; no processing.
3. Extract audio from v.mp4 → "Extracted 3.1 s of audio (MP3)". From silent.mp4 → "This video has no audio track" at load, with Extract disabled.
4. Fillable form with agree blank → "1 required field is empty: agree", focused. When complete → "Filled 3 fields".
5. Flip/rotate ab.png CW → "Rotated 90° clockwise — 200×300".
6. Copy on any text tool with a real clipboard write → "Copied", and the clipboard matches. When blocked → no "Copied" (B-0156).
7. Repair, flatten and remove-pages keep their current wording inside the shared component.
8. Every status node has role="status"; CLS < 0.1 at 390 and 1280 px.
