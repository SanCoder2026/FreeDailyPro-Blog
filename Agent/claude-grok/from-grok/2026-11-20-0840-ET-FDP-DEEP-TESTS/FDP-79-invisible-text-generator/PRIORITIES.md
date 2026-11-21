Sent: 2026-11-21 18:03 ET

# FDP-79 priorities

**P0 / P1:** none found.

**Owner question**
1. Invisible Text Generator takes no trial use. Copy at 10/10 (Chromium, clipboard filled) and at 0/10 (Firefox, try 20): 7 copies each, 0 `usage.log` POSTs, no dialog, counter unchanged. No strip or Quick Buy on the page (tool not `known`), yet JSON-LD Offer $4.99 and a "Pro" chip in the video. Count it, or list it as uncounted (precedents #68, #74, #76, #77).

**P2**
1. **First Copy after clearing the count box does nothing.** With the box empty (or letters / full-width digits), the red note "Type a number from 1 to 500…" shows. Clicking Copy blurs the box, the note disappears and the button jumps up 24 px (desktop) / 33 px (Pixel 7) between mousedown and mouseup, so the click is lost: no copy, no toast (Chromium, Firefox, Pixel 7; iPhone tap OK). `shift.json`, `shift-*.png`, cases N03/N06/N11.
2. **"Couldn't copy. Select the text and copy it by hand."** When the browser refuses clipboard access, the generated characters exist nowhere on the page to select (0 text nodes), so the fallback is impossible. Add a selectable/readonly field or an `execCommand` fallback.
3. Blog /blog/invisible-text-generator: "six variants" and "slider … from 1 to 20"; the tool has 9 variants and 1–500.
4. Video AIYW2os7qxE: old UI (2 variants, slider only, no count box, no Test box), "Free" title and end card "200+ Free Productivity Tools"; the bookmarks bar and a Notepad window with tab names are visible.
5. Locale pages: title, H1, labels, notes and FAQ English on all 10 hreflang pages.

**P3**
1. Typing a leading 0 becomes 1: clearing then typing "007" gives **107**; "05" gives 15. "2.5" → 25 and "1e2" → 12 silently; "-3" → 3 silently.
2. Slider runs only 1–20 while the count goes to 500: at 50 it shows 20, and ArrowLeft jumps the count from 50 to 19. The FAQ says "drag the slider" for 1–500.
3. Invisible Line Break copies a trailing newline (many fields trim it); toasts stack (4 identical).
4. iPhone SE 9 px overflow (header button); ja desktop 3 px; one 1920 run logged CLS 1.0 at 0.4 s (body margin transition). axe desktop label-content-name-mismatch (serious) + region; Pixel 7 clean.
