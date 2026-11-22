Sent: 2026-11-21 23:07 ET

# FDP-88 desk findings

- **Flow:**
  - On drop: `Cn` (pdf-lib load with `ignoreEncryption`) gives fieldCount and signatureCount, and pdf.js renders the thumbnails.
  - Flatten runs `Rn`:
    1. Load.
    2. Throw if there are 0 fields.
    3. `formAppearance.r` refreshes appearances if NeedAppearances is set or a field is dirty, and stops with "Couldn't draw the answer in …" if any fail.
    4. `a` sets NeedAppearances false.
    5. pdf-lib `form.flatten({updateFieldAppearances:false})`.
    6. `d` removes dangling annotation refs.
    7. Optional stamp.
    8. Set Producer and ModDate, then save.
- **Hidden field:** no check of widget `/F` (Hidden/NoView/Print) anywhere. This is the root of P1-2.
- **Hindi:** `formAppearance.s` is used when `needsPicture(text)` is true (non-WinAnsi text). It embeds a temporary page with text drawn by `drawTextAnywhere` as the field's appearance. There is no border or background, and no complex-script shaping. This is the root of P2-1.
- **Gate:** the result `D` (= ToolPage `ql`) has no key (per-load P1). The dropzone uses `gateAtDownload`. A pass-through "Download file" for 0-field PDFs exists only inside a workflow (`z()`).
- **Text vs code:**
  - The FAQ and Tips say the note uses UTC; the code default is `"local"`.
  - Limitations says password PDFs can't be flattened; the shared unlock dialog makes them work.
- **JSON-LD:** WebSite, SoftwareApplication, VideoObject, FAQPage.
- **Links:**
  - The next step is Compress PDF, plus 2 guides.
  - There are no links to Sign PDF / Fillable Forms.
  - The sister pages don't link here either; Sign PDF only mentions it in text.
