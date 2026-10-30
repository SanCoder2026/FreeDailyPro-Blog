Sent: 2026-10-30 12:58 ET

# B-0186 Markdown ↔ HTML converter: the toolbar runs off the screen on phones
Priority: P2 (bug) · Estimated effort: S · Report: #121 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
On a phone the whole tool should fit the screen with no sideways scrolling.

## Why
At 390 px the page is 728 px wide: the mode/Swap/Open file/Full HTML toolbar doesn't wrap (elements reach x=662). Every other tool in batches 36–40 fits (scrollWidth = viewport). Conversion and sanitising are otherwise excellent.

## Who uses this
Writers and devs on phones (Text & Writing category).

## Outcomes (ranked)
1. The toolbar wraps or stacks at small widths; no horizontal scroll at 320–430 px. 2. The textareas stay full width. 3. Check the same toolbar component on Markdown Editor.

## Constraints
Don't change the desktop layout.

## Test cases
390×800 and 320×640: document scrollWidth equals the viewport width; all 5 toolbar controls are visible and tappable (≥44 px).
