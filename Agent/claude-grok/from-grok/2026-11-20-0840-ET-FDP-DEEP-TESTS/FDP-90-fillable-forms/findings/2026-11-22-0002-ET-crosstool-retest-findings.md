Sent: 2026-11-22 00:04 ET

# Cross-tool retests (#88 flatten-pdf, #89 create-fillable-pdf)

## 1. Flatten prints hidden fields — YES (P1)
- Input `form.pdf`: field `hiddenf`, widget /F has the Hidden bit, value "HIDDEN FIELD VALUE".
- UI lists `hiddenf` between "ro (read only)" and "empty" like any input.
- Output with Flatten (files/left-b-0-filled_form.pdf): 0 widgets; page-1 text contains "HIDDEN FIELD VALUE" (verify-FORM-flat.json `hidden_leak: 1`).
- Code: `W()` → `l.flatten({updateFieldAppearances:false})`; no Hidden/NoView filter. pdf-lib's flatten draws every widget's /AP N.
- Same root as Flatten PDF (#88). A shared "flatten but drop hidden widgets" helper fixes both.

## 2. Box-height font size hides answers — YES on Create Fillable PDF forms (P1, root #89)
- `created89.pdf` notes: DA `/Helvetica 69 Tf`, box 261×81 pt. Three lines typed → appearance `Helvetica 69` → page shows "Line" (MuPDF and PDFium identical). Flattened copy: same.
- Country (DA 17 pt) shows "Germany" fine; single-line answers fit.
- `limits.pdf` control: `0 Tf` fields auto-fit (single line 9 pt with a 72-char answer; multi-line 28 pt, all 3 lines visible). `10 Tf` multi-line prints at 10 pt. So the tool honours the form's DA exactly.
- Suggestion: when text measured at the DA size overflows the box, refit (as for 0) or show "answer too big for this box at the form's font size".

## 3. Non-Latin text — works (P3 polish)
- Hindi "राम कुमार": real text, FreeSans embedded (not subset), searchable in the output text layer.
- "東京都 山田 محمد": PNG picture appearance (1 image). Visible in MuPDF and PDFium, unflattened and flattened. Not searchable (disclosed in Details and FAQ).
- Field V keeps the real Unicode string (verify-C89.json), so a reader that regenerates appearances would redraw it with its own font.
- Lost: field border and background on picture fields; multi-line non-Latin uses a fixed 11 pt.
- Flattened file 275 KB vs 143 KB unflattened.

## 4. Test-filling a Create Fillable PDF form takes a use — YES (owner question)
- handoff.json: Create Fillable PDF download 0→1 (1 POST); "Fill it in" → this tool loads `fillable-form-fillable.pdf`; type → Fill form → Download 1→2 (1 POST). The pooled Premium day is gone after making and checking one form.
