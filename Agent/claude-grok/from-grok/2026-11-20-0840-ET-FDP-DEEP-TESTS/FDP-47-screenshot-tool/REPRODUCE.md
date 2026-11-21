Sent: 2026-11-21 06:49 ET

# FDP-47: how to reproduce (guest, fresh profile, no sign-in)

**Setup:** desktop Chrome, https://www.freedailypro.com/tool/screenshot-tool. Use a fresh profile whose strip shows "2 remaining today" (fresh headless contexts sometimes load already at 2/2, so retry).

## P1: per-page-load charging
1. Take Screenshot → share a tab → Download: the strip drops.
2. Without reloading: drag a box → Download; Copy; Crop → draw → Download PNG; switch to JPG → Download JPG; Take Another → Capture whole page → scroll → Finish → Download. All succeed; no dialog, even with "0 remaining today".
3. Reload → Take Screenshot → Download (or Copy): the cap dialog appears.
- Headless: `scripts/st-live.js main` (stub screen; see README).

## P1: Android
1. Open the page in Chrome on an Android phone (or Pixel 7 emulation with `getDisplayMedia` removed: `st-live.js mobile`).
2. No note on the page; the Day pass/Monthly offer shows. Tap Take Screenshot → toast "Screen capture isn't supported in this browser".

## P2 items
- **Video:** https://www.youtube.com/watch?v=lBBMlLTJYMw (0:15–1:10 old UI; overlay "10 free uses daily!").
- **Locales:** /hi/tool/screenshot-tool → Take Screenshot, delay help, How to use in English.

## Owner questions
- Drag a small box (one line of text) → Download → two badges over the text. Copy the same box → the clipboard image has no badge.

## Gate at the cap
- Download / Copy / editor Download → "Today's trial uses are done" dialog. Buy Day Pass → email (stop). Quick Buy monthly → Stripe (stop).
