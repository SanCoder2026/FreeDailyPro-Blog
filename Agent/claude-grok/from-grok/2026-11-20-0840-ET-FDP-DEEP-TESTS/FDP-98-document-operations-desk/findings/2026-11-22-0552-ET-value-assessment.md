Sent: 2026-11-22 05:52 ET

Sent: 2026-11-22 05:52 ET

# FDP-98 Is the bundle worth $29.99 (or $49.99)?

## What the buyer could use instead (live prices, /pricing)
| Option | Price | Covers |
|---|---|---|
| Professional pass | $1/day or $4.99/month | OCR PDF, Redact PDF, Add Page Numbers, Compress PDF, Merge PDF, Watermark, Bates, Password, Flatten (each one file at a time) |
| Premium plan | $3/day or $9.99/month (also unlocks every Professional Tool) | + Organize PDF (visual), Document Scanner (crop/straighten), Sign PDF |
| Document Operations Desk | $29.99/month, 7-day trial, not covered by passes | 7 chained steps over a packet + recipe, audit CSV, SHA-256 manifest, project file |

## What the desk adds (per shipped code)
- One run over many documents, with a stop button, per-step audit (pages and bytes in/out, notes) and errors that don't stop the rest.
- Recipes: 4 starters + save/load (redaction words never saved, good).
- Order warnings (redact before OCR, number before organize, sign not last…).
- Continuous page numbering across the packet.
- Export: `NN-name.pdf` in order + manifest.json/.csv with SHA-256 + audit-log.csv + recipe.json; project file with order and notes.

## Where it is weaker than the individual apps or missing what packets need
- **No merge**: the most common packet deliverable (one PDF) needs a separate Merge PDF job after export.
- Organize is a typed page list applied to every document (R6), not the visual Premium Organize; it also uses the #93 leak engine (R1).
- Scan = photo placed on an A4 page; cropping/straightening needs the Premium Document Scanner.
- Sign = typed name on a line at a fixed spot on the last page; non-ASCII → "?" (R5). Sign PDF (Premium) places drawn signatures.
- OCR English only (R7). No watermark/Bates/"CONFIDENTIAL" stamp, no password, no flatten.
- Nothing to see before paying (no video, sample, demo).

## Verdict
- **$29.99:** not yet convincing for most office buyers. It costs 3× Premium (which unlocks every step) and 6× the Professional pass, and lacks the merged-PDF output. It is worth it for a coordinator doing several packets a week who needs the audit trail and manifest, if R1–R3 are fixed.
- **$49.99:** not justified today. A higher tier would need clear extras, for example cloud project storage (like Event Suite's 1 GB), team seats, multi-language OCR, a real e-signature or drawn signature, and the Legal Production Desk features (Bates, production log) in one desk.

## What would make it clearly worth $29.99
1. A Merge step ("one PDF + bookmarks per document") and a Stamp/Watermark step (CONFIDENTIAL, Bates-lite), plus Password at the end.
2. Fix the Organize engine (R1) and say so ("removed pages are really removed; verified by the manifest").
3. Drag to reorder steps; OCR language picker; drawn signature.
4. A sample packet and a short video on the page; a "recipient export" without internal logs.
5. Optionally one desk with a Legal mode (Q2), so a $29.99 subscriber gets both.
