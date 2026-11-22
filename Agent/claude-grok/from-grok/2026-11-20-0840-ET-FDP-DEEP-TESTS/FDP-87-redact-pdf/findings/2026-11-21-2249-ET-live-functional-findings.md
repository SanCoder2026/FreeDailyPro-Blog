Sent: 2026-11-21 22:51 ET

# FDP-87 live functional findings

## Usage (P1, per load)
| Run | Step | Counter | POSTs |
|---|---|---|---|
| left | R02 Apply | 0/10 | 0 (Apply is free) |
| left | R02 Download redacted_secrets.pdf | 0→1 | 1 |
| left | R02 Download summary (.txt) | 1 | 0 (free by design) |
| left | New → R04 scan.pdf → Apply → Download | 1→1 | **0** |
| left | New → R07 → Download | 1→1 | **0** |
| left | New → R09 → Download | 1→1 | **0** |
| left | Reload → X08 → Download | 1→2 | 1 |
| leftb | R01 Download | 0→1 | 1 |
| leftb | X02 same result again | 1→1 | 0 |
| leftb | New → R03 → Download | 1→1 | **0** |
| zero | At 10/10: full run, Download | 10/10 | 0, cap dialog "Today's trial uses are done … downloading needs a pass" |
| zero | Download summary (.txt) at 0 | 10/10 | 0, file saved |
| zerob | Preview first page at 0 | — | redacted page-1 image shown |

- **Code:** the result uses `Ye` = ToolPage `ql` (DownloadButton) without a key → `logUsageNow` → `tryUse` → `xI` with the per-tool `Kt` flag, which is cleared only on unmount.
- **Fresh profiles:** most showed 10/10 (pooled). Retries found 0/10.

## UI behaviour
- **Search box:** "Text to find and mark", one term per line, "A space matches any run of spaces".
- **Options:**
  - Match case and Whole words.
  - 6 detectors plus "Select all detectors".
  - Custom pattern (Simple / Regular expression).
  - Lookahead etc. are rejected with a clear message (code).
- **Session memory:** settings are remembered in the tab (`useSessionState`), so detectors and options stay set after New or reload. Worth knowing when testing; it's also stated on the page ("Remembered in this tab only").
- **Toasts:**
  - "Marked N matches — review before applying".
  - "No matches found for …".
  - The scanned-image message.
- **Amber panel:** "The text was also found outside the page text" lists the link address, comment, form field and bookmark.
- **Thumbnails:** a red border and a count badge. Click one to open "Page N of M — drag to mark an area". Each box has a "Remove this redaction" X; "Back to pages" returns.
- **Result:** "Everything under your boxes is gone, and the rest of the text is still real, selectable text. A small 'Created with FreeDailyPro.com' mark is added…".
  - A per-detector summary, "Metadata cleared / not cleared", and the attachment count.
  - "Show the full summary", "Download summary (.txt)" and "Preview first page".
- **Password PDF:** an in-browser dialog. A wrong password gives "That password didn't work — please try again"; test123 unlocks and loads 4 pages.
- **Corrupt PDF:** a toast saying "corrupt.pdf can't be read — it looks damaged" with a "Repair PDF" button.
- **Quick Buy:** Day Pass $1 → email dialog (stopped). Monthly $4.99 → checkout.stripe.com (stopped, ID redacted).
- **Open from Google Drive:** Google sign-in popup (closed).
