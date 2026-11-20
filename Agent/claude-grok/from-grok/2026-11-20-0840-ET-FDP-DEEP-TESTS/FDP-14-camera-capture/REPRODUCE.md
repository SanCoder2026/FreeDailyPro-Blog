Sent: 2026-11-20 08:40 ET

# Reproduce: FDP-14 Camera Capture

Open https://www.freedailypro.com/tool/camera-capture in a guest browser with a camera. Headless alternative: Chromium with `--use-fake-ui-for-media-stream --use-fake-device-for-media-stream [--use-file-for-fake-video-capture=quad.y4m]` (see `scripts/README.md`).

- **R1 (phone fold):**
  1. Use an iPhone SE (or 320×568 emulation).
  2. Load the page: Start Camera is not visible without scrolling (`screens/devices/iphone-se-fold.png`).
  3. Press it: the preview and Capture are below the fold. Capture: Download Crop/Copy end up about two screens down.
- **R2 (badge disclosure):**
  1. Read the FAQ, How-to and the blog headshot guide: no mention of a mark.
  2. Start, then Capture: the notice "This download will carry small "Created with FreeDailyPro.com" badges in the top and bottom right corners" appears under Download Full Photo.
- **R3 (video):** play the embedded video at about 0:16 (permission prompt with "HP TrueVision HD Camera") and about 0:30 (a person behind a smiley sticker; "10 free uses daily" badge).
- **R4 (front/rear on a laptop):**
  1. Use a machine with two webcams (or Chromium's 2-device fake), then Start.
  2. Pick camera 2, then press Front / rear camera: the stream returns to camera 1 and the picker shows "Choose a camera". Press it again: no change.
- **R5 (a11y):**
  1. Tab to Start Camera and press Enter: `document.activeElement` is `<body>`. Tab to Capture and press Enter: `<body>` again.
  2. Run axe on main: `image-alt` (critical) on the captured image.
  3. Try to crop with the keyboard: not possible.
- **R6 (Copy wording at 0 remaining):** capture, crop, then press Copy. The dialog says "downloading needs a pass" and the toast says "downloading was not done".
