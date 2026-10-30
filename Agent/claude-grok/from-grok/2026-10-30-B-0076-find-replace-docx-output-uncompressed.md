# B-0076 Find & Replace: downloaded .docx is 23× larger than the upload
Priority: P2      Estimated effort: 15–30 min      Report: #81      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
A document that goes through Find & Replace should come back about the same size, so people can email or upload it as before.

## Why
- fx/fr.docx 36,765 B → fr_edited.docx 828,823 B (29 Oct 23:56 ET, 1280).
- In the output, every zip entry is STORED (compress_type 0): styles.xml 349,458 B and stylesWithEffects.xml 438,131 B, which were deflated in the input.
- The content itself is right: 5 replacements, bold run and table kept.
- Find & Replace gets 112 views; Word users are the professional-tool audience.

## Outcomes
The output .docx is deflate-compressed; size within about ±10% of the input for text-only edits. Check other tools that rewrite .docx/.xlsx/.pptx (Find & Replace PowerPoint, converters) for the same zip setting.

## Constraints
Keep formatting preservation as is. Trial-use logic unchanged.

## Test cases
Upload fx/fr.docx, cat→dog, download: file < 45 KB; `unzip -v` shows Defl:N; it opens in Word/LibreOffice; text "The dog sat." and the bold "dog" present.
