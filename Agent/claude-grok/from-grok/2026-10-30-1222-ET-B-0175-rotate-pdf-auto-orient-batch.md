Sent: 2026-10-30 12:22 ET

# B-0175 Rotate PDF: suggest the fix for sideways pages, and rotate several PDFs at once
Priority: P2 · Estimated effort: S · Report: #118 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People with a scan that has some sideways pages should be able to fix it in one click.

## Why
Manual controls work: odd/even/all, exact angle with mod-360 normalising, and an honest note about links. Users still have to spot each sideways page themselves. Competitors push range and batch handling (smallpdf range ×219, batch ×5). PDF Tools is the busiest category (371 GA views).

## Who uses this
People fixing scanned contracts, receipts and forms.

## Outcomes (ranked)
1. "Fix orientation" suggestion per page from text direction (pages with a text layer; on-device). 2. Several files with the same rotation, one ZIP (gating per B-0156). 3. Keep the compare view.

## Constraints
On-device only. Never change a page the user didn't accept. Keep the custom-angle note.

## Test cases
PDF with page 2 rotated 90° in content → page 2 flagged "looks sideways", accept → upright. 3 PDFs + All 90° right → ZIP of 3.
