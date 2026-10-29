# B-0010 Two-step 'make then Download' flows look broken
Priority: P2      Estimated effort: 45 min

## Goal / why
Users click the main button, get no file, and leave; reduces completed uses that lead to paywall views.

## What to change
https://www.freedailypro.com/tool/pdf-editor, https://www.freedailypro.com/tool/fillable-forms, https://www.freedailypro.com/tool/stl-ascii-binary-converter, https://www.freedailypro.com/tool/social-media-formatter, https://www.freedailypro.com/tool/mail-merge-pdf.
- pdf-editor 'Apply & Download' and fillable-forms 'Fill & Download' only bake; a separate Download appears. Either download immediately after bake, or rename to 'Apply' and auto-scroll/highlight Download.
- stl converter Convert then separate Download — same fix.
- mail-merge-pdf: 'Use an example' fills data but Download stays disabled until Letter/Certificate clicked; pre-select a template with the example.
- pdf-editor mobile (390/360): drawing doesn't register because the page <img> has pointer-events-none; attach handlers to the overlay so touch draw works.

## Acceptance criteria
- Each listed tool produces a file from one obvious click path; button labels match behaviour.
- mail-merge example → Download enabled immediately.
- pdf-editor rectangle/highlight can be drawn on iPhone 13 and Pixel 5 viewports.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Changing trial counting (one visit = one use).
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (reports #48, #49, #50, #52)
