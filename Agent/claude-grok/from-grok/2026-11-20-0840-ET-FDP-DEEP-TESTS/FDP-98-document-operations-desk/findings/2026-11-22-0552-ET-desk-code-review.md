Sent: 2026-11-22 05:52 ET

Sent: 2026-11-22 05:52 ET

# FDP-98 shipped-code review (guest download, 2026-11-22 05:37 ET)

Chunks (evidence/js): `DocumentOperationsDesk-DxX6-EiM.js` (UI), `docOpsEngine-lVJXDlBe.js` (steps, recipes, run, export list), `auditLog-DSfy6bBy.js` (desk shell, project save/open, ZIP + manifest with SHA-256), `WorkflowProductGate-BDNk2iP2.js` (paywall, status polling), `workflowCta-oWYKzOWD.js` (CTA labels: trial / subscribe / manage / open), `operations-BlL6iX51.js` (+ pretty), `redactApply`, `redactSearch`, `ocrText`, `ocrImage`.

| Page claim | Code | Match |
|---|---|---|
| Packet project, ordered documents, notes, manifest, saved as a file | `re()` desk shell; `<name>.fdp-document-operations-desk.json`; "Project saved to a file. Keep it: it is the only copy."; up/down arrows, per-document note | Yes |
| Recipes chain scan, OCR, organize, redact, number, compress, sign "in the order you choose" | Steps `J=[scan,ocr,organize,redact,number,compress,sign]`; ticking sorts by `J` order; recipe file `packet.fdp-recipe.json` keeps its own order | **Order not choosable in the UI** (R4) |
| Starter recipes | archive, share, sign, full | Yes (match the guide) |
| Scanner module for paper pages and photos | "Scanner panel" → camera/photo input; Scan step = picture on an A4 page; crop/straighten → "use the Document Scanner" | Partly (light) |
| Audit log of every step, exported as CSV | `audit-log.csv` (When, Document, Step, Result, Pages in/out, Bytes in/out, Note) + `desk-log.csv` | Yes |
| One-click packet export: ZIP in order + manifest with checksums | `NN-name.pdf`, manifest.json + manifest.csv (SHA-256, description), audit-log.csv, recipe.json → `<name>-packet.zip` | Yes (always includes audit + recipe, R10) |
| OCR and redact use the same engines as OCR PDF / Redact PDF | `operations` `Vn` (OCR, `eng` default, no UI field), `redactPdfPages` with `removeHidden:true` | Yes; English only (R7) |
| "Signing places a drawn or typed signature image" | Typed name, Helvetica-Oblique, line at (w−260, 64) on the last page; non-ASCII → "?" | **No image / no drawing** (R5) |
| Project file lists docs and notes "unless you choose to include them" | No include option; UI: "the file stores the list, not the contents" | **No** (R8) |
| Number pages | `operations` `pn()` in place (#96 PASS); continuous across documents option; plain or Page X of Y | Yes |
| Organize | `operations` `_n()`→`_e()`→`Pt()` (#93 P0 engine), one page list for every document | Risk R1, R6 |
| Compress | `operations` `gn()` balanced / aggressive ("may turn pages into pictures"); keeps the original if not smaller | Yes; R2 for hidden fields |
| Downloads | ToolPage download with `{free:true}` (no trial count) | Subscription design; R3 |
| Gate | `workflowProduct.status` → entitled renders the desk; guest sees the paywall; `?checkout=success` polls 20× | Server-side |
