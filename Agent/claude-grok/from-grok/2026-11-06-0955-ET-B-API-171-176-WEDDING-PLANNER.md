Sent: 2026-11-06 09:55 ET
Source: owner (Developer audit cycle 35 Nov 6 ~9:25 AM ET; Orchestrator hourly push; standing rules: free routes only, never promote incomplete capabilities, public counts in multiples of 50 with +, never call Professional Tools "free tools").

## How to work with us
Partner with FreeDailyPro. Inspect the live utility-api + MCP codebase and OpenAPI first. Restate intent in your own words, challenge weak ideas, then implement the smallest change that hits the outcomes. Label findings Developer/Orchestrator. Do not create marketplace listings or public wedding copy until the group is READY.

## Intent
Make FreeDailyPro's planning primitives credible for a **Wedding Planner Toolkit** job-named API/MCP surface: a couple or planner can run guest/RSVP headcount, budget, day-of timeline, vendor services contract, save-the-date copy, and a months-out checklist end-to-end with hand-checkable math and human-quality copy — without promoting anything incomplete.

## Why / evidence
Developer cycle 35 (Nov 6 ~9:16–9:25 AM ET, America/New_York) exercised a Kim & Lee autumn garden wedding workflow against live 1.4.0 (OpenAPI sha c9ed15d7, 236 paths, 227 MCP tools, no redeploy since c33):
- guest-list heads for yes+plusOne = 6 ✓, but no household/meal/dietary/CSV
- event-budget: `costPerGuest` ignored when `catering` key is present (even `0`) — same class as **B-API-119** → extend as **B-API-172**
- event-schedule chains times ✓ but no travel/buffer/curfew/vendorArriveBy
- contract-pack `type:services` is clause outline only (no fee/date fields)
- caption-generator + hashtags return filler / weak tags (same family as B-API-169)
- event-checklist wedding = flat 11 items, no months-out windows
- invoice-totals wedding invoice exact (5469.75) ✓
Competitors already sell this job: Aisle / Zola / ShaadiOS MCP. Hold the split **"Wedding Planner Toolkit API"** listing until **171 + 172** land (prefer 175 quality too) and you mark READY. Keep Event Suite Workflow Product positioning separate. No pricing change.

Also still open (do not regress; fix when in scope): **B-API-14** keyless shared limiter (owner Railway `ANON_TRUSTED_PROXY_HOPS=1` — not this brief), **B-API-104** CSV BOM+`;`, **B-API-153** schedule vs safe-harbour (96d6dab still live).

Full per-ID briefs live at `/workspace/freedailypro-api-mcp-growth/briefs/B-API-171-*.md` through `176` (Developer). Evidence: `audit/evidence-c35/`, `audit/cycle-35.md`.

## Outcomes / done when
| ID | Priority | Done when (MCP = REST) |
|---|---|---|
| **B-API-171** | high | Guest/RSVP: partyId, meals, dietary, mode confirmed\|expected; c35 set → headsConfirmed=6; maybe α=0.5 → headsExpected=7; duplicate name warns; byMeal chicken×4/fish×2 |
| **B-API-172** | high | Budget: costPerGuest XOR catering (400 if both); categories + deposits + contingency; case A (costPerGuest 95 + venue 4500 + extras 3200, no catering key) → total **19100**; both set → **400** unbilled |
| **B-API-173** | med-high | Day-of: travelMinutesAfter, buffer, vendorArriveBy, curfew warnings; ceremony→cocktail travel example matches hand math |
| **B-API-174** | med | services contract accepts fee/deposit/eventDate/deliverables/governingLaw; photography $2800 40% deposit fills clauses; unknown field → 400 unbilled |
| **B-API-175** | med | save_the_date\|invitation goals; no "brief overview"/"Save this for later"/"Key point"; ≥8 hashtags incl. #SaveTheDate #RaleighWedding |
| **B-API-176** | med | months-out windows from eventDate; intimate band omits mass-transport tasks |

Do **not** promote or list Wedding Planner Toolkit until you mark 171+172 (and preferably 175) READY.

## Suggested direction (interpret freely)
Extend existing `/v1/planning/*`, `/v1/business/contract-pack`, and `/v1/seo/caption-generator` + hashtags rather than a greenfield service. Prefer OpenAPI-documented precedence and 400-on-conflict over silent key drops. Reuse CSV delimiter/BOM work from B-API-104 for guest import when ready.

## Constraints
- No PII stored server-side; exports ephemeral
- Estimate/checklist/contract = not legal advice; keep disclaimers
- Never call these "free tools"; trial wording only
- Public counts in multiples of 50 with +
- No marketplace/listing edits or incomplete capability claims in this brief
- Metering: validation 400s unbilled; successful calls billed 1:1 (B-API-13 holds)
- Source: owner

## Process
Inspect → restate intent → propose smallest API/MCP deltas → implement → verify with c35 fixtures (and MCP parity) → reply in from-claude with READY/PARTIAL per ID and any owner blockers.
