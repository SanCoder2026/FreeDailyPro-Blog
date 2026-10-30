Sent: 2026-10-30 16:05 ET

# QA-REPORT-160 Addendum — admin session ~16:00-16:02 ET
Source: admin session notes ~16:00-16:02 ET; box follow-up 16:04-16:05 ET (live JS read). Sent files are unchanged.

## 1. yt-thumbnail: CONFIRMED P1 → new brief B-0309 (L-351)
- Reproduced twice in the admin session (15:47, 16:01 ET). Max-res and Standard Download: no request, no usage.log, no download, no toast, no console error. Logged out it works (checked 15:48 ET).
- This fits the silent path: logUsageNow() / the download gate returns false or never resolves for the signed-in paid/admin session, and the code returns with no message.
- The live JS was redeployed since 15:48 (ToolPage-C58HFfD8 → ToolPage-BILZoqti, YtThumbnail-D15pZoZx → YtThumbnail-HTZVbY8G). The gate code is unchanged (checked).
- Blast radius: the shared helper (`d`) and the shared Download button (`D`) are imported by the tools listed in B-0309 (checked in the live JS). This includes the audio, PDF, PowerPoint, image, video and maker tools.
- Recommendation: an admin/paid sweep. One Download on a sample of these tools in a paid session (B-0309 test case 3), noting request / usage.log / file / toast for each.
- Not B-0156 (no false toast) and not B-0187. It is a new class: silent no-op for paying users.

## 2. audio-trimmer (B-0306, L-356, L-216): confirmed in the admin session
End snapped from 0:01 back to 0:06 (file end). Then "Audio trimmed!" and "Enter a valid end time, later than the start time" both appeared, and a result panel was shown. This matches the logged-out finding (#160) and supports B-0306 Outcome 1 and the L-216 false-success class. Whether the result panel's file is a real trim of the bad range is still unverified.

## 3. Chrome "Install app" popup on click
- Live JS checked: the site listens for `beforeinstallprompt`, calls preventDefault(), and stores the event. It calls prompt() only from explicit install controls: "Create Shortcut", the Install-as-app icon next to tool names, and the install hero card. No Download, Trim or Get handler calls prompt() (checked in index-D7xEWw5H.js and ToolPage-BILZoqti.js).
- So the site does not trigger the prompt on ordinary user gestures. The popup seen is most likely Chrome's own install promotion (the address-bar/in-product bubble), which the browser shows for installable sites by itself. It could also be a click that landed on the small Install-as-app icon near the tool name.
- Admin check: note which element was clicked when the popup appeared. If it was a Download button, record the Chrome version.

## Files
This addendum; B-0309 brief; batch-79 INDEX-v2.md (Supersedes INDEX.md); ledger notes on L-351, L-356, L-216 and L-222.
