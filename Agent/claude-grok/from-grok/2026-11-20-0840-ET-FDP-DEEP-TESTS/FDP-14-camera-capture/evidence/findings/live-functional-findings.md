Sent: 2026-11-20 08:40 ET

# Live functional findings: Camera Capture (FDP-14)

- **Run window:** 2026-11-19 14:28–14:40 EST (box `date`). Guest contexts only, headless Chromium (plus Firefox for the denied case). Camera = Chromium's fake device fed a known 1280×720 test card (`screens/live/fake-camera-reference.png`: red top-left, lime top-right, blue bottom-left, yellow bottom-right, text "FDP TEST LEFT" top-left), or Chromium's built-in 2-device fake for the camera-picker tests.
- **Starting counts (display-only, `fdp-usage-v1`):** every fresh context loaded at 10 of 10 used (0 remaining): probe, ui, kbd (desktop, iPhone SE, Pixel 7), cloud, and 4 read-only contexts in `cc-count.js` (desktop, Pixel 7, Galaxy S9+, de-DE). /terms says trial uses are counted "per browser and per network address", which fits. Counts never moved.

## 1. Capture path (no trial use): PASS
| Step | Observed | Evidence |
|---|---|---|
| Start Camera | Live preview; "Camera resolution: 1280 x 720" (test card) and "3840 x 2160" (built-in fake, so the 4096×2160 request works); steps panel "1 of 4 steps done. Current step: Press Capture." (aria-live polite) | `json/desk-probe.json`, `json/ui-cameras.json` |
| Capture | Still image 1280×720, colours exact in all four quadrants, not mirrored (red top-left); the camera stream stops (no `<video>` left) as the page says | `json/ui.json` → `capturePixels`, `trackLive:false` |
| Crop (mouse) | Drag 55%→95% → 512×286 crop, all yellow (correct quadrant); 10%→40% → 384×216 | `json/desk-probe.json`, `json/ui.json` |
| Crop (touch, CDP touch events, iPhone SE / Pixel 7 emulation) | 512×288 / 512×287 crops | `json/kbd.json` |
| Save as JPG | Ticked during preview → crop blob `image/jpeg` | `json/ui.json` → `cropBlob` |
| Cancel | Stops camera, back to Start, steps reset to 0 of 4 | `json/ui.json` |
| Retake | Restarts the live camera; the JPG tick is kept | `json/ui.json` |
| No camera | "No camera was found on this device." | `screens/live/ui-no-camera.png` |
| Permission denied (Firefox, `permissions.default.camera=2`) | "Camera access was denied. Browsers only show the "allow camera?" prompt once — to try again, click the lock/info icon in your address bar, set Camera to Allow, then reload this page." Matches the FAQ. | `screens/live/ui-denied-firefox.png` |
| Headless Chromium without a permission grant | `NotSupportedError` → generic "Couldn't access the camera. Try again." (a headless quirk, not a site bug) | `screens/live/ui-headless-notsupported.png` |

## 2. Gate at 0 remaining: PASS (behaviour); copy wording P2
- **Download Full Photo, Download Crop, Copy and Save to Google Drive** each open the cap dialog "Today's trial uses are done … downloading needs a pass …", the count stays at 10, nothing is downloaded and the clipboard stays empty (`json/desk-probe.json`, `json/cloud.json`, `screens/live/desk-*-dialog.png`).
- Charging Copy follows the owner policy and /terms ("download, copy, print or save"), so it isn't a bug. **Wording (P2):** the Copy dialog and toast say "downloading needs a pass" and "downloading was not done" after a Copy click. Better: "copying needs a pass".
- **Save to my cloud storage** opens "Cloud storage | Add cloud storage, $4.99 per month, 1 GB … Sign in with your email first … Not now | Sign in | Close". **Stopped at the sign-in dialog; not signed in (feature untested).**
- **Not observable (RERUN-AFTER-RESET row 14):** what each export costs with uses left; whether downloads carry the badges; real file names; whether the copied crop is marked.

## 3. Watermark on guest photos (P1, wording and policy)
- After Capture the page shows the notice "This download will carry small "Created with FreeDailyPro.com" badges in the top and bottom right corners. Go paid to avoid the mark." (`json/kbd.json` → `notices`).
- The page title, meta, FAQ ("What format and file name will the photo have?"), the How-to and the blog ("Take a Webcam Headshot for an Onboarding Form … HR portal wants a profile photo") never mention the badge. They sell exactly the use cases (profile photo, ID-sized crop for an online application, onboarding headshot) where a corner badge makes a trial-use photo unusable.
- The image mark is site policy (not a bug). The fix is wording: say it on the page and FAQ before the user grants camera access. Santosh may also want to decide whether a headshot tool should mark faces at all. **Unverified until the RERUN row:** whether and where the badge is actually drawn on the downloaded photo.

## 4. Camera choice
- With 2 cameras (Chromium's built-in fake), a picker appears after Start, listing both by name; choosing fake_device_1 switches the stream (`json/ui-cameras.json`). PASS for the FAQ claim.
- **Front / rear camera** on a device whose cameras report no facing mode (laptops, external webcams) always lands on the first camera, and the picker then shows the placeholder "Choose a camera" while a camera is live (afterToggle and afterToggle2 both `fake_device_0`). On phones the facing-mode switch should work; **real-phone check not done (no device)**. P2: hide the button when the active track has no `facingMode`, or keep the picker value in sync.
- The picker has no accessible name (no aria-label or label; its name is just the current camera's name).
- With `--use-file-for-fake-video-capture` Chromium exposes only one camera, so the picker is correctly hidden in that run.

## 5. Other behaviour from code (`js/CameraCapture-0Z_gFqDj.pretty.js`)
- "Save as JPG" exists only while the preview is live (L369–379). After Capture the checkbox is gone (`checkboxAfterCapture: 0`), so forgetting it means Retake. This is documented ("set it first"), but a format choice at download time would be friendlier (P2).
- Copy exists only for the crop, not the full photo (documented).
- Mousedown on the photo starts a new selection and clears the current crop result (L191–194, `u(null)`), so a stray tap discards the crop preview. P2, code-read; the live check was inconclusive.
- `URL.createObjectURL(v)` is called inside render (L466) and never revoked, so each re-render leaks a blob URL. P2 hygiene.
- No countdown/self-timer, mirror toggle, square/aspect lock, or keyboard shutter (all standard in competitors; see desk findings).
- No network request carried image data during the probe; only telemetry (funnel.hit, insight.hit) was seen in the filtered POST list (`json/desk-probe.json` → `net`). This was not a full network audit.

## 6. Keyboard and a11y (`json/kbd.json`)
- Start Camera, then Capture, Front/rear, Save as JPG and Cancel are all reachable with Tab, with a visible focus ring; Enter works.
- **Focus is lost to `<body>`** after Start Camera and after Capture (the pressed button unmounts), so keyboard and screen-reader users start again from the top of the page. P2.
- **Crop is mouse/touch only:** the crop area has no tabindex, role or keys, and Crop Selection stays disabled without a drag. P2 (Download Full Photo remains available).
- axe on `main`: 0 violations while idle or live. After Capture, **1 critical `image-alt`**: the captured `<img>` has no alt. The crop preview `<img>` has no alt either.
