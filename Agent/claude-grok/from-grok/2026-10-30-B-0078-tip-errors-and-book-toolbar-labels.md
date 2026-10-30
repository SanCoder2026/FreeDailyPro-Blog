# B-0078 Small clarity fixes: Tip invalid input, Book toolbar labels on mobile
Priority: P3      Estimated effort: 15–30 min      Report: #81, #82      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Tell users why there is no result, and make the mobile Book toolbar usable by screen readers and clear to touch users.

## Why
- Tip: bill −50 or 0 people → Tip/Total/Per Person show "—" with no message (both widths). Percentage Calculator does this well ("Enter numbers", "division by zero").
- Book Writing Toolbox at 390: the menu, cover-preview (book-open), Preview (eye) and Download buttons are icon-only with no aria-label or title. "New book" and "My Books" already have titles.

## Outcomes
Tip shows a short inline reason (e.g. "Enter a bill above 0", "At least 1 person"). The four icon buttons get aria-label and title.

## Constraints
No calculation changes.

## Test cases
Tip: bill −50 → message visible; people 0 → message. Book 390: every toolbar button has an accessible name.
