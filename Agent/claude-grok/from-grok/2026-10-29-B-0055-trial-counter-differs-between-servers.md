# B-0055 Trial counter gives different answers on each page load (server instances disagree)
Priority: P1 (revenue + trust)      Estimated effort: 60–120 min      Report: #68      Source: Testing Bot (retest cycle 2)

**How to work with us:** you are the implementation partner, not an order-taker. Inspect the real code and the Railway deploy setup, challenge this diagnosis if the code says otherwise, and choose the best fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
One visitor should get one answer to "how many trial uses do I have left today", on every page load, on every tool, from every server. The counter is the gate to the Day Pass, our main conversion moment (B-0001/B-0021), so it has to be right.

## Why
- Live on Oct 29, 2026, from one IP with no actions in between (22:02–22:08 ET). We opened fresh browser contexts (new `deviceId` each time) on /tool/compress-pdf. `usage.check` (`/api/trpc/auth.me,usage.check,usage.check`, edge iad1, server railway-hikari) returned `{"allowed":true,"usageToday":0,"limit":10}` on some loads and `{"allowed":false,"usageToday":10,"limit":10}` on others. The pattern was 10/0/10/0/0 in 6 loads, and the same flip showed on income-tax, qr-generator, split-pdf and bulk-qr. Evidence: `test-cases/results/` chk3/chk4 output in REPORT-68 §B-0055.
- It even flips inside one visit. On compress-pdf the header read "10 remaining" and changed to "0 remaining" after a single download (comp-scan.json, Aggressive run, 21:58 ET).
- Two kinds of harm:
  - **Trust and conversion.** A brand-new visitor who has never used the tool can land on "0 remaining today" and see "Get a Day Pass to download". It happened on income-tax-calculator, which we had never used, at 22:02 ET.
  - **Revenue leak.** A visitor who is out of uses can reload until they hit the other instance, and gets 10 more.
- Most likely cause (please confirm in code): the per-IP daily usage is kept in process memory (or in a per-replica cache), and there is more than one replica. The response body has no instance id, so confirming this needs the server code or logs.

## Outcomes
- The same IP plus device gets an identical `usageToday` from every replica and on every reload. Shared store: Postgres, Redis, or whatever the app already uses.
- A visitor with no usage today never sees 0.
- Once a visitor is at the limit, reloading never brings uses back.
- The day boundary and the 10/day Professional and 2/day Premium limits stay exactly as they are today.
- Report back: where the counter lives now, which store you chose, and a 20-reload proof (fresh context each time) showing a constant value.

## Constraints
Don't change prices, limits or what counts as a use. Keep the B-0021 events (`limit_hit`, `upgrade_cta_view`). We saw them fire, see REPORT-68.

## Test cases
R68-CNT-01: open /tool/compress-pdf in 20 fresh incognito contexts in a row, read "N remaining" and the `usage.check` JSON, and expect the same value every time.
R68-CNT-02: use one trial use, then reload 10× and expect remaining to stay at limit−1 on every reload.
Owner decisions needed: none.
