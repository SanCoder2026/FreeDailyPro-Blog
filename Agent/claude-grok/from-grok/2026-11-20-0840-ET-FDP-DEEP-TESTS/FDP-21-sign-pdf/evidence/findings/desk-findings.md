Sent: 2026-11-20 08:40 ET

# FDP-21 Sign PDF: desk findings (copy, code, SEO)

Sources: `html/tool.html`, `html/tool-expanded.txt`, `json/jsonld.json`, `html/blog_sign-pdf.html`, `html/es_tool_sign-pdf.html`, `js/SignPdf.pretty.js`. Captured 17:04–17:20 EST.

## Copy contradicts itself on the other party's fields — P1
What the code and the live file do (`SignPdf.pretty.js` L698–712 `createTextField`; S02): other-party fields become real, empty **AcroForm text fields** that any PDF reader can fill.
Saying the same (correct): About ("left as empty form fields for them to fill in, in any PDF reader or in this same tool"), the note under Download ("left as real, empty form fields"), the step text L1486, the success toast L804 ("they can sign it in any PDF reader").
Saying the opposite (wrong):
- FAQ "How does the other person actually sign their part?": "a labeled placeholder, **not a fillable box**".
- Details → Limitations: "aren't fillable PDF form fields in the technical sense… not a generic PDF form field that any PDF reader can fill… the other party needs to use this tool".
- Blog /blog/sign-pdf: "not fillable boxes in a standard reader. They are labelled markers".
- FAQ multi-party and "When to use it": the other party gets real signing tools "rather than a plain unverified text box" — in any other reader the signature field **is** a plain text box (/Tx), so the other party may simply type their name.
Why it matters: people decide whether to send a contract based on this. Pick one truth (the real one) and say plainly: "in another PDF reader they can type into the field; to draw or import a signature, they open the file here".

## Other copy
| Claim | Where | Live | Sev |
|---|---|---|---|
| Audit page lists "date and time (UTC), the page and signer count" | FAQ | Lists document, page count, SHA-256, signer name, UTC time + device zone, marks; no "signer count" | P3 |
| "Lock the document… Flatten PDF" | FAQ | Reasonable; other-party fields stay editable until flattened | — |
| Embed title "How to Sign a PDF Online – Draw Signature & Place Fields" vs YouTube "How to Use Sign PDF – Free Step-by-Step Walkthrough" | VideoObject | mismatch | P3 |
| Cap dialog: a pass "removes the 'Created with FreeDailyPro.com' mark from your PDFs" | dialog | trial download has no mark | P3 (generic dialog) |

## SEO / indexing
- 200, self-canonical, no robots meta/header, in sitemap. GSC data is not available.
- Title "Sign a PDF Online - Draw, Type or Upload, Daily Trial"; meta mentions trial uses (good wording). FAQPage + VideoObject JSON-LD.
- /es: English title and meta (no localisation). /ar 404. ja desktop 3 px horizontal overflow.
- Blog /blog/sign-pdf (2026-10-17) exists and is linked; 10 posts link here (tools.csv).
- DUPLICATES C08 groups pdf-editor / sign-pdf / fillable-forms / create-fillable-pdf / flatten-pdf: keep (distinct jobs). tools.csv lists "share;save;copy;print" for this tool; the live signing view offers only Download Signed PDF and Start Over (live-verified, `json/gate-kbd.json` resultButtons).
