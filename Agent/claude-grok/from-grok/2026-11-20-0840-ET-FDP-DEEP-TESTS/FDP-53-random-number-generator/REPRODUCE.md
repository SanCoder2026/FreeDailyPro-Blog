Sent: 2026-11-21 09:47 ET

# FDP-53: how to reproduce (guest, fresh profile)

**Setup:** open https://www.freedailypro.com/tool/random-number-generator.

## Trial uses (policy question)
1. In DevTools, read localStorage `fdp-usage-v1` (e.g. 0/10 professional).
2. Generate 5 numbers → Copy Results → Download .txt → Copy again. The value is unchanged, and there's no `usage.log` POST in Network.
3. In a context at 10/10, Copy and Download still work and no dialog opens.

## Video
Play buvkdsqCW5w:
- t≈30 s: old header "10 free uses daily · 8 free uses left today", no mode tabs, caption overlapping the help text.
- End card: "200+ Free Productivity Tools".

## Blog
Open /blog/random-number-generator. Find "If you only see integers…", "Most everyday UIs do not expose seeds", and "Without-replacement workflow".

## Locales
Open /de/tool/random-number-generator (or any of the 9). The H1, subtitle and controls are English, and the breadcrumb is German.

## Stale result
1. Numbers → How many 20, No duplicates on → Generate.
2. Set Max 5 and How many 6. The error appears, and the 20-number card stays.
3. The same happens in Dice: roll 3d8+2, then type 2d1.

## Accessibility
- With a screen reader, Generate announces nothing.
- With focus in Max, pressing Enter does nothing.
