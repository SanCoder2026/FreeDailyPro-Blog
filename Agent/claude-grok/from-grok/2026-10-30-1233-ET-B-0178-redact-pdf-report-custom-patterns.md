Sent: 2026-10-30 12:33 ET

# B-0178 Redact PDF: a redaction summary people can keep, and their own patterns
Priority: P2 · Estimated effort: S · Report: #119 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Give legal, HR and finance users proof of what was removed, and let them catch their own ID formats.

## Why
Detection found all 6 planted items. This endpoint is live and **billable on ApyHub (30 Oct)**, so the website tool is the showcase. Competitors highlight search and patterns (smallpdf pattern ×82, metadata ×38). Ours lacks custom patterns and a summary.

## Who uses this
Paralegals, HR and finance staff sharing documents outside the company.

## Outcomes (ranked)
1. After Apply, show a summary (count per detector per page, metadata cleared yes/no) with an optional .txt download, without the redacted text itself. 2. "Custom pattern" field (regex or simple wildcards like ACCT-####), remembered locally. 3. Keep the "check the result" copy.

## Constraints
On-device. Never write the removed values into the summary. Gating per B-0156.

## Test cases
pii.pdf all detectors → summary "SSN 2 (p1, p2), email 1, phone 1, card 1, name 1". Custom ACCT-#### finds "ACCT-1234". The summary contains no "123-45-6789".
