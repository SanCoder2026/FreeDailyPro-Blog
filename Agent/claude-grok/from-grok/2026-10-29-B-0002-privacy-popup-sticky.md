# B-0002 Privacy opt-out pop-up stays open on every step in fresh sessions
Priority: P1      Estimated effort: 30 min (MUST-DO tonight)

## Goal / why
Conversion. In a fresh session the privacy opt-out pop-up never closes and stays over the tool and even behind the paywall, covering the Day Pass offer.

## What to change
Site-wide privacy/consent opt-out pop-up component. Repro: new incognito window → https://www.freedailypro.com/tool/avatar-builder → use the tool, reload, use again, trigger paywall. Actual: pop-up stays open on each step including behind the paywall dialog. Expected: once dismissed or a choice is made it stays closed (persisted), and it never renders on top of/behind the paywall.

## Acceptance criteria
- Fresh session: pop-up shows once, closes on dismiss/choice, and does not reappear on reload or next tool.
- Paywall dialog is fully visible with no pop-up layered on it.
- Opt-out choice is still honoured (no behaviour change to tracking logic).
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Changing what the privacy choice does, consent wording, or analytics setup.
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (premium 2-trial end-to-end check, 29 Oct)
