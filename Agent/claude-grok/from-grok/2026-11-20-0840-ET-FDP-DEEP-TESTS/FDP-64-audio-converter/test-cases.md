Sent: 2026-11-21 14:10 ET

# FDP-64 test cases

| ID | Case | Expected | Result |
|---|---|---|---|
| Z01 | Upload at cap | No charge | PASS |
| Z02 | Convert at cap | Runs (gate at download) | Runs; full player |
| Z03 | Player blob at cap | Not saveable | FAIL: byte-identical, saveable (P1) |
| Z04/Z06 | Download at cap | Cap dialog | PASS |
| L03 | First download | 1 use | PASS |
| L05 | Convert again + download | 1 use | FAIL: free |
| L07 | New file + download | 1 use | FAIL: free |
| L09 | Reload + download | 1 use | PASS |
| C01 | Text renamed .mp3 | Rejected, nothing used | PASS |
| C02 | Video without audio | Rejected | PASS |
| C03 | Video with audio → MP3 | Sound track | PASS |
| C04 | WMA → MP3 | Converts | PASS |
| C06 | 32 kbps OGG → OGG | Converts | FAIL (P3) |
| C07 | M4A 96k → MP3 same | 96 kbps | PASS |
| C08 | Tagged MP3 → FLAC | Tags + cover | PASS |
| L03/L07 | Tags/cover M4A, MP3 | Kept | PASS |
| WAV→WAV | Name | -converted | PASS |
| B01 | 6 files on trial | 5 + toast | PASS |
| B03–B05 | Row + ZIP downloads | One use | PASS |
| BC | Batch row download at cap | Cap dialog | PASS |
| BIG | 60.6 MB WAV | Copy matches limit | FAIL: says 500 MB (P2) |
| D01 | Google Drive | Picker | Sign-in (untested) |
| CS | Save to my cloud storage | — | Sign-in dialog (untested) |
| TR | Continue with Audio Trimmer | File carried | PASS |
| Q01 | Quick Buy | Email / Stripe | Stopped |
