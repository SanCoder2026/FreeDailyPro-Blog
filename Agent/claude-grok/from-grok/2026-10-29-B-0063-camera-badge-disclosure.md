# B-0063 Camera Capture adds trial badges to the full photo without telling the user first
Priority: P2 (trust + conversion; our top-impression camera page)      Estimated effort: 20–40 min      Report: #73      Source: Testing Bot      Related: SW-14 (badge disclosure pattern), B-0001

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
If a download carries a "Created with FreeDailyPro.com" badge, the user should know before they click, on every download path. That way the badge works as an honest nudge to the Day Pass, not a surprise that sends them to a competitor.

## Why
- Oct 29 22:44–22:46 ET, desktop and mobile, logged out: "Download Full Photo" (PNG and JPG) produced 3840×2160 files with badges top-right and bottom-right (screenshots cam-1280-png-top.png / -bot.png). **No notice appears before that button.**
- The notice ("This download will carry small 'Created with FreeDailyPro.com' badges… Go paid to avoid the mark.") only appears after you drag a crop, next to "Download Crop".
- Merge/Split PDF already show the notice before download (#67/#68 PASS), so camera is the odd one out.
- Camera is our largest image entry page: 2,439 GSC impressions, 50 clicks, 77 GA views since Jul 10. Its top competitors (freephotobooth.online, lensbooth.app) headline "no watermark".

## Outcomes
- The same disclosure (with the Day Pass link) shows before **every** badged download on camera: Full Photo, Crop and Copy, if Copy is badged.
- Check other image-output tools that share the capture/crop component for the same gap, and say which you fixed.
- Optional (P3): a 3-second self-timer and a mirror toggle; competitors filtercamera.com and toea.com offer both.

## Constraints
Do not change badge policy or pricing (owner decision). Copy: say "trial uses" and "professional tools", with no new visible "free".

## Test cases
Fresh visitor → Start Camera → Capture: the notice is visible before Download Full Photo. Download: badges present and match the notice. Crop path: unchanged. Mobile 390: the notice is visible without overlapping the buttons.
