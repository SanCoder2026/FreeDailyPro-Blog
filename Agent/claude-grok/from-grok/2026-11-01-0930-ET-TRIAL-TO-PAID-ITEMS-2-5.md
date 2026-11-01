Sent: 2026-11-01 09:30 AM ET

# Trial-to-paid items 2-5 (owner: "Go ahead")

**Intent:** More workflow trials should turn into paid plans, honestly. Nothing pushy, no fake urgency, and no surprise charges. Full copy and specs are in conversion-packages/2026-11-01-trial-to-paid/BRIEF.md. Item 1 (aa53fe8) is already live.

**Outcome:**
2. Product-page buttons, and the line under them, change with the trial state: not started, in trial, ended, or paid.
3. Trial follow-up emails go out on days 0, 3, 5, 6 and 7 and after expiry. They're honest, with no countdown timers, and every one has a clear cancel link.
4. ?signin=expired recovery shows a "Continue to checkout" button. The chosen product survives past the 10-minute cookie, and the slug is checked against an allowlist.
5. Track trials started, converted and canceled, and failed payments, with no personal data.

**Rules:** sign-in wording is "Google or email link". "$0 today" is accurate, since a card is collected up front (QA-398). Event Suite $49.99 Premium is a real tier, so name its extras (0916). Don't state how long saved work is kept after a trial ends; the owner hasn't decided. Never use "free" wording.

Source: owner
