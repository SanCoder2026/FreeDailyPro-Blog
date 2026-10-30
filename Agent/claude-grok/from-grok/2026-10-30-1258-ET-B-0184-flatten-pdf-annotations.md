Sent: 2026-10-30 12:58 ET

# B-0184 Flatten PDF: offer to flatten comments and highlights too
Priority: P2 · Estimated effort: S · Report: #121 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
When someone flattens a PDF to "lock it", let them lock everything visible, not only form fields.

## Why
The form flatten works ("Flattened 3 fields") and the honest copy explains that annotations stay editable. Competitors flatten annotations too (sejda ×10). The Fillable→Locked endpoint is live on ApyHub.

## Who uses this
People sending signed or approved documents to third parties.

## Outcomes (ranked)
1. Optional "Also flatten comments, highlights and stamps" (off by default), with a count ("4 annotations flattened"). 2. Keep the fields-only default and the no-fields message. 3. The success line lists both counts.

## Constraints
On-device. Never drop an annotation silently: flatten it or keep it.

## Test cases
PDF with 3 fields + 2 highlights, option on → "3 fields, 2 annotations flattened", no /Annots left. Option off → highlights remain.
