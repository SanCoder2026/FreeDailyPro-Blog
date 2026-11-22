Sent: 2026-11-21 23:07 ET

# FDP-88 flatten verification

**Method:** `verify88.py` checks, for each output:
- AcroForm `/Fields`, NeedAppearances, SigFlags.
- `/Annots` subtypes per page and widgets left (pikepdf + PyMuPDF).
- Values present in PyMuPDF text and pdftotext.
- The hidden-field leak.
- A render diff against the original at 72 dpi with annotations on (changed-pixel bbox).
- OCG, docinfo, `/Sig` objects, the stamp line, rotation.

| Output | AcroForm fields | Widgets | Other annots kept | Values as text | Hidden leak | Stamp | Diff outside badge/stamp |
|---|---|---|---|---|---|---|---|
| left-0 form | 0 | 0 | Highlight, Text, Ink, FreeText (+badge Links) | all 8 | **1** | — | hidden field only |
| left-2 form + stamp local | 0 | 0 | same | all 8 | **1** | "2026-11-21 22:55 EST" ×3 | hidden field only |
| left-3 form + UTC | 0 | 0 | same | all 8 | **1** | "2026-11-22 03:55 UTC" ×3 | hidden field only |
| left-4 signed | 0 (SigFlags 3 left) | 0 | same | all 8 + "SIGNED J. Reed" | **1** | UTC (option persisted) | hidden field only; /Sig dict kept |
| left-5 stale (flag on) | 0 | 0 | same | refreshed "NEW VALUE Maria Lopez", "NO AP VALUE" | **1** | UTC | refreshed fields (expected) |
| left-6 stale2 (no flag) | 0 | 0 | same | old "Jonathan Reed" | **1** | UTC | hidden field only |
| left-7 hindi | 0 | 0 | same | "नमϗते राम" (broken) | **1** | UTC | name field box lost, conjunct broken |
| left-8 form (after reload) | 0 | 0 | same | all 8 | **1** | — (option reset by reload) | hidden field only |

## Notes
- **Text stays selectable:** the values are real text operators in the page content, using Helvetica or embedded FreeSans for Hindi. With 0 widgets left, PyMuPDF still finds them, and they print through pdftotext.
- **Checkbox/radio look:** the ✓ on "Agree", the empty "Not ticked" box, and radio B filled / A empty are identical to the original in the render diff.
- **List box:** all options are still drawn and Green is highlighted, which matches what the form showed.
- **Rotation:** page 3 keeps /Rotate 90, and "ROTATED VALUE" is in place.
- **OCG layer:** `/OCProperties` is kept and "LAYER TEXT visible layer" is still in an optional-content group. It is not flattened, which is out of scope per the page.
- **Annotations:** highlight, sticky note, ink and FreeText stay editable annotations, as the page states ("forms-only").
- **Metadata:** Producer is set to "FreeDailyPro" and ModDate is updated (UTC). Title/Author etc. are kept.
- **Hidden field:** the widget has `/F 2` (Hidden). pdf-lib's `PDFForm.flatten()` draws each widget's `/AP /N` into the page without checking `/F`. Crop: `screens/form0-p1-crop.jpg`, right of "READONLY VALUE".
