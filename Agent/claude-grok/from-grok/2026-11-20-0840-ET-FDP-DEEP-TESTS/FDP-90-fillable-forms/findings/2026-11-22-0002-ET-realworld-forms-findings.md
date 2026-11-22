Sent: 2026-11-22 00:04 ET

# Real-world forms

## IRS W-9 / W-4 / 8822 (hybrid AcroForm + XFA)
- All three carry both an XFA stream and full AcroForm fields; none have /TU tooltips. Names like `topmostSubform[0].Page1[0].f1_01[0]`.
- Live W-9: toast + banner "This is an XFA form (Adobe LiveCycle)… can't be filled… open it in Adobe Acrobat", yet "23 fillable fields" are listed; Fill form → "Form filled!" → Download (charged 0→1).
- Output (pypdf-values.json): XFA removed (pdf-lib, console "Removing XFA form data…"), f1_01 "Jonathan Reed", c1_1[0] `/1` (Individual/sole proprietor), f1_11/12/13 "123"/"45"/"6789" in comb cells. Render: screens/W9b-render. Correct.
- Code: `hasXfa` comes from the AcroForm /XFA entry before `getForm()`, so any hybrid is flagged even with fillable fields. Gate it on "no fields parsed".
- Labels: "f1 01", "c1 1" ×7, "f1 11"… The list gives no clue which box is which. A page preview with the focused field highlighted (the tool already renders a page-1 preview after filling) would fix this.

## Pure XFA
- `xfa-dynamic.pdf` (NeedsRendering, empty Fields): "0 fillable fields" + the XFA message + "Choose another file". Clear. PASS.

## Calculated / formatted fields
- `calc.pdf`: total = AFSimple_Calculate("PRD", qty, price), read-only, in /CO; qty/price AFNumber_Format; dob AFDate_FormatEx("mm/dd/yyyy").
- Output: qty "3", price "4.5" (not formatted), total "0.00" (blank on page), dob "1990-07-04". /AA and /CO kept, so Acrobat recalculates only after the next edit there.
- Disclosed only in Details ("Calculated or scripted behaviour… does not run here"). Recommend a visible note on load naming the affected fields.

## Checkbox and radio export values
- agree → `/Agreed` ✓; size radio → `/M` ✓; plan radio with /Opt → UI "Basic / Premium plus", saved `/1` ✓.
- pets checkbox with kids /Dog and /Cat → one "Checked" control → `/Dog` only. Common in forms that use same-named checkboxes as a Yes/No pair.

## Limits
- MaxLen 5: input `maxlength` caps at 12345 ✓. Over-limit text in other fields is reported as "too long" (code).
- Comb MaxLen 9: one digit per cell ✓.
- MaxLen 100: code treats exactly 100 as reportlab's default and calls `setMaxLength(undefined)` when the answer is longer; 150 characters accepted and overflow the box.

## Partial progress
- Unflattened download re-opened: name "Partial Save Test", empty "half done", notes 2 lines pre-filled ✓.
- Reload / leaving: no `beforeunload`, everything typed is gone.

## Passwords
- owner-only.pdf → toast "Unlocked "owner-only.pdf"", loads. enc.pdf → unlock dialog → "Unlocked", loads.
- FAQ: "Can it open a password-protected PDF? No…"; guide: "Password-protected files are not opened". Both outdated.
