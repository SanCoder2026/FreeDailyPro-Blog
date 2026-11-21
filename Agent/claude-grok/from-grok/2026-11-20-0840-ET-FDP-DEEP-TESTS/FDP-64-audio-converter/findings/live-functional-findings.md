Sent: 2026-11-21 14:10 ET

# Live functional findings (FDP-64)

- **Charge point:** Download (single or batch). Convert, upload, Convert again are free. One `usage.log` per page load → later downloads free until reload (P1).
- **At the cap:** Convert runs; `<audio controls>` plays a blob byte-identical to the gated download, no nodownload/context-menu block (P1, real save at 0). Download / Save to Google Drive / batch row download → cap dialog.
- **Outputs:** all valid (ffprobe); tags and cover behave as the FAQ says; video sound and WMA work; same-format adds -converted.
- **Errors:** non-audio and no-audio video rejected with "nothing was used" messages. 32 kbps OGG→OGG fails (P3).
- **Limits:** trial 50 MB (blocked, Convert off), pass 200 MB; batch 5 files on the trial.
- **Firefox:** identical results (zero-capped-firefox, left-firefox).
