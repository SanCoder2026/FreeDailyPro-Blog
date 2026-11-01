Sent: 2026-11-01 01:55 ET (Grok Orchestrator)

# RapidAPI listing pack: fix it at the source

## Intent
Make sure the RapidAPI listing pack only promises things that are complete and verified, and follows our listing rules.

## Why
We never promote incomplete capabilities, and RapidAPI buyers pay through RapidAPI's own checkout. Some lines in the current pack break those rules, so the Developer bot is removing them by hand.

## Outcome
1. Remove the "free" tags, and remove the freedailypro.com link at the end of every long description.
2. Take out redact, cron, QR, SEO, pay stub, the NDA/lease drafts and TDEE.
3. Confirm "files are not stored" is true and give the evidence: how long files are kept and where. Otherwise remove the line.
4. Add label/alias matching to PDF form fill (it works only with exact field names today), and fix B-API-83 (retirement). Each gets promoted only after it's fixed.

Source: owner
