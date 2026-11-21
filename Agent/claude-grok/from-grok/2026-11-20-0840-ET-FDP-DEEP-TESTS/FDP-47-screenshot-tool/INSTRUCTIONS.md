Sent: 2026-11-21 06:49 ET

# Instructions for Claude: FDP-47 Screenshot Capture & Editor

1. Read REPORT.md ("How to work with us" first, including how capture was stubbed), then PRIORITIES.md.
2. Fix the shared Download/Copy trial-use wrapper: charge per new result and re-check the cap every time. It's the same fix as FDP-44/45/46, so verify all four.
3. Feature-detect `getDisplayMedia` on load and show a phone note (with a pointer to Resize & Crop / Camera Capture) before any capture button or pass offer. Fix "especially on mobile" and the JSON-LD operatingSystem.
4. Plan the video re-record (current editor, trial-use wording).
5. Translate locale tool strings, title and meta.
6. Ask Santosh about the double badge and the unbadged Copy (owner questions, not bugs).
7. P3s: highlighter rendering, undo across rotate, meta/subtitle, overflow, aria label, ad category blocking (keep the slot).
8. Verify with test-cases.md and `scripts/` (README). No sign-in in automated tests, and no real payments. Do one real capture by hand in desktop Chrome and Safari.
9. Wording: "Professional Tools" / "Premium Applications" / "Workflow Products" and "trial uses". Keep the reserved ad slots and the intentional badge.
