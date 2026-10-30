Sent: 2026-10-30 12:22 ET

# B-0177 PDF watermark: say why an empty watermark can't be added; offer "behind content"
Priority: P2 · Estimated effort: S · Report: #118 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Every invalid state on this tool should explain itself, as the page-range error already does, and logos shouldn't cover body text.

## Why
Empty Watermark Text leaves Add Watermark enabled, and clicking it does nothing with no message. "Page 9" by contrast shows a clear inline error and disables the button. Competitors offer layer above/below content (smallpdf layer ×8).

## Who uses this
People marking drafts and branding PDFs before sharing.

## Outcomes (ranked)
1. Empty text → inline "Type the watermark text" and disable the button, as for the page-range error. 2. "Behind page content" option (default stays on top). 3. Keep the batch mode.

## Constraints
No change to defaults (CONFIDENTIAL, 40%, 45°).

## Test cases
Clear text → message + disabled; type "DRAFT" → enabled. Behind-content on a text page → text stays fully dark where it overlaps.
