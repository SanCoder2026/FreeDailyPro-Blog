Sent: 2026-11-20 08:40 ET

# Test cases: FDP-14 Camera Capture (rerun after any fix)

"Today" = observed 2026-11-19 14:28–14:40 EST with a fake camera test card (`screens/live/fake-camera-reference.png`).

| ID | Action | Expected | Today |
|---|---|---|---|
| CC-01 | Start Camera (permission granted) | Live preview; resolution line; steps 1 of 4 | PASS (1280 x 720 / 3840 x 2160) |
| CC-02 | Capture | Still = camera frame, exact colours, camera off | PASS |
| CC-03 | Mouse-drag crop 55%→95%, Crop Selection | ≈512×288 bottom-right region | PASS (512×286) |
| CC-04 | Touch-drag crop on a phone | Same region | PASS (512×288 / 512×287) |
| CC-05 | Tick Save as JPG during preview, then crop | Crop `image/jpeg` | PASS |
| CC-06 | Change format after Capture | Possible without Retake | FAIL (checkbox gone; P2) |
| CC-07 | Cancel during preview | Camera off, back to Start | PASS |
| CC-08 | Retake | Live camera again, settings kept | PASS |
| CC-09 | No camera | "No camera was found on this device." | PASS |
| CC-10 | Permission denied (Firefox) | Clear "set Camera to Allow, then reload" message | PASS |
| CC-11 | Two cameras: picker lists and switches | Both listed; switch works | PASS |
| CC-12 | Front / rear on a laptop with 2 cameras | Hidden, or switches to the other camera; picker in sync | FAIL (back to camera 1, picker "Choose a camera") |
| CC-13 | Download Full / Download Crop / Copy / Drive at 0 remaining | Cap dialog, count unchanged, nothing exported | PASS |
| CC-14 | Copy cap text | Mentions copying | FAIL ("downloading") |
| CC-15 | Download Full with uses left | Cost per policy; file `camera-YYYYMMDD-HHMMSS.png` | PENDING (RERUN 14) |
| CC-16 | Download Crop with uses left (JPG ticked) | `…-cropped.jpg`; cost per policy | PENDING |
| CC-17 | Badge on trial downloads | As the notice says (top and bottom right), and disclosed before Start | PENDING (file) / FAIL (disclosure) |
| CC-18 | iPhone SE first screen | Start Camera visible | FAIL (y≈828) |
| CC-19 | iPhone SE live | Preview and Capture on one screen | FAIL |
| CC-20 | Keyboard: Enter on Start, then on Capture | Focus moves to the next control | FAIL (focus on body) |
| CC-21 | axe on main after Capture | 0 critical | FAIL (`image-alt`) |
| CC-22 | Crop without a mouse | Preset or keyboard path | FAIL |
| CC-23 | Save to my cloud storage (guest) | Explains sign-in plus add-on | PASS (dialog; sign-in not done) |
| CC-24 | Video, FAQ and blog match the UI and disclose the mark | Consistent | FAIL |
