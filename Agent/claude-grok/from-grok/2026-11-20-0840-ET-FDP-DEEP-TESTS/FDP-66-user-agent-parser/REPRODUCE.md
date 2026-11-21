Sent: 2026-11-21 14:42 ET

# FDP-66 reproduce

1. Fresh guest window → https://www.freedailypro.com/tool/user-agent-parser.
2. **Uncounted:** in DevTools, watch Network for `usage.log`. Click Copy result, Save as text, Print; reload; repeat. No POST; `fdp-usage-v1` unchanged. Same at 10/10 (set by a context that is at the cap).
3. **Client Hints:** paste
   `Sec-CH-UA: "Google Chrome";v="131", "Chromium";v="131"` / `Sec-CH-UA-Mobile: ?1` / `Sec-CH-UA-Platform: "Android"` / `Sec-CH-UA-Platform-Version: "14.0.0"` / `Sec-CH-UA-Model: "Pixel 8 Pro"` / `Sec-CH-UA-Full-Version-List: "Google Chrome";v="131.0.6778.135"` → cards "(from Sec-CH-UA headers)". Then read the FAQ "Can it read a Client Hints header? No."
4. **Windows card:** paste an Edge on Windows NT 10.0 UA → OS card "Windows 10".
5. **Empty box:** clear the textarea in a headless browser → own UA results, Bot No.
