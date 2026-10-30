Sent: 2026-10-30 13:20 ET

# B-0193 Add Page Numbers: inline validation, margin control, live position preview
Priority: P2 · Estimated effort: S · Report: #123 · Source: QA sweep + live competitor fetch 2026-10-30 13:12 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should see mistakes and where the number will sit before they spend a trial use.
## Why
- Validation on submit works and the messages are clear:
  - "The starting number has to be 1 or higher"
  - "Type size has to be between 6 and 48"
  - "Page 9 is outside this PDF's 3 pages"
- But the inputs accept -1, 0, 500, "5-2" and "abc" with no feedback and the button enabled. Only one error shows at a time, and only after clicking.
- At 0 trial uses, Add still produced a Download, with a "Created with FreeDailyPro.com" badge notice (gating policy → B-0156).
- smallpdf mentions margin ×83, position ×64 and format ×56; ilovepdf mentions font ×12 (live fetch). There's no margin control and no visual preview of the position.
- Website tool for the PDF Toolkit paid API (selection rule 1).
## Who uses this
Students, legal and office users numbering reports, theses and filings.
## Outcomes (ranked)
1. Validate each field when it loses focus, with the message next to the field (aria-describedby). Show all errors at once.
2. A first-page thumbnail showing the number at the chosen position, size and margin.
3. A margin control (in mm/pt).
4. Range parsing errors name the problem ("5-2: start is after end").
## Constraints
Keep the current submit-time checks and their wording. Labels → B-0155. Status → B-0187.
## Test cases
1. Start -1 then Tab → an inline error; the button is disabled.
2. Size 0 and range "9" together → both errors are shown.
3. Range "5-2" → "start is after end".
4. Bottom Right with a 20 pt margin → the preview and the output match.
