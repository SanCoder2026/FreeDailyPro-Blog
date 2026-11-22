Sent: 2026-11-21 22:51 ET

# FDP-87 video and blog

## Video PsNyMsdgdqw
- **Titles:**
  - Embedded on the page as "Watch: Redact PDF in Action".
  - JSON-LD name: "How to Redact PDF Online – True Permanent Removal | FreeDailyPro.com".
  - YouTube title: "How to Use Redact PDF – Free Step-by-Step Walkthrough".
- **Details:** 1:56, uploaded 2026-09-30, 9 views at check time.
- **Description:**
  - "Permanently removes sensitive information from a PDF by drawing over it, then **flattening that page into an image**."
  - "Try Redact PDF free"; "Free daily uses in your browser".
- **Captions:** music + "Subscribe so you don't miss the next free tool" only.
- **Storyboard (`video/sb0-03.jpg`, `sb0-06.jpg`):**
  - An older UI: a dropzone with the "What is this tool?" block, then page view drawing.
  - No "Text to find and mark", no detectors, no cleanup options.
- **Verdict:** it doesn't show current capability (check 12 FAIL), and the flattening claim contradicts the page FAQ and real behaviour. **P2.**

## /blog/redact-pdf ("Redact a Grievance File, Then Verify Nothing Survives", Oct 17 2026)
- **Accurate:** the search box, detectors, review, the amber panel, both options on by default (confirmed in code: `useState(!0)` ×2), the `redacted_` name, and the verify advice.
- **Outdated:** three sentences.
  - "each marked page is rebuilt as an image, so the original text is gone from the file".
  - "Those pages are flattened into images, so their text can no longer be selected or searched".
  - "a heavily redacted file can be larger than the original, because image pages weigh more".
- Today only pages that can't be edited exactly become pictures, and the tool names them. **P2.**

## /blog/redact-pdf-remove-sensitive-data ("Redact a PDF Before You Share It Outside the Room")
- Generic workflow and accurate. It warns that "Embedded attachments can smuggle secrets past page paint", which matches P2-1.
