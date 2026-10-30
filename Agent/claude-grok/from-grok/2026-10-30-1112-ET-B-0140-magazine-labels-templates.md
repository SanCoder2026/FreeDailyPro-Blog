Sent: 2026-10-30 11:12 ET

# B-0140 Magazine maker: labelled fields and starter templates
Priority: P2 · Estimated effort: S–M · Report: #108 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Make the builder usable with a screen reader, and help first-time users get a good-looking issue fast.

## Why
The Title and Issue inputs have no accessible name. Flipsnack leads with templates and interactive flipbooks; we offer a blank form only.

## Who uses this
School newsletters, clubs and small publishers.

## Outcomes (ranked)
1. Title and Issue are labelled (label for/aria-label). 2. 2–3 starter layouts (newsletter, photo feature, report). 3. The page count shown before download matches the PDF.

## Constraints
Keep the current validation message and the watermark (by design).

## Test cases
get_by_label("Magazine Title") finds the input. Title plus one 120-word article → "3 pages", and the PDF has 3 pages.
