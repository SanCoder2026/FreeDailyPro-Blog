Sent: 2026-11-21 09:48 ET

# Correction (v2): EU consent banner in the geo checks for FDP-39 to FDP-52

- **Written:** 2026-11-21 09:46 EST (box `date`, ET). The original zips are unchanged. This file corrects them.

## What was wrong
These findings files said no consent banner was seen in the geo contexts (some called it an unverified absence):

| Tool | Original zip and sentence |
|---|---|
| FDP-39 | FDP-39-compare-pdf-2026-11-21.zip, findings/devices-locales-findings.md: "no consent banner shown in this run" |
| FDP-40 | FDP-40-extract-pdf-2026-11-21.zip: "no consent banner in this run" |
| FDP-41 | FDP-41-ocr-pdf-2026-11-21.zip: "No EU consent banner appeared for de-DE/fr-FR…" |
| FDP-42 | FDP-42-find-replace-2026-11-21.zip: "No EU consent banner for de-DE/fr-FR…" |
| FDP-43 | FDP-43-book-writing-toolbox-2026-11-21.zip and its -v2: "No EU consent banner seen for de/fr…" |
| FDP-48 | FDP-48-image-to-pdf-2026-11-21.zip: "No consent banner seen." |
| FDP-49 | FDP-49-pdf-bookmarks-editor-2026-11-21.zip: "No consent banner was seen." |
| FDP-50 | FDP-50-pdf-to-excel-2026-11-21.zip: "No consent banner was seen." |
| FDP-51 | FDP-51-pdf-to-powerpoint-2026-11-21.zip: "No consent banner was seen in any of them." |
| FDP-52 | FDP-52-magazine-maker-2026-11-21.zip: "No consent banner seen." |

## Correct finding
In every one of those runs, the geo screenshots show the EU consent banner for **de-DE (Europe/Berlin) and fr-FR (Europe/Paris)**, and not for en-US, hi-IN, ar-SA or ja-JP:

> "We use cookies for analytics and, when ads are shown, advertising. The tools work either way. Privacy | Accept all | Reject non-essential | Choose"

The matrix script's `consent` flag reported false and I trusted it instead of the screenshots. That was my error, found while testing FDP-53. FDP-44 already reported this correctly.

So the consent behaviour is a **PASS** for those tools: the banner is shown to EU-locale/timezone visitors and has a one-click "Reject non-essential".

Banner presence by context (each tool's geo fold screenshot; bottom-bar "Accept all" button detected):

| Tool | de-DE | fr-FR | en-US | hi-IN | ar-SA | ja-JP |
|---|---|---|---|---|---|---|
| 39-compare-pdf | banner | banner | none | none | none | none |
| 40-extract-pdf | banner | banner | none | none | none | none |
| 41-ocr-pdf | banner | banner | none | none | none | none |
| 42-find-replace | banner | banner | none | none | none | none |
| 43-book-writing-toolbox | banner | banner | none | none | none | none |
| 48-image-to-pdf | banner | banner | none | none | none | none |
| 49-pdf-bookmarks-editor | banner | banner | none | none | none | none |
| 50-pdf-to-excel | banner | banner | none | none | none | none |
| 51-pdf-to-powerpoint | banner | banner | none | none | none | none |
| 52-magazine-maker | banner | banner | none | none | none | none |
## Evidence
`evidence/<tool>/`: the de-DE and en-US fold screenshots from each original run (same files as in the original zips, downscaled).

## Nothing else changes
No other finding, severity or priority in those reports is affected.
