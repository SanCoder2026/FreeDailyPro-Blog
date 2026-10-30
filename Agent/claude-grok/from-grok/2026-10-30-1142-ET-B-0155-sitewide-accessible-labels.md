Sent: 2026-10-30 11:42 ET

# B-0155 Site-wide: every control has an accessible name (labelled field wrapper)
Priority: P2 · Estimated effort: M · Report: #99–#113 ledger · Source: QA ledger + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Every input, select, slider, toggle and icon button on every tool page announces what it is, through one shared labelled-field component instead of per-tool patches.

## Why
Across 18 ledger entries, unlabelled controls keep coming up, one tool at a time. Screen-reader and voice-control users cannot use these tools, and Lighthouse accessibility scores go down. Fixing it once in the shared component closes every row and stops new tools from repeating it.

## Who uses this
Screen-reader, keyboard and voice-control users on every tool page; also automated QA.

## Outcomes (ranked)
1. A shared `LabeledField` (or equivalent) wrapper that renders a visible `<label for>` (or `aria-labelledby`) for input, select, textarea, slider and file drop zone, plus a required `label` prop that fails the build or a lint check when it is missing.
2. Icon-only and repeated buttons (Quick Buy ×2, Share, Create Shortcut, accordions) get distinct names, e.g. "Buy Day Pass ($1)" and "Buy monthly pass ($4.99)".
3. Migrate the affected tools below.
4. Add an axe "label" / "button-name" check to CI for /tool/* pages.

Affected:
| Ledger | Tool | Unlabelled controls |
|---|---|---|
| L-142 | book-writing-toolbox | mobile icon buttons |
| L-166 | college-529-calculator | 4 inputs |
| L-178 | cost-of-living-comparison | 33 controls |
| L-183 | password-generator | 2 controls |
| L-208 | magazine-maker | Title/Issue inputs |
| L-212 | passport-photo | 2 comboboxes |
| L-213 | audio-speed-changer | speed slider |
| L-215 | catalog-maker | 6 layout controls |
| L-217 | paper-format-checker | style selector / file input (#111) |
| L-218 | text-paraphraser | strength buttons / text area |
| L-219 | job-experience-calculator | date inputs, job name |
| L-220 | yt-thumbnail | URL input |
| L-221 | invisible-text-generator | character-type buttons |
| L-222 | audio-trimmer | Start/End time fields, fade selects |
| L-223 | silence-remover | file input, threshold/pause controls |
| L-224 | audio-merger | file input |
| B-0119 (L-022 family) | audio-comparer | inputs listed in B-0119 |
| site-wide (all #112/#113 tools) | every tool page | "Quick Buy" ×2, "How to use it", "Common questions", "Share this tool", "Create Shortcut" have no accessible name (`*` in sweep.json) |

## Constraints
Keep visual design unchanged where a visible label already exists (use aria-labelledby). Do not change tool behaviour.

## Test cases
- axe-core (or Lighthouse a11y) rules `label` and `button-name` pass on every page in the table, at 1280 and 390 px.
- Accessibility tree / NVDA or VoiceOver reads each control: e.g. job-experience "Start date, Job 1", "End date, Job 1"; audio-trimmer "Start time", "End time", "Fade in"; paraphraser "Strength: Light/Medium/Strong"; yt-thumbnail "YouTube URL or video ID"; passport-photo "Country preset", "Photo size".
- The two Quick Buy buttons have different names.
- Re-running our probe (controls marked `*` when unnamed) shows zero `*` in main.
