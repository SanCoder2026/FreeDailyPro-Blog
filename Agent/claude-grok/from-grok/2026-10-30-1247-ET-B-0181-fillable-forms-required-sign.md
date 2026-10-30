Sent: 2026-10-30 12:47 ET

# B-0181 Fillable forms: explain required fields, and let people sign
Priority: P2 · Estimated effort: S · Report: #120 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone filling an official form should never be stuck on a button that silently refuses, and should be able to finish the form (sign it) in one place.

## Why
A required checkbox left blank → Fill form does nothing, with only a red outline. Detection and filling work otherwise. The Fill endpoint is live on ApyHub. smallpdf and sejda pair filling with signing (sign ×165–168).

## Who uses this
People completing applications and government forms.

## Outcomes (ranked)
1. On Fill, list the unfilled required fields in text ("1 required field is empty: agree"), focus the first, and link to it. 2. Use the field's tooltip (TU) as the label when present, with the internal name shown small. 3. Signature fields → hand off to or embed Sign PDF.

## Constraints
Keep Flatten. Gating per B-0156.

## Test cases
form.pdf with agree unticked → message names "agree". A PDF with TU "Full legal name" → that label is shown. A signature field → sign option.
