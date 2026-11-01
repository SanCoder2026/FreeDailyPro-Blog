Sent: 2026-11-01 08:59 AM ET
# ADDENDUM to 0852 AUDIO & SCREEN TEST KIT: three-layer packaging (B format)

**Working with us:** same partner framing as the 0852 brief. Inspect, challenge, and pick the best design. Full spec: /workspace/freedailypro-growth-orchestrator/plans/2026-11-01-audio-screen-test-kit-plan.md (ADDENDUM section).

## Intent
Santosh, 8:58 AM ET: "professional tools is first layer, we must have it, then reuse to offer premium complex applications by combining multiple tools, if its possible to create pretty large workflow product then we will do it, it can then support if needed saving on server." We want the kit to grow usage (Layer 1) and earn money by reusing those tools in Premium apps (Layer 2) and one Workflow product (Layer 3).

## Why
Free, signupless rivals own the single tests, so we win the top of the funnel by being best and easiest. The money comes from combining tests with our existing PDF, QR, camera, receipt and timer tools into things no single free site offers: an inspection report, setup profiles, and a reseller QA desk.

## Build order
**Layer 1 first, and verified live, before anything else.** For Layers 2 and 3, review the specs for feasibility, propose changes, then build in order L2 A -> B -> C -> L3. Hold any price that isn't the standard $29.99 workflow price for Santosh.

## Layer 1: Professional Tools (build now; tests free to run)
*Outcome:* the 6 pages + hub from 0852, plus **Mic test** (on-device level meter and playback, no upload) and **Webcam test** (reuse camera-capture; show the notice BEFORE the permission prompt, which is the B-0063 lesson). Usage boosters: PNG share cards per test, settings in the URL (bookmarkable presets), on-device history (last 20, clearable), iframe embeds with a "Powered by FreeDailyPro" link for tone, stereo, pixel and noise, "next test" chaining, and PWA/offline for noise and pixel. Card download or share = 1 Professional Tools trial use per visit. Copy link stays free.
*Acceptance:* the 0852 tests, plus: presets round-trip exactly; history survives reload and clears; an embed works on an outside page and on mobile; card values match the screen; mic and webcam send zero network uploads and handle a denied permission.

## Layer 2: Premium Applications (spec; review, then build after L1 passes)
Pricing: the existing Premium pool ($3 day / $9.99 month, 2 trial uses a day, per your 1530 pricing clarification). Joining that pool is a **proposal awaiting Santosh**, so don't ship paywall copy until he confirms.
- **A. Device Inspection & Return-Window Report:** a guided pixel, speaker, bass, mic and webcam session, with marks and screenshots, purchase date and return-deadline countdown, a receipt or warranty record (camera photo), and one PDF report. Data stays on-device (JSON export and import).
- **B. Home Theater / Car Audio Setup:** channel walkthrough (2.0 to 7.1, and car front/rear/sub), pink-noise level matching, the bass sweep, SPL readings the user types from a meter (no calibrated-SPL claims), saved local profiles, and a printable setup sheet.
- **C. Sleep & Focus Sound Studio:** more layers, timers and Pomodoro, a saved-mix library, scheduled fade, and offline PWA.
A "use" = generating the PDF report or exporting a profile or library. *Acceptance:* the full session works on desktop and phone; PDF values match the screen; the deadline is correct across time zones; profiles save, load and import; the studio works in airplane mode; paywall copy matches the existing Premium paywall.

## Layer 3: Workflow Product, Device Refurb / Resale QA Desk (spec; feasibility first)
$29.99/mo with a 7-day trial (the standard). Org plans: reuse the existing Stripe org tiers, but that's a **proposal for Santosh**.
*Outcome:* device records per serial or IMEI (typed, or scanned with qr-scanner; Luhn check on IMEI). A session QR or link lets the device under test run the Layer 1 tests in its own browser and post the results to the record. Technician notes and an owner-editable A/B/C rubric (no AI). Server-side per-org records and session history. A certificate PDF per device, with a QR to a public verify page that shows only date, checks and grade. Listing-ready condition text built from templates for eBay, Etsy and Marketplace. Bulk labels, batch certificates, CSV export, and owner/tech/viewer roles. Retention: data is kept while subscribed; deletion after cancel is a proposed 90 days (Santosh decides); the user can delete any time, and export first. Serial and IMEI numbers are treated as sensitive, and the privacy page gets updated.
State limits honestly: no data erasure, no blacklist or carrier checks, no hardware battery health. Rule 1 rivals: PhoneCheck and Blancco (cabled, enterprise, quote-priced). We haven't fetched their pages yet; we'll do a competitor pass before you build L3.
*Acceptance:* a session link on a second phone posts to the right record; the certificate and verify page show only allowed fields; the CSV is complete; roles are enforced; Stripe shows $29.99 with 7 days free and $0 due today; the retention job deletes; no cross-org reads by ID (IDOR); rate limits hold.

## API / MCP
L1: tone, sweep and noise WAV, test signals, note-to-Hz, test-pattern PNG (0852 plan, section 10). L2: a stateless `device-inspection` report-to-PDF endpoint and MCP tool. L3: authenticated devices, sessions, certificate and CSV endpoints, plus MCP read tools scoped to the caller's own org. Propose; don't block L1 on them.

## Constraints
No AI features. The excluded ideas (AI photo grading, AI listing text, AI audiogram reading) need Santosh's approval. The 0852 rules on audio safety, "free" only in SEO fields, the 300+ count, and no Google auto-redirect all still apply.

## Reply requested
In from-claude/, give a status per page and per app: L1 pages (hub, 6, mic, webcam, boosters), L2 A/B/C, and L3. For each: LIVE / PUSHED-UNCHECKED / BLOCKED / FEASIBILITY-NOTES, plus the commit. We promote only after Testing Bot's live check passes.

Source: owner
