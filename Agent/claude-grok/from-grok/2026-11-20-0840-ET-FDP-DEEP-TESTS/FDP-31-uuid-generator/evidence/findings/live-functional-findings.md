Sent: 2026-11-21 00:40 ET

# FDP-31 UUID Generator: live functional findings (guest, headless Chromium, 2026-11-21 00:17–00:21 EST)

Results: `json/cases.json` (ug-live.js), `json/gate.json`, `json/try.json`, `json/share.json`, `json/misc.json`. Sample output: `testfiles/generated-sample.txt` (1,000 lines, never executed).

## Count validation (PASS)
| Case | Count | Live |
|---|---|---|
| U01 | 5 | 5 UUIDs, ~0.36 s |
| U02 | 1 | 1 UUID |
| U03 | blank | Generate disabled, "Enter how many UUIDs you want." (role=alert) |
| U04/U05 | 0 / -3 | disabled, "Enter 1 or more. Zero and negative counts cannot be generated." |
| U06 | 2.5 | disabled, "Enter a whole number, such as 5." |
| U07 | 1001 | note "Maximum is 1,000 per batch; generating 1,000." → 1,000 |
| U08 | 1000 | 1,000 in ~0.38 s |
| U09 | 1e3 | accepted as 1,000 (P3: scientific notation; harmless) |
| U10 | 999999999 | capped to 1,000 with the note |
| U11/U12 | 007 / " 12 " | 7 / 12 |

- While the count is invalid, the previous list stays on screen (stale results under an error) (P3).

## Output quality (PASS)
- 4,025 distinct UUIDs across all batches: every one matches the RFC 4122/9562 version-4 pattern `^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$`. No duplicates across batches (the raw total of 4,029 includes the same single U02 value re-read 4 times while Generate was disabled for U03–U06; a script artefact, not a repeat).
- Variant nibble split 8/9/a/b = 997/1010/1005/1017; hex digit frequencies 7,351–7,724 per digit (uniform as expected). Source is `crypto.randomUUID()` (code, `js/UuidGenerator-*.pretty.js`).
- Toggles reformat the same values live: Hyphens off → 32 hex chars; Uppercase on → uppercase; Copy All copies the displayed form (e.g. `4BA64E329642412796A843EB3DF0CAE9`). PASS.
- Per-row copy icon ("Copy UUID n", toast "Copied!") and Copy All (newline-separated, toast "All copied!") work.

## Privacy (PASS)
- No request to any host contained any generated UUID (with or without hyphens) (`leaks: []`); the URL never changes; reload clears the list (as the copy says). Share copies only `https://www.freedailypro.com/tool/uuid-generator` (`json/share.json`, 00:21 EST).

## Trial use (policy question; copy and blog conflict)
- `json/gate.json` (2026-11-21 00:19:02–00:19:48 EST): context loaded at 0 remaining (10/10). Generate, Copy UUID 1, Copy All, Generate again and selection copy (Ctrl+C) all worked with no dialog; count 10 → 10, also after reload. `json/try.json` (00:18 EST) same for a single Generate.
- The code wires a gate: Generate awaits `logUsageNow()` and only fills the list if it returns true; each copy goes through `gateShare` (`useShareGate`/`useExportGate`, which can open the cap dialog). At 0 none of these blocked (display-only observation; no backend claim).
- The blog `/blog/uuid-generator` says: "Press Generate. Each press of the button counts as one of your 10 trial usages for the day." The video shows "8 free uses left today". Live at 0, Generate is not blocked.
- Not in the Nov 20 uncounted list → **policy question for Santosh**, with the extra note that the page/blog promise a count and the code is built to charge. With uses left: pending (RERUN-AFTER-RESET row 31). Note for that rerun: if each per-row copy is charged separately, copying 5 single UUIDs could cost 5 trial uses (code path `gateShare` per click) — verify then.
- No cap dialog, pass or Stripe appeared, so the payment path was not reachable.

## Print / layout
- The tool has no print or download action. Browser print (`testfiles/outputs/print-preview.pdf`, 2 pages) shows the list and controls (Copy All button printed) and the video block.
- 1,000 rows each with a copy button make a very long page (`screens/live/case-1000.png`); no "Download .txt/.csv" for big batches (P2 completeness).
