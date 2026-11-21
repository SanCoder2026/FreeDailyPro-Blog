Sent: 2026-11-21 13:20 ET

# FDP-62: how to reproduce (guest, desktop Chrome)

## P1-1 Clip saveable at 0 trial uses
1. Use a profile at the cap (strip "0 remaining today"). Open https://www.freedailypro.com/tool/screen-recorder.
2. Start Recording → share a tab → Record Full Capture → record ~5 s → Stop.
3. Download Recording → the cap dialog appears.
4. Now use the player's ⋮ menu → Download, or right-click → Save video as…. The clip saves.

## P1-2 Per-page-load charging
1. Use a profile with uses left. Record → Download Recording (the counter goes up).
2. Record Another → record again → Download Recording. It saves with no cap dialog and the counter doesn't change.
3. Reload → record → Download → cap dialog.

## P2 video
YouTube DEwAYXXSJ-c, 0:20–1:30: game-guide site recorded, share picker lists other tabs, old toggles-free UI.

## P2 Safari
Mac Safari: record a tab with the camera bubble. Check MP4 output and the bubble. (Linux WebKit crashes on `enumerateDevices()` even on example.com.)

## P3 unsupported browser
Phone browser (or no `getDisplayMedia`): Start Recording is clickable and only toasts "not supported".

## Payment (stop points)
Quick Buy Day pass → "Premium Day Pass, $3 · Email" (stop). Quick Buy Monthly → checkout.stripe.com (stop).
